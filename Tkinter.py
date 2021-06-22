import tkinter
from tkinter.ttk import Combobox, Checkbutton, Radiobutton, Spinbox
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

def first_be_clicked():
    if text_field.get().isdigit() and not selected.get():
        text=  f'Result: {bin(int(text_field.get()))[2:] if choose.get() == "BIN" else oct(int(text_field.get()))[2:] if choose.get() == "OCT" else hex(int(text_field.get())).upper()[2:]}' if text_field.get().isdigit() else ''
        result_field.configure(text=text)
        scroll.insert(tkinter.INSERT, f"{text_field.get()}, {choose.get()} - {text} \n")
        return
    elif text_field.get().isdigit() and selected.get() == 1:
        alphabet, res = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', ''
        step, a, num = int(steps.get()), 0, int(text_field.get())
        while step ** (a + 1) <= num:
            a += 1
        while num:
            res += alphabet[num // step ** a]
            num %= step ** a
            a -= 1
        if len(res) <= a:
            res += '0'
        scroll.insert(tkinter.INSERT, f'Степ. счисл = {step}, результат = {res}\n')
        return

    messagebox.askquestion('Converter!\n', 'Неправильный формат')





def clicked():
    cur_chosen.configure(text=var2.get())

display = tkinter.Tk()
#display2 = tkinter.Tk()
display.title('Converter')
display.geometry('800x600')
sign = tkinter.Label(display, text='Converter', font=('Cambria', 50), fg='blue')
cur_chosen = tkinter.Label(display)
btn = tkinter.Button(display, text='Convert', fg='black', command=first_be_clicked)
var = tkinter.BooleanVar()
var.set(True)
selected = tkinter.IntVar()

var2 = tkinter.StringVar()
info =  Checkbutton(display, text='Выбрать', var=var)
radio1, radio2 = [Radiobutton(display, text=["Первый", "Второй", "Третий"][i], variable=selected, value=i, command=clicked) for i in range(2)]
scroll = ScrolledText(display, width=55, height=10)
scroll.insert(tkinter.INSERT, 'История запросов:\n')
text_field = tkinter.Entry(width=15)
result_field = tkinter.Label(text='Result')
choose = Combobox(display)
choose['values'] = ('BIN', 'OCT', 'HEX')
choose.current(0)
steps = Spinbox(display, from_=2, to=16)


sign.grid(column=0, row=0)
btn.place(x=300, y=80)
text_field.grid(column=0, row=1)
result_field.grid(column=0, row=2)
info.grid(column=1, row=2)
text_field.focus()
choose.grid(row=3)
radio1.grid(column=0, row=4)
radio2.place(x=340, y=150)
cur_chosen.grid(row=5)
scroll.grid(row=6)
steps.place(x=320, y=125)
display.mainloop()
#display2.mainloop()