import main as m
from tkinter import *


# Creates new window for 'Application'
def create_application_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Apply To Internship")
    # Sets window size
    top.geometry("400x250")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)
    # Sets background color
    top.configure(bg="#029E6D")

    # Creates connection to database
    conn = m.create_connection('internship.db')
    # Creates cursor
    c = conn.cursor()

    # Creates display text
    Label(top, text="Please fill in the boxes below:", font=14).grid(row=0)
    Label(top, text="Student ID:", font=14).grid(row=1)
    Label(top, text="First Name:", font=14).grid(row=2)
    Label(top, text="Last Name:", font=14).grid(row=3)
    Label(top, text="Internship ID:", font=14).grid(row=4)

    # Creates input boxes. '.grid()' function must go on a separate line in order for user data to be saved properly
    box_student_id = Entry(top, width=30)
    box_student_id.grid(row=1, column=1)
    box_first = Entry(top, width=30)
    box_first.grid(row=2, column=1)
    box_last = Entry(top, width=30)
    box_last.grid(row=3, column=1)
    box_internship_id = Entry(top, width=30)
    box_internship_id.grid(row=4, column=1)

    submit_button = Button(top, text="Submit", font=14, command=lambda: m.confirmation_application_input(
        box_student_id, box_first, box_last, box_internship_id))
    submit_button.grid(row=5, column=1)

    main_menu_btn = Button(top, text="Main Menu", font=14, command=lambda: m.return_to_main_menu(top))
    main_menu_btn.grid(row=6, column=1)


# Creates new window for creating internships
def create_new_internship_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Create Internship")
    # Sets window size
    top.geometry("400x250")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)
    # Sets background color
    top.configure(bg="#029E6D")

    # Creates connection to database
    conn = m.create_connection('internship.db')
    # Creates cursor
    c = conn.cursor()

    # Creates display text
    Label(top, text="Please fill in the boxes below:", font=14).grid(row=0)
    Label(top, text="Company Name:", font=14).grid(row=1)
    Label(top, text="Start Date:", font=14).grid(row=2)
    Label(top, text="End Date:", font=14).grid(row=3)
    Label(top, text="Description:", font=14).grid(row=4)

    # Creates input boxes. '.grid()' function must go on a separate line in order for user data to be saved properly
    box_company_name = Entry(top, width=30)
    box_company_name.grid(row=1, column=1)
    box_start = Entry(top, width=30)
    box_start.grid(row=2, column=1)
    box_end = Entry(top, width=30)
    box_end.grid(row=3, column=1)
    box_description = Entry(top, width=30)
    box_description.grid(row=4, column=1)

    submit_button = Button(top, text="Submit", font=14, command=lambda: m.confirmation_internship_input(
        box_company_name, box_start, box_end, box_description))
    submit_button.grid(row=5, column=1)
    main_menu_btn = Button(top, text="Main Menu", font=14, command=lambda: m.return_to_main_menu(top))
    main_menu_btn.grid(row=6, column=1)
