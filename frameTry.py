import sys
sys.path.insert(0,'/Users/soufyanbelkaid/Research/The Network Inst/excercises')
from Tkinter import *
from A import questions
from generator import QuestionGenerator


def nextQuestion():
	print 'Moving on to the next question'

def displayMultipleChoice():
	cb_container = Frame(bd=1, relief=RIDGE, bg='blue', width=150, height=150)
	cb_container.pack(padx=5, pady=5, anchor=NW)
	cb_container.pack_propagate(0)
	answers = QuestionGenerator.question_data.get(str(1))['possible_answers']
	vars = []
	for key in answers:
		var = IntVar()
		Checkbutton(cb_container, text=key, variable=var, bg='blue').pack(anchor=NW)
	vars.append(var)
	Button(cb_container, text="Next", command=nextQuestion).pack(side=LEFT)
	Button(cb_container, text="Quit", command=cb_container.quit).pack(side=LEFT)

displayMultipleChoice()
mainloop()





