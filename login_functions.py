import hashlib as _hash_

def hashInput(input):
    return _hash_.md5(input.encode('utf-8')).hexdigest()

def login():
    print("Start Login")
    
    print("Enter your name")
    name = input().lower() # SeRgey  -->  SERGEY
    print("Enter your pass")    
    password = input()
    
    with open("user.db", "r") as f:
        passwordsData = f.readlines()
    passList = [line.strip() for line in passwordsData]
    
    hashNameAndPass = hashInput(name+password)

    if hashNameAndPass in passList:
        print("Welcome!")
    else: print("Invalid name or password!")


def register():
    print("Start Register")
    
    print("Enter your name")
    name = input().lower()
    print("Enter your pass")
    password = input()

    passFile = open("user.db", "a")
    passFile.write(hashInput(name+password)+'\n')
    passFile.close()
    print("Registration successful!")