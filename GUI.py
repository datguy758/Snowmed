from tkinter import *
from tkinter.ttk import Frame, Button, Label, Style
from SnomedNLP import NLPFunc
from filter import filtering


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Reading in information
        leveling, children, parent = filtering()

        # From NLP
        NLP = NLPFunc()

        self.master.title("SNOMED")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(2, weight=1)
        self.rowconfigure(4, weight=1)

        # Parent
        parlab = Label(self, text="Parents", justify=LEFT)
        parlab.grid(row=0, column=0, sticky=W)
        par = Text(self, height=5, width=35)
        par.grid(row=1, column=0, columnspan=3)

        # Search bar
        sealab = Label(self, text="Search", justify=LEFT)
        sealab.grid(row=2, column=0, sticky=W)
        search = Text(self, width=20, height=1)
        search.grid(row=3, column=0)
        abtn = Button(self, text="Search", width=10, command=lambda: set_text())
        abtn.grid(row=3, column=1)

        # Level
        level = Text(self, width=5, height=1)
        level.grid(row=3, column=2)

        # Definition
        deflab = Label(self, text="Definition", justify=LEFT)
        deflab.grid(row=0, column=3, sticky=W)
        area = Text(self, width=20, height=21)
        area.grid(row=1, column=3, rowspan=5, padx=5)

        # Children
        sealab = Label(self, text="Children", justify=LEFT)
        sealab.grid(row=4, column=0, sticky=W)
        kid = Text(self, height=5, width=35)
        kid.grid(row=5, column=0, columnspan=3)

        def set_text():
            # Getting ID
            text = search.get('1.0', END)

            # Setting Parent
            try:
                par.delete('1.0', END)
                par.insert('1.0', parent[int(text)])
            except:
                pass

            # Setting Level
            try:
                level.delete('1.0', END)
                level.insert('1.0', leveling[int(text)])
            except:
                pass

            # Setting Child
            try:
                kid.delete('1.0', END)
                kid.insert('1.0', children[int(text)])
            except:
                pass

            # Setting Definiation
            try:
                area.delete('1.0', END)
                area.insert('1.0', NLP[int(text)])
            except:
                pass

def main():
    root = Tk()
    root.maxsize(450, 250)
    root.minsize(450, 250)
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
