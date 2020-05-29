import pymysql.cursors  
import connection


conn = connection.get_connection()
sql =  "SELECT * FROM tbltest"
try:
  cursor = conn.cursor()
  cursor.execute(sql)
  for row in cursor:
   print(row["name"])
finally:
 conn.close()

             
