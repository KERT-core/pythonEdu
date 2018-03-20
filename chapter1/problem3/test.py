from solutions import solution
import os

def test_case_1():
    assert solution(2, 4) == 16

def test_case_2():
    assert solution(2.00000, 10) == 1024.0000

def test_case_3():
    assert solution(2.10000, 3) == 9.261000000000001


if __name__ == "__main__":
    os.system("py.test test.py")