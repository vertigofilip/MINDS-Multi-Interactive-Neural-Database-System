import tkinter as tk
from tkinter import ttk

class ChatInterface:
    def __init__(self, root):
        self.root = root
        self.message_count = 0  # Keep track of the number of messages

        # Set up the chat display area
        self.chat_display = tk.Text(root, state='disabled', width=40, height=15, wrap='word')
        self.chat_display.pack(padx=10, pady=10)

        # Input frame for text input and send button
        self.input_frame = ttk.Frame(root)
        self.text_input = ttk.Entry(self.input_frame, width=30)
        self.send_button = ttk.Button(self.input_frame, text='Send', command=self.send_message)
        self.text_input.pack(side='left', padx=10)
        self.send_button.pack(side='left')
        self.input_frame.pack(pady=5)

    def send_message(self):
        message = self.text_input.get()
        if message:  # Check if the message is not empty
            self.display_message(message)
            self.text_input.delete(0, tk.END)  # Clear the input field

    def display_message(self, message):
        self.chat_display.config(state='normal')  # Enable editing of the Text widget
        side = 'left' if self.message_count % 2 == 0 else 'right'
        color = '#DFF0D8' if self.message_count % 2 == 0 else '#F0D8DF'
        tag_name = f"tag_{self.message_count}"
        
        # Add message to the chat display
        self.chat_display.insert(tk.END, f"{message}\n\n", tag_name)
        
        # Configure tag for message alignment and background color
        self.chat_display.tag_configure(tag_name, justify=side, lmargin1=20, lmargin2=20, rmargin=10,
                                        background=color, borderwidth=2, relief='solid', wrap='word')
        
        self.chat_display.config(state='disabled')  # Disable editing of the Text widget
        self.message_count += 1
        self.chat_display.see(tk.END)  # Scroll to the bottom

# Set up the window
window = tk.Tk()
window.title('M.I.N.D.S. Text Interface')
window.geometry('400x350')

app = ChatInterface(window)

# Run the application
window.mainloop()
