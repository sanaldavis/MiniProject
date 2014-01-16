import MySQLdb
db1 = MySQLdb.connect(host="localhost",user="root",passwd="tharayil",db="result")
cursor = db1.cursor()
sql = 'create table TABLES(NAME varchar(20))'
cursor.execute(sql)

