''' Quick Test for TDD '''

def test(func, expected_value):
    recieved_value = func
    print(" PASSED: {}".format(recieved_value) if recieved_value == expected_value else "FAILED:\n Expected: {} \n Recieved: {} ".format(expected_value, recieved_value))
