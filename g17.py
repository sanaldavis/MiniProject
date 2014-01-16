from Tkinter import *
import pyPdf
import MySQLdb
import ttk
import tkMessageBox
import string
from urllib2 import Request, urlopen
from pyPdf import PdfFileWriter, PdfFileReader
from StringIO import StringIO


root=Tk()
root.withdraw()
root1=Toplevel()
root2=Toplevel()
root3=Toplevel()
root4=Toplevel()
root1.withdraw()
root2.withdraw()
root4.withdraw()


e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()
e5 = StringVar()
e6 = StringVar()
e7 = StringVar()
e8 = StringVar()
e9 = StringVar()
e10 = StringVar()
e11 = StringVar()
e12 = StringVar()
e13 = StringVar()
e14 = StringVar()

r1 = StringVar()
r2 = StringVar()
r3 = StringVar()
code={}
codes={}
regf={}
regl={}
grade=['q','q','q','q','q','q','q','q']
sgpa=''

#reg=e1.get()
#print reg
#reg=reg.upper()
global line
global length
global a
global n
global w
global sem
global semstr



	

def sample1():
		
	flag=0;		
	branch=e14.get()
	branch=branch.upper()
	batch=e1.get()
	month=e2.get()
	month=month.upper()
	year=e3.get()
	sem=e4.get()
	sem=sem.upper()
	semstr=sem+branch+batch
	print semstr
	exam=month+year
	n=e5.get()
	n=int(n)
	db1 = MySQLdb.connect(host="localhost",user="root",passwd="tharayil",db="result")
	cursor = db1.cursor()
	sql="select * from TABLES"
	cursor.execute(sql)
	for row in cursor.fetchall():
		print row[0]
		if  row[0]==semstr:
			flag=1;
	if flag!=1:
		code[0]=e6.get()
		code[1]=e7.get()
		code[2]=e8.get()
		code[3]=e9.get()
		code[4]=e10.get()
		code[5]=e11.get()
		code[6]=e12.get()
		code[7]=e13.get()
		for i in range(n):
			code[i]=code[i].upper()
			codes[i]=code[i].replace(" ",'_')
		
	
		db1 = MySQLdb.connect(host="localhost",user="root",passwd="tharayil",db="result")
		cursor = db1.cursor()
		sql = 'create table %s (REGNO varchar(20) primary key, %s varchar(20), %s varchar(20), %s varchar(20), %s varchar(20), %s varchar(20), %s varchar(20),  %s varchar(20), %s varchar(20),  SGPA varchar(20), MONTH_YEAR varchar(20))' %(semstr,codes[0],codes[1],codes[2],codes[3],codes[4],codes[5],codes[6],codes[7])
		cursor.execute(sql)
		sql = 'insert into TABLES values("%s")' %semstr
		cursor.execute(sql)
		sql = 'insert into sub_codes values("%s","%s","%s","%s","%s","%s","%s","%s","%s")' %(codes[0],codes[1],codes[2],codes[3],codes[4],codes[5],codes[6],codes[7],semstr)
		cursor.execute(sql)
	class Application(Frame):
		def __init__(root1, master=None):
			Frame.__init__(root1, master, bd=100, height=100, width=100, bg="cyan")
			root1.grid()
			root1.createWidgets()
	
		def createWidgets(root1):
			
			
			Label(root1, text="Starting Regno", width=15, anchor=W, bg="blue").grid(column=100,row=3)
			Label(root1, text="Ending   Regno", width=15, anchor=W, bg="green").grid(column=110,row=3)
			Label(root1, text="Enter the url(replace regno with %s)", width=30, anchor=W, bg="green").grid(column=80,row=1)
			Entry(root1, width=50, textvariable=r3, bg="blue").grid(column=90, row=1, sticky=(E),pady=5, padx=5)
			Entry(root1, width=15, textvariable=r1, bg="blue").grid(column=100, row=4, sticky=(E),pady=5, padx=5)
			Entry(root1, width=15, textvariable=r2, bg="green").grid(column=110, row=4, sticky=(E),pady=5, padx=5)
		
			Button ( root1, text='SUBMIT', command=sample, bg="yellow").grid(ipadx=10, column=105,row=20)
	root2.destroy()
	root1.update()
	root1.deiconify()	
	app = Application(root1)
	app.master.title("REGISTER NUMBER") 
	app.mainloop()

	

def sample():

		regf=r1.get()
		regl=r2.get()
		branch=e14.get()
		branch=branch.upper()
		batch=e1.get()
		month=e2.get()
		month=month.upper()
		year=e3.get()
		sem=e4.get()
		sem=sem.upper()
		semstr=sem+branch+batch
		exam=month+year
		n=e5.get()
		n=int(n)
		sgpa=''
		code[0]=e6.get()
		code[1]=e7.get()
		code[2]=e8.get()
		code[3]=e9.get()
		code[4]=e10.get()
		code[5]=e11.get()
		code[6]=e12.get()
		code[7]=e13.get()
		for i in range(n):
			code[i]=code[i].upper()
			codes[i]=code[i].replace(" ",'_')
		
		
		regf=regf.upper()
		regl=regl.upper()
		regb=r1.get()
		regb=regb.upper()
		url=r3.get()
		
		while(1):
			print "correct"
			flag=0
			url1 = url %(regb)
			#url1="http://202.88.252.6/exams/results1/btechNEW/creditresrevalnet1.php?id=1108&regno=EPAJECS069&Submit=Submit" 
			print url1
			writer = PdfFileWriter()
			content=""
			remoteFile = urlopen(Request(url1)).read()
			memoryFile = StringIO(remoteFile)
			pdfFile = PdfFileReader(memoryFile)
			
			content += pdfFile.getPage(0).extractText() + "\n"
			content = " ".join(content.replace(u"\xa0", " ").strip().split())
			f= open('test2.txt','w')
			pdfl = content.encode("ascii", "ignore")
			f.write(pdfl)
			f.close()			
			f = open('test2.txt', "r") # Opening the text file
			line = f.readline() # Reading the whole line
			length=len(line)
			print regb
			len_reg=len(regb)
			for i in range(length-len_reg):
				if regb==line[i:i+len_reg]:
					flag=1		
			if flag==1:
				
		
		
				def check(code,c):
					print code
					l=len(code)
				
					for i in range(length-len(code)):
					
						if code==line[i:i+l]:
							#print "found %s" %code
							k=i+l
							for j in range(k,length,1):
								if (line[j].isdigit()) and (month==line[j+2:j+2+len(month)]):
									grade[c]=line[j+1]
									break
								
									
				
					return
				
				
				
				c=0
				n=e5.get()
				n=int(n)
				for i in range(n):				
					check(code[i],i)
				
				for i in range(length):
					if 'sgpa'==line[i:i+4].lower():
						for p in range(i,i+100,1):
							if  (line[p].isdigit()):
								break
							else:
								p=p+1
				for p in range(p,p+5,1):
					if line[p].isdigit() or line[p]=='.' or line[p]=='*':		
						sgpa=sgpa+line[p]
					else:
						break
				print sgpa
						
				db1 = MySQLdb.connect(host="localhost",user="root",passwd="tharayil",db="result")
				cursor = db1.cursor()
			
				sql='insert into %s values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' %(semstr,regb,grade[0],grade[1],grade[2],grade[3],grade[4],grade[5],grade[6],grade[7],sgpa,exam)
				cursor.execute(sql)
			
				
			else:
				tkMessageBox.showerror("Not Found", regb+" NOT VALID")
			if regb==regl:
				break
			fr=regb.rstrip()[7:]
			regb=regf.rstrip()[0:7]
										
			fr1=int(fr)
			fr1=fr1+1
			
			fr1=str(fr1)
			regb=regb+'0'+fr1
		tkMessageBox.showinfo("SUCCESS", "SUCCESSFULLY COMPLETED")
		root2.destroy()
		barchart()

def barchart():
	root4.destroy()
	branch=e14.get()
	branch=branch.upper()
	batch=e1.get()
	sem=e4.get()
	sem=sem.upper()
	semstr=sem+branch+batch	

	x3={}
	x4={}
	y1={}
	x5={}
	x6={}
	y2={}
	flag=0
	flag1=100
	i=0
	k=100
	p=100
	a={}
	db1 = MySQLdb.connect(host="localhost",user="root",passwd="tharayil",db="result")
	cursor = db1.cursor()
	sql='select * from sub_codes where sem="%s"' %(semstr)
	cursor.execute(sql)
	cd_fetch=cursor.fetchall()
	for cd in cd_fetch:
		
		for j in range(8):
			print semstr
			sql = 'select count(%s) from %s where %s!="u"' %(cd[j],semstr,cd[j])
			cursor.execute(sql)
			cd1=cursor.fetchall()
			for r in cd1:
				a[i]=r[0]
			print a[i]		
			i=i+1
			print cd[j]
		
	
	sql = 'select count("%s") from %s' %(cd[0],semstr)
	cursor.execute(sql)
	cd1=cursor.fetchall()
	for r in cd1:
		sum=r[0]
	#sum=1000
	avg=0
	print "sum"
	print sum

	#for i in range(8):
	#	a[i]=raw_input("\nEnter the number:")
	#	a[i]=int(a[i])
	
	master1=Toplevel()
	w = Canvas(master1, width=1500, height=900)
	w.pack()
#	Button ( master1, text='NEXT', command=sample1, bg="yellow").grid(ipadx=10, column=50,row=20)
	
	s=cd[0][-3:]
	s=int(s)
	x=55
	x1=40
	x2=70
	w.create_line(10,620,620,620)
	w.create_line(10,620,10,10)
	for i in range(8):
		w.create_text(x,640, text=s, fill="red")
		s=s+1
		x=x+60
	for i in range(8):
		avg=a[i]*100/sum
		y=avg*5
		if avg>flag:
			k=0
			x3[k]=x1
			x4[k]=x2
			y1[k]=y
			flag=avg
		elif avg==flag:
			k=k+1
			x3[k]=x1
			x4[k]=x2
			y1[k]=y	

		if avg<flag1:
			p=0
			x5[k]=x1
			x6[k]=x2
			y2[k]=y
			flag1=avg
		elif avg==flag1 and avg!=flag:
			p=p+1
			x5[k]=x1
			x6[k]=x2
			y2[k]=y	
		w.create_rectangle(x1,600,x2,600-y, fill="red")
		w.create_text(x1+15,590-y, text=avg, fill="red")
		x1=x1+60
		x2=x2+60
	k=k+1
	p=p+1
	if k<100:
		for i in range(k):
			w.create_rectangle(x3[i],600,x4[i],600-y1[i], fill="green")
	if p<100:
		for i in range(p):
			w.create_rectangle(x5[i],600,x6[i],600-y2[i], fill="yellow")


	w.create_rectangle(800,200,830,230,fill="green" )
	w.create_text(900,215, text="highest percentage",fill="red")

	w.create_rectangle(800,160,830,190,fill="yellow" )
	w.create_text(900,175, text="lowest percentage",fill="red")
	#master.update()
	#master.deiconify()
	
	
	
	mainloop()
			

def sample3():

	class Application(Frame):
		def __init__(root2, master=None):
			w=Frame.__init__(root2, master, bd=100, height=100, width=200, bg="cyan")
			root2.grid()
			root2.createWidgets()
	
		def createWidgets(root2):
			
			Label(root2, text="Enter the branch", width=35, anchor=W, bg="green").grid()
			Label(root2, text="Enter the year of admission", width=35, anchor=W, bg="green").grid()
			Label(root2, text="Enter the month of examination", width=35, anchor=W, bg="green").grid()
			Label(root2, text="Enter the year of examination", width=35, anchor=W, bg="green").grid()
			Label(root2, text="Enter the semester", width=35, anchor=W, bg="green").grid(padx=0)
			Label(root2, text="Enter the total number of subjects", width=35, anchor=W, bg="green").grid()
			Label(root2, text="Enter the code first subject", width=35, anchor=W, bg="green").grid()
			Label(root2, text="Enter the code second subject", width=35, anchor=W, bg="green").grid()
			Label(root2, text="Enter the code third subject", width=35, anchor=W, bg="green").grid()
			Label(root2, text="Enter the code fourth subject", width=35, anchor=W, bg="green").grid()
			Label(root2, text="Enter the code fifth subject", width=35, anchor=W, bg="green").grid()
			Label(root2, text="Enter the code sixth subject", width=35, anchor=W, bg="green").grid()
			Label(root2, text="Enter the code seventh subject", width=35, anchor=W, bg="green").grid()
			Label(root2, text="Enter the code eight'th subject", width=35, anchor=W, bg="green").grid()
			
			Entry(root2, width=10, textvariable=e14, bg="green").grid(column=90, row=0, sticky=(E),pady=5)
			Entry(root2, width=10, textvariable=e1, bg="green").grid(column=90, row=1, sticky=(E),pady=5)
			Entry(root2, width=10, textvariable=e2, bg="green").grid(column=90, row=2, sticky=(E),pady=5)
			Entry(root2, width=10, textvariable=e3, bg="green").grid(column=90, row=3, sticky=(E),pady=5)
			Entry(root2, width=10, textvariable=e4, bg="green").grid(column=90, row=4, sticky=(E),pady=5)
			Entry(root2, width=10, textvariable=e5, bg="green").grid(column=90, row=5, sticky=(E),pady=5)
			Entry(root2, width=10, textvariable=e6, bg="green").grid(column=90, row=6, sticky=(E),pady=5)
			Entry(root2, width=10, textvariable=e7, bg="green").grid(column=90, row=7, sticky=(E),pady=5)
			Entry(root2, width=10, textvariable=e8, bg="green").grid(column=90, row=8, sticky=(E),pady=5)
			Entry(root2, width=10, textvariable=e9, bg="green").grid(column=90, row=9, sticky=(E),pady=5)
			Entry(root2, width=10, textvariable=e10, bg="green").grid(column=90, row=10, sticky=(E),pady=5)
			Entry(root2, width=10, textvariable=e11, bg="green").grid(column=90, row=11, sticky=(E),pady=5)
			Entry(root2, width=10, textvariable=e12, bg="green").grid(column=90, row=12, sticky=(E),pady=5)
			Entry(root2, width=10, textvariable=e13, bg="green").grid(column=90, row=13, sticky=(E),pady=5)
			#Button ( root2, text='CREATE TABLE', command=sample1, bg="yellow").grid(ipadx=10, column=100,row=20)
			Button ( root2, text='NEXT', command=sample1, bg="yellow").grid(ipadx=10, column=50,row=20)
		
	#root3.destroy()	
	root2.update()
	root2.deiconify()
	app = Application(root2)
	app.master.title("Sample application") 
	app.mainloop()	


def sample4():
	class Application(Frame):
		def __init__(root4, master=None):
			w=Frame.__init__(root4, master, bd=100, height=900, width=900, bg="cyan")

			root4.grid()
			root4.createWidgets()
	
		def createWidgets(root4):
			
			
			Label(root4, text="Enter the branch", width=35, anchor=W, bg="green").grid()
			Label(root4, text="Enter the year of admission", width=35, anchor=W, bg="green").grid()
			Label(root4, text="Enter the semester", width=35, anchor=W, bg="green").grid(padx=0)
			
			
			Entry(root4, width=10, textvariable=e14, bg="green").grid(column=90, row=0, sticky=(E),pady=5)
			Entry(root4, width=10, textvariable=e1, bg="green").grid(column=90, row=1, sticky=(E),pady=5)
			Entry(root4, width=10, textvariable=e4, bg="green").grid(column=90, row=2, sticky=(E),pady=5)
						
			Button ( root4, text='NEXT', command=barchart, bg="yellow").grid(ipadx=10, column=50,row=20)
	#root3.destroy()
	root4.withdraw()	
	root4.update()
	root4.deiconify()	
	app = Application(root4)
	app.master.title("GET RESULT") 
	app.mainloop()

def main_entry():
	class Application(Frame):
		def __init__(root3, master=None):
			Frame.__init__(root3, master, bd=100, height=100, width=100, bg="cyan")
			root3.grid()
			root3.createWidgets()
	
		def createWidgets(root3):
			
			
			Button ( root3, text='MAIN ENTRY', command=sample3, bg="yellow").grid(ipadx=10, column=105,row=20)
			Button ( root3, text='GET STATUS', command=sample4, bg="yellow").grid(ipadx=10, column=105,row=30)
			Button ( root3, text='EXIT', command=exit, bg="yellow").grid(ipadx=10, column=105,row=40)
			
		
	app = Application(root3)
	app.master.title("STARTING") 
	app.mainloop()
def exit():
	root.update()
	root.deiconify()
	root.destroy()
main_entry()
			
