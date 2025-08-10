import sqlite3
import os

# Define the database file path
DB_FILE = "students.db"

def setup_database():
    """Create and populate the database if it doesn't exist."""
    # Check if the database file already exists
    db_exists = os.path.exists(DB_FILE)
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    if not db_exists:
        print(f"Creating new database: {DB_FILE}")
        # Create the Students table
        cursor.execute('''
        CREATE TABLE Students (
            StudentID INTEGER PRIMARY KEY,
            FirstName TEXT,
            LastName TEXT,
            Age INTEGER,
            Major TEXT
        )
        ''')

        # Insert sample data into the table
        students_data = [
            (1, 'John', 'Smith', 20, 'Computer Science'),
            (2, 'Jane', 'Doe', 22, 'Mathematics'),
            (3, 'Peter', 'Jones', 21, 'Physics'),
            (4, 'Mary', 'Johnson', 20, 'Computer Science'),
            (5, 'David', 'Williams', 23, 'Chemistry')
        ]
        cursor.executemany('INSERT INTO Students VALUES (?,?,?,?,?)', students_data)
        conn.commit()
        print("Database created and populated successfully.")
    else:
        print(f"Database '{DB_FILE}' already exists.")

    return conn, cursor

def execute_and_print(description, query, cursor):
    """Execute a query and print the results."""
    print(f"\n--- {description} ---")
    print(f"Query: {query}")
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No results found.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to run the SQL exercises."""
    conn, cursor = setup_database()

    # --- Run Exercises ---
    queries = [
        ("Exercise 1: Select all students", "SELECT * FROM Students;"),
        ("Exercise 2: Select students by major ('Computer Science')", "SELECT * FROM Students WHERE Major = 'Computer Science';"),
        ("Exercise 3: Select students older than 21", "SELECT * FROM Students WHERE Age > 21;"),
        ("Exercise 4: Select only FirstName and LastName", "SELECT FirstName, LastName FROM Students;"),
        ("Exercise 5: Select all students, ordered by Age (descending)", "SELECT * FROM Students ORDER BY Age DESC;")
    ]

    for desc, sql in queries:
        execute_and_print(desc, sql, cursor)

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()
