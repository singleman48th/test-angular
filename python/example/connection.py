import pymysql.cursors  
# Kết nối vào database.
def get_connection():
   return  pymysql.connect(host='192.168.100.127',
                             user='admin',
                             password='Ominext2020!@#',                             
                             db='gp_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)                        
 