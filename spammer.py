import time
from tkinter import *
from pyautogui import typewrite, press

# def spam_messages(iters, str_to_spam="A"):
#   for _ in range(iters): typewrite(str_to_spam); press("enter")
#   # for _ in range(iters): print(str_to_spam)

def spam_messages():
  for _ in range(20): print("A")

def main():
  root = Tk()
  
  root['bg'] = '#2F353B'
  root.title('Spam root')
  root.geometry('300x250')
  root.resizable(width=False, height=False)

  # title = Label(root, text='Spamm application')
  # title.pack()

  # iter_entry = Entry(root)
  # iter_entry.pack()

  # str_entry = Entry(root)
  # str_entry.pack()

  # spam_button = Button(root, text="Spam", command=spam_messages)
  # spam_button.pack()

  root.mainloop()

if __name__ == "__main__":
  main()
