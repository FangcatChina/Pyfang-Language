import time
import os
import turtle as tu
bl = []
bls = []
def valuecheck(checks):
    if checks in bl:
        return(bls[bl.index(checks)])
    try:
        return(int(checks))
    except:
        try:
            return(float(checks))
        except:
            if checks == 'bool;True' or checks == 'bool;False' or checks.split(';')[0] == 'bool':
                if bool(checks.split(';')[1]) == True:
                    return(True)
                else:
                    return(False)
            else:
                if list(checks)[0] == "'" and list(checks)[-1] == "'":
                    return(str(checks.split("'")[1]))
                elif checks == 'input':
                    return(input())
                elif checks.split(' ')[0] == 'if':
                    if valuecheck(checks.split(' ')[1]) == checks.split(' ')[2]:
                        print(True)
                    else:
                        print(False)
                else:
                    return('ValueError!')
def pyfangrun(command):
    splited = command.split(' ')
    if len(splited) >= 2:
        if splited[1] == '=':
            if splited[0] in bl:
                blj = bl.index(splited[0])
                bls.pop(blj)
                bls.insert(blj-1,splited[2])
            else:
                bl.append(splited[0])
                bls.append(valuecheck(splited[2]))
        elif splited[0] == 'print' and len(splited) < 3:
            print(valuecheck(splited[1]))
        elif splited[0] == 'print':
            print(valuecheck(splited[1]))
        elif splited[0] == 'fd':
            tu.fd(int(splited[1]))
        elif splited[0] == 'back':
            tu.back(int(splited[1]))
        elif splited[0] == 'head':
            tu.setheading(int(splited[1]))
        elif splited[0] == 'color':
            tu.pencolor(splited[1])
        elif splited[0] == 'dot':
            tu.dot(int(splited[1]))
        elif splited[0] == 'size':
            tu.pensize(int(splited[1]))
        elif splited[0] == 'right':
            tu.right(int(splited[1]))
        elif splited[0] == 'left':
            tu.left(int(splited[1]))
        elif splited[0] == 'goto':
            tu.goto(int(splited[1]),int(splited[2]))
    elif splited[0] == 'down':
        tu.pendown()
    elif splited[0] == 'up':
        tu.penup()
    elif splited[0] == 'clear':
        tu.clear()
print('''
  _____        __                  
 |  __ \      / _|                 
 | |__) |   _| |_ __ _ _ __   __ _ 
 |  ___/ | | |  _/ _` | '_ \ / _` |
 | |   | |_| | || (_| | | | | (_| |
 |_|    \__, |_| \__,_|_| |_|\__, |
         __/ |                __/ |
        |___/                |___/ 
''')
print('''
Pyfang 2.7-pre Copyright by Fangcat(Fang.Zixian)
Loading....
''')
cmd = []
time.sleep(2)
print('Enter your command:')
while True:
    a = input()
    if a == 'startrun':
        print('Running Pyfang file...')
        for i in cmd:
            pyfangrun(i)
        print('Run is end')
    elif a.split(' ')[0] == 'save':
        f = open(a.split(' ')[1], 'w', encoding='utf-8')
        for i in cmd:
            f.write(i)
            f.write('|')
    elif a.split(' ')[0] == 'runfile':
        f = open(a.split(' ')[1],'r',encoding='utf-8')
        print('Running Pyfang file...')
        for i in f.readlines()[0].split('|'):
            pyfangrun(i)
        print('Run is end')    
    else:
        cmd.append(a)
