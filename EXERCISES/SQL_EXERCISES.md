# SQL Exercises

Below are some simple exercises to test your understanding of basic SQL queries.

We will use a sample table named `Students` for these exercises.

**Students Table:**

| StudentID | FirstName | LastName | Age | Major |
|-----------|-----------|----------|-----|-------|
| 1         | John      | Smith    | 20  | Computer Science |
| 2         | Jane      | Doe      | 22  | Mathematics |
| 3         | Peter     | Jones    | 21  | Physics |
| 4         | Mary      | Johnson  | 20  | Computer Science |
| 5         | David     | Williams | 23  | Chemistry |

---

## Exercises

1.  **Select all students:** Write a query to retrieve all records from the `Students` table.
2.  **Select students by major:** Write a query to retrieve all students who are majoring in 'Computer Science'.
3.  **Select students by age:** Write a query to retrieve all students who are older than 21.
4.  **Select specific columns:** Write a query to retrieve only the `FirstName` and `LastName` of all students.
5.  **Select and order students:** Write a query to retrieve all students, ordered by `Age` in descending order.

---

## Solutions

Here are the solutions to the exercises above.

### 1. Select all students

This query selects all columns and all rows from the `Students` table.

```sql
SELECT * FROM Students;
```

**Explanation:**
*   `SELECT *` means select all columns.
*   `FROM Students` specifies the table to retrieve the data from.

### 2. Select students by major

This query retrieves all students whose `Major` is 'Computer Science'.

```sql
SELECT * FROM Students WHERE Major = 'Computer Science';
```

**Explanation:**
*   `WHERE Major = 'Computer Science'` is a condition that filters the rows, only returning those where the `Major` column has the value 'Computer Science'.

### 3. Select students by age

This query retrieves all students who are older than 21.

```sql
SELECT * FROM Students WHERE Age > 21;
```

**Explanation:**
*   `WHERE Age > 21` filters the records to include only students whose age is greater than 21.

### 4. Select specific columns

This query retrieves only the `FirstName` and `LastName` for all students.

```sql
SELECT FirstName, LastName FROM Students;
```

**Explanation:**
*   `SELECT FirstName, LastName` specifies that only these two columns should be returned in the result set.

### 5. Select and order students

This query retrieves all students and orders them by their age, from oldest to youngest.

```sql
SELECT * FROM Students ORDER BY Age DESC;
```

**Explanation:**
*   `ORDER BY Age` sorts the results based on the `Age` column.
*   `DESC` specifies that the sort order should be descending. The default is ascending (`ASC`).

---

## Running the Exercises with Python

To test these SQL queries, you can use the provided Python script. This script will create a `students.db` file in the same directory, set up the `Students` table, and run all the exercise queries.

**Instructions:**

1.  Navigate to the `EXERCISES` directory in your terminal.
2.  Run the script using the following command:

    ```bash
    python run_exercises.py
    ```

The script will print the results of each query to the console. You can also inspect the `students.db` file with a database tool to see the data directly.

