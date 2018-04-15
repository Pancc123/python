#!-*- coding:utf-8 -*-
from tkinter import *
import tkinter.messagebox as mb
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack() 
        #pack()方法把Widget加入到父容器中，并实现布局。
		self.createWidgets()
		
	def createWidgets(self):
		self.helloLabel=Label(self,text='Hello,world!')
		self.helloLabel.pack()
		self.quitButton=Button(self,text='Quit',command=self.quit())
		self.quitButton.pack()
		'''self.nameInput=Entry(self)
		self.nameInput.pack()
		self.alterButton=Button(self,text='Hello',command=self.hello)
		self.alterButton.pack()'''
		
       #在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出。
	def hello(self):
		name=self.nameInput.get() or'world'
		mb.showinfo('Message','Hello,%s' %name)
app=Application()
app.master.title('Hello World!')
app.mainloop()
