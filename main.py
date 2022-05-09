import sqlite3
import create as c
import query as q
import registration as r
from sqlite3 import Error
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


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


# Create table
def create_table(conn, sql_table_create):
    try:
        c = conn.cursor()
        c.execute(sql_table_create)
        conn.commit()
    except Error as e:
        print(e)


# Confirms user data collected from 'Application' window is correct and then enters it into database
def confirmation_application_input(s_id, first, last, internship_id):
    message = messagebox.askquestion("Confirm submission", "Is all of your information correct?", icon="question")
    if message == "yes":
        try:
            if not s_id.get() or not first.get() or not last.get() or not internship_id.get():
                messagebox.showwarning(title="Empty Field", message="Please complete each section.")
            else:
                try:
                    # Checks if data in Student ID and Internship ID fields are integers
                    int(s_id.get())
                    int(internship_id.get())

                    app_id__placeholder = None

                    # need connection for cursor to work
                    conn = create_connection('internship.db')
                    c = conn.cursor()
                    c.execute('''INSERT INTO application VALUES (?, ?, ?, ?, ?)''', (app_id__placeholder, s_id.get(),
                                                                                     first.get(), last.get(),
                                                                                     internship_id.get()))
                    conn.commit()

                    c.execute('''SELECT application_id FROM application ORDER BY application_id DESC LIMIT 1''')
                    application_number = c.fetchone()

                    messagebox.showinfo(title="You're all set!", message="Application successfully submitted! Your"
                                                                         "application ID is: " +
                                                                         str(application_number[0]))
                except ValueError:
                    messagebox.showwarning(title="Invalid Data Type", message="Student ID and Internship ID may only "
                                                                              "contain numbers.")
        except Error as e:
            print(e)
    else:
        messagebox.showinfo("Return", "Returning to the previous screen...")


# Confirms user data collected from 'Company Registration' window is correct and then enters it into database
def confirmation_company_input(name, location, phone, email):
    message = messagebox.askquestion("Confirm submission", "Is all of your information correct?", icon="question")
    if message == "yes":
        try:
            if not name.get() or not location.get() or not phone.get() or not email.get():
                messagebox.showwarning(title="Empty Field", message="Please complete each section.")
            else:
                try:
                    increment_placeholder = None

                    # need connection for cursor to work
                    conn = create_connection('internship.db')
                    c = conn.cursor()

                    c.execute('''INSERT INTO registered_companies VALUES (?, ?, ?, ?, ?)''', (increment_placeholder,
                                                                                              name.get(),
                                                                                              location.get(),
                                                                                              phone.get(), email.get()))
                    conn.commit()

                    c.execute('''SELECT company_id FROM registered_companies ORDER BY company_id DESC LIMIT 1''')
                    company_number = c.fetchone()

                    messagebox.showinfo(title="You're all set!", message="Company registration successful! Your "
                                                                         "company ID is: " + str(company_number[0]))
                except ValueError:
                    messagebox.showwarning(title="Invalid Data Type", message="**update this**")
        except Error:
            messagebox.showwarning(title="Unable To Register", message="This email address has already been "
                                                                       "registered. Please try a different one.")
    else:
        messagebox.showinfo("Return", "Returning to the previous screen...")


# Confirms user data collected from 'Internships' window is correct and then enters it into database
def confirmation_internship_input(name, start, end, description):
    message = messagebox.askquestion("Confirm submission", "Is all of your information correct?", icon="question")
    if message == "yes":
        try:
            if not name.get() or not start.get() or not end.get() or not description.get():
                messagebox.showwarning(title="Empty Field", message="Please complete each section.")
            else:

                increment_placeholder = None

                # need connection for cursor to work
                conn = create_connection('internship.db')
                c = conn.cursor()

                c.execute('''INSERT INTO internships VALUES (?, ?, ?, ?, ?)''', (increment_placeholder, name.get(),
                                                                                 start.get(), end.get(),
                                                                                 description.get()))
                conn.commit()

                c.execute('''SELECT internship_id FROM internships ORDER BY internship_id DESC LIMIT 1''')
                internship_number = c.fetchone()

                messagebox.showinfo(title="You're all set!", message="Internship successfully created! The ID number "
                                                                     "for this internship is: " +
                                                                     str(internship_number[0]))
        except Error as e:
            print(e)
    else:
        messagebox.showinfo("Return", "Returning to the previous screen...")


# Confirms user data collected from 'Student Registration' window is correct and then enters it into database
def confirmation_student_input(s_id, first, last, address, phone, email):
    message = messagebox.askquestion("Confirm submission", "Is all of your information correct?", icon="question")
    if message == "yes":
        try:
            # Checks each variable to see if it is empty
            if not s_id.get() or not first.get() or not last.get() or not phone.get() or not email.get():
                messagebox.showwarning(title="Empty Field", message="Please complete each section.")
            else:
                try:
                    # Checks if s_id is an integer type
                    int(s_id.get())

                    # need connection for cursor to work
                    conn = create_connection('internship.db')
                    c = conn.cursor()
                    c.execute('''INSERT INTO registered_students VALUES (?, ?, ?, ?, ?, ?)''', (s_id.get(), first.get(),
                                                                                                last.get(),
                                                                                                address.get(),
                                                                                                phone.get(),
                                                                                                email.get()))
                    conn.commit()
                    messagebox.showinfo(title="You're all set!", message="Student registration successful!")
                except ValueError:
                    messagebox.showwarning(title="Invalid Data Type", message="Student ID may only contain numbers")

        except Error:
            messagebox.showwarning(title="Unable To Register", message="This email address has already been "
                                                                       "registered. Please try a different one.")
    else:
        messagebox.showinfo("Return", "Returning to the previous screen...")


# Return to 'Main Menu' prompt. Closes current window if 'yes' is clicked
def return_to_main_menu(current_window):
    message = messagebox.askquestion("Please confirm", "Return to Main Menu?", icon="question")
    if message == "yes":
        current_window.destroy()
    else:
        messagebox.showinfo("Return", "Returning to the previous screen...")


def main():
    # creates database file or connects to database if the file already exists
    conn = create_connection('internship.db')

    # Creates main window
    root = Tk()
    root.title("Main Window")

    # Create FGCU image
    img_banner = ImageTk.PhotoImage(Image.open("fgcu_logo.png"))
    label_banner = Label(image=img_banner)
    label_banner.grid(row=0)

    # Sets background color
    root.configure(bg="#029E6D")

    Label(root, text="Welcome to the internship database. Please choose an option below:", font=14).grid(row=1)

    # Creation of Main Menu buttons
    Button(root, text="Student Registration", font=14, command=r.create_student_registration_window).grid(row=2,
                                                                                                          pady=5)
    Button(root, text="Company Registration", font=14, command=r.create_company_registration_window).grid(row=3, pady=5)
    Button(root, text="Apply To Internship", font=14, command=c.create_application_window).grid(row=4, pady=5)
    Button(root, text="Create Internship", font=14, command=c.create_new_internship_window).grid(row=5, pady=5)
    Button(root, text="Query Internships", font=14, command=q.internship_query_window).grid(row=6, pady=5)

    # Disabled buttons
    # Button(root, text="Query Applications", font=14, command=q.application_query_window).pack()

    # Creation of SQL tables
    sql_create_registered_students_table = '''CREATE TABLE IF NOT EXISTS registered_students (
                    student_id integer NOT NULL UNIQUE, 
                    firstname text NOT NULL,
                    lastname text NOT NULL,
                    address text NOT NULL,
                    phone_number text NOT NULL,
                    email text NOT NULL UNIQUE
                    )'''

    sql_create_internships_table = '''CREATE TABLE IF NOT EXISTS internships (
                        internship_id integer primary key AUTOINCREMENT,
                        company_name text NOT NULL,
                        start_date text NOT NULL,
                        end_date text NOT NULL,
                        description text NOT NULL
                        )'''

    sql_create_registered_companies_table = '''CREATE TABLE IF NOT EXISTS registered_companies (
                            company_id  integer primary key AUTOINCREMENT,
                            company_name text NOT NULL,
                            location text NOT NULL,
                            phone text NOT NULL,
                            email text NOT NULL UNIQUE
                            )'''

    sql_create_application_table = '''CREATE TABLE IF NOT EXISTS application (
                           application_id integer primary key AUTOINCREMENT,
                           student_id text NOT NULL,
                           student_first text NOT NULL,
                           student_last text NOT NULL,
                           internship_id integer
                           )'''

    if conn is not None:
        # Create 'registered_users' table
        create_table(conn, sql_create_registered_students_table)

        # Create 'internships' table
        create_table(conn, sql_create_internships_table)

        # Create 'company' table
        create_table(conn, sql_create_registered_companies_table)

        # Create 'application' table
        create_table(conn, sql_create_application_table)

    else:
        print("Error! Cannot establish connection to database.")

    root.mainloop()


if __name__ == '__main__':
    main()
