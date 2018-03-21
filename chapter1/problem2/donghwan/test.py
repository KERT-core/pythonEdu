from solutions import solution
import os

def test_case_1():
    test_case = [1, 1, 2]
    assert solution(test_case) == 2

def test_case_2():
    test_case = [1, 1, 1, 1, 1]
    assert solution(test_case) == 1

def test_case_3():
    test_case = ['a', 'b', 'a', 'c', 'd', 'e', 'e', 'z']
    assert solution(test_case) == 6

def test_case_4():
    test_case = ['dog', 'cat', 'pudding', 'cat', 'pizza', 'soju', 'dog', 'dog', 'hamburger']
    assert solution(test_case) == 6

def test_case_5():
    test_case = []
    assert solution(test_case) == 0



if __name__ == "__main__":
    os.system("py.test test.py")