from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

root = Tk()
root.geometry('500x660')
root.title("Mail Application using GUI")
Label_0 = Label(root, text="Enter your account details", width=20, fg="blue", font=("bold", 20))
Label_0.place(x=90, y=33)
Label_1 = Label(root, text="Your Email ID:", width=20, font=("bold", 10))
Label_1.place(x=40, y=110)

# for getting entry input
mail = StringVar()
pswrd = StringVar()
sender = StringVar()
subject = StringVar()

email = Entry(root, width=40, textvariable=mail)
email.place(x=200, y=110)
Label_2 = Label(root, text="Your Password:", width=20, font=("bold", 10))
Label_2.place(x=40, y=160)
password = Entry(root, width=40, show="*", textvariable=pswrd)
password.place(x=200, y=160)
compose = Label(root, text="Compose", width=20, fg='green', font=("bold", 15))
compose.place(x=180, y=210)
Label_3 = Label(root, text="Send to Email ID:", width=20, font=("bold", 10))
Label_3.place(x=40, y=260)
sender = Entry(root, width=40, textvariable=sender)
sender.place(x=200, y=260)
Label_4 = Label(root, text="Subject:", width=20, font=("bold", 10))
Label_4.place(x=40, y=310)
subject = Entry(root, width=40, textvariable=subject)
subject.place(x=200, y=310)
Label_5 = Label(root, text="Message:", width=20, font=("bold", 10))
Label_5.place(x=40, y=360)
msgbody = Text(root, width=30, height=10)
msgbody.place(x=200, y=360)
Label_7 = Label(root, width=80, font=("bold", 10))
Label_7.place(x=10, y=620)


def sendemail():

    try:
        mymsg = MIMEMultipart()
        mymsg['From'] = str(mail.get())
        mymsg['To'] = str(sender.get())
        mymsg['Subject'] = str(subject.get())
        mymsg.attach(MIMEText(msgbody.get(1.0, 'end'), 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(str(mail.get()), str(pswrd.get()))
        text = mymsg.as_string()
        server.sendmail(str(mail.get()), str(sender.get()), text)
        Label_6 = Label(root, text="Done!", width=20, fg='green', font=("bold", 15))
        Label_6.place(x=140, y=550)
        server.quit()
    except:
        Label_6 = Label(root, text="something went wrong!", width=20, fg='red', font=("bold", 15))
        Label_6.place(x=140, y=550)


Button(root, text="Send", width=20, bg='brown', fg="white", command=sendemail).place(x=180, y=590)

root.mainloop()