import main as m
import menu_student as ms
import menu_company as mc
from tkinter import *
from tkinter import messagebox


# Verify student login information
def verify_student_login(active_window, login_id, login_pin):
    # Creates connection to database
    conn = m.create_connection('internship.db')
    # Creates cursor
    c = conn.cursor()

    # Checks each variable to see if it is empty
    if not login_id.get() or not login_pin.get():
        messagebox.showwarning(title="Empty Field", message="Please complete each section.")
    elif len(login_pin.get()) != 6:
        messagebox.showwarning(title="Invalid PIN Length", message="PIN must be 6 digits.")
    else:
        try:
            # Checks if s_id is an integer type
            int(login_id.get())
            int(login_pin.get())

            # select company id and pin from registered_companies table
            c.execute("SELECT student_id, student_pin FROM registered_students WHERE student_id=? AND student_pin=?",
                      (login_id.get(), login_pin.get()))
            results = c.fetchone()

            if results is None:
                messagebox.showwarning(title="Account Not Found", message="Invalid login information. Please try "
                                                                          "again.")
            else:
                x = login_id.get()
                active_window.destroy()
                ms.student_window(x)
                messagebox.showinfo(title="Welcome", message="Login successful!")
        except ValueError:
            messagebox.showwarning(title="Invalid Data Type", message="ID and PIN may only contain numbers")


# Verify company login information
def verify_company_login(active_window, login_id, login_pin):
    # Creates connection to database
    conn = m.create_connection('internship.db')
    # Creates cursor
    c = conn.cursor()

    # Checks each variable to see if it is empty
    if not login_id.get() or not login_pin.get():
        messagebox.showwarning(title="Empty Field", message="Please complete each section.")
    elif len(login_pin.get()) != 6:
        messagebox.showwarning(title="Invalid PIN Length", message="PIN must be 6 digits.")
    else:
        try:
            # Checks if s_id is an integer type
            int(login_id.get())
            int(login_pin.get())

            # select company id and pin from registered_companies table
            c.execute("SELECT company_id, company_pin FROM registered_companies WHERE company_id=? AND company_pin=?",
                      (login_id.get(), login_pin.get()))
            results = c.fetchone()

            if results is None:
                messagebox.showwarning(title="Account Not Found", message="Invalid login information. Please try "
                                                                          "again.")
            else:
                x = login_id.get()
                active_window.destroy()
                mc.company_window(x)
                messagebox.showinfo(title="Welcome", message="Login successful!")
        except ValueError:
            messagebox.showwarning(title="Invalid Data Type", message="ID and PIN may only contain numbers")


# Creates login/registration window
def login_register_window():
    # Creates a window
    login_screen = Tk()
    # Sets window size
    login_screen.geometry("690x300")
    # Creates window title
    login_screen.title("Account Login")
    # Sets background color
    login_screen.configure(bg="#029E6D")

    image_header = PhotoImage(file="internship_header.png")
    Label(login_screen, image=image_header).pack()

    # Frames
    frame1 = Frame(login_screen, bg="#029E6D")
    frame2 = Frame(login_screen, bg="#029E6D")
    frame3 = Frame(login_screen, bg="#029E6D")
    frame4 = Frame(login_screen, bg="#029E6D")
    frame5 = Frame(login_screen, bg="#029E6D")

    # ----------Frame 1: login or register----------
    # Labels
    Label(frame1, text="Welcome! If you are a new user, please register first.",
          font=14).pack()
    # Buttons
    Button(frame1, text="Login", font=14, command=lambda: m.frame_transition(frame1, frame5)).pack()
    Button(frame1, text="Register", font=14, command=lambda: m.frame_transition(frame1, frame2)).pack()
    Button(frame1, text="Exit Program", font=14, command=lambda: login_screen.destroy()).pack()
    frame1.pack()

    # ----------Frame 2: select student or company----------
    # Labels
    Label(frame2, text="Are you a student or company?", font=14).pack()
    # Buttons
    Button(frame2, text="Student", font=14, command=lambda: m.frame_transition(frame2, frame3)).pack()
    Button(frame2, text="Company", font=14, command=lambda: m.frame_transition(frame2, frame4)).pack()
    Button(frame2, text="Back", font=14, command=lambda: m.frame_transition(frame2, frame1)).pack()

    # ----------Frame 3: student registration----------
    # Labels
    Label(frame3, text="Please fill in the boxes below:", font=14).grid(row=0)
    Label(frame3, text="Student ID:", font=14).grid(row=1)
    Label(frame3, text="First Name:", font=14).grid(row=2)
    Label(frame3, text="Last Name:", font=14).grid(row=3)
    Label(frame3, text="Phone:", font=14).grid(row=4)
    Label(frame3, text="E-mail:", font=14).grid(row=5)
    Label(frame3, text="Create a 6-digit PIN:", font=14).grid(row=6)
    # Entry boxes
    box_student_id = Entry(frame3, width=30)
    box_student_id.grid(row=1, column=1)
    box_first = Entry(frame3, width=30)
    box_first.grid(row=2, column=1)
    box_last = Entry(frame3, width=30)
    box_last.grid(row=3, column=1)
    box_phone_student = Entry(frame3, width=30)
    box_phone_student.grid(row=4, column=1)
    box_email_student = Entry(frame3, width=30)
    box_email_student.grid(row=5, column=1)
    box_pin_student = Entry(frame3, width=30)
    box_pin_student.grid(row=6, column=1)
    # Buttons
    register_button = Button(frame3, text="Register", font=14, command=lambda: m.confirmation_student_input(
        box_student_id, box_first, box_last, box_phone_student, box_email_student, box_pin_student, frame3, frame1))
    register_button.grid(row=7, column=1)

    back_button = Button(frame3, text="Back", font=14, command=lambda: m.frame_transition(frame3, frame2))
    back_button.grid(row=8, column=1)

    # ----------Frame 4: company registration----------
    # Labels
    Label(frame4, text="Please fill in the boxes below:", font=14).grid(row=0)
    Label(frame4, text="Company Name: ", font=14).grid(row=1)
    Label(frame4, text="Location: ", font=14).grid(row=2)
    Label(frame4, text="Phone: ", font=14).grid(row=3)
    Label(frame4, text="Email: ", font=14).grid(row=4)
    Label(frame4, text="Create a 6-digit PIN: ", font=14).grid(row=5)
    # Entry boxes
    box_company_name = Entry(frame4, width=30)
    box_company_name.grid(row=1, column=1)
    box_location = Entry(frame4, width=30)
    box_location.grid(row=2, column=1)
    box_phone_company = Entry(frame4, width=30)
    box_phone_company.grid(row=3, column=1)
    box_email_company = Entry(frame4, width=30)
    box_email_company.grid(row=4, column=1)
    box_pin_company = Entry(frame4, width=30)
    box_pin_company.grid(row=5, column=1)
    # Buttons
    register_button = Button(frame4, text="Register", font=14, command=lambda: m.confirmation_company_input(
        box_company_name, box_location, box_phone_company, box_email_company, box_pin_company, frame4, frame1))
    register_button.grid(row=6, column=1)

    back_button = Button(frame4, text="Back", font=14, command=lambda: m.frame_transition(frame4, frame2))
    back_button.grid(row=7, column=1)

    # ----------Frame 5: user login----------
    # Labels
    Label(frame5, text="ID:", font=14).grid(row=3, column=0)
    Label(frame5, text="PIN:", font=14).grid(row=4, column=0)
    # Entry boxes
    box_enter_id = Entry(frame5, width=30)
    box_enter_id.grid(row=3, column=1)
    box_enter_pin = Entry(frame5, width=30, show='*')
    box_enter_pin.grid(row=4, column=1)
    # Buttons
    student_button = Button(frame5, text="Student Login", font=14, command=lambda: verify_student_login(login_screen,
                                                                                                        box_enter_id,
                                                                                                        box_enter_pin))
    student_button.grid(row=5, column=1)
    company_button = Button(frame5, text="Company Login", font=14, command=lambda: verify_company_login(login_screen,
                                                                                                        box_enter_id,
                                                                                                        box_enter_pin))
    company_button.grid(row=6, column=1)
    back_button = Button(frame5, text="Back", font=14, command=lambda: m.frame_transition(frame5, frame1))
    back_button.grid(row=7, column=1)

    login_screen.mainloop()
