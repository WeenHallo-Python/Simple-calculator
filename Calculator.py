from tkinter import *

window = Tk()
window.title("Calculator")

number = 0

previous_number = 0

action = '+'


def make_action(chosen_action):
    global number
    global previous_number
    global action


    action = chosen_action

    previous_number = number

    number = 0

    entry_text.set(str(number))


def button_press_add():
    make_action('+')

def button_press_substract():
    make_action('-')

def button_press_multiply():
    make_action('*')

def button_press_divide():
    make_action('/')

def button_press_stepen():
    make_action('^x')

def button_press_mkm():
    make_action('M=km')

def button_press_mcm():
    make_action('M=cm')

def button_press_mmm():
    make_action('M=mm')

def button_press_kmm():
    make_action('KM=m')

def button_press_kmcm():
    make_action('KM=cm')

def button_press_kmmm():
    make_action('KM=mm')

def button_press_cmkm():
    make_action('CM=km')

def button_press_cmm():
    make_action('CM=m')

def button_press_cmmm():
    make_action('CM=mm')

def button_press_mmkm():
    make_action('MM=km')

def button_press_mmvm():
    make_action('MM=m')

def button_press_mmcm():
    make_action('MM=cm')


#AC
def button_press_clear():
    global number
    global previous_number

    number = 0
    previous_number = 0

    entry_text.set(number)

def button_press_result():
    global number
    global previous_number
    global action

    if action == '+':
        number = previous_number + number
    elif action == '-':
        number = previous_number - number
    elif action == '*':
        number = previous_number * number
    elif action == '/':
        number = previous_number / number
    elif action == '^x':
        number = previous_number ** number
    elif action == 'M=km':
        number = previous_number / 1000
    elif action == 'M=cm':
        number = previous_number * 100
    elif action == 'M=mm':
        number = previous_number * 1000
    elif action == 'KM=m':
        number = previous_number * 1000
    elif action == 'KM=cm':
        number = previous_number * 100000
    elif action == 'KM=mm':
        number = previous_number * 1e+6
    elif action == 'CM=km':
        number = previous_number / 100000
    elif action == 'CM=m':
        number = previous_number / 100
    elif action == 'CM=mm':
        number = previous_number * 10
    elif action == 'MM=km':
        number = previous_number / 1e+6
    elif action == 'MM=m':
        number = previous_number / 1000
    elif action == 'MM=cm':
        number = previous_number / 10


    entry_text.set(number)

def add_digit(digit):
    global number


    number = number * 10 + digit


    entry_text.set(number)

def button_press_1():
    add_digit(1)

def button_press_2():
    add_digit(2)

def button_press_3():
    add_digit(3)

def button_press_4():
    add_digit(4)

def button_press_5():
    add_digit(5)

def button_press_6():
    add_digit(6)

def button_press_7():
    add_digit(7)

def button_press_8():
    add_digit(8)

def button_press_9():
    add_digit(9)

def button_press_0():
    add_digit(0)

Button(window, text='7', height=5, width=10, command=button_press_7).grid(row=1, column=0)
Button(window, text='8', height=5, width=10, command=button_press_8).grid(row=1, column=1)
Button(window, text='9', height=5, width=10, command=button_press_9).grid(row=1, column=2)
Button(window, text='4', height=5, width=10, command=button_press_4).grid(row=2, column=0)
Button(window, text='5', height=5, width=10, command=button_press_5).grid(row=2, column=1)
Button(window, text='6', height=5, width=10, command=button_press_6).grid(row=2, column=2)
Button(window, text='1', height=5, width=10, command=button_press_1).grid(row=3, column=0)
Button(window, text='2', height=5, width=10, command=button_press_2).grid(row=3, column=1)
Button(window, text='3', height=5, width=10, command=button_press_3).grid(row=3, column=2)
Button(window, text='=', height=5, width=10, command=button_press_result).grid(row=4, column=0)
Button(window, text='0', height=5, width=10, command=button_press_0).grid(row=4, column=1)
Button(window, text='AC', height=5, width=10, command=button_press_clear).grid(row=4, column=2)
Button(window, text='^x', height=5, width=10, command=button_press_stepen).grid(row=1, column=4)

Button(window, text='M=km', height=5, width=10, command=button_press_mkm).grid(row=5, column=2)
Button(window, text='M=cm', height=5, width=10, command=button_press_mcm).grid(row=5, column=1)
Button(window, text='M=mm', height=5, width=10, command=button_press_mmm).grid(row=5, column=0)
Button(window, text='KM=m', height=5, width=10, command=button_press_kmm).grid(row=6, column=0)
Button(window, text='KM=cm', height=5, width=10, command=button_press_kmcm).grid(row=6, column=1)
Button(window, text='KM=mm', height=5, width=10, command=button_press_kmmm).grid(row=6, column=2)
Button(window, text='CM=km', height=5, width=10, command=button_press_cmkm).grid(row=7, column=0)
Button(window, text='CM=m', height=5, width=10, command=button_press_cmm).grid(row=7, column=1)
Button(window, text='CM=mm', height=5, width=10, command=button_press_cmmm).grid(row=7, column=2)
Button(window, text='MM=km', height=5, width=10, command=button_press_mmkm).grid(row=8, column=0)
Button(window, text='MM=m', height=5, width=10, command=button_press_mmvm).grid(row=8, column=1)
Button(window, text='MM=cm', height=5, width=10, command=button_press_mmcm).grid(row=8, column=2)

Button(window, text='+', height=5, width=10, command=button_press_add).grid(row=1, column=3)
Button(window, text='-', height=5, width=10, command=button_press_substract).grid(row=2, column=3)
Button(window, text='*', height=5, width=10, command=button_press_multiply).grid(row=3, column=3)
Button(window, text='/', height=5, width=10, command=button_press_divide).grid(row=4, column=3)

entry_text = StringVar()
Entry(window, width=40, textvariable=entry_text).grid(row=0, column=0, columnspan=4)

mainloop()
