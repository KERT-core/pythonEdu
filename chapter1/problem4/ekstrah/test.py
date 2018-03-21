from solutions import solution
import os

def test_case_1():
    heightList = [4, 10]
    assert solution(heightList) == 4

def test_case_2():
    heightList = [25, 15]
    assert solution(heightList) == 15

def test_case_3():
    heightList = [25, 15, 18]
    assert solution(heightList) == 36

def test_case_4():
    heightList = [8, 10, 12, 29]
    assert solution(heightList) == 24

if __name__ == "__main__":
    os.system("py.test test.py")
