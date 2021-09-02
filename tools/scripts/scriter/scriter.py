#!/usr/bin/python

import os
import sys

NEXT = "<h>"

scriter_src_path = os.environ["SCRITER_SRC_PATH"]
meta_path = scriter_src_path + "/.scriter/"
src_path_path = os.path.join(meta_path, "src")
entry_path = os.path.join(meta_path, "entry")

# scriter.py init_persistence
def init_persistence():
    try:
        os.mkdir(meta_path)
    except OSError:
        pass
    
    src_path = open(src_path_path, "w+")
    src_path.close()

    entry = open(entry_path, "w+")
    entry.close()

# scriter.py reset
def reset():
    entry = open(entry_path, "w")
    entry.write("0")
    entry.close()
    
# scriter.py use <filepath>
def use(args):
    src_path = open(src_path_path, "w")
    src_path.write(os.path.abspath(args[2]))
    src_path.close()
    reset()

def get_src():
    try:
        src_path = open(src_path_path, "r")
    except IOError:
        print("Source Path File Does Not Exist")
        exit()
    try:
        src = open(src_path.read(), "r")
    except IOError:
        print("Source File Not Found Or Not Set")
        exit()
    src_path.close()
    return src

def get_start_line_num():
    try:
        entry = open(entry_path, "r")
    except IOError:
        print("Entry Num File Does Not Exist")
        exit()
    start_line_num = int(entry.read())
    if start_line_num == -1:
        print("Reached EOF")
        exit()
    entry.close()
    return start_line_num;

# scriter.py iterate
def iterate():
    src = get_src()
    src_contents = enumerate(src)
    
    start_line_num = get_start_line_num()
    
    line_num, line = src_contents.next()

    assert line[0:len(NEXT)] == NEXT

    # go past start line
    while line_num <= start_line_num:
        try:
            line_num, line = src_contents.next()
        except StopIteration:
            entry = open(entry_path, "w")
            print("Reached EOF")
            entry.write("-1")
            exit()

    # continue until next NEXT
    while line[0:len(NEXT)] != NEXT:
        try:
            line_num, line = src_contents.next()
        except StopIteration:
            entry = open(entry_path, "w")
            print("Reached EOF")
            entry.write("-1")
            exit()

    src.close()

    entry = open(entry_path, "w")
    entry.write(str(line_num))
    entry.close()

# scriter.py info
def info():
    src = get_src()
    src_contents = enumerate(src)
    
    start_line_num = get_start_line_num()
    
    line_num, line = src_contents.next()

    assert line[0:len(NEXT)] == NEXT

    # go past start line
    while line_num <= start_line_num:
        try:
            line_num, line = src_contents.next()
        except StopIteration:
            break

    # continue until next NEXT
    while line[0:len(NEXT)] != NEXT:
        print(line[:-1])
        try:
            line_num, line = src_contents.next()
        except StopIteration:
            break
    
    src.close()

def main(args):
    if len(args) == 1:
        raise Exception("No Command Specified")
    if args[1] == "init_persistence":
        init_persistence()
    else:
        if args[1] == "reset":
            reset()
        elif args[1] == "use":
            use(args)
        elif args[1] == "iter":
            iterate()
        elif args[1] == "info":
            info()
        elif args[1] == "next":
            iterate()
            info()
        else:
            raise Exception("Command " + args[1] + " Unrecognized")

if __name__ == "__main__":
    main(sys.argv)
