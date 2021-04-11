import tkinter as tk
from tkinter import *
import re
from tkinter import messagebox
from tkinter import scrolledtext
from cx_Oracle import *
import bs4
import requests
import socket
import matplotlib.pyplot as plt
def only_name(e):
	if e.isalpha():
		return TRUE
	elif e=="":
		return TRUE
	else:
		msg = "Enter Character only"
		messagebox.showerror("Error",msg)
		entAddName.focus(),entUpdateName.focus()
		return FALSE
def only_rno(e):
	if e.isdigit():
		return TRUE
	elif e=="":
		return TRUE
	else:
		msg = "Enter Integers only"
		messagebox.showerror("Error",msg)
		entAddRno.focus(),entUpdateRno.focus(),entDeleteRno.focus()
		return FALSE		
def only_marks(e):
	if e.isdigit():
		return TRUE
	elif e=="":
		return TRUE
	else:
		msg = "Enter Integers between 0 to 100 only"
		messagebox.showerror("Error",msg)
		entAddMarks.focus(),entUpdateMarks.focus()
		return FALSE
def f1():            
	root.withdraw()
	adst.deiconify()
def f2():
	entAddRno.delete(0,END)
	entAddName.delete(0,END)
	entAddMarks.delete(0,END)        
	adst.withdraw()
	root.deiconify()
def f3():			
	stview.delete(1.0,END)
	root.withdraw()
	vist.deiconify()
	con = None
	try:
		con = connect("system/abc123")
		cursor = con.cursor()
		sql = "select * from student order by rno"
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = ""
		for d in data:
			msg = msg + "Rno=" + str(d[0]) + "  Name= " + str(d[1]) + "  Marks=" + str(d[2]) + "\n"
		stview.insert(INSERT, msg)
	except DatabaseError as e:
		messagebox.showerror("Error", e)
	finally:
		if con is not None:
			con.close()

def f4():			
	vist.withdraw()
	root.deiconify()
def f5():			
	
	root.withdraw()	
	upst.deiconify()
def f6():			
	upst.withdraw() 
	root.deiconify()
def f7():			
	root.withdraw()
	dest.deiconify()				
def f8():			
	dest.withdraw()
	root.deiconify()
def f9():	
	con = None
	try:
		con = connect("system/abc123")
		try:
			rno = int(entAddRno.get())
			name = entAddName.get()
			marks =int(entAddMarks.get())
		except ValueError:
			e = "Please Enter Input"
			return messagebox.showerror("ERROR",e)
		try:
			if marks >101:
				e = "Enter marks between 1 to 100"
				return messagebox.showerror("Error",e)
		finally:
			entAddMarks.delete(0,END)
		cursor = con.cursor()
		sql = "insert into student values('%d','%s','%d')"
		args = (rno,name,marks)
		cursor.execute(sql % args)
		con.commit()
		msg = str(cursor.rowcount) + " records inserted"
		messagebox.showinfo("Inserted",msg)
		entAddRno.delete(0,END)
		entAddName.delete(0,END)
		entAddMarks.delete(0,END)
		entAddRno.focus()
	except DatabaseError as e:
		con.rollback()
		print("Issue",e)
	finally:
		if con is not None:
			con.close()
def f10():	
	con = None
	try:
		con = connect("system/abc123")
		try:
			rno = int(entUpdateRno.get())
			name = entUpdateName.get()
			marks =int(entUpdateMarks.get())
		except ValueError:
			e = "Please Enter Input"
			return messagebox.showerror("ERROR",e)
		try:
			if marks >=100:
				e = "Enter marks between 1 to 100"
				return messagebox.showerror("Error",e)
		finally:
			entAddMarks.delete(0,END)
		cursor = con.cursor()
		sql = "update student set name='%s',marks= '%d'  where rno = '%d'"
		args = (name,marks,rno)
		cursor.execute(sql % args)
		con.commit()
		msg = str(cursor.rowcount) + "  records updated"
		messagebox.showinfo("Updated",msg)
		entUpdateRno.delete(0,END)
		entUpdateName.delete(0,END)
		entUpdateMarks.delete(0,END)
		entUpdateRno.focus()
	except DatabaseError as e:
		con.rollback()
		print("issue ", e)
	finally:
		if con is not None:
			con.close()
def f11(): 
	con = None
	try:
		con = connect("system/abc123")
		try:
			rno = int(entDeleteRno.get())
		except ValueError:
			e = "Please Enter Input"
			return messagebox.showerror("ERROR",e)
		cursor = con.cursor()
		sql = "delete from student where rno ='%d'"
		args = (rno)
		cursor.execute(sql % args)
		con.commit()
		msg = str(cursor.rowcount) + " record deleted"
		messagebox.showinfo("Deleted",msg)
		entDeleteRno.delete(0,END)
		entDeleteRno.focus()
	except DatabaseError as e:
		con.rollback()
		print("issue ", e)
	finally:
		if con is not None:
			con.close()



def f12(): 
	marks = []  
	student = []
	con = None
	try:
		con = connect("system/abc123")
		cursor = con.cursor()
		sql ="select * from (select * from student order by marks desc) where rownum<=5 order by rno" # sql query
		cursor.execute(sql)
		data = cursor.fetchall() 
		for row in data:
			marks.append(row[2])   
			student.append(row[1])
		marks_list = plt.bar(student,marks)   
		marks_list[0].set_color('blue')   
		marks_list[1].set_color('green')
		marks_list[2].set_color('red')
		marks_list[3].set_color('orange')
		marks_list[4].set_color('pink')

		plt.title("Top 5 students")
		plt.xlabel("Students")
		plt.ylabel("Marks")
		plt.show()
	except DatabaseError as e:
		messagebox.showerror("Error", e)
	finally:
		if con is not None:
			con.close()


size = '400x550+600+150'
root = Tk()
root.title('S.M.S')
root.geometry(size)




btnAdd = Button(root,text="Add",width =15,font =('arial',20,'bold'),command = f1)
btnView = Button(root,text="View",width =15,font =('arial',20,'bold'),command = f3)
btnUpdate = Button(root,text="Update",width= 15,font =('arial',20,'bold'),command = f5)
btnDelete = Button(root,text="Delete",width= 15,font =('arial',20,'bold'),command= f7)
btnGraph = Button(root,text="Graph",width= 15,font =('arial',20,'bold'),command = f12)

try:
	socket.create_connection(("www.google.com",80))
	res = requests.get("https://ipinfo.io/")
	data = res.json()
	city = "mumbai"
	a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q="+city
	a3="&appid=c6e315d09197cec231495138183954bd"
	api_address = a1 + a2 + a3
	res1 = requests.get(api_address)
	data = res1.json()
	temperature1 = data['main']['temp']
	res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")

	soup = bs4.BeautifulSoup(res.text,'lxml')

	quote = soup.find('img',{"class":"p-qotd"})

	text = quote['alt']
	
except OSError:
	print('check network')

label = Label(root,font =('arial',10),wraplength = 200,width = 40,height = 10,text='Temperature in {} is {} \n\n {}'.format(city,temperature1,text))


btnAdd.pack(pady=7)
btnView.pack(pady=5)
btnUpdate.pack(pady=5)
btnDelete.pack(pady=5)
btnGraph.pack(pady=5)
label.pack(pady=5)



adst = Toplevel(root)
adst.title("Add Student")
adst.geometry(size)
adst.withdraw()

lblAddRno = Label(adst,text="Enter Roll No ",width= 15,font =('arial',20))

validation_rno= adst.register(only_rno)
entAddRno = Entry(adst,bd=5,width= 15,font=('arial',20),validate="key",validatecommand=(validation_rno,"%P"))

lblAddRno.pack(pady=5)
entAddRno.pack(pady=5)

lblAddName = Label(adst,text="Enter Name ",width= 15,font =('arial',20))

validation_name = adst.register(only_name)
entAddName = Entry(adst,bd=5,width= 15,font=('arial',20),validate="key",validatecommand=(validation_name,"%P"))

lblAddName.pack(pady=5)
entAddName.pack(pady=5)

lblAddMarks = Label(adst,text="Enter Marks ",width= 15,font =('arial',20))

validation_marks = adst.register(only_marks)
entAddMarks = Entry(adst,bd=5,width= 15,font=('arial',20),validate="key",validatecommand=(validation_marks,"%P"))

lblAddMarks.pack(pady=5)
entAddMarks.pack(pady=20)

btnAddSave = Button(adst,text="Save",width= 15,font =('arial',20,'bold'),command = f9)
btnAddBack = Button(adst,text="Back",width= 15,font =('arial',20,'bold'),command = f2)

btnAddSave.pack(pady=5)
btnAddBack.pack(pady=5)

vist = Toplevel(root)
vist.title("View Student")
vist.geometry(size)
vist.withdraw()

stview = scrolledtext.ScrolledText(vist,width=35, height=20)
btnViewBack = Button(vist,text="Back",width= 15,font =('arial',20,'bold'),command = f4)

stview.pack(pady=5)
btnViewBack.pack(pady=5)

upst = Toplevel(root)
upst.title("Update Student")
upst.geometry(size)
upst.withdraw()

validation_urno = upst.register(only_rno)
validation_urname = upst.register(only_name)
validation_umarks = upst.register(only_marks)

lblUpdateRno = Label(upst,text="Enter Roll No ",width= 15,font =('arial',20))
entUpdateRno = Entry(upst,bd=5,width= 15,font=('arial',20),validate="key",validatecommand=(validation_urno,"%P"))

lblUpdateRno.pack(pady=5)
entUpdateRno.pack(pady=5)

lblUpdateName = Label(upst,text="Update Name ",width= 15,font =('arial',20))
entUpdateName = Entry(upst,bd=5,width= 15,font=('arial',20),validate="key",validatecommand=(validation_urname,"%P"))

lblUpdateName.pack(pady=5)
entUpdateName.pack(pady=5)

lblUpdateMarks = Label(upst,text="Update Marks ",width= 15,font =('arial',20))
entUpdateMarks = Entry(upst,bd=5,width= 15,font=('arial',20),validate="key",validatecommand=(validation_umarks,"%P"))

lblUpdateMarks.pack(pady=5)
entUpdateMarks.pack(pady=5)

btnUpdateSave = Button(upst,text="Save",width= 15,font =('arial',20,'bold'),command=f10)
btnUpdateBack = Button(upst,text="Back",width= 15,font =('arial',20,'bold'),command = f6)

btnUpdateSave.pack(pady=5)
btnUpdateBack.pack(pady=5)

dest = Toplevel(root)
dest.title("Delete Student")
dest.geometry(size)
dest.withdraw()

validation_drno = dest.register(only_rno)

lblDeleteRno = Label(dest,text="Enter Roll No ",width= 15,font =('arial',20))
entDeleteRno = Entry(dest,bd=5,width= 15,font=('arial',20),validate="key",validatecommand=(validation_drno,"%P"))

lblDeleteRno.pack(pady=5)
entDeleteRno.pack(pady=30)

btnDeleteBack = Button(dest,text="Back",width= 15,font =('arial',20,'bold'),command = f8)
btnDeleteSave = Button(dest,text="Save",width= 15,font =('arial',20,'bold'),command = f11)

btnDeleteSave.pack(pady=5)
btnDeleteBack.pack(pady=5)

root = mainloop()
