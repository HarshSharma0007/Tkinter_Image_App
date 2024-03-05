from tkinter import *
from PIL import ImageTk,Image
import os

# creating the counter.
counter =1

#defining a function for next button.
def rotate_img():
    global counter
    #use simple mechanism
    img_label.config(image=img_array[counter%len(img_array)])
    counter +=1

# creating the window.
root = Tk()

# Naming the window.
root.title("MY_MASKS")

# Making geometry of the window.
root.geometry("500x550")

# Making the window fixed (So that no one can resize it.)
root.resizable(0,0)

# let background colour be black (^-^)
root.config(background="black")

# importing the list 
files = os.listdir("MaskImg")

# creating the array for display
img_array = [] 
for file in files:
    # for the imported images, making their geometry fit to the window. 
    img = Image.open(os.path.join("MaskImg",file))
    resized_image = img.resize((450,450))
    img_array.append(ImageTk.PhotoImage(resized_image))

img_label = Label(root,image=img_array[0])
img_label.pack(pady=(15,10))

# creating next button.
next_btn = Button(root,text="NEXT",fg='black',bg='white',height=2,width=28,command=rotate_img)
next_btn.pack()


root.mainloop()