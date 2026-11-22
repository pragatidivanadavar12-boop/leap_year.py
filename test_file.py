from leap_year import is_leap_year
def test_leap_year():
    assert is_leap_year(2024) == True
def test_non_leap_year():
    assert is_leap_year(2023) == False
def test_divisible_by_400():
    assert is_leap_year(2000) == True
def test_divisible_by_100():
    assert is_leap_year(1900) == False
def test_next_leap_year():
    assert is_leap_year(2028) == True
def test_century_year():
    assert is_leap_year(2100) == False
