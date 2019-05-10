"""
Just useful utilities i've needed more than once in my career
"""


def column_num_to_excel_letters(num, zero_index=True):
    """
    Function to turn a column number (0 or 1 based index) into an excel worksheet letter combination
    :param num:
    :param zero_index:
    :return:
    """
    BASE = 26
    char_int = ord('A')

    if not zero_index:
        num -= 1

    if num < 0:
        raise ValueError('Number must be positive. Check that the zero index flag is set correctly')

    (mag, non_mag) = divmod(num, BASE)

    if mag == 0:
        return chr(char_int + non_mag)
    else:
        return column_num_to_excel_letters(mag-1) + column_num_to_excel_letters(non_mag)


def test_column_num_to_excel_letters():
    assert column_num_to_excel_letters(0) == 'A'
    assert column_num_to_excel_letters(1, False) == 'A'
    assert column_num_to_excel_letters(26, False) == 'Z'
    assert column_num_to_excel_letters(26) == 'AA'
    assert column_num_to_excel_letters(27) == 'AB'
    assert column_num_to_excel_letters(28, False) == 'AB'
    assert column_num_to_excel_letters(26*2) == 'BA'
    assert column_num_to_excel_letters(26*26 + 26*3 + 4) == 'ACE'
    assert column_num_to_excel_letters(26*26 + 26*3 + 4, False) == 'ACD'

test_column_num_to_excel_letters()