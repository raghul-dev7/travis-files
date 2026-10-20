from app import add, check_eligibility

def test_add():
    assert add(5, 3) == 8

def test_eligible():
    assert check_eligibility(20) == "Eligible"

def test_not_eligible():
    assert check_eligibility(16) == "Not Eligible"