"""
xengsort/cptasks_kmers.py
Functions for compiling ConsumerProducerTasks for k-mers
"""

import numpy as np
from numba import njit, int32, int64, uint64

from .dnaencode import compile_revcomp_and_canonical_code
from .lowlevel import debug
from .lowlevel.conpro import \
    find_buffer_for_reading, find_buffer_for_writing, \
    mark_buffer_for_reading, mark_buffer_for_writing, \
    mark_my_buffers_failed
from .dnaencode import quick_dna_to_2bits


"""
TODO:
compile_cptask_scatter_kmers_from_buffers():
  For each k-mer in the sequence input buffers,
  translate the sequence, encode kmers as integers,
  compute a hash function (modulus = subtable) and quotient (subkey),
  send the subkey (and optionally positions)
  to the corresponding subtable's output buffer.
"""


def compile_cptask_scatter_kmers_from_linemarked(
        mask, rcmode, hf0,
        nsubtables, noutbuffers_per_subtable, outbufsize):
    """
    Compile a cptask function that
    creates (gapped) k-mers from linemarked buffers.
    - mask: a Mask object
    - rcmode: how to treat reverse complements; f, r, b, max, min
    - hf0: the 0-th hash function that determines the subtable
    - nsubtables: the number of subtables
    - noutbuffers_per_subtable: number of output buffers per subtable
    - outbufsize: the output buffer size for which to compile this function
    """
    debugprint0, debugprint1, debugprint2 = debug.debugprint
    both = (rcmode[0].lower() == "b")

    k, w, tpl = mask.k, mask.w, mask.tuple
    assert len(tpl) == k
    if k < 1 or k > 32:
        raise ValueError(f"Only 1 <= k <= 32 is supported, but {k=}.")
    codemask = uint64(4**(k - 1) - 1)
    revcomp, ccode = compile_revcomp_and_canonical_code(k, rcmode)
    if mask.is_contiguous:
        debugprint1(f"- compiling cptask_scatter_kmers for contiguous {k}-mers.")
    else:
        debugprint1(f"- compiling cptask_scatter_kmers for gapped ({k},{w})-mers: {mask.mask}.")

    @njit(nogil=True, locals=dict(
        code=uint64, st=uint64, sk=uint64,
        j=int32, stj=int32, p=int32, wait=int64))
    def _store(code, outidx, outpos, outbuffers, outcontrol):
        st, sk = hf0(code)
        j = outidx[st]
        p = outpos[st]
        error = 0
        wait_write = 0
        if p >= outbufsize:
            if j >= 0:
                outcontrol[j, 7] = outbufsize
                mark_buffer_for_reading(outcontrol, j)
                stj = j - st * noutbuffers_per_subtable  # the "local" j for subtable st
                assert 0 <= stj < noutbuffers_per_subtable
            else:
                assert j == -1
                stj = -1
            stoutcontrol = outcontrol[(st * noutbuffers_per_subtable):(st + 1) * noutbuffers_per_subtable]
            stj, wait = find_buffer_for_writing(stoutcontrol, stj)
            outidx[st] = j = (stj + st * noutbuffers_per_subtable)
            outpos[st] = p = 0
            error = outcontrol[j, 1]
        outbuffers[j, p] = sk  # put subkey (not code!) into outbuffer
        outpos[st] += 1
        return (wait, error)

    @njit(nogil=True, locals=dict(
        code=uint64, i=int64, j=int64, c=uint64,
        errorcode=int32, _errorcode=int32,
        wait=int64, _wait=int64))
    def _process_gapped(seq, *allout):  # (outidx, outpos, outbuffers, outcontrol):
        startpoints = seq.size - tpl[k - 1]
        errorcode = 0
        wait = 0
        for i in range(startpoints):
            code = 0
            for j in tpl:
                c = seq[i + j]
                if c > 3:
                    break
                code = uint64(code << 2) | uint64(c)
            else:  # no break
                if both:
                    _wait, errorcode = _store(code, *allout)  # outidx, outpos, outbuffers, outcontrol)
                    wait += wait
                    _wait, _errorcode = _store(revcomp(code), *allout)  # outidx, outpos, outbuffers, outcontrol)
                    wait += _wait
                    errorcode |= _errorcode
                else:
                    _wait, errorcode = _store(ccode(code), *allout)  # outidx, outpos, outbuffers, outcontrol)
                    wait += _wait
            if errorcode != 0:
                break
        return (wait, errorcode)

    @njit(nogil=True, locals=dict(
        code=uint64, i=int64, j=int64, c=uint64, errorcode=int32,
        wait=int64, _wait=int64))
    def _process_contiguous(seq, *allout):  # (outidx, outpos, outbuffers, outcontrol):
        endpoint = seq.size - (k - 1)
        valid = False
        errorcode = 0
        wait = 0
        i = 0
        while i < endpoint:
            if not valid:
                code = 0
                for j in range(k):
                    c = seq[i + j]
                    if c > 3:
                        i += j + 1  # skip invalid
                        break
                    code = (code << 2) | c
                else:  # no break
                    valid = True
                if not valid:
                    continue  # with while
            else:  # was valid, we have an old code
                c = seq[i + k - 1]
                if c > 3:
                    valid = False
                    i += k  # skip invalid
                    continue  # with while
                code = ((code & codemask) << 2) | c
            # at this point, we have a valid code
            if both:
                _wait, errorcode = _store(code, *allout)  # outidx, outpos, outbuffers, outcontrol)
                wait += _wait
                _wait, _errorcode = _store(revcomp(code), *allout)  # outidx, outpos, outbuffers, outcontrol)
                wait += _wait
                errorcode |= _errorcode
            else:
                _wait, errorcode = _store(ccode(code), *allout)  # outidx, outpos, outbuffers, outcontrol)
                wait += _wait
            i += 1
            if errorcode != 0:
                break
        return (wait, errorcode)

    _process = _process_contiguous if mask.is_contiguous else _process_gapped

    @njit(nogil=True, locals=dict(
        nactive=int32, nseqs=int32, i=int32, j=int32, outj=int32,
        wait=int64, wait_read=int64, wait_write=int64,
        errorcode=int32, _errorcode=int32))
    def _cptask_scatter_kmers(inbuffers, incontrol, ininfos, outbuffers, outcontrol, outinfos):
        # find a linemarked buffer to read (among inbuffers)
        # find and reserve nsubtables output buffers among the output buffers [outinfos]
        # incontrol[i, 7]: number of FASTQ reads in input buffer i
        # ininfos[i]: linemarks for input buffer i
        # outcontrol[B, 7]: k-mers in buffer B
        debugprint2("- running: cptask_scatter_kmers; outbuffers shape =", outbuffers.shape)
        assert inbuffers.ndim == 2
        assert outbuffers.ndim == 2
        M, N = ininfos.shape
        assert N % 4 == 0
        linemarkbuffers = ininfos.reshape(M, N // 4, 4)
        assert outbuffers.shape[0] == nsubtables * noutbuffers_per_subtable
        assert outbuffers.shape[1] >= outbufsize
        assert outinfos.shape[1] == 0

        wait_read = wait_write = 0
        nactive = -1  # active input buffer
        outidx = np.full(nsubtables, (-1), dtype=np.int32)
        outpos = np.full(nsubtables, outbufsize, dtype=np.int32)
        while True:
            nactive, wait = find_buffer_for_reading(incontrol, nactive)
            wait_read += wait
            if nactive < 0:  # all finished
                errorcode = int(nactive <= -2)
                break
            active_buffer = inbuffers[nactive]
            nseqs = incontrol[nactive, 7]
            errorcode = 0
            linemarks = linemarkbuffers[nactive]
            for i in range(nseqs):
                sq = active_buffer[linemarks[i, 0]:linemarks[i, 1]]
                quick_dna_to_2bits(sq)
                (wait, _errorcode) = _process(
                    sq, outidx, outpos, outbuffers, outcontrol)
                wait_write += wait
                errorcode |= _errorcode
            if errorcode:
                mark_my_buffers_failed(incontrol)
                debugprint2("- FAILED: cptask_scatter_kmers", errorcode)
                break
            mark_buffer_for_writing(incontrol, nactive)
        # We break out of while True loop when all bufferes were marked as finished by FASTQ reader processes
        # We then let the next task read our output buffers one final time.
        if not errorcode:
            for st in range(nsubtables):
                j = outidx[st]
                if j >= 0:
                    # assert outpos[st] > 0
                    outcontrol[j, 7] = outpos[st]
                    mark_buffer_for_reading(outcontrol, j)
            debugprint2("- ending: cptask_scatter_kmers", errorcode)
        return (wait_read, wait_write, -errorcode)

    return _cptask_scatter_kmers


def compile_cptask_insert_filtered_subkeys(
        myhashtable,
        myfilter,
        constant_value=0,
        maxfailures=0,
        maxwalk=1000):
    debugprint0, debugprint1, debugprint2 = debug.debugprint
    if myfilter is not None:
        wwo = "with"
        lookup_and_insert_in_subfilter = myfilter.private.lookup_and_insert_in_subfilter
    else:
        wwo = "without"

        @njit(nogil=True, inline="always")
        def lookup_and_insert_in_subfilter(ft, st, subkey):
            return True
    update = myhashtable.private.update_ssk
    value = uint64(constant_value)
    debugprint1(f"- compiling cptask_insert_filtered_subkeys {wwo} filter: {constant_value=}, {maxfailures=}, {maxwalk=}")

    @njit(nogil=True, locals=dict(
        nactive=int32, mytotal=int64, failed=int64,
        nsubkeys=int32, subkey=uint64, status=int32, result=uint64,
        wait=int64, wait_read=int64, wait_write=int64))
    def _cptask_insert_filtered_subkeys(st, ht, ft, inbuffers, incontrol, ininfos, outbuffers, outcontrol, outinfos):
        """
        Insert subkeys of k-mers into subtables of a hash table.
        Do filtering first.
        """
        # incontrol[i, 0]: buffer status
        # incontrol[i, 1]: set to nonzero on error
        # incontrol[i, 7]: k-mers (or subkeys) in input buffer i
        assert inbuffers.ndim == 2
        assert outbuffers.ndim == 2
        assert outbuffers.shape[0] == 1
        assert outbuffers.shape[1] >= maxwalk + 1
        assert outinfos.shape[1] == 0
        debugprint2("- running: cptask_insert_filtered_subkeys; subtable", st)

        wait_read = wait_write = 0
        nactive = -1  # active input buffer
        active_buffer = inbuffers[0]  # irrelevant
        out = outbuffers[0]
        failed = mytotal = 0
        while True:
            nactive, wait = find_buffer_for_reading(incontrol, nactive)
            wait_read += wait
            if nactive < 0:  # all finished
                debugprint2("- ending: cptask_insert_filtered_subkeys; subtable", st, "with", mytotal, "total and", failed, "failed k-mers.")
                break
            active_buffer = inbuffers[nactive]
            nsubkeys = incontrol[nactive, 7]
            # consume the buffer
            for subkey in active_buffer[:nsubkeys]:
                if lookup_and_insert_in_subfilter(ft, st, subkey):
                    status, result = update(ht, st, subkey, value)  # see docstring below
                    if status & 128 == 0:
                        out[result] += 1
                        failed += (status == 0)
            mytotal += nsubkeys
            mark_buffer_for_writing(incontrol, nactive)
            if failed > maxfailures:
                mark_my_buffers_failed(incontrol)
                debugprint2("- FAILED: cptask_insert_filtered_subkeys; subtable", st, "with", mytotal, "total and", failed, "failed k-mers.")
                break
        return (mytotal, failed, wait_read, wait_write, -(failed > 0))

    return _cptask_insert_filtered_subkeys


def compile_cptask_update_existing_subkeys(
        myhashtable,
        constant_value=1):
    debugprint0, debugprint1, debugprint2 = debug.debugprint
    update_existing = myhashtable.private.update_existing_ssk
    value = uint64(constant_value)
    debugprint1(f"- compiling cptask_update_existing_subkeys: {constant_value=}")

    @njit(nogil=True, locals=dict(
        nactive=int32, mytotal=int64, failed=int64,
        nsubkeys=int32, subkey=uint64, status=int32, result=uint64,
        wait=int64, wait_read=int64, wait_write=int64))
    def _cptask_update_existing_subkeys(st, ht, inbuffers, incontrol, ininfos, outbuffers, outcontrol, outinfos):
        """
        Update only existing or any k-mers within subtables of a hash table.
        """
        assert inbuffers.ndim == 2
        debugprint2("- running: cptask_update_existing_subkeys; subtable", st)

        wait_read = wait_write = 0
        nactive = -1  # active input buffer
        active_buffer = inbuffers[0]  # irrelevant
        failed = mytotal = 0
        while True:
            nactive, wait = find_buffer_for_reading(incontrol, nactive)
            wait_read += wait
            if nactive < 0:  # all finished
                break
            active_buffer = inbuffers[nactive]
            nsubkeys = incontrol[nactive, 7]
            # consume the buffer
            for subkey in active_buffer[:nsubkeys]:
                status, result = update_existing(ht, st, subkey, value)  # see docstring below
                if status & 128 == 0:
                    failed += (status == 0)
            mytotal += nsubkeys
            mark_buffer_for_writing(incontrol, nactive)
        debugprint2("- ending: cptask_update_existing_subkeys; subtable", st, "with", mytotal, "total and", failed, "failed k-mers.")
        return (mytotal, failed, wait_read, wait_write, 0)

    return _cptask_update_existing_subkeys


"""
How to interpret the return value of update:

status: if status == 0, the subkey was not found,
    and, if allow_new=True, it could not be inserted either.
    If (status & 127 =: c) != 0, the subkey exists or was inserted w/ choice c.
    If (status & 128 != 0), the subkey was aleady present.

result: If the subkey was already present (status & 128 != 0),
    then result is the new value that was stored.
    Otherwise (if status & 128 == 0), result is the walk length needed
    to store the new (subkey, value) pair.
"""
