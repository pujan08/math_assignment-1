import write_your_name as name_point

def test_hi_my_name_is():
    assert len(name_point.hi_my_name_is()) > 1


if __name__ == "__main__":
    test_hi_my_name_is()
    print("All tests passed.")
    print(f"{name_point.value}")