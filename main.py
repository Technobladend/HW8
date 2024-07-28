import sqlite3 as sql

with sql.connect('person.db') as connection:

    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departments (
        DepartmentID INTEGER PRIMARY KEY,
        DepartmentName TEXT NOT NULL)''')


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        EmployeeID INTEGER PRIMARY KEY,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL,
        DepartmentID INTEGER,
        FOREIGN KEY (DepartmentID) REFERENCES Departments (DepartmentID))''')

    cursor.execute('''INSERT INTO Departments (DepartmentID, DepartmentName) 
        VALUES
        (101, 'HR'),
        (102, 'IT'),
        (103, 'Sales')
        ''')

    cursor.execute('''INSERT INTO Employees (FirstName, LastName, DepartmentID) 
        VALUES
        ('Иван', 'Иванов', 101),
        ('Петр', 'Петров', 101),
        ('Алексей', 'Алексеев', 102),
        ('Ольга', 'Ольгова', 102),
        ('Сергей', 'Сергеев', 103),
        ('Мария', 'Мариева', 103)
        ''')


    cursor.execute('''SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName
        FROM Employees
        JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
        ''')


    cursor.execute('''SELECT * FROM Departments''')

for row in cursor.fetchall():
    print(row)


    cursor.execute('''SELECT * FROM Employees''')
for row in cursor.fetchall():
    print(row)

