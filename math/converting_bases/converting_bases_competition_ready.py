# If base below 62, treat as string
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def from_base(s, b):
    val = 0
    for c in s:
        val = val * b + DIGITS.index(c)
    return val

def to_base(x, b):
    if x == 0:
        return "0"
    out = []
    while x > 0:
        out.append(DIGITS[x % b])
        x //= b
    return "".join(reversed(out))

def convert_base(s, b1, b2):
    return to_base(from_base(s, b1), b2)



# IF base above 62, treat as list
def from_base_list(digits, base):
    val = 0
    for d in digits:
        assert 0 <= d < base
        val = val * base + d
    return val

def to_base_list(x, base):
    if x == 0:
        return [0]
    out = []
    while x > 0:
        out.append(x % base)
        x //= base
    return out[::-1]

def convert_base_list(digits, b1, b2):
    return to_base_list(from_base_list(digits, b1), b2)
