import MySQLdb
db1 = MySQLdb.connect(host="localhost",user="root",passwd="tharayil",db="result")
cursor = db1.cursor()
sql = 'create table sub_codes(code1 varchar(20),code2 varchar(20),code3 varchar(20),code4 varchar(20),code5 varchar(20),code6 varchar(20),code7 varchar(20),code8 varchar(20),sem varchar(20))'
cursor.execute(sql)





