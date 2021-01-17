import tkinter
from tkinter import Frame, Label, Entry, Button, Canvas
from PIL import ImageTk, Image
from random import randrange

# ===== Main window ===== #
root = tkinter.Tk()
root.title('Dice Rolling Simulator')
root.configure(background='#212529')
root.geometry('700x400')
root.resizable(False, False)

# ===== Functions ===== #
# 1. Helper
def empty_frame(frame):
    for widget in frame.winfo_children():
       widget.destroy()

def validation(input_):
    if input_.strip().isdigit() and int(input_) <= 3 and len(input_) == 1:
        return True
    else:
        # Remove previous error message
        empty_frame(frm_error_msg)
        lbl_msg = Label(master=frm_error_msg, text='Only number between 1 and 3 is allowed')
        lbl_msg.config(font=('Comic Sans MS', 9))
        lbl_msg.configure(background='#212529', foreground='#fff')
        lbl_msg.pack()
        return False

# 2. Game logic
def start_game(event):
    btn_start.pack_forget()
    empty_frame(frm_error_msg)
    
    try:
        dice_num = int(ent_dice_num.get())
    except ValueError:
        dice_num = 1
    
    for _ in range(dice_num):
        num = randrange(1, 7)
        img = Image.open('img/' + str(num) + '.png').resize((200, 200))
        filename = ImageTk.PhotoImage(img)
        
        canvas = Canvas(master=frm_dice, height=200, width=200, highlightthickness=0)
        canvas.image = filename
        canvas.configure(background='#212529')
        canvas.create_image(0, 0, anchor='nw', image=filename)
        canvas.pack(side='left')
    
    btn_repeat.pack(side='left', expand=True)
    
def repeat_game(event):
    # Remove previous dice
    empty_frame(frm_dice)
    return start_game(event)

def exit_game(event):
    root.destroy()

# ===== Widgets ===== #
# 1. Header
frm_header = Frame(master=root)
frm_header.configure(background='#212529')
frm_header.pack()

# 1.1 Dice number
frm_dice_num = Frame(master=frm_header, pady=10)
frm_dice_num.configure(background='#212529')
frm_dice_num.pack()

lbl_dice_num = Label(master=frm_dice_num, text='Number of dice (1-3)', padx=15)
lbl_dice_num.config(font=('Comic Sans MS', 13))
lbl_dice_num.configure(background='#212529', foreground='#fff')
lbl_dice_num.pack(side='left')

register = root.register(validation)
ent_dice_num = Entry(master=frm_dice_num, width=5, justify='center', relief='groove', borderwidth=2)
ent_dice_num.config(font=('Comic Sans MS', 11))
ent_dice_num.configure(background='#212529', foreground='#fff')
ent_dice_num.pack(side='right')
ent_dice_num.insert(0, 1)
ent_dice_num.config(validate='key', validatecommand=(register, '%S'))

# 1.2 Error message
frm_error_msg = Frame(master=frm_header, pady=15)
frm_error_msg.configure(background='#212529')
frm_error_msg.pack()

# 1.3 Start Button
btn_start = Button(text='Start', padx=10, borderwidth=0)
btn_start.config(font=('Comic Sans MS', 10))
btn_start.configure(background='#0d6efd', foreground='#fff')
btn_start.pack()
btn_start.bind('<Button-1>', start_game)

# 2. Body
frm_dice = Frame(master=root, height=200)
frm_dice.configure(background='#212529')
frm_dice.pack()

# 3. Footer
frm_footer = Frame(master=root)
frm_footer.configure(background='#212529')
frm_footer.pack()

btn_repeat = Button(text='Repeat (Enter)', padx=10, borderwidth=0)
btn_repeat.config(font=('Comic Sans MS', 10))
btn_repeat.configure(background='#198754', foreground='#fff')
btn_repeat.bind('<Button-1>', repeat_game)
root.bind('<Key-Return>', repeat_game)

btn_exit = Button(text='Exit (Esc)', padx=10, borderwidth=0)
btn_exit.config(font=('Comic Sans MS', 10))
btn_exit.configure(background='#dc3545', foreground='#fff')
btn_exit.pack(side='right', expand=True)
btn_exit.bind('<Button-1>', exit_game)
root.bind('<Escape>', exit_game)

# ===== Pop window up ===== #
root.mainloop()