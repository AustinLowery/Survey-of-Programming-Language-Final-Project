from tkinter import *


class View:

    class Window(Frame):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.master = master

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.value = None
        self.communicate = False
        self.root = Tk()

        self.res_entry = None
        self.cost_entry = None
        self.tax_entry = None
        self.tip_entry = None

    def update_result(self, value):
        self.res_entry.delete(0, END)
        self.res_entry.insert(0, value)

    def display_view(self):
        app = self.Window(self.root)

        cost_text = StringVar()
        cost_text = Label(self.root, text='Meal Cost:', font=('normal', 14), pady=20)
        cost_text.grid(row=0, column=0, sticky=W)
        self.cost_entry = Entry(self.root, textvariable=cost_text, width=self.width//33)
        self.cost_entry.grid(row=0, column=1, padx=10)

        tax_text = StringVar()
        tax_text = Label(self.root, text='Tax Amount:', font=('normal', 14), pady=20)
        tax_text.grid(row=0, column=2, sticky=W)
        self.tax_entry = Entry(self.root, textvariable=tax_text, width=self.width//33)
        self.tax_entry.grid(row=0, column=3, padx=10)

        tip_text = StringVar()
        tip_text = Label(self.root, text='Tip Amount:', font=('normal', 14), pady=20)
        tip_text.grid(row=0, column=4, sticky=W)
        self.tip_entry = Entry(self.root, textvariable=tip_text, width=self.width // 33)
        self.tip_entry.grid(row=0, column=5, padx=10)

        res_text = StringVar()
        res_text = Label(self.root, text='Result:', font=('normal', 14), pady=20)
        res_text.grid(row=1, column=0, sticky=W)
        self.res_entry = Entry(self.root, textvariable=res_text, width=self.width//33)
        self.res_entry.grid(row=1, column=1, padx=10)

        self.root.wm_title("Meal Cost Calculator")
        self.root.geometry(f'{self.width}x{self.height}')


if __name__ == "__main__":
    print("Please run the Meal Cost Controller.")
