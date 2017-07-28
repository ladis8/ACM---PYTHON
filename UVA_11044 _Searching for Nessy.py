import sys
def Nessy():
    t = int (input())

    for _ in range (t):
        [m,n] = list(map (int,sys.stdin.readline().split()))
        m-=2
        n-=2
        print((m//3 + ( 0 if m%3==0 else 1)) * (n//3 + (0 if n%3==0 else 1)))



if __name__ == '__main__':
    Nessy()