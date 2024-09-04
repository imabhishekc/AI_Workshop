#Importing modules
from textblob import TextBlob
from tkinter import *

#Function to check the spelling and show the correct spelling
def checkSpelling():
    a = text.get() #Getting the word user entered
    b = TextBlob(a) #Getting the object for the word
    correctedText.set("The corrected word is: " +str(b.correct())) #showing the correct

#Creating the window
wn = Tk()
wn.title("My spell checker")
wn.geometry('1100x1100')
wn.config(bg='SlateGray1') 

#Creating the variables to get the word and set the correct word
text = StringVar(wn)

correctedText = StringVar(wn)

#The main label
Label(wn, text='My Spell Checker', bg='SlateGray1',
      fg='gray30', font=('Times', 20, 'bold')).place(x=100, y=10)

#Getting the input of word from the user
Label(wn, text='Please enter the word', bg='SlateGray1', font=('Calibre', 13, 'normal'), anchor="e", justify=LEFT).place(x=20, y=70)

Entry(wn, textvariable=text, width=35, font=('Calibre', 13, 'normal')).place(x=20,y=110)

#Label to show the correct word
opLabel = Label(wn, textvariable=correctedText, bg='SlateGray1', anchor="e", font=('Calibre', 13, 'normal'), justify=LEFT).place(x=20, y=130)

#Button to do the spell check
Button(wn, text="Click Me", bg='SlateGray4', font=('calibre', 13), command=checkSpelling).place(x=230, y=190)

#Runs the window till it is closed by the user
wn.mainloop()