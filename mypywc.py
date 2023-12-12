import sys


def wc_bytes(filepath):
    with open(filepath, "rb") as f:
        return len(f.read())


def wc_newline(filepath):
    with open(filepath, "r") as f:
        return f.read().count('\n')


def wc_word_count(filepath):
    with open(filepath, "r") as f:
        return len(f.read().split())


def wc_char_count(filepath):
    with open(filepath, "r", newline='') as f:
        return len(f.read())


def parse_arguments(argv):
    args = argv[1:]
    length = len(args)
    if length == 0:
        return None, None
    if length == 1:
        if args[0][0] == '-':
            return args[0], input("Enter a path to file: ")
        else:
            return [-1], args[0]

    return args[0], args[1]


def wc(argv):
    output = "  "
    if len(argv) > 3:
        return "Too many arguments"
    options, filepath = parse_arguments(argv)
    if options == [-1]:
        output = f"  {wc_bytes(filepath)} {wc_newline(filepath)} {wc_word_count(filepath)} {filepath}"
        return output

    if 'c' in options:
        output += f"{wc_bytes(filepath)} "
    if 'l' in options:
        output += f"{wc_newline(filepath)} "
    if 'w' in options:
        output += f"{wc_word_count(filepath)} "
    if 'm' in options:
        output += f"{wc_char_count(filepath)} "
    output += filepath

    return output


if __name__ == '__main__':
    print(wc(sys.argv))
