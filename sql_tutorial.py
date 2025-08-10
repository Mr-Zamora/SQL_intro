import sqlite3

# Connect to a database (or create one if it doesn't exist)
# This will create a file named 'mydatabase.db' in the same folder.
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object. This is what you use to execute SQL commands.
cursor = conn.cursor()

# 1. CREATE a table
# We'll create a table called 'users' with three columns: id, name, and email.
# The 'id' will be our primary key, which means it's a unique identifier for each row.
# --- SQL QUERY: CREATE ---
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')
print("Table 'users' created successfully.")

# 2. INSERT data into the table
# Let's add some users to our table.
users_to_add = [
    (1, 'Alice', 'alice@example.com'),
    (2, 'Bob', 'bob@example.com'),
    (3, 'Charlie', 'charlie@example.com')
]

# Use executemany to insert all the users at once
# The '?' are placeholders for the data we are inserting.
# --- SQL QUERY: INSERT ---
cursor.executemany('INSERT OR IGNORE INTO users (id, name, email) VALUES (?,?,?)', users_to_add)
print(f"{cursor.rowcount} users added successfully.")

# Save (commit) the changes
conn.commit()

# 3. SELECT data from the table
# Let's see what's in our table.
print("\n--- All users in the table ---")
# --- SQL QUERY: SELECT ALL ---
cursor.execute('SELECT * FROM users')
all_users = cursor.fetchall() # fetchall() gets all the results
for user in all_users:
    print(user)

# 4. UPDATE data
# Let's say Bob changes his email address.
print("\n--- Updating Bob's email ---")
# --- SQL QUERY: UPDATE ---
cursor.execute("UPDATE users SET email = 'bob_new@example.com' WHERE name = 'Bob'")
conn.commit()
print("Bob's email has been updated.")

# Let's select Bob's record to see the change
# --- SQL QUERY: SELECT ONE ---
cursor.execute("SELECT * FROM users WHERE name = 'Bob'")
bob = cursor.fetchone() # fetchone() gets the first result
print(bob)

# 5. DELETE data
# Now, let's say Charlie decides to leave.
print("\n--- Deleting Charlie from the table ---")
# --- SQL QUERY: DELETE ---
cursor.execute("DELETE FROM users WHERE name = 'Charlie'")
conn.commit()
print(f"{cursor.rowcount} user(s) deleted.")

# Let's look at the table one last time
print("\n--- Final state of the table ---")
# --- SQL QUERY: SELECT ALL ---
cursor.execute('SELECT * FROM users')
final_users = cursor.fetchall()
for user in final_users:
    print(user)

# Close the connection to the database
conn.close()
