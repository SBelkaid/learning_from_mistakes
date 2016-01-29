from Tkinter import *



class CustomEntryForm(Frame):
	def __init__(self, parent=None, **kw):
		Frame.__init__(self, parent, **kw)
		# self.config(width=500,height=40,bg='yellow')
		self.pack()
		# self.pack_propagate(0)
		self.setInitial()

	def setInitial(self):
		self.input_field = Entry(self, textvariable=StringVar())
		self.input_field.pack(side=LEFT)
		self.input_field.bind('<Button-1>', lambda x: self.clearOnClick(x))
		self.input_field.bind('<Return>', lambda x: self.returnHandler(x))
		self.input_field.insert(0,'Type input..')
		self.count_clicks = 0
		self.submit_btn = Button(self, text='Submit', command=self.returnEntry)
		self.submit_btn.pack(pady=5, side=LEFT)


	def clearOnClick(self, event):
		'''
		clear entry widget only on first click
		'''
		print event.char
		if self.count_clicks == 0:
			self.input_field.delete(0, 'end') 
		self.count_clicks += 1
		print "clicked the input button"

	def returnEntry(self):
		print self.input_field.get()

	def returnHandler(self, event):
		print "pressed return key"
		print event.char
		print self.input_field.get()

if __name__ == '__main__':
	CustomEntryForm().mainloop()