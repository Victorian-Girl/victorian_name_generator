from tkinter import *
from tkinter import ttk
from victorian_female_names import *
from victorian_male_names import *
from victorian_other_anything_names import *
from victorian_surnames import *
from victorian_pets_compagnons import *

global male_mapping
global female_mapping

root = Tk()
root.title("Victorian Name Creator")
root.geometry("474x380")
root.resizable(False, False)

bg = PhotoImage(file="images/victorian_1.png")


# create function to generate names
def generate_name():
    selected = drop.get()
    if selected == "Male":
        fist_name_entry.delete("1.0", END)
        # generate random name
        names_list = [f"{v}" for v in male_mapping]
        random.shuffle(names_list)
        result_names = names_list[:1]
        result_end = result_names
        fist_name_entry.insert(END, "".join(result_end))

        surname_entry.delete("1.0", END)
        # generate random surname
        names_list = [f"{v}" for v in surname_mapping]
        random.shuffle(names_list)
        result_names = names_list[:1]
        result_end = result_names
        surname_entry.insert(END, "".join(result_end))

        # pets random name
        pets_entry.delete("1.0", END)
        # generate random surname
        names_list = [f"{v}" for v in pets_mapping]
        random.shuffle(names_list)
        result_names = names_list[:1]
        result_end = result_names
        pets_entry.insert(END, "".join(result_end))

    if selected == "Female":
        fist_name_entry.delete("1.0", END)
        # generate random name
        names_list = [f"{v}" for v in female_mapping]
        random.shuffle(names_list)
        result_names = names_list[:1]
        result_end = result_names
        fist_name_entry.insert(END, "".join(result_end))

        surname_entry.delete("1.0", END)
        # generate random surname
        names_list = [f"{v}" for v in surname_mapping]
        random.shuffle(names_list)
        result_names = names_list[:1]
        result_end = result_names
        surname_entry.insert(END, "".join(result_end))

        # pets random name
        pets_entry.delete("1.0", END)
        # generate random surname
        names_list = [f"{v}" for v in pets_mapping]
        random.shuffle(names_list)
        result_names = names_list[:1]
        result_end = result_names
        pets_entry.insert(END, "".join(result_end))

    if selected == "Other, Anything!":
        fist_name_entry.delete("1.0", END)
        # generate random name
        names_list = [f"{v}" for v in other_mapping]
        random.shuffle(names_list)
        result_names = names_list[:1]
        result_end = result_names
        fist_name_entry.insert(END, "".join(result_end))

        surname_entry.delete("1.0", END)
        # generate random surname
        names_list = [f"{v}" for v in surname_mapping]
        random.shuffle(names_list)
        result_names = names_list[:1]
        result_end = result_names
        surname_entry.insert(END, "".join(result_end))

        # pets random name
        pets_entry.delete("1.0", END)
        # generate random surname
        names_list = [f"{v}" for v in pets_mapping]
        random.shuffle(names_list)
        result_names = names_list[:1]
        result_end = result_names
        pets_entry.insert(END, "".join(result_end))




# create a label for the image
my_image_label = Label(root, image=bg)
my_image_label.place(x=0, y=0, relwidth=1, relheight=1)

# create a lable title
my_label1 = Label(my_image_label, text="Welcome To The Victorian Random Name Generator", bg="linen",
                  font=("Helvetica", 13))
my_label1.pack(pady=35)

box_label = Label(my_image_label, text="Chose a gender", font=("Helvetica", 13), width=15, bg="linen")
# box_label.pack(pady=10)
box_label.place(x=90, y=100)

# create the dropbox menue
choices_menue = StringVar()
drop = ttk.Combobox(my_image_label, textvariable=choices_menue, state="readonly")

drop["values"] = ("Chose One", "Male", "Female", "Other, Anything!")
drop.current(0)
# drop.pack(pady=5)
drop.place(x=260, y=100)

# create button for the dropbox
drop_button = Button(my_image_label, text="Initialise", font=("Helvetica", 13), width=10, bg="lavenderblush2",
                     command=generate_name)
# drop_button.pack(pady=5)
drop_button.place(x=190, y=150)

my_label2 = Label(my_image_label, text="Fist name", font=("Helvetica", 13), width=15, bg="linen")
# my_label2.pack(pady=10)
my_label2.place(x=90, y=210)


fist_name_entry = Text(my_image_label, width=15, height=1, font=("Helvetica", 13), bg="lavenderblush2")
# fist_name_entry.pack(pady=5)
fist_name_entry.place(x=260, y=210)

my_label3 = Label(my_image_label, text="Surname", font=("Helvetica", 13), width=15, bg="linen")
# my_label3.pack(pady=10)
my_label3.place(x=90, y=260)

surname_entry = Text(my_image_label, width=15, height=1, font=("Helvetica", 13), bg="lavenderblush2")
# surname_entry.pack(pady=5)
surname_entry.place(x=260, y=260)

my_label4 = Label(my_image_label, text="Pet", font=("Helvetica", 13), width=15, bg="linen")
# my_label3.pack(pady=10)
my_label4.place(x=90, y=310)

pets_entry = Text(my_image_label, width=15, height=1, font=("Helvetica", 13), bg="lavenderblush2")
# surname_entry.pack(pady=5)
pets_entry.place(x=260, y=310)

root.mainloop()
