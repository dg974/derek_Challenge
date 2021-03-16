from math import sqrt

def parse_input_line(s):
    s = s.strip()
    words = s.split(' ')
    words = [x for x in words if len(x) > 0] # since strip doesn't remove extraneous spaces between the words
    try:
        if len(words) != 2:
            raise Exception()
        (a, b) = words
        return complex(float(a), float(b))
    except Exception as e:
        print(e)
        raise ValueError(f"Expected 2 numbers in input string, got: {','.join(words)}")

# Hackerrank intends for you to make a Complex data type and override __add__, __sub__, __str__, etc
# This is easy enough to do, except Python has a Complex data type built in to the stdlib ;)
# I choose to use that because I believe anything in the stdlib is fair game (especially in the global namespace)
# Otherwise, am I supposed to write my own sqrt function? etc.
# Not to mention, if it comes in the stdlib, I _probably_ don't need to write a test for it :)
def complex_mod(c):
    mod = sqrt(c.real**2 + c.imag**2)
    return complex(mod, 0) # The problem asks for the mod to be printed as a complex number

def format_complex_number(c):
    operator = "+" if c.imag >= 0 else "" # if negative, c.imag will be printed with a - so a minus isn't necessary
    return f'{c.real:.2f}{operator}{c.imag:.2f}i'

# I move this to its own function simply so I can write a test for it. It's simple enough it could go in __main__
def generate_output(c1, c2):
    outputs = [
        c1 + c2,
        c1 - c2,
        c1 * c2,
        c1 / c2,
        complex_mod(c1),
        complex_mod(c2),
    ]
    s = "\n".join([format_complex_number(c) for c in outputs])
    return s + "\n" # don't forget trailing new-line

if __name__ == "__main__":
    c1 = parse_input_line(raw_input())
    c2 = parse_input_line(raw_input())
    print(generate_output(c1, c2))