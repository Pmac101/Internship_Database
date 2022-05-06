import main as m
from tkinter import *


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
    # Creates a window
    top = Toplevel()
    # Creates window title
    top.title("Internship Query")
    # Sets window size
    top.geometry("800x400")
    # Ensures this window stay on top of Main Menu when confirmation window pops up
    top.attributes('-topmost', True)

    # Creates connection to database
    conn = m.create_connection('internship.db')
    # Creates cursor
    c = conn.cursor()

    c.execute("SELECT * FROM internships")

    rows = c.fetchall()
    results = ""

    for row in rows:
        results += str(row) + "\n"

    conn.commit()

    Label(top, text="Internship search results: ").grid(row=1, column=0)
    # Creates output Text box
    output_box = Text(top, height=15, width=95, bg="white")
    output_box.grid(row=2, column=0)
    output_box.insert(END, results)

    main_menu_btn = Button(top, text="Main Menu", command=lambda: m.return_to_main_menu(top))
    main_menu_btn.grid(row=3, column=0)