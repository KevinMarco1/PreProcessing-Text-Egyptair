import tkinter as tk
from tkinter import scrolledtext , messagebox
import processing_data
import excel


# Create a tkinter window
window = tk.Tk()
window.title("Egypt Air")
window.geometry('800x600')

# Create a scrollable text input field
txt = scrolledtext.ScrolledText(window, width=100, height=20, wrap=tk.WORD)
txt.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a frame for the buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# Create a clear button
clear_button = tk.Button(button_frame, text="Clear", width=20, height=3, command=lambda: txt.delete(1.0, tk.END) , font=("Arial", 10, "bold") )
clear_button.pack(side=tk.LEFT, padx=20)

# Create a processing button
processing_button = tk.Button(button_frame, text="Process", width=20, height=3, command=lambda: process_input(txt.get("1.0", tk.END)) ,font=("Arial", 10, "bold"))
processing_button.pack(side=tk.LEFT, padx=20)

# Define a function to process the input
def process_input(input_text):
    input_text += r'\n'
    data = [str]
    try:
        data = processing_data.main(input_text)
    except IndexError:
        # Show a pop-up message when the program crash 
        messagebox.showinfo("Error", "This is message not in the required format. Please put it in the format and try again")
    else:
        excel.fill_data_into_excel_sheet(data)

# Center the window on the screen
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())

# Start the tkinter event loop
window.mainloop()

    