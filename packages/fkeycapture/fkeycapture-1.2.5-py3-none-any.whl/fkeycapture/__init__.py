"""Firepup650's fkeycapture module"""
import termios, fcntl, sys, os
from typing import Union

global fd, flags_save, attrs_save
fd = sys.stdin.fileno()
flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
attrs_save = termios.tcgetattr(fd)


def __getp1():
    """Internal Method - Modify terminal settings"""

    fd = sys.stdin.fileno()
    # save old state
    flags_save = fcntl.fcntl(fd, fcntl.F_GETFL)
    attrs_save = termios.tcgetattr(fd)
    # make raw - the way to do this comes from the termios(3) man page.
    attrs = list(attrs_save)  # copy the stored version to update
    # iflag
    attrs[0] &= ~(
        termios.IGNBRK
        | termios.BRKINT
        | termios.PARMRK
        | termios.ISTRIP
        | termios.INLCR
        | termios.IGNCR
        | termios.ICRNL
        | termios.IXON
    )
    # oflag
    attrs[1] &= ~termios.OPOST
    # cflag
    attrs[2] &= ~(termios.CSIZE | termios.PARENB)
    attrs[2] |= termios.CS8
    # lflag
    attrs[3] &= ~(
        termios.ECHONL | termios.ECHO | termios.ICANON | termios.ISIG | termios.IEXTEN
    )
    termios.tcsetattr(fd, termios.TCSANOW, attrs)
    # turn off non-blocking
    fcntl.fcntl(fd, fcntl.F_SETFL, flags_save & ~os.O_NONBLOCK)


def __getp2():
    """Internal Method - Reset terminal settings"""
    termios.tcsetattr(fd, termios.TCSAFLUSH, attrs_save)
    fcntl.fcntl(fd, fcntl.F_SETFL, flags_save)


def __handleDelete(base: list, current: str) -> list:
    """Internal Method - Handle deletes"""
    if current.encode() == b"\x7f":
        base.pop()
    else:
        base.append(current)
    return base


def get(
    keycount: int = 1, bytes: bool = False, allowDelete: bool = False
) -> Union[str, bytes]:
    """# Function: get

    # Inputs:
      keycount: int     - Number of keys, defualts to 1
      bytes: bool       - Wether to return the key(s) as bytes, defaults to False
      allowDelete: bool - Wether to allow deleting chars, defaults to False

    # Returns:
      Union[str, bytes]

    # Raises:
      None"""
    __getp1()
    internalcounter = 0
    keys = []
    while internalcounter != keycount:
        key = sys.stdin.read(1)
        if allowDelete:
            keys = __handleDelete(keys, key)  # type: ignore
        else:
            keys.append(key)
        internalcounter = len(keys)
    key = "".join(keys)  # type: ignore[arg-type]
    __getp2()
    if bytes:
        return key.encode()
    else:
        return key


def getnum(
    keycount: int = 1, ints: bool = False, allowDelete: bool = False
) -> Union[str, int]:
    """# Function: getnum

    # Inputs:
      keycount: int     - Number of keys, defualts to 1
      ints: bool        - Wether to return the keys as ints, defaults to False
      allowDelete: bool - Wether to allow deleting chars, defaults to False

    # Returns:
      Union[str, int]

    # Raises:
      None"""
    internalcounter = 0
    keys = []
    while internalcounter != keycount:
        key = get()
        if key in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if allowDelete:
                keys = __handleDelete(keys, key)
            else:
                keys.append(key)
            internalcounter = len(keys)
    key = "".join(keys)  # type: ignore[arg-type]
    if not ints:
        return key
    else:
        return int(key)


def getchars(
    keycount: int = 1,
    chars: list = ["1", "2"],
    bytes: bool = False,
    allowDelete: bool = False,
) -> Union[str, bytes]:
    """# Function: getchars

    # Inputs:
      keycount: int     - Number of keys, defualts to 1
      chars: list       - List of allowed keys, defaults to ["1", "2"]
      bytes: bool       - Wether or not to return the key(s) as bytes, defaults to False
      allowDelete: bool - Wether to allow deleting chars, defaults to False

    # Returns:
      Union[str, bytes]

    # Raises:
      None"""
    internalcounter = 0
    keys = []
    while internalcounter != keycount:
        key = get()
        if key in chars:
            if allowDelete:
                keys = __handleDelete(keys, key)  # type: ignore
            else:
                keys.append(key)
            internalcounter = len(keys)
    key = "".join(keys)  # type: ignore[arg-type]
    if not bytes:
        return key
    else:
        return key.encode()
