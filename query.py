import main as m
from tkinter import *
from tkinter import ttk


# Creates application query window
def application_query_window(return_window, current_user_id):
    # Creates connection to database
    conn = m.create_connection('internship.db')
    # Creates cursor
    c = conn.cursor()

    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Application Query")
    # Sets window size
    top.geometry("1050x300")
    # Ensures this window stay on top
    top.attributes('-topmost', True)
    # Sets background color
    top.configure(bg="#029E6D")

    Label(top, text="Application search results: ", font=14).grid(row=1, column=0)

    # Define columns
    columns = ("application_id", "student_id", "student_first", "student_last", "internship_id")

    # Creates display table
    tree_application = ttk.Treeview(top, columns=columns, show='headings')
    tree_application.grid(row=2, column=0, padx=20)

    # Define headings
    tree_application.heading("application_id", text="Application ID", anchor=W)
    tree_application.heading("student_id", text="Student ID", anchor=W)
    tree_application.heading("student_first", text="First Name", anchor=W)
    tree_application.heading("student_last", text="Last Name", anchor=W)
    tree_application.heading("internship_id", text="Internship ID", anchor=W)

    # Fetches the current user's applications
    if return_window == "student":
        c.execute("SELECT * FROM application WHERE student_id=?", (current_user_id,))
    else:
        c.execute("SELECT * FROM application WHERE internship_id IN (SELECT internship_id FROM "
                  "internships WHERE company_id=?)", (current_user_id,))

    rows = c.fetchall()
    count = 0
    for row in rows:
        tree_application.insert("", index='end', text="", values=(row[0], row[1], row[2], row[3], row[4]))
        count += 1

    # Creates scrollbar
    scroll = Scrollbar(top, orient=VERTICAL, command=tree_application.yview)
    scroll.configure(command=tree_application.yview)
    tree_application.configure(yscrollcommand=scroll.set)
    scroll.grid(row=2, column=0, sticky='NSE')

    menu_btn = Button(top, text="Close Window", font=14, command=lambda: top.destroy())
    menu_btn.grid(row=3, column=0)


# Creates internship query window
def internship_query_window():
    # Creates connection to database
    conn = m.create_connection('internship.db')
    # Creates cursor
    c = conn.cursor()

    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Internship Query")
    # Sets window size
    top.geometry("850x300")
    # Ensures this window stay on top
    top.attributes('-topmost', True)
    # Sets background color
    top.configure(bg="#029E6D")

    Label(top, text="Internship search results: ", font=14).grid(row=1, column=0)

    # Define columns
    columns = ("internship_id", "company_name", "company_id", "start_date", "end_date", "description")

    # Creates display table
    tree_internship = ttk.Treeview(top, columns=columns, show='headings')
    tree_internship.grid(row=2, column=0, padx=20)

    # Define headings
    tree_internship.column("internship_id", width=75)
    tree_internship.heading("internship_id", text="Internship ID", anchor=W)
    tree_internship.column("company_name", width=200)
    tree_internship.heading("company_name", text="Company Name", anchor=W)
    tree_internship.column("company_id", width=100)
    tree_internship.heading("company_id", text="Company ID", anchor=W)
    tree_internship.column("start_date", width=100)
    tree_internship.heading("start_date", text="Start Date", anchor=W)
    tree_internship.column("end_date", width=100)
    tree_internship.heading("end_date", text="End Date", anchor=W)
    tree_internship.column("description", width=200)
    tree_internship.heading("description", text="Description", anchor=W)

    # Fetches all data from 'internships' table and outputs it into a display table
    c.execute("SELECT * FROM internships")
    rows = c.fetchall()
    count = 0

    for row in rows:
        tree_internship.insert("", index='end', text="", values=(row[0], row[1], row[2], row[3], row[4], row[5]))
        count += 1

    menu_btn = Button(top, text="Close Window", font=14, command=lambda: top.destroy())
    menu_btn.grid(row=3, column=0)

    # Creates scrollbar
    scroll = Scrollbar(top, orient=VERTICAL, command=tree_internship.yview)
    scroll.configure(command=tree_internship.yview)
    tree_internship.configure(yscrollcommand=scroll.set)
    scroll.grid(row=2, column=0, sticky='NSE')
