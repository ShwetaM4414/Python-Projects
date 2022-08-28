# import libraries

from socket import gaierror
from tkinter import *
from tkinter import messagebox, filedialog
from email.message import EmailMessage
import smtplib
import os
import imghdr

import pandas

# global variables are declared
global c, cr, emails1

# Initialising check as False
check = False


# Function for Browse Button
def Browse():

    # Open the filedailog box
    # Returns the complete path of the file that user have selected
    Path1 = filedialog.askopenfilename(initialdir='c:/', title='Select Excel File')

    # If there is no file
    if Path1 == '':
        # Show the error message
        messagebox.showerror('Error', 'Please Select an Excel File')

    else:
        # try except block is used to handle the error
        try:
            # Read excel file
            data = pandas.read_excel(Path1)

            # Checks if email is present in columns
            if 'Email' in data.columns:

                # Creates list to store the emails addresses
                emails = list(data['Email'])

                #  list is created for storing all the emails addresses
                emails1 = []
                for i in emails:

                    # Checks if emails address is present or not
                    if pandas.isnull(i) == False:
                        emails1.append(i)

            if len(emails1) == 0:
                # Show the error message
                messagebox.showerror('Error', 'File does not contain any email addresses')
            else:
                # Entry is used to input the single line text entry from the user
                toEntry.config(state='readonly')
                toEntry.config(state=NORMAL)

                # os.path.basename(Path1) give us the name of the file
                toEntry.insert(0, os.path.basename(Path1))
                total.config(text='Total: ' + str(len(emails1)))
                sent.config(text='Sent: ')
                left.config(text='Left: ')
                failed.config(text='Failed: ')

        except ValueError:
            # Show the error message
            messagebox.showerror('Error', 'File must be excle file')


# Function for the RadioButton
def button_check():

    # If user selected multiple RadioButton
    if a.get() == 'Multiple':

        # Makes state of browse button to normal
        browse.config(state=NORMAL)
        toEntry.config(state='readonly')

    # If user selected multiple RadioButton
    if a.get() == 'Single':

        # Makes state of browse button to normal
        browse.config(state=DISABLED)
        toEntry.config(state=NORMAL)


# Function for the Attachment Button
def Attachment():
    global name, type, Path, check
    check = True

    # Open the filedailog box
    # Returns the complete path of the file that user have selected
    Path = filedialog.askopenfilename(initialdir='c:/', title='Select File')

    # Splits the path on the basis of (.)
    type = Path.split('.')
    type = type[1]

    # give us the name of the file
    name = os.path.basename(Path)
    text.insert(END, f'\n{name}\n')


def SendingEmail(to1, sub1, body1):
    # Opens the file read format
    f = open('Settings.txt', 'r')
    for i in f:
        c = i.split(',')

    msg = EmailMessage()
    msg['subject'] = sub1
    msg['to'] = to1
    msg['from'] = c[0]
    msg.set_content(body1)

    # Checks if user selected the attachment or not
    if check:

        # If file type is image file
        if type == 'png' or type == 'jpg' or type == 'jpeg':

            # opens the file
            f = open(Path, 'rb')
            file_data = f.read()

            # Returns the type of the file
            subType = imghdr.what(Path)

            # Image added as an attachment
            msg.add_attachment(file_data, maintype='image', subtype=subType, filename=name)

        else:
            # opens the file
            f = open(Path, 'rb')
            file_data = f.read()
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=name)

    # try except block is used to handle the error
    try:
        # Create object of SMTP class
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # Secure the connection between the client and the server
        s.starttls()

        # Login to gmail using the credentials stored in the Settings.txt file
        # At index 0 we have from email address and at index 1 we have password
        s.login(c[0], c[1])

        s.send_message(msg)

        y = s.ehlo()
        if y[0] == 250:
            return 'sent'
        else:
            return 'failed'

    except gaierror:
        # Show the error message
        messagebox.showerror('Error', 'You are Offline')
    except:
        # Show the error message
        messagebox.showerror('Error', 'Wrong Email Address')


# Function for Send button
def SendEmail():

    # Checks if the fields are empty or not
    if toEntry.get() == '' or SubjectEntry.get() == '' or text.get(1.0, END) == '\n':

        # Show error message
        messagebox.showerror('Error', 'All fields are required', parent=root)

    else:
        # Condition to check if single RadioButton selected or not
        if a.get() == 'Single':
            result = SendingEmail(toEntry.get(), SubjectEntry.get(), text.get(1.0, END))

            # Condition for mail sent successfully
            if result == 'sent':
                # Show the info message
                messagebox.showinfo('Success', 'Email is sent Successfully')

            # Condition for sending of mail failed
            if result == 'failed':
                # Show the error message
                messagebox.showerror('Error', 'Email is not Sent')

        # Condition to check if Multiple RadioButton selected or not
        if a.get() == 'Multiple':

            # Keep a count on how many emails are sent
            SentVar = 0

            # Keep a count on how many emails are failed
            FailedVar = 0

            # It will iterate through all the email addresses in the list one by one
            for x in emails1:

                result = SendingEmail(x, SubjectEntry.get(), text.get(1.0, END))

                # Condition for mail sent successfully
                if result == 'sent':

                    # Increase count of SentVar by 1
                    SentVar += 1

                # Condition for sending of mail failed
                if result == 'failed':

                    # Increase count of FailedVar by 1
                    FailedVar += 1

                total.config(text='')
                sent.config(text='Sent : ' + str(SentVar))
                left.config(text='Left : ' + str(len(emails1) - (SentVar + FailedVar)))
                failed.config(text='Failed : ' + str(FailedVar))

                # Updating the labels
                total.update()
                sent.update()
                left.update()
                failed.update()

            # Show info message
            messagebox.showinfo('Success', 'Emails are sent Successfully')


# Function for Account Credential Button
def Settings():

    # Funcrion for Clear Button
    def Clear1():

        # Delete everything from entry field and Password entry field
        FromEntry.delete(0, END)
        PasswordEntry.delete(0, END)

    # Function for Save Button
    def Save():

        # If there is nothing in the From entry field or Password entry field
        if FromEntry.get() == '' or PasswordEntry.get() == '':

            # Show error message
            messagebox.showerror('Error', 'All fields are Required', parent=root1)

        else:
            # opens the file in write format
            f = open('Settings.txt', 'w')
            f.write(FromEntry.get() + ',' + PasswordEntry.get())
            f.close()

            # show info message
            messagebox.showinfo('Information', 'Credential Saves Successfully', parent=root1)

    # Creates a window on top of another window
    root1 = Toplevel()

    # set the title of GUI window
    root1.title('Setting')

    # Set a height and width to the window
    root1.geometry('650x340+350+90')

    # Set the background color
    root1.config(bg='light grey')

    # create a label : Credential Settings
    # grid method is used for placing the widgets at respective positions in table like structure
    Label(root1, text='  Credential Settings', image=logoImage, compound=LEFT, font=('Goudy Old Style', 20, 'bold'),
          fg='Black', bg='light grey').grid(padx=200, pady=20)

    # Frame is a type of box within which a collection of graphical control elements can be grouped
    FromlabelFrame = LabelFrame(root1)
    FromlabelFrame.grid(row=1, column=0, padx=50)

    # create a label : From (Email Address)
    Label(FromlabelFrame, text="From (Email Address) : ", height=2, font=('Goudy Old Style', 15, 'bold'), bd='5',
          fg='black', bg='light grey').grid(row=1, column=0, sticky=W)

    # adding Entry Field
    FromEntry = Entry(FromlabelFrame, font=('Goudy Old Style', 15), width=30)
    FromEntry.grid(row=1, column=1)

    PasswordlabelFrame = LabelFrame(root1)
    PasswordlabelFrame.grid(row=2, column=0, padx=50, pady=30)

    # create a label : Password
    Label(PasswordlabelFrame, text="Password : ", height=2, font=('Goudy Old Style', 15, 'bold'), bd='5',
          fg='black', bg='light grey').grid(row=2, column=0, sticky=W)

    # adding Entry Field
    PasswordEntry = Entry(PasswordlabelFrame, font=('Goudy Old Style', 15), width=30, show='*')
    PasswordEntry.grid(row=2, column=1)

    # Creates button widget
    Button(root1, text='Save', font=('Goudy Old Style', 15, 'bold'), cursor='hand2', activeforeground='black',
           activebackground='gold2', width=12, fg='Dark slate gray', command=Save).place(x=190, y=280)

    # Creates button widget
    Button(root1, text='Clear', font=('Goudy Old Style', 15, 'bold'), cursor='hand2', activeforeground='black',
           activebackground='wheat4', width=12, fg='Dark slate gray', command=Clear1).place(x=370, y=280)

    # Opens the Settings.txt file in read format
    f = open('Settings.txt', 'r')
    for i in f:
        cr = i.split(',')

    # Inserts email address in From Entry field
    FromEntry.insert(0, cr[0])

    # Inserts password in Password Entry field
    PasswordEntry.insert(0, cr[1])

    # Keep a window on loop
    root1.mainloop()


# Function for exit Button
def Exit():

    # returns true or false
    res = messagebox.askyesno('Notification', 'Do you want to exit?')

    if res:
        # Close the window
        root.destroy()
    else:
        pass


# Function for Clear Button
def Clear():
    # Delete everything from to field ,subject entry field and text field
    toEntry.delete(0, END)
    SubjectEntry.delete(0, END)
    text.delete(1.0, END)


# create a window
root = Tk()

# set the title of GUI window
root.title('Send Email')

# Set a height and width to the window
root.geometry('800x690+100+50')

root.resizable(0, 0)

# Set the background color
root.config(bg='light grey')

# Frame is a type of box within which a collection of graphical control elements can be grouped
# grid method is used for placing the widgets at respective positions in table like structure
TitleFrame = Frame(root, bg='white')
TitleFrame.grid(row=0, column=0, pady=10)
logoImage = PhotoImage(file='email.png')

# Create a label : Email Sender
TitleLabel = Label(TitleFrame, text='  Email Sender', image=logoImage, compound=LEFT,
                   font=('Goudy Old Style', 24, 'bold'), bg='white', fg='DodgerBlue4')
TitleLabel.grid(row=0, column=0)

ChooseFrame = Frame(root)
ChooseFrame.grid(row=1, column=0)
a = StringVar()

# Create a Radio Button
RadioButton1 = Radiobutton(ChooseFrame, text='Single', font=('Goudy Old Style', 20, 'bold'), pady=8
                           , variable=a, value='Single', bg='light grey', padx=20, activebackgroun='light grey'
                           , command=button_check)
RadioButton1.grid(row=1, column=0)
RadioButton2 = Radiobutton(ChooseFrame, text='Multiple', font=('Goudy Old Style', 20, 'bold')
                           , variable=a, value='Multiple', bg='light grey', padx=20, pady=8,
                           activebackground='light grey', command=button_check)
RadioButton2.grid(row=1, column=1)
a.set('Single')

# Create a Button widget and calls the Settings function
Button(text='Account Credentials', bd=0, bg='white', fg='Dark slate gray', font=('Goudy Old Style', 20, 'bold'),
       activeforeground='black', activebackground='wheat4', cursor='hand2', height='1',
       width='16', command=Settings).grid(pady=10)

TolabelFrame = LabelFrame(root)
TolabelFrame.grid(row=3, column=0, padx=100, pady=10)

# Create a Label : To (Email Address)
Label(TolabelFrame, text="To (Email Address) : ", height=2, font=('Goudy Old Style', 15, 'bold'), bd='5', fg='black',
      bg='light grey').grid(row=0, column=0, sticky=W)

# adding Entry Field
toEntry = Entry(TolabelFrame, font=('Goudy Old Style', 15), width=30)
toEntry.grid(row=0, column=1)

# Create a Button widget and calls the Browse function
browse = Button(TolabelFrame, text='Browse', font=('Goudy Old Style', 15, 'bold'), cursor='hand2', bg='white', bd=0,
                activeforeground='black', activebackground='wheat4', fg='Dark slate gray', state=DISABLED,
                command=Browse)
browse.grid(row=0, column=2, padx=20)

SubjectlabelFrame = LabelFrame(root)
SubjectlabelFrame.grid(row=4, column=0, padx=100, pady=10)

# Create a Label : Subject
Label(SubjectlabelFrame, text="Subject : ", height=2, font=('Goudy Old Style', 15, 'bold'), bd='5', fg='black',
      bg='light grey').grid(row=1, column=0, sticky=W)

# Adding Entry field
SubjectEntry = Entry(SubjectlabelFrame, font=('Goudy Old Style', 15), width=35)
SubjectEntry.grid(row=1, column=1)

BodyFrame = LabelFrame(root)
BodyFrame.grid(row=5, column=0, padx=100, pady=10)

# Create a label : Body
Label(BodyFrame, text="Body : ", height=1, font=('Goudy Old Style', 15, 'bold'), bd='5', fg='black',
      bg='light grey').grid(row=0, column=0, sticky=W)

attachImage = PhotoImage(file='attachment.png')

# Create Button widget and calls the Attachment function
Button(BodyFrame, text='Attachment', image=attachImage, compound=LEFT, font=('Goudy Old Style', 15, 'bold'),
       cursor='hand2', bd=0, bg='white', fg='Dark slate gray', activeforeground='black',
       activebackground='wheat4', command=Attachment).grid(row=0, column=1)

# For multi-line text input, Text widget is used
text = Text(BodyFrame, font=('Goudy Old Style', 14), height=7, width=45)
text.grid(row=1, column=0)

# Create Button widget and calls the SendEmail function
Button(root, text='Send', bd=0, bg='white', fg='Dark slate gray', font=('Goudy Old Style', 15, 'bold'),
       activeforeground='black', activebackground='wheat4', cursor='hand2', height='1',
       width='10', command=SendEmail).place(x=380, y=610)

# Create Button widget and calls the Clear function
Button(root, text='Clear', bd=0, bg='white', fg='Dark slate gray', font=('Goudy Old Style', 15, 'bold'),
       activeforeground='black', activebackground='wheat4', cursor='hand2', height='1',
       width='10', command=Clear).place(x=520, y=610)

# Create Button widget and calls the Exit function
Button(root, text='Exit', bd=0, bg='white', fg='Dark slate gray', font=('Goudy Old Style', 15, 'bold'),
       activeforeground='white', activebackground='red', cursor='hand2', height='1',
       width='10', command=Exit).place(x=660, y=610)


total = Label(root, font=('Goudy Old Style', 13, 'bold'), bg='light grey', fg='black')
total.place(x=10, y=610)

sent = Label(root, font=('Goudy Old Style', 13, 'bold'), bg='light grey', fg='black')
sent.place(x=90, y=610)

left = Label(root, font=('Goudy Old Style', 13, 'bold'), bg='light grey', fg='black')
left.place(x=170, y=610)

failed = Label(root, font=('Goudy Old Style', 13, 'bold'), bg='light grey', fg='black')
failed.place(x=240, y=610)

root.mainloop()
