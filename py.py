import random
def toord(text):
    ords=''
    for char in text:
        ords+=('chr('+gof(addr_(ord(char)))+')')+'+'
    return addrc(ords[:-1])
def gof(text):
    text=str(text)
    ords=''
    for char in text:
        ords+=('chr('+str(addr_(ord(char)))+')')+'+'
    return addrc('int('+ords[:-1]+')')
def addrc(text):
    rannum=random.randint(1,5)
    return ('('*rannum)+text+(')'*rannum)
def addr_(text:int):
    strtext=str(text)
    return '_'.join(list(strtext))
def run(text):
    return addrc(toord(text))
# print(run('hello world'))

'hello world'

def print_color(color, message):
    if color.lower() == "red":
        print("\033[31m%s\033[0m" % message,end='')
    elif color.lower() == "green":
        print("\033[32m%s\033[0m" % message,end='')
    elif color.lower() == "yellow":
        print("\033[33m%s\033[0m" % message,end='')
    elif color.lower() == "blue":
        print("\033[34m%s\033[0m" % message,end='')
    elif color.lower() == "purple":
        print("\033[35m%s\033[0m" % message,end='')
    elif color.lower() == "skyblue":
        print("\033[36m%s\033[0m" % message,end='')
    elif color.lower() == "white":
        print("\033[37m%s\033[0m" % message,end='')
    else:
        print("\033[31m%s\033[0m" % "err color")

print_color("color", "text")

(((((((((chr(((int(chr(4_9)+chr(9_5)+chr(4_8)+chr(9_5)+chr(5_2)))))+chr((int(chr(4_9)+chr(9_5)+chr(4_8)+chr(9_5)+chr(4_9))))+chr((((int(chr(4_9)+chr(9_5)+chr(4_8)+chr(9_5)+chr(5_6))))))+chr((((((int(chr(4_9)+chr(9_5)+chr(4_8)+chr(9_5)+chr(5_6))))))))+chr((((((int(chr(4_9)+chr(9_5)+chr(4_9)+chr(9_5)+chr(4_9))))))))+chr((((((int(chr(5_1)+chr(9_5)+chr(5_0))))))))+chr(((int(chr(4_9)+chr(9_5)+chr(4_9)+chr(9_5)+chr(5_7)))))+chr((int(chr(4_9)+chr(9_5)+chr(4_9)+chr(9_5)+chr(4_9))))+chr(((((int(chr(4_9)+chr(9_5)+chr(4_9)+chr(9_5)+chr(5_2)))))))+chr(((((int(chr(4_9)+chr(9_5)+chr(4_8)+chr(9_5)+chr(5_6)))))))+chr(((int(chr(4_9)+chr(9_5)+chr(4_8)+chr(9_5)+chr(4_8))))))))))))))