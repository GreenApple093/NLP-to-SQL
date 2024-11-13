# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect("test.db")

# Enabling foreign key support for SQLite
conn.execute("PRAGMA foreign_keys = ON")

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Dropping tables if they already exist to ensure fresh setup
cursor.execute("DROP TABLE IF EXISTS STUDENT")
cursor.execute("DROP TABLE IF EXISTS TEACHER")

# Creating TEACHER table with primary key
teacher_table = """CREATE TABLE TEACHER(
                   ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                   NAME VARCHAR(255), 
                   CLASS VARCHAR(255), 
                   SUBJECT VARCHAR(255)
               );"""
cursor.execute(teacher_table)

# Creating STUDENT table with a foreign key referencing TEACHER
student_table = """CREATE TABLE STUDENT(
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   NAME VARCHAR(255), 
                   CLASS VARCHAR(255), 
                   SECTION VARCHAR(255), 
                   MARKS INT,
                   TEACHER_ID INT,
                   FOREIGN KEY (TEACHER_ID) REFERENCES TEACHER(ID)
               );"""
cursor.execute(student_table)

# Inserting records into TEACHER table
cursor.execute("""INSERT INTO TEACHER (NAME, CLASS, SUBJECT) VALUES ('Mr. Smith', 'Data Science', 'Machine Learning')""")
cursor.execute("""INSERT INTO TEACHER (NAME, CLASS, SUBJECT) VALUES ('Ms. Johnson', 'Devops', 'Cloud Computing')""")
cursor.execute("""INSERT INTO TEACHER (NAME, CLASS, SUBJECT) VALUES ('Dr. Brown', 'Data Science', 'Statistics')""")

# Inserting records into STUDENT table, associating students with a teacher by TEACHER_ID
cursor.execute("""INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, TEACHER_ID) VALUES ('Krish', 'Data Science', 'A', 89, 1)""")
cursor.execute("""INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, TEACHER_ID) VALUES ('Darius', 'Data Science', 'B', 76, 1)""")
cursor.execute("""INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, TEACHER_ID) VALUES ('Sudhanshu', 'Devops', 'C', 90, 2)""")
cursor.execute("""INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, TEACHER_ID) VALUES ('Vikash', 'Data Science', 'C', 68, 3)""")

# Display data inserted into TEACHER table
print("Data in the TEACHER table:")
data = cursor.execute("""SELECT * FROM TEACHER""")
for row in data:
    print(row)

# Display data inserted into STUDENT table
print("\nData in the STUDENT table:")
data = cursor.execute("""SELECT * FROM STUDENT""")
for row in data:
    print(row)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
