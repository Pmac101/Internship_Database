import sqlite3
import sys
from sqlite3 import Error


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


# Create new internship in 'internship' table - NOT done
def create_new_internship(conn):
    c = conn.cursor()

    # TODO error handling for invalid input
    company_name = input("Please enter the name of the company providing the internship:\n")

    # TODO the following 2 variables are currently placeholders. need to edit once we choose column names for
    #  'internship' table. don't forget to change variable names in SQL statement, too
    x = input("Please enter the type of internship: ***placeholder1***\n")
    y = input("Please enter...: ***placeholder2***\n")

    # TODO maybe add prompt to verify user input is correct before executing INSERT statement
    c.execute('''INSERT INTO internships VALUES (?, ?, ?)''', (company_name, x, y))

    conn.commit()
    print("Internship successfully created!\n")
    choice = int(input("What would you like to do?\n1. Create another internship\n2. Return to Main Menu\n"))

    if choice == 1:
        print("\'Create another internship\' selected")
        create_new_internship(conn)
    else:
        print("Returning to Main Menu...")
        main_menu(conn)


# Create new user in registered_users table - NOT done
def create_new_user(conn):
    c = conn.cursor()

    # TODO all data needs to have a specific format to allow for easy querying
    last = input("Please enter your last name:\n")
    first = input("Please enter your first name:\n")
    home_address = input("Please enter your home address:\n")
    phone = input("Please enter your phone number:\n")
    email_address = input("Please enter your email address:\n")

    # TODO maybe add prompt to verify user input is correct before executing INSERT statement
    try:
        c.execute('''INSERT INTO registered_users VALUES (?, ?, ?, ?, ?)''', (last, first, home_address, phone,
                                                                              email_address))
        conn.commit()
        print("Registration successful! Returning to Main Menu.")
        main_menu(conn)
    # TODO may need to modify this and make error message more accurate
    except Error:
        print("The email address " + email_address + " is already registered.")
        choice = int(input("What would you like to do?\n1. Try again\n2. Return to Main Menu\n"))

        if choice == 1:
            create_new_user(conn)
        else:
            print("Returning to Main Menu...")
            main_menu(conn)


# Create table - done
def create_table(conn, sql_table_create):
    try:
        c = conn.cursor()
        c.execute(sql_table_create)
        conn.commit()
    except Error as e:
        print(e)


# Create a query - NOT done
def create_query(conn):
    c = conn.cursor()

    # TODO need to add functionality that allows different types of queries.
    # -------optional retrieval functions-----
    # fetchone() function retrieves 1 row
    # fetchall() function retrieves all rows
    # ----------------------------------------

    choice = int(input("Select an option:\n1. Search available internships\n2. Placeholder_option_2 ***currently "
                      "queries 'registered_users' table***\n"))

    if choice == 1:
        # Selects all rows from 'internships' table
        c.execute("SELECT * FROM internships")
    elif choice == 2:
        # Selects all rows from 'registered_user' table **used for testing purposes at the moment**
        c.execute("SELECT * FROM registered_users")

    rows = c.fetchall()
    print("----------------Results----------------")
    for row in rows:
        print(row)
    print("---------------------------------------")

    # Submenu that appears after query results
    choice = int(input("\nWhat would you like to do?\n1. Return to Query Menu\n2. Return to Main Menu\n"))
    if choice == 1:
        create_query(conn)
    else:
        print("Returning to Main Menu...")
        main_menu(conn)


# Drop a table - may not need this, but saving it for now
#def drop_table(conn, sql_table_drop):
#    try:
#        c = conn.cursor()
#        c.execute(sql_table_drop)
#        conn.commit()
#    except Error as e:
#        print(e)


# TODO Displays main menu - NOT done
def main_menu(conn):
    menu_selection = int(input("Welcome to the internship database. Please enter a number from the menu below.\n"
                               "1. Registration\n2. Query\n3. Create internship\n4. Exit program\n"))

    if menu_selection == 1:
        print("Registration selected")
        create_new_user(conn)
    elif menu_selection == 2:
        print("Query selected")
        create_query(conn)
    elif menu_selection == 3:
        print("Create internship selected")
        create_new_internship(conn)
    elif menu_selection == 4:
        # Closes connection
        conn.close()
        # Ends program
        sys.exit("Exiting program now...")
    else:
        # TODO need error handling here for input other than integer
        print("Invalid input. Please try again.")
        main_menu(conn)


def main():

    # creates database file or connects to database if the file already exists
    conn = create_connection('internship.db')

    # Creates a cursor to execute SQL commands
    cur = conn.cursor()

    # Creation of SQL tables
    sql_create_registered_users_table = '''CREATE TABLE IF NOT EXISTS registered_users (
                    lastname text NOT NULL,
                    firstname text NOT NULL,
                    address text,
                    phone_number text,
                    email text NOT NULL UNIQUE
                    )'''

    # TODO in order to edit column names: database tab on right side of screen > tables > columns > right-click the
    #  column name and select 'rename'. Make sure to edit name in the code below, too
    sql_create_internships_table = '''CREATE TABLE IF NOT EXISTS internships (
                    company text,
                    placeholder1 text,
                    placeholder2 text
                    )'''

    if conn is not None:
        # Create 'registered_users' table
        create_table(conn, sql_create_registered_users_table)

        # Create 'internships' table
        create_table(conn, sql_create_internships_table)
    else:
        print("Error! Cannot establish connection to database.")

    # Commit changes to tables
    # conn.commit()

    # Display main menu
    main_menu(conn)


if __name__ == '__main__':
    main()