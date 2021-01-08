import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import _flatten
import PIL
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np



def tracer(event, canvas):
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    id = canvas.create_line(X, Y, event.x+1, event.y+1, fill='black', width = 30, capstyle="round")
    canvas.bind('<Control-Button1-Motion>', lambda event: deplacement(event, id, canvas))
 
 
def deplacement(event, id, canvas):
    coordonné = canvas.coords(id)
    coordonné.append(event.x+1)
    coordonné.append(event.y+1)
    canvas.coords(id, _flatten(coordonné))


def test():
    canvas.postscript(file='image.eps')
    image = PIL.Image.open('image.eps')
    image.save('image.png', 'png')
    image = cv2.imread('image.png',0)
    image = cv2.bitwise_not(image)
    image = cv2.resize(image, (28, 28))
    image = image.reshape(-1, 28, 28, 1)
    image = tf.keras.utils.normalize(image)
    prediction = model.predict(image)
    prediction = np.argmax(prediction, axis=1)[0]
    display_label.config(text=str(prediction))



 
def reset(event):
    old_x, old_y = None, None

def clear():
    canvas.delete("all")
    display_label.config(text='  ')

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=480, bg='white')
canvas.bind('<Control-1>', lambda event: tracer(event, canvas))
canvas.grid(row=0, columnspan=3, pady=10, padx=10)

model = tf.keras.models.load_model('mnist_model')

reset = tk.Button(root, text='tester', command = test)
reset.grid(row=1, column=0, pady=10)

reset = tk.Button(root, text='Reset', command = clear)
reset.grid(row=1, column=2, pady=10)

display_label = tk.Label(root, text='   ', font=("Helvetica", 20))
display_label.grid(row=1, column=1, pady=(0, 10))


root.mainloop()