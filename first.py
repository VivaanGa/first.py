from tkinter import *

class MyApp(Tk):
  def __init__(self):
    super().__init__()
    self.title("My Page")
    self.geometry("800x800")
    self.v = StringVar()
    Entry(self, textvariable=self.v).pack()
    self.c = v.get()
    Label(self, text=self.c).pack()
    Label(self, text=self.c[::-1]).pack()
if __name__ == "__main__":
  app = MyApp()
  app.mainloop()
