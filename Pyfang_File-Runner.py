import easygui as es
import turtle as tu
import tkinter as tk
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
                elif checks.split('#')[0] == 'if':
                    if valuecheck(checks.split('#')[1]) == valuecheck(checks.split('#')[2]):
                        return(True)
                    else:
                        return(False)
                elif checks == 'enter':
                    return(es.enterbox('Enter'))
                elif checks == 'list':
                    return(lista)
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
        elif splited[0] == 'print':
            t1.color('green')
            t1.write(valuecheck(splited[1]),font=('arial',12))
            t1.setheading(-90)
            t1.penup()
            t1.fd(24)
        elif splited[0] == 'fd':
            t2.fd(int(splited[1]))
        elif splited[0] == 'back':
            t2.back(int(splited[1]))
        elif splited[0] == 'head':
            t2.setheading(int(splited[1]))
        elif splited[0] == 'color':
            t2.pencolor(splited[1])
        elif splited[0] == 'dot':
            t2.dot(int(splited[1]))
        elif splited[0] == 'size':
            t2.pensize(int(splited[1]))
        elif splited[0] == 'right':
            t2.right(int(splited[1]))
        elif splited[0] == 'left':
            t2.left(int(splited[1]))
        elif splited[0] == 'goto':
            t2.goto(int(splited[1]),int(splited[2]))
        elif splited[0] == 'msgbox':
            es.msgbox(valuecheck(splited[1]),valuecheck(splited[2]),valuecheck(splited[3]))
        elif splited[0] == 'listadd':
            lista.append(valuecheck(splited[1]))
        elif splited[0] == 'listpop':
            lista.remove(valuecheck(splited[1]))
        else:
            es.msgbox("NameError: name "+splited[0]+"' is not defined",'Error')
    elif splited[0] == 'down':
        t2.pendown()
    elif splited[0] == 'up':
        t2.penup()
    elif splited[0] == 'clear':
        t2.clear()
    else:
        es.msgbox("NameError: name "+splited[0]+"' is not defined",'Error')
cmd = []
r = tu._Root()
r.set_geometry(800,800,0,0)
cv2 = tu.ScrolledCanvas(r)
cv2.pack(expand = True, fill = tk.BOTH)
cv2.reset(400, 4000)
t1 = tu.RawPen(cv2)
cv3 = tu.ScrolledCanvas(r)
cv3.pack(expand = True, fill = tk.BOTH)
cv3.reset(400, 400)
t2 = tu.RawPen(cv3)
t2.shape('turtle')
t1.hideturtle()
t1.penup()
t1.goto(-350,100)
t1.color('green')
t1.write('''
  _____        __                  
 |  __ \      / _|                 
 | |__) |   _| |_ __ _ _ __   __ _ 
 |  ___/ | | |  _/ _` | '_ \ / _` |
 | |   | |_| | || (_| | | | | (_| |
 |_|    \__, |_| \__,_|_| |_|\__, |
         __/ |                __/ |
        |___/                |___/ 
Pyfang 3.1 Copyright by Fangcat(Fang.Zixian)
Using packages:Turtle,Easygui
''',font=('arial',12))
t1.setheading(-90)
t1.penup()
t1.fd(24)
t1.color('purple')
while True:
    a = es.enterbox('Enter your command here','Pyfang')
    t1.color('purple')
    t1.write(a,font=('arial',12))
    t1.setheading(-90)
    t1.penup()
    t1.fd(24)
    if a == 'startrun':
        lista = []
        t1.color('blue')
        t1.write('Running...',font=('arial',12))
        t1.setheading(-90)
        t1.penup()
        t1.fd(24)
        for i in cmd:
            pyfangrun(i)
        t1.color('blue')
        t1.write('Run was end',font=('arial',12))
        t1.setheading(-90)
        t1.penup()
        t1.fd(24)
        t1.color('purple')
    elif a.split(' ')[0] == 'save':
        f = open(a.split(' ')[1], 'w', encoding='utf-8')
        for i in cmd:
            f.write(i)
            f.write('|')
    elif a.split(' ')[0] == 'runfile':
        f = open(a.split(' ')[1],'r',encoding='utf-8')
        t1.color('blue')
        t1.write('Running...',font=('arial',12))
        t1.setheading(-90)
        t1.penup()
        t1.fd(24)
        for i in f.readlines()[0].split('|'):
            pyfangrun(i)
        t1.color('blue')
        t1.write('Run was end',font=('arial',12))
        t1.setheading(-90)
        t1.penup()
        t1.fd(24)
        t1.color('purple')
    elif a == 'listcode':
        t1.color('orange')
        t1.write(cmd,font=('arial',12))
        t1.setheading(-90)
        t1.penup()
        t1.fd(24)
        t1.color('purple')   
    else:
        cmd.append(a)
