from solutions import solution
import os

def test_case_1():
    answer = b'$2b$12$hVEug1duGIuQotj37kGtUOH7P.qSSCePZyaHJy6IAbuOxbl0mWxFO'
    assert solution('korea') == answer
    
if __name__ == "__main__":
    os.system("py.test test.py")
