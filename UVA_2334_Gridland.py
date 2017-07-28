
def init ():
    t = int (input())
    for i in range(t):
        a,b = list(map(int,input().split()))
        print("Scenario #%d:" %(i+1))
        print ("%.2f\n" %(a*b + 0.41 if a%2==1 and b%2==1 else a*b))
init()