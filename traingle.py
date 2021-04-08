import os

def triangle(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
n = os.environ.get('TR_NUMBER')
# TR_NUMBER=8 python3 traingle.py
# docker run -e TR_NUMBER=7 bff2ba77dbd1

nn = int(n)
triangle(nn)
