from solutions import isMatch
import os

def test_case_1():
    matchA = "aa"
    matchB = "a"
    assert isMatch(matchA, matchB) == False

def test_case_2():
    matchA = "aa"
    matchB = "*"
    assert isMatch(matchA, matchB) == True


if __name__ == "__main__":
    os.system("py.test test.py")