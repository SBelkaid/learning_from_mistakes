import sys
import json
sys.path.insert(0,'../exercises')
from Tkinter import *
from A import *
from collections import deque
from EntryCustom import CustomEntryForm
from tkMessageBox import askokcancel

TITLE_FONT = ("Helvetica", 18, "bold")

class QuestionGenerator(Tk):
	question_data = None
	all_questions = json.load(open('questions_dict.json', 'r'))
	def __init__(self, parent=None, controller=None, *args, **kwargs):
		Tk.__init__(self, parent, *args, **kwargs)
		self.exercises = self.all_questions.keys()
		self.exercises.sort()
		self.current_question = self.exercises[0]
		self.container = Frame(self)
		self.container.pack(side=TOP, fill=BOTH, expand=TRUE)
		self.container.grid_rowconfigure(0, weight=1)
		self.container.grid_columnconfigure(0, weight=1)

		count = 0
		self.exercise_frame_container = {}
		for ex in self.all_questions:
			print ex
			f = ExerciseFrame(ex, self.container, self)
			self.exercise_frame_container[ex] = f
			f.__name__ = ex
			f.grid(row=0, column=0, sticky="nsew")
			count +=1

		#put the start page on top of the stacking order
		self.starter = StartPage(self.container ,self)
		self.starter.__name__ = 'starter'
		self.exercise_frame_container[StartPage.__name__] = self.starter
		self.starter.grid(row=0, column=0, sticky="nsew")


		#code for debugging, loking at the stacking order. 
		# print "frames dictionairy", self.exercise_frame_container, '\n\n\n\n'
		# print "children of self: ", self.winfo_children(), '\n\n\n'
		# print "children of container that's within self", self.container.winfo_children()
		# print [e.__name__ for e in self.container.winfo_children()]
		# print len(self.container.winfo_children())
		# print len(self.winfo_children())

	def show_question(self, f=None):
		print 'button has been pressed for show_question'
		if f:
			print f
			# print self.exercise_frame_container.keys()
			frame = self.exercise_frame_container[f]
			frame.tkraise()
			# print self.container.winfo_children()

class StartPage(Frame):
    def __init__(self, parent=None, controller=None, *args, **kwargs):
    	Frame.__init__(self, parent, *args, **kwargs)
    	self.controller = controller
        label = Label(self, text="This is an overview of the exercises", font=TITLE_FONT)
        label.pack(side=TOP, fill=X, pady=10)
        exercises = controller.all_questions.keys()
        exercises.sort()
        for ex in exercises:
        	# print ex
        	Button(self, text=ex, command=lambda:controller.show_question(ex)).pack()

class ExerciseFrame(Frame):
	def __init__(self, ex_id, parent=None, controller=None,*args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.controller = controller
		self.ex_id = ex_id
		Label(self, text='Exercise '+str(ex_id)).pack()
		other_exercises = filter(lambda x: x != ex_id, self.controller.all_questions)
		other_exercises.sort()
		# print 'These are the other exercises: ', other_exercises
		explanation_label = Label(self, text=self.controller.all_questions[ex_id]['explanation'])
		explanation_label.pack()
		explanation_label.bind('<Button-1>', lambda x:self.initialize_questions(x))


		#Buttons to raise another question frame to the front
		for other in other_exercises:
			print 'These are the other exercises in the container', other_exercises
			Button(self, text=other, command=lambda:controller.show_question(other)).pack(side=LEFT)
		Button(self, text='Start Page', command=lambda:controller.show_question('StartPage')).pack(side=LEFT)

	def initialize_questions(self, event):
		print 'starting to show questions'
		self.question_frame_container = {}
		for question_id in self.controller.all_questions[self.ex_id].keys():
			q_f = QuestionFrame(question_id, self, self.controller)
			self.question_frame_container[question_id] = q_f
			q_f.__name__ = "question {}".format(question_id)
			q_f.grid(row=0, column=0, sticky="nsew")
		# print self.winfo_children()
		self.clear_questions()
		self.show_question_by_id('1')

	def show_question_by_id(self, question_number):
		to_show = self.question_frame_container[question_number]
		to_show.tkraise()
		# print self.winfo_children()

	def clear_questions(self):
		print "clearing questions"
		print zip(*self.question_frame_container.items())[1]
		# if self.question_frame_container:
			# frames = zip(*self.question_frame_container.items())[1]


class QuestionFrame(Frame):
	def __init__(self, question_id, parent, controller, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.controller = controller
		self.config(bg='blue')
		self.pack(expand=True)
		Label(self, text='this is a question {}'.format(question_id), font=TITLE_FONT).pack()
		Button(self, text='BUTTON', command=lambda:self.quit()).pack()

if __name__ == '__main__':
	QuestionGenerator().mainloop()
	# q = json.load(open('questions_dict.json', 'r'))