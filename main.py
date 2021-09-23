from tkinter import *

root = Tk()
root.title('Essential Widget')
root.geometry('400x300+50+50')
root.overrideredirect(True)
root.wm_attributes('-transparentcolor','red')
root.config(bg='red')


image_bg= PhotoImage(file='bg_main.png')


Label_bg = Label(root, image = image_bg,bg='red')

Label_bg.pack()

root.bind('a', lambda event: root.destroy())


root.mainloop()