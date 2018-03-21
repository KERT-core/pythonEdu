import hashlib

def solution(password):
    password = password.encode()
    for i in range (0, 2):
        password = hashlib.sha224(password).hexdigest()
        password = password.encode()
        print(password)
    return hashlib.sha224(password).hexdigest()

if __name__ == "__main__":
    print(solution('baegopa'))
