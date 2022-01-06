
import pymysql

conn = pymysql.connect(host="localhost", user="root",password="12222",database="day",charset="utf8")

cursor = conn.cursor()

sql = """
CREATE TABLE test7 (
    time  datetime,            
    func VARCHAR(255),
    level int,
    message VARCHAR(255),
    plateform VARCHAR(255),
    uid VARCHAR(255),
    host VARCHAR(255),
    uri VARCHAR(255)
)ENGINE=innodb DEFAULT CHARSET=utf8;
"""

cursor.execute(sql)

cursor.close()

conn.close()
