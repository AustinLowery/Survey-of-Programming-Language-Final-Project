import MealCostModel
import MealCostView
from tkinter import *

taxModel = MealCostModel.Model()
taxView = MealCostView.View(1100, 367)

taxView.display_view()


def result_update():
    try:
        taxModel.cost = float(taxView.cost_entry.get())
        taxModel.tax = float(taxView.tax_entry.get())
        taxModel.tip = float(taxView.tip_entry.get())
        taxView.update_result(taxModel.compute_total())
    except ValueError:
        taxView.update_result("Invalid Value")


# button input needed here to access model
exp_button = Button(taxView.root, text="Calculate", width=12, command=result_update)
exp_button.grid(row=0, column=6, padx=10)

taxView.root.mainloop()
