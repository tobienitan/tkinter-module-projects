''' This program does simple arithmetric and some metric conversion
    note the following:
    Km-Mi means kilometer to miles conversion
    Mi-Km means miles to Kilometer conversion
    Kg-Po means Kilogram to Pound conversion
    Po-Kg means Pound to Kilogram conversion
    all conversions are done to the nearest whole numbers
    '''


from tkinter import *
from calculator_design import Calculator

window = Tk()
calculator = Calculator(window)
window.mainloop()