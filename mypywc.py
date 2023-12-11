import argparse
import sys


def get_parser():
    parser = argparse.ArgumentParser(
        description="My implementation of wc command",
        epilog="By Medet Ramazan"
    )

    parser.add_argument("-c")
    parser.add_argument("-l")
    parser.add_argument("-w")

    return parser


def wc_bytes(filepath):
    with open(filepath, "rb") as f:
        return len(f.read())


def wc_newline(filepath):
    with open(filepath, "r") as f:
        return f.read().count('\n')


def wc_word_count(filepath):
    with open(filepath, "r") as f:
        return len(f.read().split())


def main(raw_args=None):
    parser = get_parser()
    args = parser.parse_args()
    if args.c:
        print(wc_bytes(args.c), args.c)
    if args.l:
        print(wc_newline(args.l), args.l)
    if args.w:
        print(wc_word_count(args.w), args.w)


if __name__ == '__main__':
    main(sys.argv)
