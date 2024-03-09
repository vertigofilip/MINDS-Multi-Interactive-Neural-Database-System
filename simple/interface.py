import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('M.I.N.D.S. text interface')
window.geometry('300x300')

# input_frame
input_frame = ttk.Frame(master=window)
text_input = ttk.Entry(master = input_frame)
confirm_button = ttk.Button(master = input_frame, text='send')
text_input.pack(side='left', padx=10)
confirm_button.pack(side='left')
input_frame.pack()

#run
window.mainloop()