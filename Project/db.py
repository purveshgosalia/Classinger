import cx_Oracle

con=None
try:
	con=cx_Oracle.connect("system/123abc")
	cursor=con.cursor()
	sql="insert into student values('%d','%s')"
	rno=int(input("enter the roll :"))
	name=input("enter name")
	args=(rno,name)
	cursor.execute(sql%args)
	con.commit()
	print("record saved")
except cx_Oracle.DatabaseError as e:
	print("issue",e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print("disconnected")