from Tkinter import *


class CustomEntryForm(Frame):
	def __init__(self, parent, controller, *args, **kw):
		Frame.__init__(self, parent, *args, **kw)
		self.parent = parent
		self.controller = controller
		# self.config(width=500,height=40,bg='yellow')
		self.pack()
		# self.pack_propagate(0)
		self.value = None
		self.setInitial()

	def setInitial(self):
		self.input_field = Entry(self, textvariable=StringVar())
		self.input_field.pack(side=LEFT)
		self.input_field.bind('<Button-1>', 
				lambda x: self.clearOnClick(x))
		self.input_field.bind('<Return>', 
				lambda x: self.prepareQuestionData())
		self.input_field.insert(0,'Type input..')
		self.count_clicks = 0
		self.submit_btn = Button(self, text='Submit', 
				command=lambda:self.prepareQuestionData())
		self.submit_btn.pack(pady=5, side=LEFT)

	def prepareQuestionData(self):
		cur_exercise = self.parent.parent_exercise_id
		cur_question = self.parent.parent.current_question #probably not the best way to do this
		self.parent.parent.report(self.input_field.get(), cur_exercise, cur_question)

	def clearOnClick(self, event):
		'''
		clear entry widget only on first click
		'''
		if self.count_clicks == 0:
			self.input_field.delete(0, 'end') 
		self.count_clicks += 1
		print "clicked the input button"


if __name__ == '__main__':
	CustomEntryForm().mainloop()