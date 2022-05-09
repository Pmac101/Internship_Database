import main as m
from tkinter import *


# Creates a new window for Company registration
def create_company_registration_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Company Registration")
    # Sets window size
    top.geometry("400x250")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)
    # Sets background color
    top.configure(bg="#029E6D")

    # Creates display text
    Label(top, text="Please fill in the boxes below:", font=14).grid(row=0)
    Label(top, text="Company Name: ", font=14).grid(row=1)
    Label(top, text="Location: ", font=14).grid(row=2)
    Label(top, text="Phone: ", font=14).grid(row=3)
    Label(top, text="Email: ", font=14).grid(row=4)

    # Creates input boxes. '.grid()' function must go on a separate line in order for user data to be saved properly
    box_company_name = Entry(top, width=30)
    box_company_name.grid(row=1, column=1)
    box_location = Entry(top, width=30)
    box_location.grid(row=2, column=1)
    box_phone = Entry(top, width=30)
    box_phone.grid(row=3, column=1)
    box_email = Entry(top, width=30)
    box_email.grid(row=4, column=1)

    register_button = Button(top, text="Register", font=14, command=lambda: m.confirmation_company_input(
        box_company_name, box_location, box_phone, box_email))
    register_button.grid(row=7, column=1)
    main_menu_btn = Button(top, text="Main Menu", font=14, command=lambda: m.return_to_main_menu(top))
    main_menu_btn.grid(row=8, column=1)


# Creates a new window for Student registration
def create_student_registration_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Student Registration")
    # Sets window size
    top.geometry("400x250")
    # Ensures this window stay on top
    top.attributes('-topmost', True)
    # Sets background color
    top.configure(bg="#029E6D")

    # Creates display text
    Label(top, text="Please fill in the boxes below:", font=14).grid(row=0)
    Label(top, text="Student ID:", font=14).grid(row=1)
    Label(top, text="First Name:", font=14).grid(row=2)
    Label(top, text="Last Name:", font=14).grid(row=3)
    Label(top, text="Address:", font=14).grid(row=4)
    Label(top, text="Phone:", font=14).grid(row=5)
    Label(top, text="E-mail:", font=14).grid(row=6)

    # Creates input boxes. '.grid()' function must go on a separate line in order for user data to be saved properly
    box_student_id = Entry(top, width=30)
    box_student_id.grid(row=1, column=1)
    box_first = Entry(top, width=30)
    box_first.grid(row=2, column=1)
    box_last = Entry(top, width=30)
    box_last.grid(row=3, column=1)
    box_address = Entry(top, width=30)
    box_address.grid(row=4, column=1)
    box_phone = Entry(top, width=30)
    box_phone.grid(row=5, column=1)
    box_email = Entry(top, width=30)
    box_email.grid(row=6, column=1)

    register_button = Button(top, text="Register", font=14, command=lambda: m.confirmation_student_input(
        box_student_id, box_first, box_last, box_address, box_phone, box_email))
    register_button.grid(row=7, column=1)

    main_menu_btn = Button(top, text="Main Menu", font=14, command=lambda: m.return_to_main_menu(top))
    main_menu_btn.grid(row=8, column=1)
