from solutions import solution
import os
from restGetLib import httpGetReq

def test_case_1():

    answer = httpGetReq(5)
    assert solution('korea') == answer

if __name__ == "__main__":
    os.system("py.test test.py")
