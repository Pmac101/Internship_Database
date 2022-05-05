import sqlite3
import sys
import tkinter as tk
from sqlite3 import Error
from tkinter import *
from tkinter import messagebox


# Create connection to database - done
def create_connection(database_file):
    conn = None
    try:
        conn = sqlite3.connect(database_file)
        print("Connection established")
        return conn
    except Error as e:
        print(e)

    return conn


# Create table - done
def create_table(conn, sql_table_create):
    try:
        c = conn.cursor()
        c.execute(sql_table_create)
        conn.commit()
    except Error as e:
        print(e)


# TODO when assigning 'command=' parameter to buttons, do not put '()' after the function. It will run automatically
#  if you do! example: command=query() should look like command=query

# Creates query window
def internship_query_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Query")
    # Sets window size
    top.geometry("500x400")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)

    # Creates connection to database
    conn = create_connection('internship.db')
    # Creates cursor
    c = conn.cursor()

    c.execute("SELECT * FROM internships")
    conn.commit()
    rows = c.fetchall()
    results = ""

    for row in rows[0]:
        results += str(row) + " "

    internships_label = Label(top, text="Search results: ")
    internships_label.grid(row=1, column=1)
    results_label = Label(top, text=results)
    results_label.grid(row=2, column=1)

    main_menu_btn = Button(top, text="Main Menu", command=lambda: return_to_main_menu(top))
    main_menu_btn.grid(row=3, column=1)


# Creates a new window for creating internships
def create_new_internship_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Create New Internship")
    # Sets window size
    top.geometry("500x400")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)

    # Creates connection to database
    conn = create_connection('internship.db')
    # Creates cursor
    c = conn.cursor()

    # Creates display text
    label_instructions = Label(top, text="Please fill in the boxes below:").grid(row=0)
    label_company_name = Label(top, text="Company Name: ").grid(row=1)
    label_id = Label(top, text="Internship ID: ").grid(row=2)
    label_application_term = Label(top, text="Application Term: ").grid(row=3)
    label_internship_term = Label(top, text="Internship Term: ").grid(row=4)
    label_description = Label(top, text="Description: ").grid(row=5)
    label_review = Label(top, text="Experience Review: ").grid(row=6)

    # Creates input boxes. '.grid()' function must go on a separate line in order for user data to be saved properly
    box_company_name = Entry(top)
    box_company_name.grid(row=1, column=1)
    box_id = Entry(top)
    box_id.grid(row=2, column=1)
    box_app_term = Entry(top)
    box_app_term.grid(row=3, column=1)
    box_internship_term = Entry(top)
    box_internship_term.grid(row=4, column=1)
    box_description = Entry(top)
    box_description.grid(row=5, column=1)
    box_review = Entry(top)
    box_review.grid(row=6, column=1)

    submit_button = Button(top, text="Save record", command=lambda: confirmation_internship_input(box_company_name,
                                                                                               box_id,
                                                                                               box_app_term,
                                                                                               box_internship_term,
                                                                                               box_description,
                                                                                               box_review))
    submit_button.grid(row=7, column=1)
    main_menu_btn = Button(top, text="Main Menu", command=lambda: return_to_main_menu(top))
    main_menu_btn.grid(row=7, column=2)


# Creates a new window for Company registration - not done
def create_company_registration_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Company Registration")
    # Sets window size
    top.geometry("600x300")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)

    # Creates display text
    label_instructions = Label(top, text="Please fill in the boxes below:").grid(row=0)
    label_company_id = Label(top, text="Company ID: ").grid(row=1)
    label_name = Label(top, text="Company Name: ").grid(row=2)
    label_location = Label(top, text="Location: ").grid(row=3)
    label_internship_id = Label(top, text="Internship ID: ").grid(row=4)
    label_description = Label(top, text="Description: ").grid(row=5)
    label_positions = Label(top, text="Positions Available: ").grid(row=6)

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

    submit_button = Button(top, text="Save record", command=lambda: confirmation_company_input(box_company_id, box_name,
                                                                                               box_location,
                                                                                               box_internship_id,
                                                                                               box_description,
                                                                                               box_positions))
    submit_button.grid(row=7, column=1)
    main_menu_btn = Button(top, text="Main Menu", command=lambda: return_to_main_menu(top))
    main_menu_btn.grid(row=7, column=2)


# Creates a new window for Student registration - done
def create_student_registration_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Student Registration")
    # Sets window size
    top.geometry("600x300")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)

    # Creates display text
    label_instruction = Label(top, text="Please fill in the boxes below:").grid(row=0)
    label_first = Label(top, text="First Name: ").grid(row=1)
    label_last = Label(top, text="Last Name: ").grid(row=2)
    label_address = Label(top, text="Address: ").grid(row=3)
    label_phone = Label(top, text="Phone: ").grid(row=4)
    label_email = Label(top, text="E-mail: ").grid(row=5)

    # Creates input boxes. '.grid()' function must go on a separate line in order for user data to be saved properly
    box_first = Entry(top)
    box_first.grid(row=1, column=1)
    box_last = Entry(top)
    box_last.grid(row=2, column=1)
    box_address = Entry(top)
    box_address.grid(row=3, column=1)
    box_phone = Entry(top)
    box_phone.grid(row=4, column=1)
    box_email = Entry(top)
    box_email.grid(row=5, column=1)

    submit_button = Button(top, text="Save record", command=lambda: confirmation_company_input(box_first, box_last,
                                                                                               box_address,
                                                                                               box_phone, box_email))
    submit_button.grid(row=6, column=1)
    main_menu_btn = Button(top, text="Main Menu", command=lambda: return_to_main_menu(top))
    main_menu_btn.grid(row=6, column=2)


# Confirms user data collected from 'Company Registration' window is correct and then enters it into database - not done
def confirmation_company_input(company_id, name, location, internship_id, description, positions):
    message = tk.messagebox.askquestion("Confirm submission", "Is all of your information correct?", icon="question")
    if message == "yes":
        try:
            # need connection for cursor to work
            conn = create_connection('internship.db')
            c = conn.cursor()
            c.execute('''INSERT INTO company VALUES (?, ?, ?, ?, ?, ?)''', (company_id.get(), name.get(),
                                                                            location.get(), internship_id.get(),
                                                                            description.get(),
                                                                            positions.get()))
            conn.commit()
            print("Registration successful! Returning to Main Menu.")
        except Error as e:
            print(e)
    else:
        tk.messagebox.showinfo("Return", "Returning to the previous screen...")


# Confirms user data collected from 'Internships' window is correct and then enters it into database - not done
def confirmation_internship_input(name, id_num, app_term, intern_term, description, review):
    message = tk.messagebox.askquestion("Confirm submission", "Is all of your information correct?", icon="question")
    if message == "yes":
        try:
            # need connection for cursor to work
            conn = create_connection('internship.db')
            c = conn.cursor()
            c.execute('''INSERT INTO internships VALUES (?, ?, ?, ?, ?, ?)''', (name.get(), id_num.get(),
                                                                                app_term.get(), intern_term.get(),
                                                                                description.get(), review.get()))
            conn.commit()
            print("Registration successful! Returning to Main Menu.")
        except Error as e:
            print(e)
    else:
        tk.messagebox.showinfo("Return", "Returning to the previous screen...")


# Confirms user data collected from 'Student Registration' window is correct and then enters it into database - done
def confirmation_student_input(first, last, address, telephone, email):
    message = tk.messagebox.askquestion("Confirm submission", "Is all of your information correct?", icon="question")
    if message == "yes":
        try:
            # need connection for cursor to work
            conn = create_connection('internship.db')
            c = conn.cursor()
            c.execute('''INSERT INTO registered_users VALUES (?, ?, ?, ?, ?)''', (last.get(), first.get(),
                                                                                  address.get(),
                                                                                  telephone.get(),
                                                                                  email.get()))
            conn.commit()
            print("Registration successful! Returning to Main Menu.")
        except Error as e:
            print(e)
    else:
        tk.messagebox.showinfo("Return", "Returning to the previous screen...")


# Return to 'Main Menu' prompt. Closes current window if 'yes' is clicked - done
def return_to_main_menu(current_window):
    message = tk.messagebox.askquestion("Please confirm", "Return to Main Menu?", icon="question")
    if message == "yes":
        current_window.destroy()
    else:
        tk.messagebox.showinfo("Return", "Returning to the previous screen...")


# def main_menu(conn):
#    menu_selection = int(input("Welcome to the internship database. Please enter a number from the menu below.\n"
#                               "1. Registration\n2. Query\n3. Create internship\n4. Exit program\n"))
#
#    # if menu_selection == 1:
#    #    print("Registration selected")
#    #    create_new_user(conn)
#    #if menu_selection == 2:
#    #    print("Query selected")
#    if menu_selection == 3:
#        print("Create internship selected")
#        create_new_internship(conn)
#    elif menu_selection == 4:
#        # Closes connection
#        conn.close()
#        # Ends program
#        sys.exit("Exiting program now...")
#    else:
#        # TODO need error handling here for input other than integer
#        print("Invalid input. Please try again.")
#        main_menu(conn)


def main():

    # creates database file or connects to database if the file already exists
    conn = create_connection('internship.db')

    # Creates a cursor to execute SQL commands
    cur = conn.cursor()

    # Creates main window
    root = Tk()
    root.title("Main Window")

    # TODO change window size as well as button layout. need to remove '.pack()' from label and button below first
    #  when executing geometry() function
    #root.geometry("500x300")

    myLabel1 = Label(root, text="Welcome to the internship database. Please choose an option below:").pack()
    # For the buttons below: in the section that says 'command=myClick1', do NOT add parenthesis after the
    # 'myClick1'part. if you do, the command linked to the button will run automatically
    tk.Button(root, text="Student Registration", command=create_student_registration_window).pack()
    tk.Button(root, text="Company Registration", command=create_company_registration_window).pack()
    tk.Button(root, text="Query Internships", command=internship_query_window).pack()
    tk.Button(root, text="Create Internship", command=create_new_internship_window).pack()
    tk.Button(root, text="Applications").pack()

    # Creation of SQL tables
    sql_create_registered_users_table = '''CREATE TABLE IF NOT EXISTS registered_users (
                    lastname text NOT NULL,
                    firstname text NOT NULL,
                    address text,
                    phone_number text,
                    email text NOT NULL UNIQUE
                    )'''

    # TODO change data type back to Integer for id
    sql_create_internships_table = '''CREATE TABLE IF NOT EXISTS internships (
                        company_name text,
                        internship_id text,
                        application_term text,
                        internship_term text,
                        description text,
                        experience_review text
                        )'''

    # TODO change data type back to Integer for id and positions
    sql_create_company_table = '''CREATE TABLE IF NOT EXISTS company (
                            company_id  text,
                            company_name text,
                            location text,
                            internship_id text,
                            internship_description text,
                            num_of_positions text,
                            primary key (company_id),
                            foreign key (internship_id) references internships
                            )'''

    # TODO create menu option and window
    sql_create_application_table = '''CREATE TABLE IF NOT EXISTS application (
                           application_id integer,
                           internship_id integer,
                           applicant_name text,
                           status text,
                           dates text,
                           primary key (application_id, applicant_name),
                           foreign key (internship_id) references internships
                           )'''

    if conn is not None:
        # Create 'registered_users' table
        create_table(conn, sql_create_registered_users_table)

        # Create 'internships' table
        create_table(conn, sql_create_internships_table)

        # Create 'company' table
        create_table(conn, sql_create_company_table)

        # Create 'application' table
        create_table(conn, sql_create_application_table)

    else:
        print("Error! Cannot establish connection to database.")

    root.mainloop()


if __name__ == '__main__':
    main()
