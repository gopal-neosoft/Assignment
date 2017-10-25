#!usr/bin/python3
# -*- coding: utf-8 -*-
import os, sys
import psycopg2
import csv
conn = psycopg2.connect(database="data", user = "postgres", password = "postgres", host = "localhost", port = "5432")
print "Opened database successfully"
cur = conn.cursor()
with open("usr_info.csv", 'r+') as f:
 reader = csv.reader(f, delimiter = ',')
 for row in reader:
     query="INSERT INTO user_data (ID, FirstName, LastName, Gender, Age) VALUES ({0},'{1}','{2}','{3}',{4})".format(row[0],row[1],row[2],row[3],row[4])
     print(query)
     cur.execute(query);
conn.commit()
print "Records created successfully";
conn.close()