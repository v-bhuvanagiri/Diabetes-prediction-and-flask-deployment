import pymysql as pms

conn = pms.connect(host="localhost", 
                   port=3306,
                   user="root",
                   password="root",
                   db="login")
print(conn)

cursor = conn.cursor()

def getcredentials():
    username = []
    password = []
    cursor.execute("SELECT * FROM details")
    result = cursor.fetchall()
    print(result)
    for i in result:
        username.append(i[0])
        password.append(i[1])
        
    return username,password    

