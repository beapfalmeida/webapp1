import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()


#  Cursor is an object that can execute sql queries

# Query data
cursor.execute("SELECT * FROM events WHERE band='Lions'")
result = cursor.fetchall()
print(result)
# Result is going to be a list of tuples, each item of the list is one row

# Insert new rows
new_rows = [('Cats', 'Cat City', '2088.10.17'),
            ('Hens', 'Hen City', '2088.10.17')]
cursor.executemany("INSERT INTO events VALUES (?,?,?)", new_rows)
connection.commit()

# Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)
