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


def wc(argv):
    output = "  "
    options = argv[1:-1]
    filepath = argv[-1]

    if not options:
        output = f"  {wc_bytes(filepath)} {wc_newline(filepath)} {wc_word_count(filepath)} {wc_char_count(filepath)} {filepath}"
        return output
    options = options[0]
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
