from tkinter import *

# root window
root = Tk()
root.title('BMI Calculator')
root.configure(width=100, height=100)
root.configure(bg='black')

# height label
height = DoubleVar()
h_label = Label(root, text='height', fg='red', bg='black', font=('Calibri', 14, 'bold'),
                 pady=5, padx=8)
heigh = Entry(root, textvariable=height)
h_label.grid(row=2)
heigh.grid(row=2, column=1, columnspan=2, padx=5)

