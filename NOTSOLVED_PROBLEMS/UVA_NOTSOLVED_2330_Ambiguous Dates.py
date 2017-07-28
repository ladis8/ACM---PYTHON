from sys import stdin

dividors =['/', '\\', '.', ',', '-']

monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
notleapyear = 365
leapyear = 366



def validyear(year):
    return True if year >= 1700 and year <= 2229 else False

def validmonth (month):
    return True if month >=1 and month <=12 else False

def validday(day, month, year):
    m = 29 if month == 2 and year%4 == 0 else monthdays[month]
    return True if day>=1 and day <= m else False

def validate (year, month, day):
    if validyear(year) and validmonth(month) and validday(day, month,year):
            return True
    return False


def countdifficult(s):
    if (len(s) >8 or len(s) <6):



def counteasy(s, index):
    global split


    dividor = s[index]
    parts = s.split(dividor)
    if len (parts) != 3:
        print("Illegal date")
    else:
        parts = list (map(int, parts))
        suc = False


        if validate(parts[0], parts[1], parts[2]):
            print (countfrombeggining (parts[0], parts[1], parts[2])-split)
            suc =True
        if validate(parts[0], parts[2], parts[1]):
            print(countfrombeggining(parts[0], parts[2], parts[1]) - split)
            suc = True

        if validate(parts[1], parts[0], parts[2]):
            print(countfrombeggining(parts[1], parts[0], parts[2]) - split)
            suc = True
        if validate(parts[1], parts[2], parts[0]):
            print(countfrombeggining(parts[1], parts[2], parts[0]) - split)
            suc = True

        if validate(parts[2], parts[0], parts[1]):
            print(countfrombeggining(parts[2], parts[0], parts[1]) - split)
            suc = True
        if validate(parts[2], parts[1], parts[0]):
            print(countfrombeggining(parts[2], parts[1], parts[0]) - split)
            suc = True
        if not suc:
            print("Illegal date")









def divide (s):
    for i in range (len(s)):
        if s[i] in dividors:
            counteasy(s, i)
            break

def countfrombeggining(year, month, day):
    out = 0
    leap = False

    for y in range(1700, year):
        if y % 4 ==0:
            if y%100 == 0:
                out+=notleapyear
            else:
                out+=leapyear
                leap = True
        else:
            out+=notleapyear


    for i in range (1, month):
        out+=monthdays[i-1]

    if leap or (year%100 != 0 and year%4==0):
        out += 1

    for d in range (1, day+1):#exclude
        out+=1

    print(out)
    return out








inityear =2001
initmonth = 11
initday = 4
split = countfrombeggining(inityear,initmonth,initday)

t = int (input())
for i in range (t):
    s = input()
    divide(s)
