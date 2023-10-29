

from functools import partial
import tkinter as tk


tempVal = "Celcius"
def store_temp(sel_temp):
    print(sel_temp)
    global tempVal
    tempVal = sel_temp

def call_result(rL1,rL2,inputn):
    temp = inputn.get()
    if tempVal == "Celcius":
        f = float((float(temp) * 9/5) + 32)
        k = float((float(temp) + 273.15))
        rL1. config(text="%f Fahrenheit" % f)
        rL2. config(text="%f Kelvin" % k)

    if tempVal == "Fahrenheit":
        c = float((float(temp) - 32) * 5/9)
        k = c + 273
        rL1. config(text="%f Celcius" % c)
        rL2. config(text="%f Kelvin" % k)

    if tempVal == "Kelvin":
        c = float((float(temp) - 273.15))
        f = float((float(temp) - 273.15) * 1.800 + 32)
        rL1. config(text="%f Celcius" % c)
        rL2. config(text="%f Fahrenheit" % f)
        return


root = tk.Tk()
root.wm_title('Marv Converter')

numberInput = tk.StringVar()
var = tk.StringVar()
input_label = tk.Label(root, text="Enter Temperature")
input_entry = tk.Entry(root, textvariable=numberInput)
input_label.grid(row=0)
input_entry.grid(row=0, column=1)

rLabel1 = tk.Label(root, text="Result1")
rLabel1.grid(row=2, columnspan=4)
rLabel2 = tk.Label(root, text="Result2")
rLabel2.grid(row=3, columnspan=4)

call_result = partial(call_result, rLabel1, rLabel2, numberInput)
result_button = tk.Button(root, text="Convert", command=call_result)
result_button.grid(row=1, columnspan=4)
dropdownList = ("Celcius", "Fahrenheit", "Kelvin")
dropdown = tk.OptionMenu(root, var, *dropdownList, command=store_temp)
var.set(dropdownList[0])
dropdown.grid(row=0, column=2)

root.mainloop()