import pytest
import num_string

def test_test():
    result = num_string.text_from_num(400)
    assert(result == 'FOUR AND ZERO')