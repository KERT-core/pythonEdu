from solutions import solution
import os

def test_case_1():
    assert solution(123) == 321

def test_case_2():
     assert solution(-123) == -321

def test_case_3():
    assert solution(120) == 21

def test_case_4():
    assert solution(-1827) == -7281

def test_case_5():
    assert solution(0) == 0

def test_case_6():
    assert solution(-0) == 0

if __name__ == "__main__":
    os.system("py.test test.py")