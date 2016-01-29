import sys
sys.path.insert(0,'/Users/soufyanbelkaid/Research/The Network Inst/Programming Python GUI')
sys.path.insert(0,'/Users/soufyanbelkaid/Research/The Network Inst/excercises')
from Tkinter import *
from A import questions

class Question(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack()
		self.set_label(questions)

	def set_label(self, question_data):
		widget = Label(self, text=question_data['explanation'])
		widget.config(justify=LEFT)
		widget.pack(side=LEFT)


if __name__ == '__main__':
	Question().mainloop()
	# print questions.keys()