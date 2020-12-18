import sqlite3

# Connect to database
connection = sqlite3.connect('contacts.db')

# Create a cursor
cursor_var = connection.cursor()

# Create a table
cursor_var.execute("""CREATE TABLE contacts (
    name text,
    address text,
    phone integer,
    email text
)""")