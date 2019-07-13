from tkinter import *
import tkinter.messagebox
cal=Tk()
cal.title("Cafe coffee day")
F1=Frame(cal,height=50,width=1500,bd=10,relief=RAISED,bg='black')
F1.pack(side=TOP,fill=BOTH)
l=Label(F1,text="suresh chand nirmal kumar",font="arial 50 bold",bg='sienna')
l.pack(fill=BOTH)
F2=Frame(cal,bd=5,relief=RAISED,bg="black")
F2.pack(side=BOTTOM,fill=BOTH,expand=YES)
F2L=Frame(F2,height=400,width=1000,relief=RAISED,bg='black')
F2L.pack(side=LEFT,fill=BOTH,expand=YES)
f1=Frame(F2L,height=300,width=1000,relief=RAISED,bg='black')
f1.pack(side=TOP,fill=BOTH,expand=YES)
f11=Frame(f1,height=300,width=400,bd=10,relief=RAISED,bg='black')
f11.pack(side=LEFT,fill=BOTH,expand=YES)
f111=Frame(f11,height=75,width=400,bd=10,relief=RAISED,bg="black")
f111.pack(side=TOP,fill=BOTH,expand=YES)
f11u=Frame(f111,height=15,width=400,bd=5,relief=RAISED,bg='black')
f11u.pack(side=TOP,fill=BOTH,expand=YES)
f112=Frame(f11,height=75,width=400,bd=10,relief=RAISED,bg="black")
f112.pack(side=TOP,fill=BOTH,expand=YES)
f113=Frame(f11,height=75,width=400,bd=10,relief=RAISED,bg="black")
f113.pack(side=TOP,fill=BOTH,expand=YES)
f114=Frame(f11,height=75,width=400,bd=10,relief=RAISED,bg="black")
f114.pack(side=TOP,fill=BOTH,expand=YES)
f12=Frame(f1,height=300,width=600,bd=10,relief=RAISED,bg='black')
f12.pack(side=RIGHT,fill=BOTH,expand=YES)
f121=Frame(f12,height=75,width=600,bd=10,relief=RAISED,bg="black")
f121.pack(side=TOP,fill=BOTH,expand=YES)
f122=Frame(f12,height=75,width=600,bd=10,relief=RAISED,bg="black")
f122.pack(side=TOP,fill=BOTH,expand=YES)
f123=Frame(f12,height=75,width=600,bd=10,relief=RAISED,bg="black")
f123.pack(side=TOP,fill=BOTH,expand=YES)
f124=Frame(f12,height=75,width=600,bd=10,relief=RAISED,bg="black")
f124.pack(side=TOP,fill=BOTH,expand=YES)
f2=Frame(F2L,height=100,width=1000,bd=5,relief=RAISED,bg='black')
f2.pack(side=BOTTOM,fill=BOTH)
F2R=Frame(F2,height=600,width=500,bd=5,relief=RAISED,bg='black')
F2R.pack(side=RIGHT,fill=BOTH,expand=YES)
F2RT=Frame(F2R,height=550,width=500,relief=RAISED,bd=10,bg='black')
F2RT.pack(side=TOP,fill=BOTH,expand=YES)     #forgot to expand
F2RTT=Frame(F2RT,height=30,width=500,bd=5,relief=RAISED,bg='tan')
F2RTT.pack(side=TOP,fill=BOTH)
receipt=Label(F2RTT,text="Receipt",font="arial 10 bold",bg='tan')
receipt.pack(side=LEFT,fill=BOTH)
F2RTB=Frame(F2RT,height=520,width=500,relief=RAISED,bd=10,bg="floral white")
F2RTB.pack(side=TOP,fill=BOTH,expand=YES)
T=Text(F2RTB,bg="floral white",font="arial 8 bold")
T.pack(side=TOP,fill=BOTH,expand=YES)
T.insert(END,"item name"+"\t\t\t\t"+"item quantity"+"\t\t"+"price"+"\t"+"total price"+"\n"+"\n")
F2RB=Frame(F2R,height=50,width=500,relief=RAISED,bd=5,bg='black')
F2RB.pack(side=BOTTOM,fill=BOTH)
#-------------------------------------- Total Button-------------------------------------------------------------------------------------
def total():
    SubTotal=0
    T.delete("1.0",END)
    T.insert(END,"item name"+"\t\t\t\t"+"item quantity"+"\t\t"+"price"+"\t"+"total price"+"\n"+"\n")
    for i in range(32):
        
        if (int(Entries[i].get())==0):
            T.insert(END,"")
        else:
            total=int(Entries[i].get())*(price1[i])
            T.insert( END,str(labels[i])+"\t\t\t\t"+Entries[i].get()+"\t\t"+str(price1[i])+"\t"+str(total)+"\n")
            SubTotal=SubTotal+total

    TotalCost=SubTotal+(14.5*SubTotal/100)
    e.insert(END,"2%")
    E1.insert(END,'12.5%')
    E2.insert(END,str(SubTotal))
    E3.insert(END,str(TotalCost))
B1=Button(F2RB,font="arial 20 bold",text="Total",bg='gray',command=lambda :total())
B1.pack(side=LEFT,fill=BOTH,expand=YES)
#--------------------------------------------------------------Reset Button---------------------------------------------------------------
def reset():
    T.delete("1.0",END)
    for i in range(32):
        Entries[i].delete(0,END)
        Entries[i].insert(END,'0')
    e.delete(0,END)
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    T.insert(END,"item name"+"\t\t\t\t"+"item quantity"+"\t\t"+"price"+"\t"+"total price"+"\n"+"\n")
B1=Button(F2RB,font="arial 20 bold",text="Reset",bg='gray',command=lambda :reset())
B1.pack(side=LEFT,fill=BOTH,expand=YES)
#------------------------------------------------------------------------- Receipt button-----------------------------------------------------  

B1=Button(F2RB,font="arial 20 bold",text='Receipt',bg='gray')
B1.pack(side=LEFT,fill=BOTH,expand=YES)
#-------------------------------------------------------------------------Exit Button----------------------------------------------------------
def exit():
    Exit=tkinter.messagebox.askyesno("do u want to quit","are u sure")
    print(Exit)
    if Exit==True:
        cal.destroy()
        return
    
B1=Button(F2RB,font="arial 20 bold",text='Exit',bg='gray',command=lambda :exit())
B1.pack(side=LEFT,fill=BOTH,expand=YES)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
        
Entries=[]
labels=[]
def Button1():
    upperframe1=Frame(f111,height=15,width=400,bg='tan')
    upperframe1.pack(side=TOP,fill=BOTH)
    Ew=Entry(upperframe1,bd=4,bg='cornsilk',font="arial 10 bold")
    Ew.pack(side=LEFT,fill=BOTH)

    
def fill1():
    B1u1=Button(f11u,text="Add Items",font='arial 8 bold',bg='tan',command=lambda:Button1())
    B1u1.pack(side=LEFT,fill=BOTH)
    B1u2=Button(f11u,text="OK",font='arial 8 bold',bg='tan',command=lambda:OK1())
    B1u2.pack(side=LEFT,fill=BOTH)
    upperlabel1=Label(f11u,text='Pizza',font='arial 8 bold',bg='indian red')
    upperlabel1.pack(side=TOP,fill=BOTH)
    l=['Cheese Pizza','Paneer Pizza','Vegatable Cheese Pizza','Jain Pizza']
    for i in range(4):
        upperframe1=Frame(f111,height=15,width=400,bg='tan')
        upperframe1.pack(side=TOP,fill=BOTH)
        
        l1=Label(upperframe1,text=l[i],font="arial 8 bold",bg='tan')
        l1.pack(side=LEFT,fill=BOTH)
        labels.append(l[i])
        E=Entry(upperframe1,bd=4,bg='cornsilk',font="arial 10 bold")
        E.insert(END,'0')
        E.pack(side=RIGHT,fill=BOTH)
        Entries.append(E)
    return Entries,labels
        
fill1()

def fill2():
    upperlabel1=Label(f112,text='Burger',font='arial 8 bold',bg='indian red')
    upperlabel1.pack(side=TOP,fill=BOTH)
    l=['Veg Burger','Veg And Cheese Burger','Chicken Burger','Chicken And Cheese Burger']
    for i in range(4):
        upperframe1=Frame(f112,height=15,width=400,bg='tan')
        upperframe1.pack(side=TOP,fill=BOTH)
        l1=Label(upperframe1,text=l[i],font="arial 8 bold",bg='tan')
        l1.pack(side=LEFT,fill=BOTH)
        labels.append(l[i])
        E=Entry(upperframe1,bd=4,bg='cornsilk',font="arial 10 bold")
        E.insert(END,'0')
        E.pack(side=RIGHT,fill=BOTH)
        Entries.append(E)
    return Entries,labels
        
fill2()
    
def fill3():
    upperlabel1=Label(f113,text='Sandwich',font='arial 8 bold',bg='indian red')
    upperlabel1.pack(side=TOP,fill=BOTH)
    l=['Cheese Sandwich','Vegatable And Cheese Grilled','Chicken Sandwich Grilled','Zambo Size']
    for i in range(4):
        upperframe1=Frame(f113,height=15,width=400,bg='tan')
        upperframe1.pack(side=TOP,fill=BOTH)
        l1=Label(upperframe1,text=l[i],font="arial 8 bold",bg='tan')
        l1.pack(side=LEFT,fill=BOTH)
        labels.append(l[i])
        E=Entry(upperframe1,bd=4,bg='cornsilk',font="arial 10 bold")
        E.insert(END,'0')
        E.pack(side=RIGHT,fill=BOTH)
        Entries.append(E)
    return Entries,labels
        
fill3()

def fill4():
    upperlabel1=Label(f114,text='salad',font='arial 8 bold',bg='indian red')
    upperlabel1.pack(side=TOP,fill=BOTH)
    l=['Green Salad','Onion Salad','Pasta Salad','Russian Salad']
    for i in range(4):
        upperframe1=Frame(f114,height=15,width=400,bg='tan')
        upperframe1.pack(side=TOP,fill=BOTH)
        l1=Label(upperframe1,text=l[i],font="arial 8 bold",bg='tan')
        l1.pack(side=LEFT,fill=BOTH)
        labels.append(l[i])
        E=Entry(upperframe1,bd=4,bg='cornsilk',font="arial 10 bold")
        E.insert(END,'0')
        E.pack(side=RIGHT,fill=BOTH)
        Entries.append(E)
    return Entries,labels
        
fill4()
m=['Steamed Rice','jeera rice','peas pulao','vegetable Biryani']
def fill5():
    upperlabel1=Label(f121,text='Salad',font='arial 8 bold',bg='indian red')
    upperlabel1.pack(side=TOP,fill=BOTH)
    for i in range(4):
        upperframe1=Frame(f121,height=15,width=600,bg='tan')
        upperframe1.pack(side=TOP,fill=BOTH,expand=YES)
        l1=Label(upperframe1,text=m[i],font="arial 8 bold",bg='tan')
        l1.pack(side=LEFT,fill=BOTH)
        labels.append(m[i])
        E=Entry(upperframe1,bd=4,bg='cornsilk',font="arial 10 bold")
        E.insert(END,'0')
        E.pack(side=RIGHT,fill=BOTH)
        Entries.append(E)
    return Entries,labels
fill5()

m=['Paneer Tikka','Malai Paneer Tikka','Lahsoon Paneer Tikka','Stuffed Aloo']
def fill6():
    upperlabel1=Label(f122,text='Starters',font='arial 8 bold',bg='indian red')
    upperlabel1.pack(side=TOP,fill=BOTH)
    for i in range(4):
        upperframe1=Frame(f122,height=15,width=600,bg='tan')
        upperframe1.pack(side=TOP,fill=BOTH,expand=YES)
        l1=Label(upperframe1,text=m[i],font="arial 8 bold",bg='tan')
        l1.pack(side=LEFT,fill=BOTH)
        labels.append(m[i])
        E=Entry(upperframe1,bd=4,bg='cornsilk',font="arial 10 bold")
        E.insert(END,'0')
        E.pack(side=RIGHT,fill=BOTH)
        Entries.append(E)
    return Entries,labels
fill6()

m=['Pasta in tomato sauce','Pasta in white sauce','Creamy Cheese Pasta','Chicken Pasta in Tomatao sauce']
def fill7():
    upperlabel1=Label(f123,text='Pasta',font='arial 8 bold',bg='indian red')
    upperlabel1.pack(side=TOP,fill=BOTH)
    for i in range(4):
        upperframe1=Frame(f123,height=15,width=600,bg='tan')
        upperframe1.pack(side=TOP,fill=BOTH,expand=YES)
        l1=Label(upperframe1,text=m[i],font="arial 8 bold",bg='tan')
        l1.pack(side=LEFT,fill=BOTH)
        labels.append(m[i])
        E=Entry(upperframe1,bd=4,bg='cornsilk',font="arial 10 bold")
        E.insert(END,'0')
        E.pack(side=RIGHT,fill=BOTH)
        Entries.append(E)
    return Entries,labels
fill7()

m=['Plain curd','Boondi Raita','Mixed Veg Raita','Tadka Raita']
def fill8():
    upperlabel1=Label(f124,text='Raita',font='arial 8 bold',bg='indian red')
    upperlabel1.pack(side=TOP,fill=BOTH)
    for i in range(4):
        upperframe1=Frame(f124,height=15,width=600,bg='tan')
        upperframe1.pack(side=TOP,fill=BOTH,expand=YES)
        l1=Label(upperframe1,text=m[i],font="arial 8 bold",bg='tan')
        l1.pack(side=LEFT,fill=BOTH)
        labels.append(m[i])
        E=Entry(upperframe1,bd=4,bg='cornsilk',font="arial 10 bold")
        E.insert(END,'0')
        E.pack(side=RIGHT,fill=BOTH)
        Entries.append(E)
    return Entries,labels
fill8()
price1=[12,15,13,35,45,76,98,90,76,98,65,340,678,34,567,98,120,100,132,134,150,450,69,345,23,45,67,123,456,23,456,89]
f2L=Frame(f2,height=100,width=500,bd=5,relief=RAISED)
f2L.pack(side=LEFT,fill=BOTH,expand=YES)
f2R=Frame(f2,height=100,width=500,bd=5,relief=RAISED)
f2R.pack(side=RIGHT,fill=BOTH,expand=YES)


#------------------------------------------------sub total--------------------------------------

upperframe1=Frame(f2L,height=20,width=400,bg='tan')
upperframe1.pack(side=TOP,fill=BOTH)
l1=Label(upperframe1,text="Sub Total",font="arial 15 bold",padx=10,bg='tan')
l1.pack(side=LEFT,fill=BOTH)
E2=Entry(upperframe1,bd=5,width=40,bg='cornsilk',font="arial 10 bold")
E2.pack(side=RIGHT,fill=BOTH)

#-------------------------------------------------service charge------------------------------------------------------
upperframe1=Frame(f2L,height=40,width=400,bg='tan')
upperframe1.pack(side=TOP,fill=BOTH)
l1=Label(upperframe1,text="Service Charge",font="arial 15 bold",padx=10,bg='tan')
l1.pack(side=LEFT,fill=BOTH)
e=Entry(upperframe1,bd=5,width=40,bg='cornsilk',font="arial 10 bold")
e.pack(side=RIGHT,fill=BOTH) 
#-----------------------------------------------paid tax------------------------------------------------------- 
upperframe1=Frame(f2R,height=20,width=400,bg='tan')
upperframe1.pack(side=TOP,fill=BOTH)
l1=Label(upperframe1,text="Paid Tax",font="arial 15 bold",padx=10,bg='tan')
l1.pack(side=LEFT,fill=BOTH)
E1=Entry(upperframe1,bd=5,width=40,bg='cornsilk',font="arial 10 bold")
E1.pack(side=RIGHT,fill=BOTH)

#------------------------------------------------total cost-------------------------------------------------------
upperframe1=Frame(f2R,height=20,width=400,bg='tan')
upperframe1.pack(side=TOP,fill=BOTH)
l1=Label(upperframe1,text="Total Cost",font="arial 15 bold",padx=10,bg='tan')
l1.pack(side=LEFT,fill=BOTH)
E3=Entry(upperframe1,bd=5,width=40,bg='cornsilk',font="arial 10 bold")
E3.pack(side=RIGHT,fill=BOTH)
cal.mainloop()

