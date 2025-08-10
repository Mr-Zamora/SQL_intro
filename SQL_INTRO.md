# Introduction to SQL with Python

This file provides a simple, beginner-friendly introduction to using SQL (Structured Query Language) with Python. We use Python's built-in `sqlite3` library to create and interact with a simple database.

## SQL vs. JSON: What's the Difference?

If you've worked with data before, you might have used JSON files. It's helpful to understand how a SQL database is different and why you would use one.

| Feature | JSON (like a text file) | SQL Database (like a collection of smart spreadsheets) |
| :--- | :--- | :--- |
| **Purpose** | Storing and exchanging data in a human-readable format. | Storing, managing, and **querying** large sets of structured data efficiently. |
| **Structure** | Hierarchical (data nested inside other data, like a tree). | Relational (data organized into tables with strict rows and columns). |
| **Rules** | No rules. You can put anything anywhere. | Strict rules (schema) that you define. e.g., a column must be a number and cannot be empty. |
| **Querying** | You must load the **entire file** into your program (e.g., Python) and write code to search through it. | You send a short query (an SQL command) to the database, and it sends back **only the data you asked for**. |

### Why Use SQL Instead of a JSON File?

While a JSON file is great for configuration or small amounts of data, you should use a SQL database when your data becomes more important or complex. Here's why:

1.  **Powerful Querying**: SQL can instantly find, filter, sort, and calculate data, even across millions of rows. To find all users from a specific country in a large JSON file, you'd have to write a slow, manual search in Python. With SQL, it's a single, fast command: `SELECT * FROM users WHERE country = 'Canada';`.
2.  **Data Integrity**: SQL enforces your rules. It can prevent duplicate emails, ensure every user has an ID, and stop you from accidentally saving a user's age as "ninety-nine". A JSON file offers no such protection.
3.  **Performance & Scalability**: Databases are built for speed. They can retrieve a single record from millions without loading everything into memory. A JSON file becomes very slow and memory-intensive as it grows.
4.  **Concurrency**: A database can safely handle multiple programs (or users) reading and writing data at the same time. Trying to have multiple programs write to the same JSON file at once often leads to data corruption.

**In short:** Use JSON for sending data or for simple configuration files. Use a SQL database when you need to reliably store, manage, and query structured data.

## Python Code Example

The following Python script demonstrates the basic `CRUD` (Create, Read, Update, Delete) operations in SQL.

```python
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
```

## Key Python `sqlite3` Components Explained

While SQL is the language for talking to the database, Python's `sqlite3` library provides the tools to send those commands and handle the results. Here are the key components from the script:

### Why use `sqlite3`?

*   **It's Built-In**: `sqlite3` is part of Python's standard library, so you don't need to install anything to use it.
*   **It's Serverless**: Unlike other databases (like PostgreSQL or MySQL), SQLite doesn't require a separate server process. It reads and writes directly to a single file on your computer (`mydatabase.db` in our case), making it incredibly simple and portable for smaller projects.

### The Connection and Cursor

*   `conn = sqlite3.connect(...)`: This function establishes a connection to your database file. If the file doesn't exist, it is created automatically. The `conn` object represents your live connection to the database.
*   `cursor = conn.cursor()`: You don't execute commands directly on the connection. Instead, you create a `cursor` object. Think of the cursor as your personal remote control for the database—it lets you execute commands and fetch results, one operation at a time.

### `execute()` vs. `executemany()`

*   `cursor.execute('...')`: This is the most common method. You use it to execute a **single** SQL command. In our script, we use it to `CREATE` the table, `UPDATE` a record, and `DELETE` a record.

*   `cursor.executemany('...', data)`: This is a powerful and efficient method for running the **same** SQL command multiple times with different data. We used it to `INSERT` all three users at once. It takes a template query (with `?` placeholders) and a list of tuples, where each tuple contains the data for one execution. This is much faster than running `execute()` in a loop.

### `commit()` and `close()`

*   `conn.commit()`: When you perform an action that changes the database (like `INSERT`, `UPDATE`, or `DELETE`), the changes are staged but not yet saved to the file. `conn.commit()` is the crucial step that writes all pending changes to the database, making them permanent. If you forget to commit, your changes will be lost when the script ends.
*   `conn.close()`: This cleanly terminates the connection to the database. It's important to close the connection when you are finished to release the file and free up resources.

## Core SQL Commands Explained

*   **`CREATE TABLE`**: Creates a new table (like a spreadsheet) with defined columns.
*   **`INSERT INTO`**: Adds a new row of data to a table.
*   **`SELECT`**: Retrieves data from a table. `SELECT *` gets all columns, and `WHERE` filters which rows to show.
*   **`UPDATE`**: Edits data that already exists in a table. `WHERE` is crucial to specify which row to change.
*   **`DELETE FROM`**: Removes a row from a table. `WHERE` is essential to ensure you delete the correct data.

## Step-by-Step: SQL Queries and Their Results

This section walks through each SQL command from the Python script and shows the exact output it produces. This makes it easy to see the direct impact of each query.

| Action | SQL Query | Script Output |
| :--- | :--- | :--- |
| **1. Create Table** | `CREATE TABLE IF NOT EXISTS users (...)` | `Table 'users' created successfully.` |
| **2. Insert Users** | `INSERT OR IGNORE INTO users (...) VALUES (?,?,?)` | `3 users added successfully.` |
| **3. View All Users** | `SELECT * FROM users` | `(1, 'Alice', 'alice@example.com')`<br>`(2, 'Bob', 'bob@example.com')`<br>`(3, 'Charlie', 'charlie@example.com')` |
| **4. Update a User** | `UPDATE users SET email = ? WHERE name = ?` | `Bob's email has been updated.` |
| **5. View One User** | `SELECT * FROM users WHERE name = 'Bob'` | `(2, 'Bob', 'bob_new@example.com')` |
| **6. Delete a User** | `DELETE FROM users WHERE name = 'Charlie'` | `1 user(s) deleted.` |
| **7. View Final Table**| `SELECT * FROM users` | `(1, 'Alice', 'alice@example.com')`<br>`(2, 'Bob', 'bob_new@example.com')` |

## Working with the `mydatabase.db` File

Our Python script creates and interacts with a file named `mydatabase.db`. But what is this file, and how can you look inside it?

### What is `mydatabase.db`?

This file **is** your database. It's a binary file where SQLite stores all of your tables, data, and indexes in an organized format. You cannot open it with a normal text editor and expect to see plain text.

### How to View and Edit the Database

To see what's inside `mydatabase.db`, you need a special program called a **database browser** or **SQLite client**. These tools give you a user-friendly, spreadsheet-like interface to view, edit, and query your data.

A highly recommended, free, and open-source tool is **[DB Browser for SQLite](https://sqlitebrowser.org/)**.

### Using a Database Browser (Example with DB Browser for SQLite)

1.  **Download and Install**: First, you would download and install [DB Browser for SQLite](https://sqlitebrowser.org/) from their website.
2.  **Open Database**: Run the program and click "Open Database". Navigate to your project folder and select the `mydatabase.db` file.
3.  **Browse Data**: Once opened, you will see a tab called "Browse Data". Select the `users` table from the dropdown menu. You will see all your data (Alice and Bob) laid out in a clean, table format.
4.  **Execute SQL**: There is also a tab called "Execute SQL". Here, you can type and run any SQL query you want (e.g., `SELECT * FROM users;`) and see the results immediately. This is a great way to experiment with SQL commands without having to modify and run your Python script every time.

Using a tool like this is the standard way to inspect and manage SQLite databases during development.

## Script Output

When you run the Python script, this is the output you will see:

```
Table 'users' created successfully.
3 users added successfully.

--- All users in the table ---
(1, 'Alice', 'alice@example.com')
(2, 'Bob', 'bob@example.com')
(3, 'Charlie', 'charlie@example.com')

--- Updating Bob's email ---
Bob's email has been updated.
(2, 'Bob', 'bob_new@example.com')

--- Deleting Charlie from the table ---
1 user(s) deleted.

--- Final state of the table ---
(1, 'Alice', 'alice@example.com')
(2, 'Bob', 'bob_new@example.com')
```
