import tkinter as tk
import os

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Сложение двух чисел")
        
        self.num1 = tk.StringVar()
        self.num2 = tk.StringVar()
        self.result = tk.StringVar()
        
        self.load_previous_values()
        self.create_widgets()
    
    def load_previous_values(self):
        if os.path.exists("previous_values.txt"):
            with open("previous_values.txt", "r") as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    self.num1.set(lines[0].strip())
                    self.num2.set(lines[1].strip())

    def create_widgets(self):
        frame = tk.Frame(self)
        frame.pack(padx=10, pady=10)

        label1 = tk.Label(frame, text="Первое число:")
        label1.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        entry1 = tk.Entry(frame, textvariable=self.num1)
        entry1.grid(row=0, column=1, padx=5, pady=5)

        label2 = tk.Label(frame, text="Второе число:")
        label2.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        entry2 = tk.Entry(frame, textvariable=self.num2)
        entry2.grid(row=1, column=1, padx=5, pady=5)

        calculate_button = tk.Button(frame, text="Сложить", command=self.add_numbers)
        calculate_button.grid(row=2, columnspan=2, padx=5, pady=5)

        self.result_label = tk.Label(frame, textvariable=self.result)
        self.result_label.grid(row=3, columnspan=2, padx=5, pady=5)
    
    def add_numbers(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            result = num1 + num2
            self.result.set("Результат: " + str(result))
            self.save_current_values()
        except ValueError:
            self.result.set("Ошибка! Введите числа.")
    
    def save_current_values(self):
        with open("previous_values.txt", "w") as file:
            file.write(self.num1.get() + "\n")
            file.write(self.num2.get() + "\n")

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
