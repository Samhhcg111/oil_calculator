import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.font_manager as fm
import random
import os
import inspect
import matplotlib.pyplot as plt

class PieChart(tk.Frame):
    def __init__(self, master,database, title):
        super().__init__(master)
        path = os.path.abspath(inspect.getfile(PieChart))
        path = os.path.join(os.path.dirname(path), "HanyiSentyPagoda.ttf")
        self.fontprop = fm.FontProperties(fname=path)
        # while True:
        #     pass
        # Create a Figure object and add a subplot
        self.figure = Figure(figsize=(4, 4))
        self.subplot = self.figure.add_subplot(111)
        self.database = database
        self.old_datadict_len = 0
        self.title=title
        # Set the title of the chart
        self.subplot.set_title(title,fontproperties=self.fontprop)

        # Create a canvas to display the chart
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack()
        
        self.safety_label = tk.Label(self, text=str(f"最終稀釋濃度0%"))
        self.safety_label.pack()
        self.colors = []
        for i in range(len(self.database.get_piechart_data())):
            self.colors.append('#{:06x}'.format(random.randint(0, 256**3-1)))

        # Start catpure
        self.update_data()

    def update_data(self):
        new_data=self.database.get_piechart_data()
        if len(new_data) !=0:
            if(self.old_datadict_len != len(new_data)):
                self.old_datadict_len=len(new_data)
                self.colors = []
                for i in range(len(new_data)):
                    self.colors.append('#{:06x}'.format(random.randint(0, 256**3-1)))

            # Extract the labels and percentages from the new data dictionary
            new_labels = list(new_data.keys())
            new_percentages = list(new_data.values())

            # Update the chart with the new data and colors, and display the labels and percentages
            self.subplot.clear()
            self.pie, self.texts, self.autotexts = self.subplot.pie(new_percentages, colors=self.colors, autopct='%.0f%%')
            ax = self.subplot
            ax.legend(new_labels,prop=self.fontprop)
            self.subplot.set_title(self.title,fontproperties=self.fontprop)
            safetyConcentration = self.database.getSafetyConcentration()
            self.safety_label.config(text=str(f"最終稀釋濃度{safetyConcentration}%"))
            self.canvas.draw()
        self.after(500,self.update_data)
