from tkinter import *

class MyApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("My Page")
        self.geometry("800x800")
        
        self.v = StringVar()  # Create a StringVar for the Entry
        Entry(self, textvariable=self.v).pack()  # Entry widget
        
        # Labels for displaying text and reversed text
        self.label_normal = Label(self, text="")
        self.label_normal.pack()
        
        self.label_reversed = Label(self, text="")
        self.label_reversed.pack()
        
        # Trace the StringVar to call update_labels when it changes
        self.v.trace("w", self.update_labels)
    
    def update_labels(self, *args):
        # Get the current text and update the labels
        current_text = self.v.get()
        self.label_normal.config(text=current_text)
        self.label_reversed.config(text=current_text[::-1])

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()

