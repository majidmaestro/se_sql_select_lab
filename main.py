# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")

# Display all employees
employee_data = pd.read_sql(
    "SELECT * FROM employees",
    conn
)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")

# STEP 2
# Select employee number and last name
df_first_five = pd.read_sql(
    """
    SELECT employeeNumber, lastName
    FROM employees;
    """,
    conn
)
print("\nSTEP 2: Employee Number and Last Name")
print(df_first_five)

# STEP 3
# Select last name first, then employee number
df_five_reverse = pd.read_sql(
    """
    SELECT lastName, employeeNumber
    FROM employees;
    """,
    conn
)
print("\nSTEP 3: Reversed Column Order")
print(df_five_reverse)

# STEP 4
# Rename employeeNumber to ID
df_alias = pd.read_sql(
    """
    SELECT employeeNumber AS ID, lastName
    FROM employees;
    """,
    conn
)
print("\nSTEP 4: Employee ID and Last Name")
print(df_alias)

# STEP 5
# Categorize employees using CASE
df_executive = pd.read_sql(
    """
    SELECT
        employeeNumber,
        lastName,
        jobTitle,
        CASE
            WHEN jobTitle = 'President'
              OR jobTitle = 'VP Sales'
              OR jobTitle = 'VP Marketing'
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees;
    """,
    conn
)
print("\nSTEP 5: Employee Roles")
print(df_executive)

# STEP 6
# Find the length of each employee's last name
df_name_length = pd.read_sql(
    """
    SELECT LENGTH(lastName) AS name_length
    FROM employees;
    """,
    conn
)
print("\nSTEP 6: Last Name Length")
print(df_name_length)

# STEP 7
# Extract the first two letters of each job title
df_short_title = pd.read_sql(
    """
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees;
    """,
    conn
)
print("\nSTEP 7: Short Job Titles")
print(df_short_title)

# STEP 8
# Calculate the total order amount
sum_total_price = pd.read_sql(
    """
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderDetails;
    """,
    conn
).sum().reset_index(drop=True)
print("\nSTEP 8: Total Order Amount")
print(sum_total_price)

# STEP 9
# Extract day, month, and year from order dates
df_day_month_year = pd.read_sql(
    """
    SELECT
        orderDate,
        STRFTIME('%d', orderDate) AS day,
        STRFTIME('%m', orderDate) AS month,
        STRFTIME('%Y', orderDate) AS year
    FROM orders;
    """,
    conn
)
print("\nSTEP 9: Order Dates")
print(df_day_month_year)

# Close the database connection
conn.close()