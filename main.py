import sqlite3
import login as l
from sqlite3 import Error
from tkinter import *
from tkinter import messagebox



# Create connection to database
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


# Forgets old frame and switches to new frame
def frame_transition(current_frame, new_frame):
    new_frame.pack()
    current_frame.pack_forget()


# Opens new window
def open_window(current_window):
    current_window


# Delete text in Entry boxes
def clear_text(entry1, entry2, entry3, entry4, entry5=None, entry6=None, entry7=None):
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)

    if entry5 is not None:
        entry5.delete(0, END)
        if entry6 is not None:
            entry6.delete(0, END)
            if entry7 is not None:
                entry7.delete(0, END)


# Saves the ID of the user logging in
def save_id(user_id):
    user_id


# Confirms user data collected from 'Application' window is correct and then enters it into database
def confirmation_application_input(s_id, first, last, internship_id, current_frame, new_frame):
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

                    messagebox.showinfo(title="You're all set!", message="Application successfully submitted! Your "
                                                                         "application ID is: " +
                                                                         str(application_number[0]))
                    clear_text(s_id, first, last, internship_id)
                    frame_transition(current_frame, new_frame)
                except ValueError:
                    messagebox.showwarning(title="Invalid Data Type", message="Student ID and Internship ID may only "
                                                                              "contain numbers.")
        except Error as e:
            print(e)
    else:
        messagebox.showinfo("Return", "Returning to the previous screen...")


# Confirms user data collected from 'Company Registration' window is correct and then enters it into database
def confirmation_company_input(name, location, phone, email, c_pin, current_frame, new_frame):
    message = messagebox.askquestion("Confirm submission", "Is all of your information correct?", icon="question")
    if message == "yes":
        try:
            if not name.get() or not location.get() or not phone.get() or not email.get() or not c_pin.get():
                messagebox.showwarning(title="Empty Field", message="Please complete each section.")
            elif len(c_pin.get()) != 6:
                messagebox.showwarning(title="Invalid PIN Length", message="PIN must be 6 digits.")
            else:
                try:
                    increment_placeholder = None
                    int(c_pin.get())

                    # need connection for cursor to work
                    conn = create_connection('internship.db')
                    c = conn.cursor()

                    c.execute('''INSERT INTO registered_companies VALUES (?, ?, ?, ?, ?, ?)''',
                              (increment_placeholder, name.get(), location.get(), phone.get(), email.get(),
                               c_pin.get()))
                    conn.commit()

                    c.execute('''SELECT company_id FROM registered_companies ORDER BY company_id DESC LIMIT 1''')
                    company_number = c.fetchone()

                    messagebox.showinfo(title="You're all set!", message="Company registration successful! Your "
                                                                         "company ID is: " + str(company_number[0]))

                    clear_text(name, location, phone, email, c_pin)
                    frame_transition(current_frame, new_frame)
                except ValueError:
                    messagebox.showwarning(title="Invalid Data Type", message="PIN may only contain "
                                                                              "numbers.")
        except Error:
            message_return_menu = messagebox.askquestion("Unable to Register", message="This email address has "
                                                                                       "already been registered. "
                                                                                       "Would you like to register a "
                                                                                       "different one?", icon="error")
            if message_return_menu == "no":
                messagebox.showinfo("", "Returning to login screen...")
                frame_transition(current_frame, new_frame)
    else:
        messagebox.showinfo("Return", "Please make desired changes and resubmit")


# Confirms user data collected from 'Internships' window is correct and then enters it into database
def confirmation_internship_input(name, c_id, start, end, description, current_frame, new_frame):
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

                c.execute('''INSERT INTO internships VALUES (?, ?, ?, ?, ?, ?)''', (increment_placeholder,
                                                                                    name.get(), c_id,
                                                                                    start.get(), end.get(),
                                                                                    description.get()))
                conn.commit()

                c.execute('''SELECT internship_id FROM internships ORDER BY internship_id DESC LIMIT 1''')
                internship_number = c.fetchone()

                messagebox.showinfo(title="You're all set!", message="Internship successfully created! The ID number "
                                                                     "for this internship is: " +
                                                                     str(internship_number[0]))
                clear_text(name, start, end, description)
                frame_transition(current_frame, new_frame)
        except Error as e:
            print(e)
    else:
        messagebox.showinfo("Return", "Returning to the previous screen...")


# Confirms user data collected from 'Student Registration' window is correct and then enters it into database
def confirmation_student_input(s_id, first, last, phone, email, s_pin, current_frame, new_frame):
    message = messagebox.askquestion("Confirm submission", "Is all of your information correct?", icon="question")
    if message == "yes":
        try:
            # Checks each variable to see if it is empty
            if not s_id.get() or not first.get() or not last.get() or not phone.get() or not email.get() or not s_pin.get():
                messagebox.showwarning(title="Empty Field", message="Please complete each section.")
            elif len(s_pin.get()) != 6:
                messagebox.showwarning(title="Invalid PIN Length", message="PIN must be 6 digits.")
            else:
                try:
                    # Checks if s_id is an integer type
                    int(s_id.get())
                    int(s_pin.get())

                    # need connection for cursor to work
                    conn = create_connection('internship.db')
                    c = conn.cursor()
                    c.execute('''INSERT INTO registered_students VALUES (?, ?, ?, ?, ?, ?)''', (s_id.get(),
                                                                                                first.get(),
                                                                                                last.get(),
                                                                                                phone.get(),
                                                                                                email.get(),
                                                                                                s_pin.get()))
                    conn.commit()
                    messagebox.showinfo(title="You're all set!", message="Student registration successful!")
                    clear_text(s_id, first, last, phone, email, s_pin)
                    frame_transition(current_frame, new_frame)
                except ValueError:
                    messagebox.showwarning(title="Invalid Data Type", message="Student ID and PIN may only contain "
                                                                              "numbers")

        except Error:
            message_return_menu = messagebox.askquestion("Unable to Register", message="This email address has "
                                                                                       "already been registered. "
                                                                                       "Would you like to register a "
                                                                                       "different one?", icon="error")
            if message_return_menu == "no":
                messagebox.showinfo("", "Returning to login screen...")
                clear_text(s_id, first, last, phone, email, s_pin)
                frame_transition(current_frame, new_frame)
    else:
        messagebox.showinfo("Return", "Please make desired changes and resubmit.")


def main():
    # creates database file or connects to database if the file already exists
    conn = create_connection('internship.db')

    l.login_register_window()

    # Creation of SQL tables
    sql_create_registered_students_table = '''CREATE TABLE IF NOT EXISTS registered_students (
                    student_id integer NOT NULL UNIQUE, 
                    firstname text NOT NULL,
                    lastname text NOT NULL,
                    phone_number text NOT NULL,
                    email text NOT NULL UNIQUE,
                    student_pin integer NOT NULL
                    )'''

    sql_create_internships_table = '''CREATE TABLE IF NOT EXISTS internships (
                        internship_id integer primary key AUTOINCREMENT,
                        company_name text NOT NULL,
                        company_id integer NOT NULL,
                        start_date text NOT NULL,
                        end_date text NOT NULL,
                        description text NOT NULL
                        )'''

    sql_create_registered_companies_table = '''CREATE TABLE IF NOT EXISTS registered_companies (
                            company_id  integer primary key AUTOINCREMENT,
                            company_name text NOT NULL,
                            location text NOT NULL,
                            phone text NOT NULL,
                            email text NOT NULL UNIQUE,
                            company_pin integer NOT NULL
                            )'''

    sql_create_application_table = '''CREATE TABLE IF NOT EXISTS application (
                           application_id integer primary key AUTOINCREMENT,
                           student_id text NOT NULL,
                           student_first text NOT NULL,
                           student_last text NOT NULL,
                           internship_id integer
                           )'''

    if conn is not None:
        # Create 'registered_students' table
        create_table(conn, sql_create_registered_students_table)

        # Create 'internships' table
        create_table(conn, sql_create_internships_table)

        # Create 'registered_companies' table
        create_table(conn, sql_create_registered_companies_table)

        # Create 'application' table
        create_table(conn, sql_create_application_table)

    else:
        print("Error! Cannot establish connection to database.")


if __name__ == '__main__':
    main()
