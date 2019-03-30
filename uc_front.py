"""
Unit Conversion program:
Length, Pressure, Temperature, Energy, Mass



User can convert from related units. Currently the option to go between greek prefixes is limited.
EX: gram -> kilogram
Version = 0.1
"""
from tkinter import *
# import uc_rear

def get_selected_unit1(event):
    global selected_unit1
    try:
        index = units_list1.curselection()[0]
        selected_unit1 = units_list1.get(index)
    #print(index)
    #print(selected_tuple)
    #return selected_tuple

        # BLAH
        g_units.set(selected_unit1)
        # l1 = Label(window, text=selected_unit1)
        # l1.grid(row=1, column=2)

    except IndexError:
        pass


def get_selected_unit2(event):
    global selected_unit2
    try:
        index = units_list2.curselection()[0]
        selected_unit2 = units_list2.get(index)

        # BLAH
        d_units.set(selected_unit2)
        # l2 = Label(window, text=selected_unit2)
        # l2.grid(row=1, column=2)


    except IndexError:
        pass







def view_length_command():
    units_list1.delete(0, END)
    units_list2.delete(0, END)
    length_units = ["cm", "m", "km", "mi", "ft", "in"]

    for row in length_units:
        units_list1.insert(END, row)
        units_list2.insert(END, row)


def view_pressure_command():
    units_list1.delete(0, END)
    units_list2.delete(0, END)
    pressure_units = ["kPa", "Pa", "psi", "atm", "bar", "mmHg", "inH2O"]

    for row in pressure_units:
        units_list1.insert(END, row)
        units_list2.insert(END, row)


def view_temperature_command():
    units_list1.delete(0, END)
    units_list2.delete(0, END)
    temperature_units = ["deg C", "deg F", "K", "R"]

    for row in temperature_units:
        units_list1.insert(END, row)
        units_list2.insert(END, row)


def view_energy_command():
    units_list1.delete(0, END)
    units_list2.delete(0, END)
    energy_units = ["J", "cal", "Therms", "BTU"]

    for row in energy_units:
        units_list1.insert(END, row)
        units_list2.insert(END, row)


def view_mass_command():
    units_list1.delete(0, END)
    units_list2.delete(0, END)
    mass_units = ["kg", "g", "mg", "oz", "lb", "ton"]

    for row in mass_units:
        units_list1.insert(END, row)
        units_list2.insert(END, row)


# Creates the window for the application
window = Tk()
window.wm_title("Unit Converter")

# Entry box for given number
entry_value1 = StringVar()
e1 = Entry(window, textvariable=entry_value1)
e1.grid(row=1, column=0, columnspan=2)

# Selected units for given number
g_units = StringVar()
g_units.set("Given Units Placeholder")
l1 = Label(window, textvariable=g_units, anchor=W)
l1.grid(row=1, column=2)

# List of GIVEN units
units_list1 = Listbox(window, height=8, width=8)
units_list1.grid(row=1, column=3, rowspan=8, columnspan=2)

# Scroll bar for GIVEN units
units_sb1 = Scrollbar(window)
units_sb1.grid(row=1, column=5, sticky=W)

units_list1.configure(yscrollcommand=units_sb1.set)
units_sb1.configure(command=units_list1.yview)


# List of DESIRED units
units_list2 = Listbox(window, height=8, width=8)
units_list2.grid(row=1, column=8, rowspan=8, columnspan=2)


# Scroll bar for DESIRED units
units_sb2 = Scrollbar(window)
units_sb2.grid(row=1, column=7, sticky=E)

units_list2.configure(yscrollcommand=units_sb2.set)
units_sb2.configure(command=units_list2.yview)


# Field where the answer will appear
desired_value1 = StringVar()
e2 = Entry(window, textvariable=desired_value1)
e2.grid(row=1, column=10)

# Selected units for desired number
d_units = StringVar()
d_units.set("Given Units Placeholder")
l2 = Label(window, textvariable=d_units, anchor=W)
l2.grid(row=1, column=11)


# Buttons for type of units
# b1 = Button(window, text="View all", width=12, command=view_command)
# b1.grid(row=2, column=3)

b1 = Button(window, text="Distance", width=5, command=view_length_command)
#  print("WE\"RE GOING THE DISTANCE")
b1.grid(row=0, column=2)

b2 = Button(window, text="Pressure", width=5, command=view_pressure_command)
b2.grid(row=0, column=3)
# print("UNDER PRESSURE")

b3 = Button(window, text="Temperature", width=9, command=view_temperature_command)
b3.grid(row=0, column=4)
# print("THEY CALL ME MR. FAHRENHEIT")

b4 = Button(window, text="Energy", width=5, command=view_energy_command)
b4.grid(row=0, column=5)
# print("I AM BECOME DEATH")

b5 = Button(window, text="Mass", width=5, command=view_mass_command)
b5.grid(row=0, column=6)
# print("HEAVY STUFF")


units_list1.bind("<<ListboxSelect>>", get_selected_unit1)
units_list2.bind("<<ListboxSelect>>", get_selected_unit2)


window.mainloop()
