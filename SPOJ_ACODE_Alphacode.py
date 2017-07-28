import sys
def alphacode():

    while True:
        array = sys.stdin.readline()
        array = array.strip()
        if array == '0':
            break
        else:
            a = int(array[0])
            b = int(array[1])
            r = 2

            if a > 2 and b == 0:
                print("0")
            else:
                if b == 0:
                    notshared = 0
                    shared = 1
                    r = 3
                elif (a * 10 + b) > 26:
                    notshared = 0
                    shared = 1
                else:
                    shared = notshared = 1

                for i in range(r, len(array)):
                    # print(shared)
                    # print(notshared)
                    a = int(array[i - 1])
                    b = int(array[i])
                    if (a == 0 and b == 0) or (a > 2 and b == 0) or a == 0:
                        print("0")
                    elif b == 0:
                        notshared = 0
                        i += 1
                    elif (a * 10 + b) > 26:
                        shared += notshared
                        notshared = 0
                    else:
                        shared, notshared = (shared + notshared), shared
                print(shared +notshared)

if __name__ == '__main__':
    alphacode()