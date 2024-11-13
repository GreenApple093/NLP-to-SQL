from dotenv import load_dotenv

load_dotenv()  ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response


def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text


## Fucntion To retrieve query from the database


def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


## Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    Example:
Question: Show me all students in section A.
SQL Query: SELECT * FROM STUDENT WHERE SECTION = 'A';

Example:
Question: List the names of students in class 10.
SQL Query: SELECT NAME FROM STUDENT WHERE CLASS = '10';

Example:
Question: How many students are there in class 12, section B?
SQL Query: SELECT COUNT(*) FROM STUDENT WHERE CLASS = '12' AND SECTION = 'B';

Example:
Question: Retrieve the details of students in class "Mathematics" from section C.
SQL Query: SELECT * FROM STUDENT WHERE CLASS = 'Mathematics' AND SECTION = 'C';

Example:
Question: List all unique classes in the database.
SQL Query: SELECT DISTINCT CLASS FROM STUDENT;

Example:
Question: Get the total number of students across all sections.
SQL Query: SELECT COUNT(*) FROM STUDENT;

Example:
Question: Show me the names of all students in section D who are in class 9.
SQL Query: SELECT NAME FROM STUDENT WHERE CLASS = '9' AND SECTION = 'D';

Example:
Question: Find all records where the student is in section B.
SQL Query: SELECT * FROM STUDENT WHERE SECTION = 'B';

Example:
Question: Give me a count of students in each class.
SQL Query: SELECT CLASS, COUNT(*) FROM STUDENT GROUP BY CLASS;

Example:
Question: Find the total number of students in each section of class 11.
SQL Query: SELECT SECTION, COUNT(*) FROM STUDENT WHERE CLASS = '11' GROUP BY SECTION;

Example:
Question: Retrieve names of students who are not in section A.
SQL Query: SELECT NAME FROM STUDENT WHERE SECTION != 'A';

Example:
Question: Get all students studying in classes other than "Computer Science."
SQL Query: SELECT * FROM STUDENT WHERE CLASS != 'Computer Science';
    also the sql code should not have ``` in beginning or end and sql word in output

Example:
Question: Which students have marks above 80 in Data Science?
SQL Query: SELECT NAME FROM STUDENT WHERE CLASS = 'Data Science' AND MARKS > 80;

Example:
Question: Show all students along with the names of their teachers.
SQL Query: SELECT STUDENT.NAME, TEACHER.NAME AS TEACHER_NAME FROM STUDENT INNER JOIN TEACHER ON STUDENT.TEACHER_ID = TEACHER.ID;

Example:
Question: Retrieve the names and marks of students in section B along with their teacher's name.
SQL Query: SELECT STUDENT.NAME, STUDENT.MARKS, TEACHER.NAME AS TEACHER_NAME FROM STUDENT INNER JOIN TEACHER ON STUDENT.TEACHER_ID = TEACHER.ID WHERE STUDENT.SECTION = 'B';

Example:
Question: Count the number of students each teacher is responsible for.
SQL Query: SELECT TEACHER.NAME, COUNT(STUDENT.ID) AS STUDENT_COUNT FROM STUDENT INNER JOIN TEACHER ON STUDENT.TEACHER_ID = TEACHER.ID GROUP BY TEACHER.NAME;

Example:
Question: List all teachers who teach the Data Science class.
SQL Query: SELECT NAME FROM TEACHER WHERE CLASS = 'Data Science';

Example:
Question: Find the average marks of students taught by Ms. Johnson.
SQL Query: SELECT AVG(STUDENT.MARKS) FROM STUDENT INNER JOIN TEACHER ON STUDENT.TEACHER_ID = TEACHER.ID WHERE TEACHER.NAME = 'Ms. Johnson';

Example:
Question: Show all students who scored less than 70, along with their teacher’s name.
SQL Query: SELECT STUDENT.NAME, TEACHER.NAME AS TEACHER_NAME FROM STUDENT INNER JOIN TEACHER ON STUDENT.TEACHER_ID = TEACHER.ID WHERE STUDENT.MARKS < 70;

Example:
Question: Retrieve the names and classes of teachers who have students in section C.
SQL Query: SELECT DISTINCT TEACHER.NAME, TEACHER.CLASS FROM TEACHER INNER JOIN STUDENT ON TEACHER.ID = STUDENT.TEACHER_ID WHERE STUDENT.SECTION = 'C';

Example:
Question: List all classes with the number of students in each section.
SQL Query: SELECT CLASS, SECTION, COUNT(*) AS STUDENT_COUNT FROM STUDENT GROUP BY CLASS, SECTION;

Example:
Question: Get the names of students who are in the same class as Krish.
SQL Query: SELECT NAME FROM STUDENT WHERE CLASS = (SELECT CLASS FROM STUDENT WHERE NAME = 'Krish') AND NAME != 'Krish';

Example:
Question: Find the total marks of students for each teacher.
SQL Query: SELECT TEACHER.NAME, SUM(STUDENT.MARKS) AS TOTAL_MARKS FROM STUDENT INNER JOIN TEACHER ON STUDENT.TEACHER_ID = TEACHER.ID GROUP BY TEACHER.NAME;

Example:
Question: Show the highest mark in each class and the name of the student who scored it.
SQL Query: SELECT CLASS, NAME, MAX(MARKS) AS HIGHEST_MARK FROM STUDENT GROUP BY CLASS;

Example:
Question: List the teachers who have at least one student scoring above 85.
SQL Query: SELECT DISTINCT TEACHER.NAME FROM TEACHER INNER JOIN STUDENT ON TEACHER.ID = STUDENT.TEACHER_ID WHERE STUDENT.MARKS > 85;

Example:
Question: Retrieve students who have the same teacher as Sudhanshu.
SQL Query: SELECT STUDENT.NAME FROM STUDENT WHERE TEACHER_ID = (SELECT TEACHER_ID FROM STUDENT WHERE NAME = 'Sudhanshu') AND NAME != 'Sudhanshu';

Example:
Question: Find the names of teachers who are teaching more than one class.
SQL Query: SELECT NAME FROM TEACHER GROUP BY NAME HAVING COUNT(DISTINCT CLASS) > 1;
    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("App to Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, "test.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)
