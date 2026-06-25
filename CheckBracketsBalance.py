def check_brackets(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for i, ch in enumerate(s, start=1):
        if ch in '([{':
            stack.append((ch, i))
        elif ch in ')]}':
            if not stack:
                return f"Extra closing '{ch}' at position {i}"
            open_ch, open_pos = stack.pop()
            if pairs[ch] != open_ch:
                return (
                    f"Mismatched '{open_ch}' at position {open_pos} "
                    f"closed by '{ch}' at position {i}"
                )

    if stack:
        open_ch, open_pos = stack[-1]
        return f"Unclosed '{open_ch}' opened at position {open_pos}"

    return "All brackets are balanced"


# Example usage
# expr = """list.countvalid(Samples.GetRange(Lsm.[CLI001CL01_R_113 Ferry Rd_MICRO].[CLI001CL01_R_113 Ferry Rd_MICRO].[E.coli_E_MF_Water_100ML_SMEWW 9222K [ELS]]], (0 - 6), 0))"""

try:
    with open("input.txt", "r", encoding="utf-8") as file:
        expr = file.read()
except FileNotFoundError:
    print("ERROR: input.txt not found. Please create the file with the expression to check.")
    exit(1)

print(check_brackets(expr))

