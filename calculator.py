from tkinter import *

window = Tk()
window.iconbitmap("C:\calculatortwo\icon\Calculatoricon.ico")
window.title("CALCULATOR")
window.geometry("335x387")
window.resizable(0, 0)
window.configure(background="#5c6b69")

equation = ""


def show(value):
    global equation
    equation += value
    result_label.config(text=equation)


def clear():
    global equation
    equation = ""
    result_label.config(text=equation)


def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
        result_label.config(text=result)

# label for output

result_label = Label(window, text="", fg="white", bg="#1d1f1e", width=50, height=3, font=("arial", 10))
result_label.pack()
# buttons
btn1 = Button(window, text="C", font=("arial", 10, "bold"), width=8, height=3, bg="#5c5033", fg="white",
              command=lambda: clear())
btn1.place(x=7, y=60)
btn2 = Button(window, text="%", font=("arial", 10, "bold"), width=8, height=3, bg="black", fg="white",
              command=lambda: show("%"))
btn2.place(x=89, y=60)
btn3 = Button(window, text="/", font=("arial", 10, "bold"), width=8, height=3, bg="black", fg="white",
              command=lambda: show("/"))
btn3.place(x=171, y=60)
btn4 = Button(window, text="x", font=("arial", 10, "bold"), width=8, height=3, bg="black", fg="white",
              command=lambda: show("x"))
btn4.place(x=253, y=60)
##
btn1 = Button(window, text="7", font=("arial", 10, "bold"), width=8, height=3, bg="black", fg="white",
              command=lambda: show("7"))
btn1.place(x=7, y=125)
btn2 = Button(window, text="8", font=("arial", 10, "bold"), width=8, height=3, bg="black", fg="white",
              command=lambda: show("8"))
btn2.place(x=89, y=125)
btn3 = Button(window, text="9", font=("arial", 10, "bold"), width=8, height=3, bg="black", fg="white",
              command=lambda: show("9"))
btn3.place(x=171, y=125)
btn4 = Button(window, text="-", font=("arial", 10, "bold"), width=8, height=3, bg="black", fg="white",
              command=lambda: show("-"))
btn4.place(x=253, y=125)
###
btn1 = Button(window, text="4", font=("arial", 10, "bold"), width=8, height=3, bg="black", fg="white",
              command=lambda: show("4"))
btn1.place(x=7, y=190)
btn2 = Button(window, text="5", font=("arial", 10, "bold"), width=8, height=3, bg="black", fg="white",
              command=lambda: show("5"))
btn2.place(x=89, y=190)
btn3 = Button(window, text="6", font=("arial", 10, "bold"), width=8, height=3, bg="black", fg="white",
              command=lambda: show("6"))
btn3.place(x=171, y=190)
btn4 = Button(window, text="+", font=("arial", 10, "bold"), width=8, height=3, bg="black", fg="white",
              command=lambda: show("+"))
btn4.place(x=253, y=190)
####
btn1 = Button(window, text="1", font=("arial", 10, "bold"), width=8, height=3, bg="black", fg="white",
              command=lambda: show("1"))
btn1.place(x=7, y=255)
btn2 = Button(window, text="2", font=("arial", 10, "bold"), width=8, height=3, bg="black", fg="white",
              command=lambda: show("2"))
btn2.place(x=89, y=255)
btn3 = Button(window, text="3", font=("arial", 10, "bold"), width=8, height=3, bg="black", fg="white",
              command=lambda: show("3"))
btn3.place(x=171, y=255)
btn4 = Button(window, text="=", font=("arial", 10, "bold"), width=8, height=7, bg="#2c4647", fg="white",
              command=lambda:calculate())
btn4.place(x=253, y=255)
#####
btn1 = Button(window, text="0", font=("arial", 10, "bold"), width=19, height=3, bg="black", fg="white",
              command=lambda: show("0"))
btn1.place(x=7, y=320)
btn2 = Button(window, text=".", font=("arial", 10, "bold"), width=8, height=3, bg="black", fg="white",
              command=lambda: show("."))
btn2.place(x=171, y=320)

window.mainloop()
