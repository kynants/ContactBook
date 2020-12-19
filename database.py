import sqlite3

# Connect to database
connection = sqlite3.connect('contacts.db')

# Create a cursor
cursor_var = connection.cursor()

# CREATE A TABLE
# cursor_var.execute("""CREATE TABLE contacts (
#     name text,
#     address text,
#     phone integer,
#     email text
# )""")

# INSERT MULTIPLE CONTACTS
# Question: How do I format the phone numbers?
# Answer: https://stackoverflow.com/questions/75105/what-datatype-should-be-used-for-storing-phone-numbers-in-sql-server-2005
# multiple_contacts = [
#     ('John', '123 Main St', '1234567890', 'john@site.com'),
#     ('Bob', '456 2nd St', '0987654321', 'bob@site.com'),
#     ('Sally', '789 3rd St', '5556667777', 'sally@site.com')
# ]
# connection.executemany("INSERT INTO contacts VALUES (?,?,?,?)", multiple_contacts)

# Commit command
connection.commit()

# Close connection
connection.close()