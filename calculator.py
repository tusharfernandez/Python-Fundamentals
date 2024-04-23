import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Calculator")

        # Configure style for buttons
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 14), background='black', foreground='white')

        # Entry widget for displaying input and output
        self.entry = ttk.Entry(master, width=30, font=('Arial', 14), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Button labels
        button_labels = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+',
            'History'
        ]

        # Create and position buttons
        row = 1
        col = 0
        self.buttons = []
        for label in button_labels:
            if label == 'History':
                button = ttk.Button(master, text=label, command=self.show_history, width=4)
            else:
                button = ttk.Button(master, text=label, command=lambda label=label: self.on_button_click(label), width=4)
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(button)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Text widget for displaying history
        self.history_text = tk.Text(master, height=10, width=40, font=('Arial', 12))
        self.history_text.grid(row=row, column=0, columnspan=4, padx=10, pady=10)

    def on_button_click(self, label):
        if label == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.history_text.insert(tk.END, f"{self.entry.get()} = {result}\n")
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif label == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, label)

    def show_history(self):
        self.history_text.delete('1.0', tk.END)
        self.history_text.insert(tk.END, "Previous Calculations:\n")
        self.history_text.insert(tk.END, "========================\n")
        self.history_text.insert(tk.END, self.history_text_content)

def main():
    root = tk.Tk()
    root.configure(background='black')
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()