from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import*
import matplotlib.pyplot as plt
import pandas as pd
import requests
import bs4
from sqlalchemy import *
	
def f1():
	add_window.deiconify()
	main_window.withdraw()
def f2():
	main_window.deiconify()
	add_window.withdraw()
	aw_ent_rno.delete(0, END)
	aw_ent_name.delete(0, END)
	aw_ent_marks.delete(0, END)
	return

def f3():
	con=None
	try:
		con=connect("sms.db")
		cursor=con.cursor()
		sql="insert into student values('%d', '%s', '%d')"
		try:	
			rno = int(aw_ent_rno.get())
			rno != 0
		except ValueError:
			showerror("Rno Issue","Invalid Rno") 
			showerror("Rno Issue","Rno should not be empty")
			aw_ent_rno.delete(0, END)
			aw_ent_rno.focus()
			return	
		else:
			if (int(rno) == 0) or (int(rno) < 0):
				showerror("Rno Issue","Rno should be positive and non-zero ")
				aw_ent_rno.delete(0, END)
				aw_ent_rno.focus()
				return
			
		name = aw_ent_name.get()	
		len(name) != 0
		if len(name) == 0:
			showerror("Name Issue", "Name is empty")
			aw_ent_name.delete(0, END)
			aw_ent_name.focus()
			return

	#Min Name Limit:

		if len(name) < 2:
			showerror("Name Issue","Enter a Name of more than 1 character ")
			aw_ent_name.delete(0, END)
			aw_ent_name.focus()
			return	
			
		if not name.isalpha() :
			showerror("Name Issue", "Invalid Name. Avoid Special Characters")
			aw_ent_name.delete(0, END)
			aw_ent_name.focus()
			return
		
	# Max Name Limit:
	
		len(name) == 15
		if len(name) > 15:
			showerror("Warning !","Name limit exceeding ")
			aw_ent_name.delete(0, END)
			aw_ent_name.focus()
			return
	
		try:
			marks = int(aw_ent_marks.get())
		except ValueError:
			showerror("Marks Issue","Invalid Marks")
			showerror("Marks Issue","Enter Some Marks")
			aw_ent_marks.delete(0, END)
			aw_ent_marks.focus()
			return
	
		else:
			if (int(marks) == 0) or (int(marks) < 0) or (int(marks) > 100):
				showerror("Marks Issue", "Enter Marks between 0-100")
				aw_ent_marks.delete(0, END)
				aw_ent_marks.focus()
				return

		cursor.execute(sql%(rno, name, marks))
		con.commit()
		showinfo("Success ","Record Added ")
		aw_ent_rno.delete(0, END)
		aw_ent_name.delete(0, END)
		aw_ent_marks.delete(0, END)
		aw_ent_rno.focus()
		return
	except Exception:
		con.rollback()
		showerror("Creation Failed", "Record Already Exists !")
		aw_ent_rno.delete(0, END)
		aw_ent_name.delete(0, END)
		aw_ent_marks.delete(0, END)
		aw_ent_rno.focus()
		return
	finally:
		if con is not None:
			con.close()
	
def f4():
	main_window.deiconify()
	view_window.withdraw()

def f5():
	view_window.deiconify()
	main_window.withdraw()
	vw_st_data.delete(1.0, END)
	info=""
	con=None
	try:
		con = connect("sms.db")
		cursor = con.cursor()
		sql = "select*from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			info = info + "rno = " + str(d[0]) + "   name = " + str(d[1]) + "   marks = " + str(d[2]) + "\n"
		vw_st_data.insert(INSERT, info)
	except Exception as e:
		showerror("Issue", str(e))
	finally:
		if con is not None:
			con.close()

def f6():
	main_window.deiconify()
	update_window.withdraw()
	uw_ent_rno.delete(0, END)
	uw_ent_name.delete(0, END)
	uw_ent_marks.delete(0, END)
	return

def f7():
	update_window.deiconify()
	main_window.withdraw()

def f8():
	con = None
	try:
		con = connect("sms.db")
		cursor = con.cursor()
		sql = "update student set name = '%s', marks = '%d' where rno = '%d' "
		try:
			rno = int(uw_ent_rno.get())
			rno != 0
		except ValueError:
			showerror("Rno Issue","Invalid Rno")
			showerror("Rno Issue","Rno should not be empty")
			uw_ent_rno.delete(0, END)
			uw_ent_rno.focus()
			return
		else:
			if (int(rno) == 0) or (int(rno) < 0):
				showerror("Rno Issue", "Rno should be positive and non-empty ")
				uw_ent_rno.delete(0, END)
				uw_ent_rno.focus()
				return
		
		name = uw_ent_name.get()
		len(name) != 0
		if len(name) == 0:
			showerror("Name Empty","Enter a new name ")
			uw_ent_name.delete(0, END)
			uw_ent_name.focus()
			return
		if len(name) < 2:
			showerror("Short Name Issue","Enter a Name of more than 1 character ")
			uw_ent_name.delete(0, END)
			uw_ent_name.focus()
			return
		
		if not name.isalpha() :
			showerror("Name Issue", "Invalid Name. Avoid Special Characters")
			uw_ent_name.delete(0, END)
			uw_ent_name.focus()
			return	

		len(name) == 15
		if len(name) > 15:
			showerror("Warning !", "Name limit exceeding")
			uw_ent_name.delete(0, END)
			uw_ent_name.focus()
			return

		
		try:
			marks = int(uw_ent_marks.get())
		except ValueError:
			showerror("Marks Issue","Invalid Marks")
			showerror("Marks Issue","Enter Some Marks ")
			uw_ent_marks.delete(0, END)
			uw_ent_marks.focus()
			return

		else:	
			if ((int(marks) == 0) or (int(marks) < 0) or (int(marks) > 100)):
				showerror("Marks Issue", "Enter Proper Marks ")
				uw_ent_marks.delete(0, END)
				uw_ent_marks.focus()
				return
		
		cursor.execute(sql%(name, marks, rno))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success ","Record Updated ")
		else:
			showerror("Updation Failed", "Record does not exists !")
		uw_ent_rno.delete(0, END)
		uw_ent_name.delete(0, END)
		uw_ent_marks.delete(0, END)
		uw_ent_rno.focus()
		return
	
	except Exception as e: 
		con.rollback()
		showerror("Issue", e)

	finally:
		if con is not None:
			con.close()

def f9():
	main_window.deiconify()
	delete_window.withdraw()
	dw_ent_rno.delete(0, END)
	return

def f10():
	delete_window.deiconify()
	main_window.withdraw()

def f11():
	con = None
	try:
		con = connect("sms.db")
		cursor = con.cursor()
		sql = "delete from student where rno = '%d' "
		try:
			rno = int(dw_ent_rno.get())
		except ValueError:
			showerror("Rno Issue", "Enter a Rno to be Deleted")
			dw_ent_rno.delete(0, END)
			dw_ent_rno.focus()
			return
	
		cursor.execute(sql % (rno))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success ","Record Deleted ")
		else:
			showerror("Failure ","Record does not exists ")
		dw_ent_rno.delete(0, END)
	except Exception as e:
		con.rollback()
		showerror("Issue", e)
		dw_ent_rno.delete(0, END)
		dw_ent_rno.focus()
		return
	finally:
		if con is not None:
			con.close()

def f12():
	cnx = create_engine('sqlite:///sms.db').connect()
	data = pd.read_sql_table('student', cnx)
	print(data)

	name = data['name'].tolist()
	marks = data['marks'].tolist()

	plt.bar(name, marks, width=0.35, color=["red", "green", "blue", "yellow", "orange", "purple", "indigo", "brown"] )
	plt.ylabel("Marks")
	plt.title("Batch Information ! ")
	plt.show()


# Fetching Location:
try:
	wa = "https://ipinfo.io/103.204.39.101?token=fd3458541faabc"
	res = requests.get(wa)
	data = res.json()						
	city_name=data['city']
except Exception as e:
	showerror("issue", e)


# Fetching Temperature:
try:
	a1 = "https://api.openweathermap.org/data/2.5/weather/?units=metric"
	a2 = "&q= "+ city_name
	a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
	wa = a1+a2+a3						
	res=requests.get(wa)
	data=res.json()
	t=data['main']['temp']
except Exception as e:
	showerror("issue", e)


# Fetching Quote of the day:
#try:
#	wa="https://www.brainyquote.com/quote_of_the_day"
#	res = requests.get(wa)
#	data = bs4.BeautifulSoup(res.text,"html.parser")
#	info=data.find("img", {"class":"p-qotd"})				
#	quote=info["alt"]
#except Exception as e:
#	showerror("issue", e)

	
main_window = Tk()
main_window.title("S.M.S")
main_window.geometry("800x600+400+100")
main_window.configure(bg="DodgerBlue2")
main_window.iconbitmap("student.ico")

f=("Times New Roman", 20, "bold")
mw_btn_add = Button(main_window, text="Add",font=("Times New Roman",20,"bold"), width=10,bg="green2",command=f1)
mw_btn_view = Button(main_window, text="View", font=("Times New Roman",20,"bold"), width=10,bg="wheat1",command=f5)
mw_btn_update = Button(main_window, text="Update", font=("Times New Roman",20,"bold"), width=10,bg="yellow",command=f7)
mw_btn_delete = Button(main_window, text="Delete", font=("Times New Roman",20,"bold"), width=10,bg="LightSkyBlue1",command=f10)
mw_btn_charts = Button(main_window, text="Charts", font=("Times New Roman",20,"bold"), width=10,bg="IndianRed1",command=f12)

mw_lbl_location = Label(main_window, text="Location: "+city_name,bg="DarkOrange1",font=("Times New Roman", 20,"bold"))
mw_lbl_location.place(x=10, y=430)

mw_lbl_temp = Label(main_window, text="Temp: "+str(t),bg="snow",font=("Times New Roman", 20,"bold"))
mw_lbl_temp.place(x=600, y=430)

#mw_lbl_qotd = Label(main_window, text="QOTD: "+quote,bg="navajo white",font=("Times New Roman", 20,"bold italic"))
#mw_lbl_qotd.place(x=10,y=525)

mw_btn_add.pack(pady=10)
mw_btn_view.pack(pady=10)
mw_btn_update.pack(pady=10)
mw_btn_delete.pack(pady=10)
mw_btn_charts.pack(pady=10)



add_window = Toplevel(main_window)
add_window.title("Add St. ")
add_window.geometry("500x550+400+100")
add_window.configure(bg="green2")
add_window.iconbitmap("add-user.ico")

aw_lbl_rno = Label(add_window, text="Enter Rno: ",bg="green2",font=("Times New Roman", 22,"bold"))
aw_ent_rno = Entry(add_window, bd=5,bg="pale green",font=("Times New Roman", 22,"bold"))
aw_lbl_name = Label(add_window, bd=5,text="Enter Name: ",bg="green2",font=("Times New Roman", 22,"bold"))
aw_ent_name = Entry(add_window, bd=5,bg="pale green",font=("Times New Roman", 22,"bold"))
aw_lbl_marks = Label(add_window, text="Enter Marks: ",bg="green2",font=("Times New Roman", 22,"bold"))
aw_ent_marks = Entry(add_window, bd=5,bg="pale green",font=("Times New Roman", 22,"bold"))
aw_btn_save = Button(add_window, text="Add",bg="pale green",font=("Times New Roman", 20,"bold"),command=f3)
aw_btn_back = Button(add_window, text="Back",bg="pale green", font=("Times New Roman", 20,"bold"),command=f2)
aw_lbl_rno.pack(pady=10)
aw_ent_rno.pack(pady=10)
aw_lbl_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_lbl_marks.pack(pady=10)
aw_ent_marks.pack(pady=10)
aw_btn_save.pack(pady=10)
aw_btn_back.pack(pady=10)
add_window.withdraw()



view_window = Toplevel(main_window)
view_window.title("View St. ")
view_window.geometry("650x500+400+100")
view_window.configure(bg="wheat1")
view_window.iconbitmap("search.ico")

vw_st_data = ScrolledText(view_window, width=40, height=10,bg="old lace", font=("Times New Roman", 22))
vw_btn_back = Button(view_window, text="Back", font=("Times New Roman", 22,"bold"),bg="old lace",command=f4)
vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)
view_window.withdraw()



update_window = Toplevel(main_window)
update_window.title("Update St. ")
update_window.geometry("500x550+400+100")
update_window.configure(bg="yellow")
update_window.iconbitmap("refresh.ico")

uw_lbl_rno = Label(update_window, text="Enter Rno: ",bg="yellow",font=("Times New Roman", 22,"bold"))
uw_ent_rno = Entry(update_window, bd=5,bg="light yellow",font=("Times New Roman", 22,"bold"))
uw_lbl_name = Label(update_window, bd=5,text="Enter Name: ",bg="yellow", font=("Times New Roman", 22,"bold"))
uw_ent_name = Entry(update_window, bd=5,bg="light yellow", font=("Times New Roman", 22,"bold"))
uw_lbl_marks = Label(update_window, text="Enter Marks: ",bg="yellow", font=("Times New Roman", 22,"bold"))
uw_ent_marks = Entry(update_window, bd=5,bg="light yellow", font=("Times New Roman", 22,"bold"))
uw_btn_save = Button(update_window, text="Save", bg="light yellow",font=("Times New Roman", 20,"bold"), command=f8)
uw_btn_back = Button(update_window, text="Back",bg="light yellow", font=("Times New Roman", 20,"bold"), command=f6)
uw_lbl_rno.pack(pady=10)
uw_ent_rno.pack(pady=10)
uw_lbl_name.pack(pady=10)
uw_ent_name.pack(pady=10)
uw_lbl_marks.pack(pady=10)
uw_ent_marks.pack(pady=10)
uw_btn_save.pack(pady=10)
uw_btn_back.pack(pady=10)
update_window.withdraw()


delete_window = Toplevel(main_window)
delete_window.title("Delete St. ")
delete_window.geometry("500x500+400+100")
delete_window.configure(bg="LightSkyBlue1")
delete_window.iconbitmap("delete.ico")

dw_lbl_rno = Label(delete_window, text="Enter Rno: ",bg="LightSkyBlue1", font=("Times New Roman", 22,"bold"))
dw_ent_rno = Entry(delete_window, bd=5,bg="light cyan", font=("Times New Roman", 22,"bold"))
dw_btn_save = Button(delete_window, text="Delete", bg="light cyan",font=("Times New Roman", 20,"bold"), command=f11)
dw_btn_back = Button(delete_window, text="Back", bg="light cyan",font=("Times New Roman", 20,"bold"), command=f9)
dw_lbl_rno.pack(pady=10)
dw_ent_rno.pack(pady=10)
dw_btn_save.pack(pady=10)
dw_btn_back.pack(pady=10)
delete_window.withdraw()


main_window.mainloop()