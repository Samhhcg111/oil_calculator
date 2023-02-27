import tkinter as tk
from lib.OilDatalist import OilDataList
from lib.OilPieChart import PieChart
if __name__ == "__main__":
    root = tk.Tk()
    oil_list = OilDataList(root)
    oil_list.pack(side=tk.RIGHT)
    pie_chart = PieChart(root,oil_list,"功能比例")
    pie_chart.pack(side=tk.RIGHT)
    root.mainloop()



