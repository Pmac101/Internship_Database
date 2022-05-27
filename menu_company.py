import main as m
import query as q
from tkinter import *


# Company main window
def company_window(current_user_id):
    # Creates a window
    company_screen = Tk()
    # Sets window size
    company_screen.geometry("550x250")
    # Creates window title
    company_screen.title("Company Menu")
    # Sets background color
    company_screen.configure(bg="#029E6D")

    # Current user ID
    current_user = current_user_id

    # Frames
    frame1 = Frame(company_screen, bg="#029E6D")
    frame2 = Frame(company_screen, bg="#029E6D")

    # ----------Frame 1: main company menu----------
    # Buttons
    Button(frame1, text="Create Internship", font=14, command=lambda: m.frame_transition(frame1, frame2)).pack()
    Button(frame1, text="Query Internships", font=14, command=lambda: m.open_window(q.internship_query_window())).pack()
    Button(frame1, text="Query Applications", font=14, command=lambda: m.open_window(q.application_query_window(
        "company", current_user))).pack()
    Button(frame1, text="Exit Program", font=14, command=lambda: company_screen.destroy()).pack()

    frame1.pack()

    # ----------Frame 2: create internship----------
    c_id = current_user_id

    # Creates display text
    Label(frame2, text="Please fill in the boxes below:", font=14).grid(row=0)
    Label(frame2, text="Company Name:", font=14).grid(row=1)
    Label(frame2, text="Start Date:", font=14).grid(row=2)
    Label(frame2, text="End Date:", font=14).grid(row=3)
    Label(frame2, text="Description:", font=14).grid(row=4)
    # Entry boxes
    box_company_name = Entry(frame2, width=30)
    box_company_name.grid(row=1, column=1)
    box_start = Entry(frame2, width=30)
    box_start.grid(row=2, column=1)
    box_end = Entry(frame2, width=30)
    box_end.grid(row=3, column=1)
    box_description = Entry(frame2, width=30)
    box_description.grid(row=4, column=1)
    # Buttons
    submit_button = Button(frame2, text="Submit", font=14, command=lambda: m.confirmation_internship_input(
        box_company_name, c_id, box_start, box_end, box_description, frame2, frame1))
    submit_button.grid(row=5, column=1)
    back_button = Button(frame2, text="Back", font=14, command=lambda: m.frame_transition(frame2, frame1))
    back_button.grid(row=7, column=1)
