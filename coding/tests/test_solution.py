from solution.main import parse_input_line, format_complex_number, complex_mod, generate_output
import pytest

def test_parseinputline_success():
    c = parse_input_line('     1.23     4.56   ')
    assert(c.real == 1.23)
    assert(c.imag == 4.56)

def test_parseinputline_fail_too_many_inputs():
    with pytest.raises(ValueError):
        parse_input_line('1 2 3')

def test_parseinputline_fail_contains_non_number():
    with pytest.raises(ValueError):
        parse_input_line('1 a')

def test_formatcomplexnumber():
    c = complex(1.23, 4.56)
    assert format_complex_number(c) == '1.23+4.56i'

# https://www.math-only-math.com/modulus-of-a-complex-number.html
def test_complexmod():
    examples = [
        (complex(6, 8), 10),
        (complex(-6, 8), 10),
        (complex(6, -8), 10),
    ]
    for c, mod_c in examples:
        assert complex_mod(c) == mod_c

# From the problem page
def test_generateoutput():
    c1 = complex(2, 1)
    c2 = complex(5, 6)
    expected = """7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
"""
    actual = generate_output(c1, c2)
    assert expected == actual