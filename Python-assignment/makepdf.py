#!usr/bin/python3
import PyPDF2
import fpdf
from fpdf import FPDF
print "Successfull"
import psycopg2
conn = psycopg2.connect(database="data", user = "postgres", password = "postgres", host = "localhost", port = "5432")
print "Opened database successfully"
cursor = conn.cursor()
print "Cursor connected successfully"
query = "SELECT * FROM user_data"
cursor.execute(query)
output = cursor.fetchall()
conn.close()
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
for row in output:
  pdf.cell(0, 10, str(row[0:]), 0, 1)
pdf.output('tuto1.pdf')
print "File created successfully"
