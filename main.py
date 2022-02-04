from tkinter import*
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

def sendASMS():
  from textmagic.rest import TextmagicRestClient
  mescontent = "Stay Calm Help is On the Way"
  username = "nikolauskeil"
  token = "VbFSW16jtejBwK5TgabVa6uUvXNCZa"
  client = TextmagicRestClient(username, token)
  message = client.messages.create(phones="13306146590", text=mescontent)


def sendSMS():
  from textmagic.rest import TextmagicRestClient
  mescontent = "Stay Calm Help is On the Way"
  username = "nikolauskeil"
  token = "VbFSW16jtejBwK5TgabVa6uUvXNCZa"
  client = TextmagicRestClient(username, token)
  message = client.messages.create(phones="13305060403", text=mescontent)


ttk.Label(frm, text="ZOMBIES! HELP!").grid(column=0, row=1)
ttk.Button(frm, text="Send Request for Nikolaus", command=sendSMS).grid(column=0, row=2)
ttk.Button(frm, text="Send Request for Aaron", command=sendASMS).grid(column=0, row=3)
ttk.Button(frm, text="Cancel", command=root.destroy).grid(column=0, row=4)

root.mainloop()