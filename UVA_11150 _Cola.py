import sys
def Cola():
    while True:
        bottles = sys.stdin.readline()
        if bottles == "":
            break
        else:
            bottles = int(bottles)
            print(max(_handle(bottles,0,0,0),_handle(bottles,1,1,0),_handle(bottles,2,2,0)))

def _handle(full, empty, mustreturn, alreadydrink):
    if full==0:
        if empty <mustreturn:
            return 0
        else:
            return alreadydrink
    else:
        return _handle((full+empty)//3, (full+empty)%3, mustreturn, alreadydrink+full)


if __name__ == '__main__':
    Cola()