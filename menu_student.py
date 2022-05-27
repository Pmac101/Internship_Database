import main as m
import query as q
from tkinter import *


# Student main window
def student_window(current_user_id):
    # Creates a window
    student_screen = Tk()
    # Sets window size
    student_screen.geometry("650x250")
    # Creates window title
    student_screen.title("Student Menu")
    # Sets background color
    student_screen.configure(bg="#029E6D")

    # Current user ID
    current_user = current_user_id

    # Frames
    frame1 = Frame(student_screen, bg="#029E6D")
    frame2 = Frame(student_screen, bg="#029E6D")

    # ----------Frame 1: main student menu----------
    # Buttons
    Button(frame1, text="Apply To Internship", font=14, command=lambda: m.frame_transition(frame1, frame2)).pack()
    Button(frame1, text="Query Internships", font=14, command=lambda: m.open_window(q.internship_query_window())).pack()
    Button(frame1, text="View Submitted Applications", font=14, command=lambda: m.open_window(
        q.application_query_window("student", current_user))).pack()
    Button(frame1, text="Exit Program", font=14, command=lambda: student_screen.destroy()).pack()
    frame1.pack()

    # ----------Frame 2: application----------
    # Labels
    Label(frame2, text="Please fill in the boxes below:", font=14).grid(row=0)
    Label(frame2, text="Student ID:", font=14).grid(row=1)
    Label(frame2, text="First Name:", font=14).grid(row=2)
    Label(frame2, text="Last Name:", font=14).grid(row=3)
    Label(frame2, text="Internship ID:", font=14).grid(row=4)
    # Entry boxes
    box_student_id = Entry(frame2, width=30)
    box_student_id.grid(row=1, column=1)
    box_first = Entry(frame2, width=30)
    box_first.grid(row=2, column=1)
    box_last = Entry(frame2, width=30)
    box_last.grid(row=3, column=1)
    box_internship_id = Entry(frame2, width=30)
    box_internship_id.grid(row=4, column=1)
    # Buttons
    submit_button = Button(frame2, text="Submit", font=14, command=lambda: m.confirmation_application_input(
        box_student_id, box_first, box_last, box_internship_id, frame2, frame1))
    submit_button.grid(row=5, column=1)

    back_button = Button(frame2, text="Back", font=14, command=lambda: m.frame_transition(frame2, frame1))
    back_button.grid(row=6, column=1)
