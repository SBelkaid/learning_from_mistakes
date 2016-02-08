import sys
import json
sys.path.insert(0,'exercises')
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
		# print "children of container that's within self", [e.__name__ for e in self.container.winfo_children()]
		# print [e.__name__ for e in self.container.winfo_children()]
		# print len(self.container.winfo_children())
		# print len(self.winfo_children())

	def show_question(self, f=None):
		print 'button has been pressed for show_question'
		if f:
			print f
			print "looking for exercise: {}".format(f)
			# print "\n\n stacking order {}".format(self.winfo_children())
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
        	print "from startpage showing the possible exercises", ex
        	Button(self, text=ex, command=lambda x=ex:controller.show_question(x)).pack()

class ExerciseFrame(Frame):
	'''
	I guess this is a controller in a controller. Probably not the right thing to do
	But it does control all the frames in the question_frame_container
	'''
	def __init__(self, ex_id, parent=None, controller=None,*args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.controller = controller
		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)
		self.ex_id = ex_id
		Label(self, text='Exercise '+str(ex_id)).pack()
		self.other_exercises = filter(lambda x: x != ex_id, self.controller.all_questions)
		self.other_exercises.sort()
		# print 'These are the other exercises: ', self.other_exercises
		explanation_label = Label(self, text=self.controller.all_questions[ex_id]['explanation'])
		explanation_label.pack()
		explanation_label.bind('<Button-1>', lambda x:self.initialize_questions(x))
		self.current_question = 1

		#Buttons to raise another question frame to the front
		for other in self.other_exercises:
			# print 'These are the other exercises in the container', self.other_exercises
			Button(self, text=other, command=lambda x=other:self.controller.show_question(x)).pack(side=LEFT)
		Button(self, text='Start Page', command=lambda:self.controller.show_question('StartPage')).pack(side=LEFT)

	def initialize_questions(self, event):
		print 'starting to show questions'
		self.question_frame_container = {}
		for question_id in self.controller.all_questions[self.ex_id].keys():
			if question_id != 'explanation':
				q_f = QuestionFrame(question_id, self, self.controller)
				self.question_frame_container[question_id] = q_f
				q_f.__name__ = "question {}".format(question_id)
				q_f.grid(row=0, column=0, sticky=NSEW)
				q_f.rowconfigure(0, weight=1)

		# print self.winfo_children()
		self.clear_questions()
		self.show_question_by_id(str(self.current_question))

	def nextExercise(self):
		print 'current exercise is {}'.format(self.ex_id)
		print 'the other exercises are {}'.format(self.other_exercises)
		# self.controller.show_question(self.other_exercises[0])
		self.controller.show_question('StartPage')
		# print self.other_exercises[0]

	def show_question_by_id(self, question_number):
		to_show = self.question_frame_container[question_number]
		to_show.tkraise()
		# print self.winfo_children()

	def clear_questions(self):
		print "clearing questions"
		print zip(*self.question_frame_container.items())[1]
		# if self.question_frame_container:
			# frames = zip(*self.question_frame_container.items())[1]
			# [e.destroy() for e in frames]
	
	def report(self, input_val, ex_id, question_id):
		'''
		currently it prints the input of the user in the entry of the questions frames
		This function should check the input or correctness. How to find the correct answer first?
		- pass with function call?
		- Controller actually should control all data, and the current question etc.

		'''
		correct_answer = QuestionGenerator.all_questions[ex_id][str(question_id)]['correct_answer']
		print input_val, ex_id, question_id, correct_answer
		input_val = input_val.encode('utf8')
		correct_answer = correct_answer.encode('utf8')

		if input_val != correct_answer:
			self.handleIncorrect(input_val, correct_answer)
		else:
			print "correct"
			self.changeColorEntryWidget('green')
	
	def changeColorEntryWidget(self, color):
		for f in self.question_frame_container[str(self.current_question)].winfo_children():
			entry_widget = f.__dict__.get('input_field')
			if entry_widget: 
				entry_widget.configure(highlightbackground=color, highlightcolor=color)

	def handleIncorrect(self, incorrect_input, correct_input):
		'''
		It should generate feedback based on the input of the user it also
		makes the entry widget red.
		functions does the following:
			find all objects in the QuestionFrameContainer
			list the attributes of the class 
			if it contains a input_field attribute that must be the Entry widget
			created by instanciating EntryCustom
		'''
		print 'You have answered incorrectly {}, the correct answer is {}'\
					.format(incorrect_input, correct_input)
		self.changeColorEntryWidget('red')

class QuestionFrame(Frame):
	def __init__(self, question_id, parent, controller, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.controller = controller
		self.parent = parent
		self.parent_exercise_id = parent.ex_id
		self.parent.current_question = 1
		# self.config(bg='blue')
		text = controller.all_questions[self.parent.ex_id][question_id]['question']
		Label(self, text=text, font=TITLE_FONT).pack()
		CustomEntryForm(self, controller)
		self.nxt_btn = Button(self, text='Next',\
				 command=lambda:self.nextQuestion())
		self.prev_btn = Button(self, text='Previous',\
				 command=lambda:self.previousQuestion())
		self.nxt_btn.pack(side=LEFT)
		self.prev_btn.pack(side=LEFT)
		Button(self, text='quit', command=lambda:self.quit()).pack(side=LEFT)

	def nextQuestion(self):
		question_list = self.controller.all_questions[self.parent.ex_id].keys()
		# pquestion_list.index(str(self.parent.current_question))
		if question_list.index(str(self.parent.current_question))==int(question_list[-1]):
			print 'Move on to next exercise, still need to implement this.'
			self.parent.nextExercise()
		if not self.parent.current_question == \
					len(self.controller.all_questions[self.parent.ex_id].keys())-1:
			self.parent.current_question += 1
			self.parent.show_question_by_id(str(self.parent.current_question))

	def previousQuestion(self):
		question_list = self.controller.all_questions[self.parent.ex_id].keys()
		print question_list
		print question_list.index(str(self.parent.current_question))
		if not self.parent.current_question == 1: 
			self.parent.current_question -= 1
			self.parent.show_question_by_id(str(self.parent.current_question))

if __name__ == '__main__':
	QuestionGenerator().mainloop()
	# q = json.load(open('questions_dict.json', 'r'))