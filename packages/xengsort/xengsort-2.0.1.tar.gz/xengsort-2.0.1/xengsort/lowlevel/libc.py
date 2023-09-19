"""
Provide the C library as an object 'libc'.
If you want to call a libc function from numba,
its attributes .argtypes and .restype have to be set correctly.

Additionally, provide
- errno():
    thread-safe OS error number.
- read_block(fd, buffer, offset=0):
    read available bytes from file descriptor fd into buffer[offset:];
    return how many bytes of the buffer are filled, or 0 (EOF),
    or a negative error code (-errno).
    Up to 5 attempts will be made to read data if EAGAIN occurs.
- write_block(fd, buffer, nbytes):
    write bytes from buffer to file with descriptor fd.
    Return how many bytes were written, or a negative error code.
    Up to 5 attempts will be made to read data if EAGAIN occurs.
"""

import sys
import os
import ctypes
import numba


def _setup_libc():
    """
    Find a libc implementation (may be platform dependent) and
    set types for the C-functions
    - open
    - read
    - close
    """
    osname = os.name.lower()
    platform = sys.platform.lower()
    msg = f"Platform '{platform}' with OS name '{osname}' not supported yet."

    if osname == 'posix':
        # _libc = ctypes.cdll.LoadLibrary(None, use_errno=True)
        _libc = ctypes.CDLL(None, use_errno=True)

        _libc.read.restype = ctypes.c_ssize_t  # bytes read
        _libc.read.argtypes = (ctypes.c_int, ctypes.c_void_p, ctypes.c_size_t)
        _read = _libc.read

        _libc.write.restype = ctypes.c_ssize_t  # bytes written
        _libc.write.argtypes = (ctypes.c_int, ctypes.c_void_p, ctypes.c_size_t)
        _write = _libc.write

        if 'linux' in platform:
            _libc.__errno_location.argtypes = tuple()
            _libc.__errno_location.restype = ctypes.POINTER(ctypes.c_int)
            _errno_location = _libc.__errno_location
        elif 'darwin' in platform:
            _libc.__error.argtypes = tuple()
            _libc.__error.restype = ctypes.POINTER(ctypes.c_int)
            _errno_location = _libc.__error
        else:
            raise NotImplementedError(msg)

        _errno = numba.njit(nogil=True)(lambda: _errno_location()[0])
        return _libc, _read, _write, _errno

    else:
        """
        https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/open-wopen
        """
        raise NotImplementedError(msg)


libc, _read, _write, errno = _setup_libc()


@numba.njit(nogil=True, locals=dict())  # offset=int32, buflen=int32, space=int32, res=int32, fill=int32, err=int32))
def read_block(fd, buf, offset=0, ATTEMPTS=5):
    """
    Read bytes from an open file with file descriptor fd (int32).
    Bytes are stored into buf[offset:], which must be a byte buffer.
    Return the end index of the filled part of the buffer,
    a negative number indicates an error.
    or -99_999, -99_998 on internal error error
    """
    buflen = buf.size
    space = buflen - offset
    if space <= 0:
        return -99_999  # no space means overflow

    # Wrap this in a loop to handle EAGAIN errors
    for attempt in range(ATTEMPTS):
        res = _read(fd, buf.ctypes.data + offset, space)
        err = errno()
        if res > 0:
            # print(res)
            fill = offset + res
            return fill if fill <= buflen else (-99_999)  # -99_999 means overflow
        elif res == 0:
            return 0
        if err == 11:
            continue  # EAGAIN: try again, no data
        return (-err) if err > 0 else (-99_998)  # negative errno on error
        # -99_998 means impossible error (res == -1 but errno is zero)
    # out of attempts, we had no data, but still EAGAIN (err==11); that's probably ok.
    return 0


@numba.njit(nogil=True, locals=dict())
def write_block(fd, buf, n, ATTEMPTS=5):
    """
    Write n bytes from buf to the file with file descriptor fd (int32).
    Return number of ele
    """
    N = n
    written = 0
    attempts = 0
    while n > 0:
        res = _write(fd, buf.ctypes.data, n)
        err = errno()
        if res > 0:
            written += res
            n -= res
        elif res < 0:  # indicates error; error is in err
            return (-err) if err > 0 else (-99_998)
        else:  # res == 0: nothing done
            attempts += 1
            if attempts >= ATTEMPTS:
                return (-99_997)  # not written enough
    return written if (written == N) else (-99_999)  # too much
