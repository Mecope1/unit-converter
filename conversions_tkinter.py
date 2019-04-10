"""
Unit Conversion program:
Length, Pressure, Temperature, Energy, Mass



User can convert related units.
EX: kilogram -> ton
Version = 0.3
"""

from tkinter import messagebox, Tk, END, Button, Frame, E, W, TOP, Y,StringVar, Entry, Label, Listbox, LEFT,\
    Scrollbar, RIGHT, BOTTOM

from conversions import prefix_modifiers, length_conversions, pressure_conversions, temp_conversions, \
    energy_conversions, mass_conversions, convert_units

# Holds the selected units for the conversion
current_state = {}


# Determines correct conversion dictionary using the collected units. Also provides prefixes for the conversion process.
def do_conversion(state):
    u1 = state.get('selected_unit1')
    u2 = state.get('selected_unit2')
    u1_prefix = state.get('selected_prefix1')
    u2_prefix = state.get('selected_prefix2')

# Checks to see if given and desired units have been selected. Then checks to see which conversion dictionary is needed.
    if u1 is not None and u2 is not None:
        try:
            current_value = float(entry_value1.get())
        except ValueError:
            messagebox.showerror("Non-numeric value", "Numeric values required!")
            return

        result = convert_units(
            current_value, u1, u2, current_state['conversion_map'], unit1_prefix=u1_prefix, unit2_prefix=u2_prefix
        )
        e2.delete(0, END)
        e2.insert(END, "{0:e}".format(result))
    else:
        messagebox.showerror("Unit Required", "No unit selected, but units are required.")
        # Function that grabs the unit for the given value from the user's selection.


def handle_unit_selection(event, state_key, state_prefix_key, unit_var):
    try:
        index = units_list1.curselection()[0]
        current_state[state_key] = units_list1.get(index)
        if current_state[state_prefix_key] is None:
            prefix = ""
        else:
            prefix = current_state[state_prefix_key]
        # Resets given units label
        unit_var.set(prefix + current_state[state_key])

    except IndexError:
        pass


# Function that grabs the unit for the given value from the user's selection.
def get_selected_unit1(event):
    try:
        index = units_list1.curselection()[0]
        current_state['selected_unit1'] = units_list1.get(index)
        if current_state['selected_prefix1'] is None:
            prefix1 = ""
        else:
            prefix1 = current_state['selected_prefix1']
        # Resets given units label
        g_units.set(prefix1 + current_state['selected_unit1'])

    except IndexError:
        pass


# Function that grabs the prefix for the given value from the user's selection.
def get_selected_prefix1(event):
    try:
        index = prefix_list1.curselection()[0]
        current_state['selected_prefix1'] = prefix_list1.get(index)
        if current_state['selected_unit1'] is None:
            unit1 = ""
        else:
            unit1 = current_state['selected_unit1']
        # Resets given units label
        g_units.set(current_state['selected_prefix1'] + unit1)

    except IndexError:
        pass


# Function that grabs the desired unit from the user's selection.
def get_selected_unit2(event):
    try:
        index = units_list2.curselection()[0]
        current_state['selected_unit2'] = units_list2.get(index)
        if current_state['selected_prefix2'] is None:
            prefix2 = ""
        else:
            prefix2 = current_state['selected_prefix2']
        # Resets desired units label
        d_units.set(prefix2 + current_state['selected_unit2'])

    except IndexError:
        pass

# Function that grabs the desired prefix from the user's selection.
def get_selected_prefix2(event):
    try:
        index = prefix_list2.curselection()[0]
        current_state['selected_prefix2'] = prefix_list2.get(index)

        if current_state['selected_unit2'] is None:
            unit2 = ""
        else:
            unit2 = current_state['selected_unit2']
        # Resets given units label

        d_units.set(current_state['selected_prefix2'] + unit2)

    except IndexError:
        pass

# Use of a closure to populate the units list.
# def set_units_command(conversions):
#     def on_click():
#         units_list1.delete(0, END)
#         units_list2.delete(0, END)
#
#         for row in conversions:
#             units_list1.insert(END, row)
#             units_list2.insert(END, row)
#         current_state['selected_unit1'] = None
#         current_state['selected_unit2'] = None
#         g_units.set("???")
#         d_units.set("???")
#     return on_click


# Changes the color of a button when a mouse pointer hovers over it. Uses a closure.
def set_color_closure_creator(button, color):
    def on_event(e):
        button['activebackground'] = color
        button['background'] = color
    return on_event


# Utilized by a lambda function in a button to fill out the lists for prefixes and units.
def set_units_command2(conversions, prefixes):
    units_list1.delete(0, END)
    units_list2.delete(0, END)
    prefix_list1.delete(0, END)
    prefix_list2.delete(0, END)

    for row in conversions:
        units_list1.insert(END, row)
        units_list2.insert(END, row)
    for row in prefixes:
        prefix_list1.insert(END, row)
        prefix_list2.insert(END, row)
# dictionary is reset to prevent user from attempting conversion without any selected units.
    current_state['selected_prefix1'] = None
    current_state['selected_unit1'] = None
    current_state['selected_prefix2'] = None
    current_state['selected_unit2'] = None
    current_state['conversion_map'] = conversions
# Label on GUI is reset to show that there are no selected units or prefixes.
    g_units.set("???")
    d_units.set("???")


# Defines a message to be displayed when the "About" button is pressed.
def about_prog():
    messagebox.showinfo("GUI Unit Converter", """
This program was originally written by Michael Cope in March 2019.
It will convert many types of units and display up to 4 digits past the decimal point.
WARNING: Error propagation not appropriately performed. Values given may not have accurate significant digits. Use only for rough calculations.""")


# Creates the window for the application
window = Tk()
window.grid_columnconfigure(0, weight=1)
window.wm_title("Unit Converter")

# Creates a top frame for the unit buttons, and the about button. This is done to allow cleaner formatting by separating
#   it from the bottom frame that contains the lists and the convert button.
top_frame = Frame(window)

# Buttons to display different categories of units.
b1 = Button(top_frame, text="Distance", command=lambda: set_units_command2(length_conversions, prefix_modifiers))
b1.grid(row=0, column=0, sticky=E+W)

b2 = Button(top_frame, text="Pressure", command=lambda: set_units_command2(pressure_conversions, prefix_modifiers))
b2.grid(row=0, column=1, sticky=E+W)

b3 = Button(top_frame, text="Temperature", command=lambda: set_units_command2(temp_conversions, prefix_modifiers))
b3.grid(row=0, column=2, sticky=E+W)

b4 = Button(top_frame, text="Energy", command=lambda: set_units_command2(energy_conversions, prefix_modifiers))
b4.grid(row=0, column=3, sticky=E+W)

b5 = Button(top_frame, text="Mass", command=lambda: set_units_command2(mass_conversions, prefix_modifiers))
b5.grid(row=0, column=4, sticky=E+W)

b7 = Button(top_frame, text="About", command=about_prog, bg="#44C430")
b7.grid(row=0, column=5, sticky=E+W)
b7.bind("<Enter>", set_color_closure_creator(b7, "#52EB3B"))
b7.bind("<Leave>", set_color_closure_creator(b7, "#44C430"))
top_frame.pack(side=TOP, fill=Y)


# Creates a bottom frame to store the lists, entry boxes, and conversion button to allow for cleaner formatting.
bottom_frame = Frame(window)


# Entry box for given number
entry_value1 = StringVar()
e1 = Entry(bottom_frame, textvariable=entry_value1)
e1.grid(row=1, column=0, columnspan=2)

# Selected units for given number
g_units = StringVar()
g_units.set("???")
l1 = Label(bottom_frame, textvariable=g_units, anchor=W)
l1.grid(row=1, column=2)


###########################################################################
# List of GIVEN prefixes
prefix_list1_frame = Frame(bottom_frame)
prefix_list1 = Listbox(prefix_list1_frame, height=8, width=8)
prefix_list1.pack(side=LEFT, fill=Y)

# Scroll bar for GIVEN prefixes
prefix_sb1 = Scrollbar(prefix_list1_frame)
prefix_sb1.pack(side=RIGHT, fill=Y)

prefix_list1.configure(yscrollcommand=prefix_sb1.set)
prefix_sb1.configure(command=prefix_list1.yview)
prefix_list1_frame.grid(row=1, column=3, rowspan=2, columnspan=3)


# List of GIVEN units
list1_frame = Frame(bottom_frame)
units_list1 = Listbox(list1_frame, height=8, width=8)
units_list1.pack(side=LEFT, fill=Y)


# Scroll bar for GIVEN units
units_sb1 = Scrollbar(list1_frame)
units_sb1.pack(side=RIGHT, fill=Y)

units_list1.configure(yscrollcommand=units_sb1.set)
units_sb1.configure(command=units_list1.yview)
list1_frame.grid(row=1, column=6, rowspan=8, columnspan=3)


# Inserts a frame in the middle of the bottom frame to allow an arrow to be created to show the direction of conversion.
center_frame = Frame(bottom_frame)
label_var = StringVar()
label_var.set("   ->   ")
center_text = Label(center_frame, textvariable=label_var)
center_text.pack()
center_frame.grid(row=1, column=9, rowspan=8, columnspan=3)


###########################################################################
# List of DESIRED prefixes
prefix_list2_frame = Frame(bottom_frame)
prefix_list2 = Listbox(prefix_list2_frame, height=8, width=8)
prefix_list2.pack(side=LEFT, fill=Y)

# Scroll bar for desired prefixes
prefix_sb2 = Scrollbar(prefix_list2_frame)
prefix_sb2.pack(side=RIGHT, fill=Y)

prefix_list2.configure(yscrollcommand=prefix_sb2.set)
prefix_sb2.configure(command=prefix_list2.yview)
prefix_list2_frame.grid(row=1, column=12, rowspan=2, columnspan=3)


# List of DESIRED units
list2_frame = Frame(bottom_frame)
units_list2 = Listbox(list2_frame, height=8, width=8)
units_list2.pack(side=LEFT, fill=Y)


# Scroll bar for DESIRED units
units_sb2 = Scrollbar(list2_frame)
units_sb2.pack(side=RIGHT, fill=Y)

units_list2.configure(yscrollcommand=units_sb2.set)
units_sb2.configure(command=units_list2.yview)
list2_frame.grid(row=1, column=15, rowspan=8, columnspan=3)


# Field where the answer will appear
desired_value1 = StringVar()
e2 = Entry(bottom_frame, textvariable=desired_value1)
e2.grid(row=1, column=18)


# Selected units for desired number
d_units = StringVar()
d_units.set("???")
l2 = Label(bottom_frame, textvariable=d_units, anchor=W)
l2.grid(row=1, column=19)

# Conversion button along with code to make the color change when the button is being hovered over by the mouse pointer.
b6 = Button(bottom_frame, text="Convert", width=5, command=lambda: do_conversion(current_state), bg='#4295f4')
b6.bind("<Enter>", set_color_closure_creator(b6, "#64ABFD"))
b6.bind("<Leave>", set_color_closure_creator(b6, "#4295f4"))
b6.grid(row=2, column=18, columnspan=2)


bottom_frame.pack(side=BOTTOM, fill=Y)

# Binds the listboxes to allow the contents to be selected and held so that the contents can be used.
prefix_list1.bind("<<ListboxSelect>>", get_selected_prefix1)
# lambda event: handle_unit_selection(event, 'selected_unit1', 'selected_prefix1', g_units)
units_list1.bind("<<ListboxSelect>>", get_selected_unit1)
prefix_list2.bind("<<ListboxSelect>>", get_selected_prefix2)
units_list2.bind("<<ListboxSelect>>", get_selected_unit2)


window.mainloop()
