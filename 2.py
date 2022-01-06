
import csv
L = csv.reader(open('access_20211229.csv'))
import pymysql

db = pymysql.connect(host="localhost", user="root",password="12211",database="day",charset="utf8")


cursor = db.cursor()
#user_id,item_id,behavior_type,user_geohash,item_category,time
sql_createTb = """CREATE TABLE test6 (
    time  datetime,            
    func VARCHAR(255),
    level int,
    message VARCHAR(255),
    plateform VARCHAR(255),
    uid VARCHAR(255),
    host VARCHAR(255),
    uri VARCHAR(255))
                 """

#cursor.execute(sql_createTb) 
for item in L:
    cursor.execute("insert into test6(time,func,level ,message, plateform, uid, host, uri) values(%s,%s,%s,%s,%s,%s,%s,%s)",tuple(item))


cursor.execute("select count(*) from test6;")
record = cursor.fetchone()

print ("select * from test6 is: ", record[0])

db.commit()

cursor.close()

db.close()


