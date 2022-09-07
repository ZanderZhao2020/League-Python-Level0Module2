import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
	window = Tk()
	window.withdraw()

	# TODO Get the user to enter a question for the 8 ball to answer
	simpledialog.askstring("Prompt", "Enter your question")
	# Make a variable and initialize it to a random number between 0 and 3
	Rand = random.randint(0, 3)
	# If the random number is 0
	if Rand == 0:
		# tell the user "Yes"
		messagebox.showinfo("Message", "Yes")
	# If the random number is 1
	elif Rand == 1:
		# tell the user "No"
		messagebox.showinfo("Message", "No")
	# If the random number is 2
	elif Rand == 2:
		# tell the user "Maybe you should ask Google?"
		messagebox.showinfo("Message", "Maybe you should ask Google?")
	# If the random number is 3
	else:
		# write your own answer
		messagebox.showinfo("Message", "Ask later")
