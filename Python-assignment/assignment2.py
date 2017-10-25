html = """
<table border="0" width="100%">
  <thead>
    <tr>
      <th width="20%">Id</th>
      <th width="20%">First Name</th>
      <th width="20%">Last Name</th>
      <th width="20%">Gender</th>
      <th width="20%">Age</th>
    </tr>
  </thead>
  <tbody>

"""
import PyPDF2
import fpdf
from fpdf import FPDF, HTMLMixin
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
    html+="""
    <tr>
      <td width="20%" align="center">{0}</td>
      <td width="20%" align="center">{1}</td>
      <td width="20%" align="center">{2}</td>
      <td width="20%" align="center">{3}</td>
      <td width="20%" align="center">{4}</td>
      </tr>
    """.format(ID, fname, lname, gender, age)
html+="""
</tbody>
</table>
"""
conn.close()
class FPDF(FPDF, HTMLMixin):
    pass
pdf = FPDF()
pdf.add_page()
pdf.write_html(html)
pdf.output('html.pdf','F')
print "OK"