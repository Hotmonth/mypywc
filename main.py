def wc_bytes(filepath):
    with open(filepath, "rb") as f:
        print(len(f.read()))



