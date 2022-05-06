import main as m
from tkinter import *
from tkinter import ttk


# TODO Create output table **continue here**
# Creates application query window
def application_query_window():
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Application Query")
    # Sets window size
    top.geometry("800x400")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)
    # Sets background color
    top.configure(bg="#029E6D")

    # Creates connection to database
    conn = m.create_connection('internship.db')
    # Creates cursor
    c = conn.cursor()

    c.execute("SELECT * FROM application")

    rows = c.fetchall()
    results = ""

    for row in rows:
        results += str(row) + "\n"

    conn.commit()

    Label(top, text="Application search results: ").grid(row=1, column=0)
    # Creates output Text box
    output_box = Text(top, height=15, width=95, bg="white")
    output_box.grid(row=2, column=0)
    output_box.insert(END, results)

    main_menu_btn = Button(top, text="Main Menu", command=lambda: m.return_to_main_menu(top))
    main_menu_btn.grid(row=3, column=0)


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
    top.geometry("1050x300")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)
    # Sets background color
    top.configure(bg="#029E6D")

    Label(top, text="Internship search results: ", font=14).grid(row=1, column=0)

    # Define columns
    columns = ("company_name", "internship_id", "start_date", "end_date", "description")

    # Creates display table
    tree_internship = ttk.Treeview(top, columns=columns, show='headings')
    tree_internship.grid(row=2, column=0, padx=20)

    # Define headings
    tree_internship.heading("company_name", text="Company", anchor=W)
    tree_internship.heading("internship_id", text="Internship ID", anchor=W)
    tree_internship.heading("start_date", text="Start Date", anchor=W)
    tree_internship.heading("end_date", text="End Date", anchor=W)
    tree_internship.heading("description", text="Description", anchor=W)

    # Fetches all data from 'internships' table and outputs it into a display table
    c.execute("SELECT * FROM internships")
    rows = c.fetchall()
    count = 0

    for row in rows:
        tree_internship.insert("", index='end', text="", values=(row[0], row[1], row[2], row[3], row[4]))
        count += 1

    # Button creation
    main_menu_btn = Button(top, text="Main Menu", command=lambda: m.return_to_main_menu(top))
    main_menu_btn.grid(row=3, column=0)
