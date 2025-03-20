#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
bodh stands for binary octal decimal hexadecimal.
Ity's a small command line utility that receives a number in argument
and outputs it in the 4 formats aforementioned.
"""

import sys
#import os
import re

#from typing import Any
import argparse


# App version
__author__  = "idealtitude"
__version__ = "0.2.0"
__license__ = "MT108"

# Constants
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
#APP_PATH = os.path.dirname(os.path.realpath(__file__))
#APP_CWD = os.getcwd()

TOKENS_PTN = {
    "bin": re.compile("^(?P<fmt>0b)(?P<num>[0-1]+)$"),
    "oct": re.compile("^(?P<fmt>0o)(?P<num>[0-7]+)$"),
    "dec": re.compile(r"^(?P<num>\d+)$"),
    "hex": re.compile("^(?P<fmt>0x)(?P<num>[0-9A-Fa-f]+)$")
}

def parse_format(uval: str) -> tuple[str|None, str|None]:
    fmt: str | None = None
    val: str | None = None

    for k, v in TOKENS_PTN.items():
        if _m := v.match(uval):
            fmt = k
            val = _m.group("num")

            break

    return (fmt, val)

def parse_int(val: str, fmt: int) -> int | None:
    ret: int | None = None

    try:
        ret = int(val, fmt)
    except TypeError as ex:
        ret = None
        print(f"Error, can't convert \033[1m{val}\033[0m to int.\n{ex}")

    return ret

def set_fillz(num: int) -> int:
    res: int = 4

    if num > 0b1111:
        res = len(bin(num)) - 2

    return res

def to_bin(num: int, fillz: int, raw: bool) -> str:
    """Format to binary repr
    TODO: one single function would suffice, instead of 4
    just adding a 3rd paramater to define the kind of representation
    """
    if not raw:
        return f"\033[31;1m0b\033[0m{num:0{fillz}b}"

    return f"{num:0{fillz}b}"

def to_oct(num: int, fillz: int, raw: bool) -> str:
    if not raw:
        return f"\033[32;1m0o\033[0m{num:0{fillz}o}"
    return f"{num:0{fillz}o}"

def to_dec(num: int, fillz: int, raw: bool) -> str:
    if not raw:
        return f"\033[34;1m0d\033[0m{num:0{fillz}d}"
    return f"{num:0{fillz}d}"

def to_hex(num: int, fillz: int, raw: bool) -> str:
    if not raw:
        return f"\033[35;1m0x\033[0m{num:0{fillz}x}"
    return f"{num:0{fillz}x}"

def fmt_and_display(val: tuple[str, str], raw: bool, full: str = "all") -> str|None:
    funcs_lookup = {
        "bin": to_bin,
        "oct": to_oct,
        "dec": to_dec,
        "hex": to_hex
    }

    fmt: int = 10

    if val[0] == "bin":
        fmt = 2
    elif val[0] == "oct":
        fmt = 8
    elif val[0] == "hex":
        fmt = 16

    get_int: int|None = parse_int(val[1], fmt)

    res_str: str = ""

    if get_int is not None:
        if full == "all":
            for key, fn in funcs_lookup.items():
                sfillz: int = set_fillz(get_int)
                if not raw:
                    res_str += f"\033[1m{key}:\033[0m\t{fn(get_int, sfillz, raw)}\n"
                res_str += f"{fn(get_int, sfillz, raw)}\n"
        elif full == "bin":
            sfillz : int = set_fillz(get_int)
            if not raw:
                res_str = f"\033[1mbin:\033[0m\t{to_bin(get_int, sfillz, raw)}\n"
            sfillz = 0
            res_str = f"{to_bin(get_int, sfillz, raw)}\n"
        elif full == "oct":
            sfillz : int = set_fillz(get_int)
            if not raw:
                res_str = f"\033[1moct:\033[0m\t{to_oct(get_int, sfillz, raw)}\n"
            sfillz = 0
            res_str = f"{to_oct(get_int, sfillz, raw)}\n"
        elif full == "dec":
            sfillz : int = set_fillz(get_int)
            if not raw:
                res_str = f"\033[1mdec:\033[0m\t{to_dec(get_int, sfillz, raw)}\n"
            sfillz = 0
            res_str = f"{to_dec(get_int, sfillz, raw)}\n"
        elif full == "hex":
            sfillz : int = set_fillz(get_int)
            if not raw:
                res_str = f"\033[1mhex:\033[0m\t{to_hex(get_int, sfillz, raw)}\n"
            sfillz = 0
            res_str = f"{to_hex(get_int, sfillz, raw)}\n"

    if len(res_str) > 0:
        return res_str.strip()

    return None


# Command line arguments
def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="bodh", description="Display a number in 4 formats: binary, octal, decimal, and hexadecimal.", epilog="Help and documentation at bodh.github.io"
    )

    parser.add_argument("number", nargs=1, help="The number to format and display; can be either binary, octal, decimal, or hexadecimal. Except for the decimal version, all others must have their respective format prefix (0b, 0o, and 0x).")
    parser.add_argument("-a", "--all", action="store_true", help="Display in the 4 formats, this is the default, can be omitted")
    parser.add_argument("-b", "--bin", action="store_true", help="Display the binary format")
    parser.add_argument("-o", "--oct", action="store_true", help="Display the octal format")
    parser.add_argument("-d", "--dec", action="store_true", help="Display the decimal format")
    parser.add_argument("-x", "--hex", action="store_true", help="Display the hexadecimal format")
    parser.add_argument("-r", "--raw", action="store_true", help="Display raw, without formatting")
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )

    return parser.parse_args()


# Entry point
def main() -> int:
    """Entry point, main function."""
    args: argparse.Namespace = get_args()

    val: str = args.number[0]
    raw: bool = False
    full: str = "all"

    if args.all:
        pass
    if args.bin:
        full = "bin"
    if args.oct:
        full = "oct"
    if args.dec:
        full = "dec"
    if args.hex:
        full = "hex"
    if args.raw:
        raw = True

    val_infos: tuple[str|None, str|None] = parse_format(val)

    if val_infos[0] is None:
        print(f"Invalid argument! The expression \033[1m{val}\033[0m can't be evaluated to one a the required format.\nUse bodh -h to display the help. Exiting now...")
        return EXIT_FAILURE

    res = fmt_and_display(val_infos, raw, full)

    if res is None:
        print(f"An error occured with argument \033[1m{val}\033[0m, it can not be parsed and/or formated. Exiting now...")
        return EXIT_FAILURE

    print(res)
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
