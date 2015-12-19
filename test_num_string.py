import pytest
import num_string

@pytest.mark.parametrize('input,expected', [    
    (1, 'ZERO AND ONE'),
    (12, 'ZERO AND TWELVE'),
    (65, 'ZERO AND SIXTY FIVE'),
    (400, 'FOUR AND ZERO'),
    (543, 'FIVE AND FORTY THREE'),
    (2424, 'TWENTY FOUR AND TWENTY FOUR'),
    (7823, 'SEVENTY EIGHT AND TWENTY THREE'),
    (73219, 'SEVEN HUNDRED THIRTY TWO AND NINETEEN'),
    (32424, 'THREE HUNDRED TWENTY FOUR AND TWENTY FOUR'),
])

def test_test(input, expected):
    result = num_string.text_from_num(input)
    assert(result == expected)