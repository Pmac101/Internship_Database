import main as m
from tkinter import *


# Creates a new window for Company registration
def create_company_registration_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Company Registration")
    # Sets window size
    top.geometry("400x400")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)

    # Creates display text
    Label(top, text="Please fill in the boxes below:").grid(row=0)
    Label(top, text="Company ID: ").grid(row=1)
    Label(top, text="Company Name: ").grid(row=2)
    Label(top, text="Location: ").grid(row=3)
    Label(top, text="Internship ID: ").grid(row=4)
    Label(top, text="Description: ").grid(row=5)
    Label(top, text="Positions Available: ").grid(row=6)

    # Creates input boxes. '.grid()' function must go on a separate line in order for user data to be saved properly
    box_company_id = Entry(top)
    box_company_id.grid(row=1, column=1)
    box_name = Entry(top)
    box_name.grid(row=2, column=1)
    box_location = Entry(top)
    box_location.grid(row=3, column=1)
    box_internship_id = Entry(top)
    box_internship_id.grid(row=4, column=1)
    box_description = Entry(top)
    box_description.grid(row=5, column=1)
    box_positions = Entry(top)
    box_positions.grid(row=6, column=1)

    submit_button = Button(top, text="Save record", command=lambda: m.confirmation_company_input(box_company_id,
                                                                                                box_name,
                                                                                               box_location,
                                                                                               box_internship_id,
                                                                                               box_description,
                                                                                               box_positions))
    submit_button.grid(row=7, column=1)
    main_menu_btn = Button(top, text="Main Menu", command=lambda: m.return_to_main_menu(top))
    main_menu_btn.grid(row=7, column=2)


# TODO finish updating student registration first
# Creates a new window for Student registration
def create_student_registration_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Student Registration")
    # Sets window size
    top.geometry("400x300")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)

    # Creates display text
    Label(top, text="Please fill in the boxes below:").grid(row=0)
    Label(top, text="First Name: ").grid(row=1)
    Label(top, text="Last Name: ").grid(row=2)
    Label(top, text="Address: ").grid(row=3)
    Label(top, text="Phone: ").grid(row=4)
    Label(top, text="E-mail: ").grid(row=5)

    # Creates input boxes. '.grid()' function must go on a separate line in order for user data to be saved properly
    box_first = Entry(top, width=20)
    box_first.grid(row=1, column=1)
    box_last = Entry(top)
    box_last.grid(row=2, column=1)
    box_address = Entry(top)
    box_address.grid(row=3, column=1)
    box_phone = Entry(top)
    box_phone.grid(row=4, column=1)
    box_email = Entry(top)
    box_email.grid(row=5, column=1)

    submit_button = Button(top, text="Save record", command=lambda: m.confirmation_student_input(box_first, box_last,
                                                                                               box_address,
                                                                                               box_phone, box_email))
    submit_button.grid(row=6, column=1)
    main_menu_btn = Button(top, text="Main Menu", command=lambda: m.return_to_main_menu(top))
    main_menu_btn.grid(row=6, column=2)
