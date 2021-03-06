'''
This project using MIT Open Source Agreement.
'''
import RPi.GPIO as RPi
import easygui as es
import turtle as tu
import tkinter as tk
import random as rd
import webbrowser as web
import os
import time
from wsgiref.simple_server import make_server
bl = []
bls = []
lista = []
GPIOset = []
def send(environ, start_response):    #This function was coded by 无情天魔精致 on Baidu.Thanks:P.
    start_response('200 OK', [('Content-Type', 'text/html')])
    return fileshttp      
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
                elif checks.split('#')[0] == 'if':
                    if valuecheck(checks.split('#')[1]) == valuecheck(checks.split('#')[2]):
                        return(True)
                    else:
                        return(False)
                elif checks == 'enter':
                    return(es.enterbox('Enter'))
                elif checks == 'list':
                    return(lista)
                elif checks.split('#')[0] == 'randint':
                    return(rd.randint(valuecheck(checks.split('#')[1]),valuecheck(checks.split('#')[2])))
                elif checks == 'fileopen':
                    return(es.fileopenbox())
                elif checks == 'filesave':
                    return(es.filesavebox()) 
                elif checks.split('#')[0] == 'GPIO_in':
                    if valuecheck(splited[1]) in GPIOset:
                        RPi.input(valuecheck(checks.split('#')[1]))
                    else:
                        RPi.setup(valuecheck(splited[1]),RPi.IN)
                        RPi.input(valuecheck(checks.split('#')[1]))
                else:
                    es.msgbox("ValueError: name '"+checks+"' is not defined",'Error')
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
        elif splited[0] == 'output':
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
        elif splited[0] == 'browse':
            web.open_new_tab(valuecheck(splited[2]))
        elif splited[0] == 'server':
            dk=valuecheck(splited[1])
            fileshttp = valuecheck(splited[2])
            httpd = make_server('', dk, send)
            httpd.serve_forever()
        elif splited[0] == 'GPIO_high':
            if valuecheck(splited[1]) in GPIOset:
                RPi.output(valuecheck(splited[1]),RPi.HIGH)
            else:
                RPi.setup(valuecheck(splited[1]),RPi.OUT)
                RPi.output(valuecheck(splited[1]),RPi.HIGH)
        elif splited[0] == 'GPIO_low':
            if valuecheck(splited[1]) in GPIOset:
                RPi.output(valuecheck(splited[1]),RPi.LOW)
            else:
                RPi.setup(valuecheck(splited[1]),RPi.OUT)
                RPi.output(valuecheck(splited[1]),RPi.LOW)
        elif splited[0] == 'GPIO_out':
            if valuecheck(splited[1]) in GPIOset:
                RPi.output(valuecheck(splited[1]),valuecheck(splited[2]))
            else:
                RPi.setup(valuecheck(splited[1]),RPi.OUT)
                RPi.output(valuecheck(splited[1]),valuecheck(splited[2]))
        elif splited[0] == '//':
            pass
        elif splited[0] == 'use':
            os.system(splited[1])
        elif splited[0] == 'sleep':
            time.sleep(valuecheck(splited[1]))
        else:
            es.msgbox("NameError: name '"+splited[0]+"' is not defined",'Error')
    elif splited[0] == 'down':
        t2.pendown()
    elif splited[0] == 'up':
        t2.penup()
    elif splited[0] == 'clear':
        t2.clear()
    elif splited[0] == 'info':
        es.msgbox('''
Pyfang copyright by Fangcat(http://fangcatchina.gitee.io)
Using MIT Open Source Agreement.
MIT License

Copyright (c) 2020 Fangcat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
        ''','Pyfang')
    else:
        es.msgbox("NameError: name '"+splited[0]+"' is not defined",'Error')
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
t1.write(r'''
  _____        __                  
 |  __ \      / _|                 
 | |__) |   _| |_ __ _ _ __   __ _ 
 |  ___/ | | |  _/ _` | '_ \ / _` |
 | |   | |_| | || (_| | | | | (_| |
 |_|    \__, |_| \__,_|_| |_|\__, |
         __/ |                __/ |
        |___/                |___/ 
-----------------------------------------------------------
|Pyfang 3.3.2 Copyright by Fangcat                         |
|Using packages:Turtle,Easygui,Random,Webbrowser,OS,wsgiref|
-----------------------------------------------------------
''',font=('arial',12))
t1.setheading(-90)
t1.penup()
t1.fd(24)
t1.color('purple')
a = es.choicebox('Choose a mode to use:','Pyfang',['IDLE','File-Runner','Online Help'])
if a == 'File-Runner':
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
            f = open(es.fileopenbox('Open a file'), 'w', encoding='utf-8')
            for i in cmd:
                f.write(i)
                f.write('|')
        elif a.split(' ')[0] == 'runfile':
            f = open(es.fileopenbox('Open a file'),'r',encoding='utf-8')
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
        elif a == 'clearcode':
            cmd.clear()
        else:
            cmd.append(a)
elif a == 'IDLE':    
    while True:
        a = es.enterbox('>>>','Pyfang')
        t1.color('purple')
        t1.write('>>>'+a,font=('arial',12))
        t1.setheading(-90)
        t1.penup()
        t1.fd(24)
        pyfangrun(a)
else:
    web.open_new('https://gitee.com/pyfang/pyfang-language/wikis/Home')
