import sqlite3

#Connect to sqlite
connection=sqlite3.connect("student.db")

#Create a cursor object to insert record,create table,retrieve
cursor=connection.cursor()

table_info=""" 
   CREATE TABLE STUDENT (NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT)
   """

cursor.execute(table_info)

###Insert records
cursor.execute(''' INSERT INTO STUDENT VALUES ('SANLAP','DATA SCIENCE','A','90')''')
cursor.execute(''' INSERT INTO STUDENT VALUES ('SOUMI','DATA SCIENCE','A','90')''')
cursor.execute(''' INSERT INTO STUDENT VALUES ('AMRIT','DATA SCIENCE','A','90')''')
cursor.execute(''' INSERT INTO STUDENT VALUES ('ROHIT','DATA SCIENCE','A','90')''')
cursor.execute(''' INSERT INTO STUDENT VALUES ('BIPUL','DATA SCIENCE','A','90')''')
cursor.execute(''' INSERT INTO STUDENT VALUES ('KAIF','DATA SCIENCE','A','90')''')
cursor.execute(''' INSERT INTO STUDENT VALUES ('DEENA','DATA SCIENCE','A','90')''')
cursor.execute(''' INSERT INTO STUDENT VALUES ('NATASHA','DATA SCIENCE','A','90')''')
cursor.execute(''' INSERT INTO STUDENT VALUES ('SAMSAD','DATA SCIENCE','A','90')''')
cursor.execute(''' INSERT INTO STUDENT VALUES ('SOURAV','DATA SCIENCE','A','90')''')
cursor.execute(''' INSERT INTO STUDENT VALUES ('AYAN','DATA SCIENCE','A','90')''')

#Display the records 
print("The inserted records are")

data=cursor.execute(''' SELECT * FROM STUDENT ''')

for row in data:
    print(row)

#Close the connection
connection.commit()
connection.close()