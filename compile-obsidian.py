#!/usr/bin/env python3

import os,sys, re
from pathlib import Path

def find_file(fn):
    p = Path('.')
    try:
        return next(p.rglob(fn))
    except StopIteration:
        raise FileNotFoundError


def get_file_contents(m):
    filename=f"{m.group(1)}.md"

    try:
        filepath=find_file(filename)
        
        with open(filepath) as fp:
            return process(fp.read())
    except FileNotFoundError:
        return 

def replace_refs(txt):
    return re.sub(r"\[{2}([^\]]+)\]{2}", r"\g<1>", txt)

def replace_inserts(txt):
    return re.sub(r"!\[{2}([^\]]+)\]{2}", get_file_contents, txt)

def process(txt):
    return replace_refs(replace_inserts(txt))


if(len(sys.argv) == 1):
    print("USAGE:\n\tPWD should be the root of the vault.\n\tcompile-obsidian.py [PATH TO FILE RELATIVE TO PWD]")
    exit()

with open(sys.argv[1]) as fp:
    print(process(fp.read()))



