from tkinter import *
from sympy import *
init_printing()
from sympy.abc import x,y,z
import math as m

root=Tk()
root.title('Scientific Calculator+')
root.resizable(0,0)

a,h,w=4,2,6
statustrig=0
moretrigger=0


numkey=["butt0","butt1","butt2","butt3","butt4","butt5","butt6","butt7","butt8","butt9","dot"]
numkey_text=[0,1,2,3,4,5,6,7,8,9,"."]

trigokey=["rad","theta","...","sine","cos","tan","cosec","sec","cot","asin","acos","atan","acosec","asec","acot"]
trigokey_text=["rad","θ","...","sin()","cos()","tan()","csc()","sec()","cot()","asin()","acos()","atan()","acsc()","asec()","acot()"]
 

functionkeys=["x","y","z","x^(2)","x^(3)","x^(y)","e","π","!","log","ln","dy/dx","d2y/dx2","∫","Graph"]
functionkeys_text=["x","y","z","()^(2)","()^(3)","()^()","e","π","!","log ()","ln()","∂()","∂(,(x,2))","∫()","plot()"]


hyperbolickeys=["sinh","cosh","tanh","csch","sech","coth","asinh","acosh","atanh","acsch","asech","acoth"]
hyperbolickeys_text=["sinh()","cosh()","tanh()","csch()","sech()","coth()","asinh()","acosh()","atanh()","acsch()","asech()","acoth()"]

insertioncursor=["sin()","cos()","tan()","csc()","sec()","cot()","asin()","acos()","atan()","acsc()","asec()","acot()","sinh()","cosh()","tanh()","csch()","sech()","coth()","asinh()","acosh()","atanh()","acsch()","asech()","acoth()",
                 "log ()","ln()","∂()","∂(,(x,2))","∫()"]
#strings=["log()","ln()","∂()","∂(,(x,2))","∫()","asin()","acos()","atan()","acsc()","asec()","acot()"]
floats=["sin()","cos()","tan()","csc()","sec()","cot()","log ()"]

def myclick(number):
    global bruh
    bruh=number
    current= disp.get()
    disp.delete(0,END)
    disp.insert(0,str(current) + str(number))
    if number in insertioncursor:
        position = disp.index(INSERT)
        disp.icursor(position - 1)

def equalclick(*args):
    global bruh
    findsolof=disp.get()
    x,y,z=symbols('x y z')
    replacements={"×":"*","÷":"/","e":"exp(x)","π":"pi","∫":"integrate","∂":"diff"}
    findsolof = [replacements.get(d,d) for d in findsolof]
    findsolof= ''.join([str(elem) for elem in findsolof])
    print(findsolof)
    solution=sympify(findsolof)
    print(solution)
    disp.delete(0,END)
    disp.insert(0,str(solution))
        
def more_click():
    global statustrig
    statustrig=4
    global moretrigger
    if moretrigger==1:

            for c in range (0,12):
                trigokey[c+3].grid_forget()
            for d in range (0,12):
                hyperbolickeys[d]=Button(root,text=hyperbolickeys_text[d], font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="BLACK",width=w,height=h,command=lambda d=d :myclick(hyperbolickeys_text[d]))
            hyperbolickeys[0].grid(row=2,column=4,sticky="news")
            hyperbolickeys[1].grid(row=2,column=5,sticky="news")
            hyperbolickeys[2].grid(row=2,column=6,sticky="news")

            hyperbolickeys[3].grid(row=3,column=4,sticky="news")
            hyperbolickeys[4].grid(row=3,column=5,sticky="news")
            hyperbolickeys[5].grid(row=3,column=6,sticky="news")

            hyperbolickeys[6].grid(row=4,column=4,sticky="news")
            hyperbolickeys[7].grid(row=4,column=5,sticky="news")
            hyperbolickeys[8].grid(row=4,column=6,sticky="news")

            hyperbolickeys[9].grid(row=5,column=4,sticky="news")
            hyperbolickeys[10].grid(row=5,column=5,sticky="news")
            hyperbolickeys[11].grid(row=5,column=6,sticky="news")
            moretrigger=0
    elif moretrigger==0:
            for e in range (0,12):
                hyperbolickeys[e].grid_forget()
            for f in range(0,12):
                trigokey[f+3]=Button(root,text=trigokey_text[f+3], font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="BLACK",width=w,height=h,command=lambda f=f :myclick(trigokey_text[f+3]))    

            trigokey[3].grid(row=2,column=4)
            trigokey[4].grid(row=2,column=5)
            trigokey[5].grid(row=2,column=6)
            trigokey[6].grid(row=3,column=4)
            trigokey[7].grid(row=3,column=5)
            trigokey[8].grid(row=3,column=6)

            trigokey[9].grid(row=4,column=4)
            trigokey[10].grid(row=4,column=5)
            trigokey[11].grid(row=4,column=6)
            trigokey[12].grid(row=5,column=4)
            trigokey[13].grid(row=5,column=5)
            trigokey[14].grid(row=5,column=6)
            moretrigger=1
    return
   
def trigo():
    global randofunc
    global statustrig
    global moretrigger
    if statustrig==2:
        for b in range(0,15):
            functionkeys[b].grid_forget()

    trignometry=Button(root,text="sine", font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=8,command=trigo,state=DISABLED)
    trignometry.grid(row=1,column=1,sticky="news")
    calclus=Button(root,text="f(x)", font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=8,command=calcu)
    calclus.grid(row=1,column=0,sticky="news")

    for f in range(0,12):
            trigokey[f+3]=Button(root,text=trigokey_text[f+3], font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="BLACK",width=w,height=h,command=lambda f=f :myclick(trigokey_text[f+3]))


    trigokey[0]=Button(root,text=trigokey_text[0], font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=w,height=1)
    trigokey[1]=Button(root,text=trigokey_text[1], font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=w,height=1)
    trigokey[2]=Button(root,text=trigokey_text[2], font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=w,height=1,command=more_click)
    trigokey[0].grid(row=1,column=4,sticky="news")
    trigokey[1].grid(row=1,column=5,sticky="news")
    trigokey[2].grid(row=1,column=6,sticky="news")
    
    trigokey[3].grid(row=2,column=4)
    trigokey[4].grid(row=2,column=5)
    trigokey[5].grid(row=2,column=6)
    trigokey[6].grid(row=3,column=4)
    trigokey[7].grid(row=3,column=5)
    trigokey[8].grid(row=3,column=6)

    trigokey[9].grid(row=4,column=4)
    trigokey[10].grid(row=4,column=5)
    trigokey[11].grid(row=4,column=6)
    trigokey[12].grid(row=5,column=4)
    trigokey[13].grid(row=5,column=5)
    trigokey[14].grid(row=5,column=6)
    statustrig=1
    moretrigger=1
    print(statustrig)
    
def calcu():
    global statustrig
    if statustrig==1:
        for b in range (0,15):
            trigokey[b].grid_forget()
    calclus=Button(root,text="f(x)", font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=8,command=calcu,state=DISABLED)
    calclus.grid(row=1,column=0,sticky="news")
    trignometry=Button(root,text="sine", font="Segoe 20", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=8,command=trigo)
    trignometry.grid(row=1,column=1,sticky="news")
    for u in range (0,12):
        functionkeys[u+3]=Button(root,text=functionkeys_text[u+3], font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="BLACK",width=2*a-1,height=h,command= lambda u=u :myclick(functionkeys_text[u+3]))
        
    functionkeys[0]=Button(root,text=functionkeys_text[0], font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=a,height=1,command= lambda u=u :myclick(functionkeys_text[0]))
    functionkeys[1]=Button(root,text=functionkeys_text[1], font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=a,height=1,command= lambda u=u :myclick(functionkeys_text[1]))
    functionkeys[2]=Button(root,text=functionkeys_text[2], font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=a,height=1,command= lambda u=u :myclick(functionkeys_text[2]))
    

    functionkeys[0].grid(row=1,column=4,sticky="news")
    functionkeys[1].grid(row=1,column=5,sticky="news")
    functionkeys[2].grid(row=1,column=6,sticky="news")
    functionkeys[3].grid(row=2,column=4,sticky="news")
    functionkeys[4].grid(row=2,column=5,sticky="news")
    functionkeys[5].grid(row=2,column=6,sticky="news")
    functionkeys[6].grid(row=3,column=4,sticky="news")
    functionkeys[7].grid(row=3,column=5,sticky="news")
    functionkeys[8].grid(row=3,column=6,sticky="news")
    functionkeys[9].grid(row=4,column=4,sticky="news")
    functionkeys[10].grid(row=4,column=5,sticky="news")
    functionkeys[11].grid(row=4,column=6,sticky="news")
    functionkeys[12].grid(row=5,column=4,sticky="news")
    functionkeys[13].grid(row=5,column=5,sticky="news")
    functionkeys[14].grid(row=5,column=6,sticky="news")

    statustrig=2
    print(statustrig)
        
def clear(*args):
    global statustrig
    global disp
    global moretrigger
    disp.delete(0,END)
    trignometry=Button(root,text="sine", font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=8,command=trigo)
    trignometry.grid(row=1,column=1,sticky="news")
    calclus=Button(root,text="f(x)", font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=8,command=calcu)
    calclus.grid(row=1,column=0,sticky="news")
    if statustrig==0:
        return
    elif statustrig==1:
        for b in range (0,15):
            trigokey[b].grid_forget()
    elif statustrig==2:
        for b in range(0,15):
            functionkeys[b].grid_forget()
    elif statustrig==4:
        if moretrigger==0:
            trigokey[0].grid_forget()
            trigokey[1].grid_forget()
            trigokey[2].grid_forget()
            for g in range (0,12):
                hyperbolickeys[g].grid_forget()
        elif moretrigger==1:
            for j in range(0,15):
                trigokey[j].grid_forget()

    moretrigger=0
    statustrig=0
    print(statustrig)
  
def delete():
    pos = len(disp.get())
    display = str(disp.get())
    if display == '':
        disp.insert(0, '0')
    elif display == ' ':
        disp.insert(0, '0')
    elif display == '0':
        pass
    else:
        disp.delete(0, END)
        disp.insert(0, display[0:pos-1])

def key_event(*args):
    if disp.get() == '0':
        disp.delete(0, END)

for z in range (0,11):
    numkey[z]=Button(root,text=numkey_text[z], font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="BLACK",width=a,height=h,command = lambda z=z :myclick(numkey_text[z]))

disp = Entry(root, font="Verdana 22", fg="black", bg="#abbab1", bd=0, justify=LEFT,cursor="arrow",width=22)
disp.grid(row=0,column=0,columnspan=8,sticky="news",ipady=8)

disp.bind("<Return>",equalclick)
disp.bind("<Key-Delete>",clear)
disp.bind("<Key-1>", key_event)
disp.bind("<Key-2>", key_event)
disp.bind("<Key-3>", key_event)
disp.bind("<Key-4>", key_event)
disp.bind("<Key-5>", key_event)
disp.bind("<Key-6>", key_event)
disp.bind("<Key-7>", key_event)
disp.bind("<Key-8>", key_event)
disp.bind("<Key-9>", key_event)
disp.bind("<Key-0>", key_event)
disp.bind("<Key-.>", key_event)
disp.insert(0, '0')
disp.focus_set()


if disp.get() == '0':
        disp.delete(0, END)

simple=Button(root,text="CE", font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=8,command=clear)
trignometry=Button(root,text="sine", font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=8,command=trigo)
calclus=Button(root,text="f(x)", font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=8,command=calcu)

equals=Button(root,text="=", font="Segoe 21", relief=GROOVE, bd=0 ,fg="BLACK", bg="#296d98",width=a,height=h,command= equalclick)

plus=Button(root,text="+", font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=a,height=h,command= lambda : myclick("+"))
minus=Button(root,text="-", font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=a,height=h,command= lambda : myclick("-"))
multiply=Button(root,text="×", font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=a,height=h,command= lambda : myclick("×"))
divide=Button(root,text="÷", font="Segoe 21", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=a,height=h,command= lambda : myclick("÷"))
delete=Button(root,text="⌫", font="Segoe 14", relief=GROOVE, bd=0 ,fg="white", bg="#333333",width=a,height=h,command=delete)

numkey[10].grid(row=5,column=1,sticky="news")
numkey[7].grid(row=2,column=0,sticky="news")
numkey[8].grid(row=2,column=1,sticky="news")
numkey[9].grid(row=2,column=2,sticky="news")
numkey[4].grid(row=3,column=0,sticky="news")
numkey[5].grid(row=3,column=1,sticky="news")
numkey[6].grid(row=3,column=2,sticky="news")
numkey[1].grid(row=4,column=0,sticky="news")
numkey[2].grid(row=4,column=1,sticky="news")
numkey[3].grid(row=4,column=2,sticky="news")
numkey[0].grid(row=5,column=0,sticky="news")



simple.grid(row=1,column=2,sticky="news")
trignometry.grid(row=1,column=1,sticky="news")
calclus.grid(row=1,column=0,sticky="news")

equals.grid(row=5,column=2,sticky="news")
plus.grid(row=2,column=3,sticky="news")
minus.grid(row=3,column=3,sticky="news")
multiply.grid(row=4,column=3,sticky="news")
divide.grid(row=5,column=3,sticky="news")
delete.grid(row=1,column=3,sticky="news")


root.mainloop()

