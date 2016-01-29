from Tkinter import *

root = Tk()
# root.pack(side="top", fill="both", expand=True)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

Label(root, text='label 1').grid(row=0, column=0, sticky="nsew")
Label(root, text='label 2').grid(row=0, column=0, sticky="nsew")



def show_lowest(element):
	root.winfo_children()[0].tkraise()

root.mainloop()