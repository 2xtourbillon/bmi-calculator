from tkinter import *
from tokenize import Double

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

# mass variable
mass = DoubleVar()
w_label = Label(root, text='Mass', fg='red', bg='black', font=('Calibri', 14, 'bold'),
                 pady=10, padx=2)

mas = Entry(root, textvariable=mass)
w_label.grid(row=4)
mas.grid(row=4, column=1)

# BMI variable
bmi_Val = DoubleVar()
stat = StringVar()
bmi = Label(root, text='BMI: ', fg='blue', bg='black', font=('Calibri', 14, 'bold'),
            padx=2, pady=10, justify=LEFT)
status = Label(root, text='Status', fg='blue', bg='black', font=('Calibri', 14, 'bold'),
            padx=2, pady=10)
status_msg = Label(root, textvariable=stat, fg='white', bg='black', font=('Calibri', 14, 'bold'),
            padx=2, pady=10)
BMI_total = Label(root, textvariable=bmi_Val, fg='white', bg='black', font=('Calibri', 14, 'bold'),
            padx=2, pady=10)

bmi.grid(row=6)
status.grid(row=7)
BMI_total.grid(row=6, column=1)
status_msg.grid(row=7, column=1)

# calc and clear buttons
calculate = Button(root, text='Calculate', command=calc, fg='white', bg='black', font=('Calibri', 12, 'bold'))
clear = Button(root, text='Reset', command=clear, fg='black', bg='white', font=('Calibri', 12, 'bold'))
calculate.grid(row=8)
clear.grid(row=8, column=3)




root.mainloop()