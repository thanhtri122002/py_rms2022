from tkinter import *

def click():
    entered_text = textbox.get().lower() # this will collect the text from the text entry box
    output.delete(0.0, END)
    result = []

    count = 0
    for i in menu:
        if entered_text in i.lower():
            result.append(i)
            count += 1
    if count == 0:
        result.append('Cannot find that dish in menu!')

    for i in result:
        output.insert(END, i + '\n')
    # output.insert(END, result)

# main
window = Tk()
window.title('Restautant Management Application')
window.config(background='#ffffff')
window.geometry('420x420')
window.resizable(FALSE, FALSE)

# label
Label(window, text='Thầy Sơn ăn gì', font='none 12').grid(row=0, column=0, sticky=W)

# text entry box
textbox = Entry(window, width=20, bg='#dddddd', fg='black')
textbox.grid(row=1, column=0, sticky=W)

# submit button
Button(window, text='Oge!', width=6, command=click).grid(row=2, column=0, sticky=W)

# label another text box but output
Label(window, text='\nRéult', bg='white', font='none 12 bold').grid(row=3, column=0, sticky=W)

# text output box
output = Text(window, width=50, height=6, wrap=WORD)
output.grid(row=5, column=0, columnspan=2, sticky=W)

# menu
menu = ['Phở bòa tái', 'Phở gà', 'Phở các thứ', 'Phở bòa chín']

# exit label
Label(window, text='Ấn ấn cái nút dưới này để cái này này trở về nhà nhà', bg='white', font='none 9').grid(row=6, column=0, sticky=W)

# exit button
Button(window, text='Back', width=6, command=window.destroy, font='none 9').grid(row=7, column=0, sticky=W)

# main
window.mainloop()
