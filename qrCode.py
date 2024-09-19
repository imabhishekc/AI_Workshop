import qrcode
from tkinter import *
from tkinter import messagebox

# Creating the window
wn = Tk()
wn.title('My QR Code Generator')
wn.geometry('700x700')  # Adjusted window size
wn.config(bg='SteelBlue3')

# Function to generate QR code and save it
def generateCode():
    qr = qrcode.QRCode(version=size.get(), box_size=10, border=5)
    qr.add_data(text.get())
    qr.make(fit=True)
    img = qr.make_image()
    fileDirec = loc.get() + '\\' + name.get()
    img.save(f'{fileDirec}.png')
    messagebox.showinfo("QR Code Generator", "QR code is saved successfully!")

# Label for the window
headingFrame = Frame(wn, bg="azure", bd=5)
headingFrame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)
headingLabel = Label(headingFrame, text="Generate QR code!", bg="azure", font=('Times', 16, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

# Input for the text/URL to generate QR code
Frame1 = Frame(wn, bg="SteelBlue3")
Frame1.place(relx=0.1, rely=0.18, relwidth=0.8, relheight=0.15)
label1 = Label(Frame1, text="Enter the text/URL:", bg="SteelBlue3", fg='azure', font=('Times', 14, 'bold'))
label1.place(relx=0.05, rely=0.2, relheight=0.3)
text = Entry(Frame1, font=('Century', 12))
text.place(relx=0.05, rely=0.6, relwidth=0.9, relheight=0.3)

# Input for the location to save QR code
Frame2 = Frame(wn, bg="SteelBlue3")
Frame2.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.15)
label2 = Label(Frame2, text="Enter save location:", bg="SteelBlue3", fg='azure', font=('Times', 14, 'bold'))
label2.place(relx=0.05, rely=0.2, relheight=0.3)
loc = Entry(Frame2, font=('Century', 12))
loc.place(relx=0.05, rely=0.6, relwidth=0.9, relheight=0.3)

# Input for the name of the QR code image
Frame3 = Frame(wn, bg="SteelBlue3")
Frame3.place(relx=0.1, rely=0.52, relwidth=0.8, relheight=0.15)
label3 = Label(Frame3, text="Enter the name:", bg="SteelBlue3", fg='azure', font=('Times', 14, 'bold'))
label3.place(relx=0.05, rely=0.2, relheight=0.3)
name = Entry(Frame3, font=('Century', 12))
name.place(relx=0.05, rely=0.6, relwidth=0.9, relheight=0.3)

# Input for the size of the QR code
Frame4 = Frame(wn, bg="SteelBlue3")
Frame4.place(relx=0.1, rely=0.69, relwidth=0.8, relheight=0.15)
label4 = Label(Frame4, text="Enter size (1-40):", bg="SteelBlue3", fg='azure', font=('Times', 14, 'bold'))
label4.place(relx=0.05, rely=0.2, relheight=0.3)
size = Spinbox(Frame4, from_=1, to=40, font=('Century', 12))
size.place(relx=0.05, rely=0.6, relwidth=0.3, relheight=0.3)

# Button to generate and save the QR code
button = Button(wn, text='Generate Code', font=('Courier', 14), command=generateCode)
button.place(relx=0.35, rely=0.88, relwidth=0.3, relheight=0.08)

# Runs the window till it is closed manually
wn.mainloop()
