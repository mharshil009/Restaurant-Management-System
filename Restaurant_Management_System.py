from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x700+0+0")
root.title("Retaurant Management System")

Tops = Frame(root, bg="black", width=1600, height=500, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=400, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

localtime = time.asctime (time.localtime (time.time()))
lblinfo = Label (Tops, font=('aria', 30, 'bold'), text="Restaurant Management System", 
                fg='blue', bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label (Tops, font=('aria', 30, 'bold'), text=localtime, fg="red", anchor=W)
lblinfo.grid(row=1, column=0)

text_Input = StringVar()
operator= ""

txtdisplay = Entry(f2, font=('arial', 20,'bold'), textvariable=text_Input, bd=5, 
                    insertwidth=7, bg='green', justify='right')
txtdisplay.grid(columnspan=4)


def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def clrdisplay():
    global operator
    operator = ""
    text_Input.set("")

def equals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def ref():
    x = random.randint(12000, 50000)
    randomRef = str(x)
    rand.set(randomRef)

    fries = float(Fries.get())
    lunch_meal = float(LargeFries.get())
    burger_meal = float(Burger.get())
    pizza_meal = float(Filet.get())
    Cheese_burger = float(Cheese_burger.get())
    drinks = float(Drinks.get())
    

    fries_cost = fries*25
    lunch_cost = lunch_meal*40
    burger_cost = burger_meal*35
    pizza_cost = pizza_meal*50
    cheese_burger_cost = cheese_burger*30
    drinks_cost = drinks*35

    Meal_cost = "Rs. ", str('%.2f'% (fries_cost + lunch_cost + burger_cost + pizza_cost + cheese_burger_cost + burger_cost + drinks_cost))

    Tax_payable = ((fries_cost + lunch_cost + burger_cost + pizza_cost + cheese_burger_cost + burger_cost + drinks_cost)*0.33)

    Totalcost = (fries_cost + lunch_cost + burger_cost + pizza_cost + cheese_burger_cost + burger_cost + drinks_cost)

    Ser_Charge = ((fries_cost + lunch_cost + burger_cost + pizza_cost + cheese_burger_cost + burger_cost + drinks_cost)/99)

    Service = "Rs. ", str('%.2f'% Ser_Charge)

    OverallCost = "Rs. ", str(Tax_payable + Totalcost + Ser_Charge)

    PaidTax = "Rs. ", str('%.2f'% Tax_payable)

    Service_Charge.set(Service)
    cost.set(Meal_cost)
    Tax.set(PaidTax)
    SubTotal.set(Meal_cost)
    Total.set(OverallCost)


def qexit():
    root.destroy()

def reset():
    rand.set("")
    Fries.set("")
    LargeFries.set("")
    Burger.set("")
    Filet.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    cheese_burger.set("")



btn7 = Button(f2,padx=16,pady=16, bd=4, fg="white", font=('arial', 20, 'bold'), 
                text="7", bg="black", command=lambda: btnclick(7))

btn7.grid(row=2, column=0)

btn8 = Button (f2,padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'), 
                text="8", bg="black", command=lambda: btnclick(8)) 
btn8.grid(row=2, column=1)

btn9 = Button (f2,padx=16,pady=16, bd=4, fg="white", font=('arial', 20, 'bold'), text="9", bg="black", command=lambda: btnclick(9)) 
btn9.grid(row=2, column=2)

Addition = Button (f2, padx=16,pady=16, bd=4, fg="white", font=('arial',20, 'bold'), text="+", bg="black", command=lambda: btnclick("+")) 
Addition.grid(row=2, column=3)

btn4 = Button(f2, padx=16,pady=16, bd=4, fg="white", font=('arial' ,20, 'bold'), text="4", bg="black", command=lambda: btnclick(4)) 
btn4.grid(row=3, column=0)

btn5 = Button(f2,padx=16,pady=16, bd=4, fg="white", font=('arial' ,20, 'bold'), text="5", bg="black", command=lambda: btnclick(5)) 
btn4.grid(row=5, column=1)

btn6 = Button(f2,padx=16,pady=16, bd=4, fg="white", font=('arial' ,20, 'bold'), text="6", bg="black", command=lambda: btnclick(6)) 
btn6.grid(row=3, column=2)

Subtraction = Button(f2, padx=16,pady=16, bd=4, fg="white", font=('arial',20, 'bold'), text="-", bg="black", command=lambda: btnclick("-")) 
Subtraction.grid(row=3, column=3)

btn1 = Button(f2,padx=16,pady=16, bd=4, fg="white", font=('arial', 20, 'bold'), text="1", bg="black", command=lambda: btnclick(1)) 
btn1.grid(row=4, column=0)

btn2 = Button (f2,padx=16,pady=16, bd=4, fg="white", font=('arial', 20, 'bold'), text="2", bg="black", command=lambda: btnclick(2)) 
btn1.grid(row=4, column=1)

btn3 = Button(f2,padx=16,pady=16, bd=4, fg="white", font=('arial', 20, 'bold'), text="3", bg="black", command=lambda: btnclick(3)) 
btn1.grid(row=4, column=2)

multiply = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'), text="*", bg="black", command=lambda: btnclick("*")) 
multiply.grid(row=4, column=3)

btn0 = Button (f2, padx=16,pady=16, bd=4, fg="white", font=('arial', 20, 'bold'), text="0", bg="black", command=lambda: btnclick(0)) 
btn0.grid(row=5, column=0)

btnc = Button(f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'), text="c", bg="black", command=clrdisplay) 
btn0.grid(row=5, column=1)

decimal = Button (f2, padx=16, pady=16, bd=4, fg="white", font=('arial', 20, 'bold'), text=".", bg="black", command=lambda: btnclick(".")) 
btn0.grid(row=5, column=2)

Division = Button(f2, padx=16,pady=16, bd=4, fg="white", font=('arial' ,20, 'bold'), text="/", bg="black", command=lambda: btnclick("/"))
Division.grid(row=5, column=3)

btnequal = Button (f2, padx=16,pady=16, bd=4, fg="white", font=('arial', 20, 'bold'),
                    text="=", bg="black", command=equals)
btnequal.grid(columnspan=4)


rand =  StringVar()
Fries =  StringVar()
LargeFries = StringVar()
Burger = StringVar()
Filet = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
cheese_burger = StringVar()


lblreference = Label(f1, font=('aria', 16, 'bold'), text="Order No.", fg="black", bd=10, anchor="w")
lblreference.grid(row=0, column=0)

txtreference = Entry (f1, font=('arial', 17, 'bold'), textvariable=rand, bd=6, insertwidth=4, bg="red", justify="right")
txtreference.grid(row=1, column = 1)

lblfries = Label (f1, font=('aria', 16, 'bold'), text="Fries Meal", fg="black", bd=10, anchor="w")
lblfries.grid(row=1, column=0)
txtfries = Entry (f1, font=('arial', 17, 'bold'), textvariable=Fries, bd=6, insertwidth=4, bg="red", justify="right")
txtfries.grid(row=1, column = 1)


lblLargefries = Label (f1, font=('aria', 16, 'bold'), text="Lunch Meal", fg="black", bd=10, anchor="w")
lblLargefries.grid(row=2, column=0)
txtLargefries = Entry (f1, font=('arial', 17, 'bold'), textvariable=LargeFries, bd=6, insertwidth=4, bg="red", justify="right")
txtLargefries.grid(row=2, column = 1)

lblburger = Label (f1, font=('aria', 16, 'bold'), text="Burger", fg="black", bd=10, anchor="w")
lblburger.grid(row=3, column=0)
txtburger = Entry (f1, font=('arial', 17, 'bold'), textvariable=Fries, bd=6, insertwidth=4, bg="red", justify="right")
txtburger.grid(row=3, column = 1)

lblFilet = Label (f1, font=('aria', 16, 'bold'), text="Pizza Meal", fg="black", bd=10, anchor="w")
lblFilet.grid(row=4, column=0)
txtFilet = Entry (f1, font=('arial', 17, 'bold'), textvariable=Filet, bd=6, insertwidth=4, bg="red", justify="right")
txtFilet.grid(row=4, column = 1)

lblCheese_burger = Label(f1, font=('aria', 16, 'bold'), text="Cheese Burger", fg="black", bd=10, anchor="w")
lblCheese_burger(row=5, column=0)
txtCheese_burger = Entry (f1, font=('arial', 17, 'bold'), textvariable=cheese_burger, bd=6, insertwidth=4, bg="red", justify="right")
txtCheese_burger.grid(row=5, column = 1)

lblDrinks = Label (f1, font=('aria', 16, 'bold'), text="Frinks", fg="black", bd=10, anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry (f1, font=('arial', 17, 'bold'), textvariable=Drinks, bd=6, insertwidth=4, bg="red", justify="right")
txtDrinks.grid(row=0, column = 3)

lblcost = Label (f1, font=('aria', 16, 'bold'), text="cost", fg="black", bd=10, anchor="w")
lblcost.grid(row=1, column=2)
txtcost = Entry (f1, font=('arial', 17, 'bold'), textvariable=Drinks, bd=6, insertwidth=4, bg="red", justify="right")
txtcost.grid(row=1, column =3)

lblService_Charge = Label (f1, font=('aria', 16, 'bold'), text="Service Charge", fg="black", bd=10, anchor="w")
lblDrinks.grid(row=2, column=2)
txtDrinks = Entry (f1, font=('arial', 17, 'bold'), textvariable=Service_Charge, bd=6, insertwidth=4, bg="red", justify="right")
txtDrinks.grid(row=2, column = 3)

lblTax = Label (f1, font=('aria', 16, 'bold'), text="Tax", fg="black", bd=10, anchor="w")
lblTax.grid(row=3, column=2)
txtTax = Entry (f1, font=('arial', 17, 'bold'), textvariable=Tax, bd=6, insertwidth=4, bg="red", justify="right")
txtTax.grid(row=3, column =3)

lblSubTotal = Label (f1, font=('aria', 16, 'bold'), text="SubTotal", fg="black", bd=10, anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal = Entry (f1, font=('arial', 17, 'bold'), textvariable=SubTotal, bd=6, insertwidth=4, bg="red", justify="right")
txtSubTotal.grid(row=4, column = 3)

lblTotal = Label (f1, font=('aria', 16, 'bold'), text="Total", fg="black", bd=10, anchor="w")
lblTotal.grid(row=5, column=2)
txtTotal = Entry (f1, font=('arial', 17, 'bold'), textvariable=Total, bd=6, insertwidth=4, bg="red", justify="right")
txtTotal.grid(row=5, column = 3)


btnTotal = Button(f1, padx=16, pady=8, bd=10, fg="white", font=('arial', 16, 'bold'), width = 10, text="TOTAL", bg="black", command=Ref) 
btnTotal.grid(row=7, column=1)

btnreset = Button(f1, padx=16, pady=8, bd=10, fg="white", font=('arial', 16, 'bold'), width = 10, text="RESET", bg="black", command=reset) 
btnreset.grid(row=7, column=2)

btnexit = Button (f1, padx=16, pady=8, bd=10, fg="white", font=('arial', 16, 'bold'), width = 10, text="EXIT", bg="black", command=qexit)
btnexit.grid(row=7, column=3)

def price():
    roo = Tk()
    roo.geometry("600x200")
    roo.title("Price List")
    x = Frame(roo, bg="white", width=600, height=220, relief=SUNKEN)
    x.pack(side=TOP)
    lblinfo = Label(x, font=('aria', 15,'bold'), text="ITEM", fg="red", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(x, font=('aria', 15,'bold'), text="________", fg="black", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(x, font=('aria', 15,'bold'), text="PRICE", fg="red", bd=5, anchor=W)
    lblinfo.grid(row=0, column=5)


    lblinfo = Label(x, font=('aria', 15,'bold'), text="Fries Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(x, font=('aria', 15,'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=5)
    
    
    lblinfo = Label(x, font=('aria', 15,'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(x, font=('aria', 15,'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=5)

    
    lblinfo = Label(x, font=('aria', 15,'bold'), text="Burger Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(x, font=('aria', 15,'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=5)

    
    lblinfo = Label(x, font=('aria', 15,'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(x, font=('aria', 15,'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=5)

    
    lblinfo = Label(x, font=('aria', 15,'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(x, font=('aria', 15,'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=5)

    
    lblinfo = Label(x, font=('aria', 15,'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(x, font=('aria', 15,'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=5)

    roo.mainloop()
    

btnprice = Button (f1, padx=16, pady=8, bd=10, fg="white", font=('arial', 16, 'bold'), width = 10, text="PRICE", bg="black", command=price)
btnprice.grid(row=7, column=0)

root.mainloop()








