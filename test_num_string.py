import pytest
import num_string

@pytest.mark.parametrize('input,expected', [
    (1, 'ZERO AND ONE'),
    (12, 'ZERO AND TWELVE'),
    (65, 'ZERO AND SIXTY FIVE'),
    (400, 'FOUR AND ZERO'),
    (313, 'THREE AND THIRTEEN'),
    (543, 'FIVE AND FORTY THREE'),
    (2424, 'TWENTY FOUR AND TWENTY FOUR'),
    (1918, 'NINETEEN AND EIGHTEEN'),
    (7823, 'SEVENTY EIGHT AND TWENTY THREE'),
    (6000, 'SIXTY AND ZERO'),
    (70000, 'SEVEN HUNDRED AND ZERO'),
    (13142, 'ONE HUNDRED THIRTY ONE AND FORTY TWO'),
    (73219, 'SEVEN HUNDRED THIRTY TWO AND NINETEEN'),
    (32424, 'THREE HUNDRED TWENTY FOUR AND TWENTY FOUR'),
    (71516, 'SEVEN HUNDRED FIFTEEN AND SIXTEEN'),
    (100000, 'ONE THOUSAND AND ZERO'),
    (601213, 'SIX THOUSAND TWELVE AND THIRTEEN'),
    (478293, 'FOUR THOUSAND SEVEN HUNDRED EIGHTY TWO AND NINETY THREE'),
    (5000000, 'FIFTY THOUSAND AND ZERO'),
    (1400001, 'FOURTEEN THOUSAND AND ONE'),
    (1800216, 'EIGHTEEN THOUSAND TWO AND SIXTEEN'),
    (3131118, 'THIRTY ONE THOUSAND THREE HUNDRED ELEVEN AND EIGHTEEN'),
    (9965467, 'NINETY NINE THOUSAND SIX HUNDRED FIFTY FOUR AND SIXTY SEVEN'),
    (70000000, 'SEVEN HUNDRED THOUSAND AND ZERO'),
    (71421518, 'SEVEN HUNDRED FOURTEEN THOUSAND TWO HUNDRED FIFTEEN AND EIGHTEEN'),
    (83248293, 'EIGHT HUNDRED THIRTY TWO THOUSAND FOUR HUNDRED EIGHTY TWO AND NINETY THREE')
])

def test_standard(input, expected):
    result = num_string.text_from_num(input)
    print(result)
    assert result == expected

def test_lower_bound():
    with pytest.raises(ValueError):
        num_string.text_from_num(0)

def test_upper_bound():
    with pytest.raises(ValueError):
        num_string.text_from_num(100000000)
        