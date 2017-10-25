#!usr/bin/python3
import PyPDF2
print "Successfull"
import psycopg2
conn = psycopg2.connect(database="data", user = "postgres", password = "postgres", host = "localhost", port = "5432")
print "Opened database successfully"
cursor = conn.cursor()
print "Cursor connected successfully"
query = "SELECT * FROM user_data"
cursor.execute(query)
output = cursor.fetchall()
for row in output:
    ID = row[0]
    fname = row[1]
    lname = row[2]
    gender = row[3]
    age = row[4]
    print "ID=%d,fname=%s,lname=%s,gender=%s,age=%d" % \
             (ID, fname, lname, gender, age )
conn.close()