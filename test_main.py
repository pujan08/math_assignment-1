import write_your_name as name_point

def test_hi_my_name_is():
    assert len(name_point.hi_my_name_is()) > 1

def test_name_value():
    assert name_point.value == "Pujan Bhatt" or name_point.value == "No name provided"
