import sqlite3

# connect to sqllite3 database

connection = sqlite3.connect('student.db')

# create cursor object to insert record, create table, retrieve record, delete record, update record

cursor = connection.cursor()

# create table

table_info = """
CREATE TABLE student(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

# insert some records

cursor.execute("INSERT INTO student VALUES('suhas', 'Data Science', 'A', 90)")
cursor.execute("INSERT INTO student VALUES('ajay', 'AI/ML', 'B', 80)")
cursor.execute("INSERT INTO student VALUES('omar', 'Data Science', 'C', 70)")
cursor.execute("INSERT INTO student VALUES('Doe', 'Economics', 'D', 60)")
cursor.execute("INSERT INTO student VALUES('John', 'Agriculture', 'E', 50)")


print('The inserted records are')

data = cursor.execute('select * from student')

for row in data:
    print(row)

# close connection

connection.commit()
connection.close()    

