import tkinter as tk



class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=30, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # create buttons
        self.create_button("1", 1, 0)
        self.create_button("2", 1, 1)
        self.create_button("3", 1, 2)
        self.create_button("+", 1, 3)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("-", 2, 3)
        self.create_button("7", 3, 0)
        self.create_button("8", 3, 1)
        self.create_button("9", 3, 2)
        self.create_button("*", 3, 3)
        self.create_button("C", 4, 0)
        self.create_button("0", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("/", 4, 3)
        self.Metric_conversion_button('Km-Mi', 1, 3)
        self.Metric_conversion_button('Mi-Km', 2, 3)
        self.Metric_conversion_button('Kg-Po', 3, 3)
        self.Metric_conversion_button('Po-Kg', 4, 3)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=7, height=2, command=lambda: self.button_click(text))
        ''' note that you don't normal put in the arguement when calling the funciton in a tkinter button class but the lambda
        function makes us able to do that without a problem occuring'''
        button.grid(row=row, column=column, padx=5, pady=5)

    def Metric_conversion_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=7, height=2, command=lambda: self.Metric_conversion(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        if text == 'C':
            self.display.delete(0, 'end')
        elif text == '=':
            result = eval(self.display.get())
            self.display.delete(0, 'end')
            self.display.insert(0, result)
        else:
            self.display.insert('end', text)

    def Metric_conversion(self, text):
        if text == 'Mi-Km':
            mile = float(self.display.get())
            self.display.delete(0, 'end')
            result = round(mile * 1.609)
            self.display.insert(0, result)
        elif text == 'Km-Mi':
            Km = float(self.display.get())
            self.display.delete(0, 'end')
            result = round(Km * 0.621371)
            self.display.insert(0, result)
        elif text == 'Po-Kg':
            Po = float(self.display.get())
            self.display.delete(0, 'end')
            result = round(Po * 0.453592)
            self.display.insert(0, result)
        else:
            Kg = float(self.display.get())
            self.display.delete(0, 'end')
            result = round(Kg * 2.20462)
            self.display.insert(0, result)

