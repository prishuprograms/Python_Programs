import string
import random
if __name__ == "__main__":
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
while True:
    p_len = int(input("Enter password length :\n"))
    if not p_len.__int__():
        print("Wrong entry !!")
        break
    else : pass
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    print("Your password is :")
    print("".join(random.sample(s, p_len)))
    # Alternate :
    # print("".join(s[0:p_len]))