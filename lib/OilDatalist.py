import tkinter as tk

class OilDataList(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        self.oil_ctrlist = []
        
        # 建立新增按鈕
        self.add_button = tk.Button(self, text="新增", command=self.add_eo)
        self.add_button.grid(row=2, column=2, padx=5, pady=5)

        # 建立標題
        oil_label = tk.Label(self, text="精油")
        oil_label.grid(row=0, column=1, padx=5, pady=5)
        
        concentration_label = tk.Label(self, text="農度%")
        concentration_label.grid(row=0, column=2, padx=5, pady=5)
        
        qty_label = tk.Label(self, text="數量(int)")
        qty_label.grid(row=0, column=3, padx=5, pady=5)

        self.add_basic_oil()

    def add_basic_oil(self):
        oil_var  = tk.StringVar()
        oil_var.set(f"稀釋基底油")
        self.basic_oil_entry = tk.Entry(self, textvariable=oil_var,width=5)
        self.basic_oil_entry.grid(row=1, column=1, padx=5, pady=5)

        self.basic_oil_qty = tk.IntVar()
        self.basic_oil_qty.set(1)
        
        self.basic_qty_entry = tk.Entry(self, textvariable=self.basic_oil_qty,width=2)
        self.basic_qty_entry.grid(row=1, column=3, padx=5, pady=5)
        
        self.add_baisc_qty_button = tk.Button(self, text="+", command=lambda qty=self.basic_oil_qty: qty.set(qty.get()+1))
        self.add_baisc_qty_button.grid(row=1, column=5, padx=5, pady=5)
        
        self.sub_baisc_qty_button = tk.Button(self, text="-", command=lambda qty=self.basic_oil_qty:  self.sub_qty_bound(qty))
        self.sub_baisc_qty_button.grid(row=1, column=4, padx=5, pady=5)
    
    def add_eo(self):
        # 建立新的 Entry 物件和按鈕
        row = len(self.oil_ctrlist) + 2
        
        oil_var  = tk.StringVar()
        oil_var.set(f"精油{row}")
        oil_entry = tk.Entry(self, textvariable=oil_var,width=5)
        oil_entry.grid(row=row, column=1, padx=5, pady=5)
        
        concentration_var=tk.DoubleVar()
        concentration_var.set(10)
        concentration_entry = tk.Entry(self, textvariable=concentration_var,width=5)
        concentration_entry.grid(row=row, column=2, padx=5, pady=5)

        qty = tk.IntVar()
        qty.set(1)
        
        qty_entry = tk.Entry(self, textvariable=qty,width=2)
        qty_entry.grid(row=row, column=3, padx=5, pady=5)
        
        add_qty_button = tk.Button(self, text="+", command=lambda qty=qty: qty.set(qty.get()+1))
        add_qty_button.grid(row=row, column=5, padx=5, pady=5)
        
        sub_qty_button = tk.Button(self, text="-", command=lambda qty=qty:  self.sub_qty_bound(qty))
        sub_qty_button.grid(row=row, column=4, padx=5, pady=5)
        
        remove_button = tk.Button(self, text="移除", command=lambda row=row: self.remove_eo(row))
        remove_button.grid(row=row, column=6, padx=5, pady=5)
        
        self.oil_ctrlist.append((oil_entry,concentration_var, concentration_entry, qty,qty_entry, add_qty_button, sub_qty_button, remove_button))
        
        self.add_button.grid(row=row+1, column=2, padx=5, pady=5)
    def getSafetyConcentration(self):
        total_oil = 0
        total_basic=1
        try:
            total_basic=self.basic_oil_qty.get()
            for oil_ctr in self.oil_ctrlist:
                oil_entry,concentration_var, concentration_entry, qty,qty_entry, add_qty_button, sub_qty_button, remove_button = oil_ctr
                total_oil+=concentration_var.get()/(100+concentration_var.get())*qty.get()
                total_basic+=100/(100+concentration_var.get())*qty.get()
        except:
            pass
        finally:
            return round(total_oil/total_basic*100,1)
    def remove_eo(self, row):
        # 取得要移除的 Entry 和按鈕
        oil_entry,concentration_var, concentration_entry, qty,qty_entry, add_qty_button, sub_qty_button, remove_button = self.oil_ctrlist.pop(row-1)
        
        # 刪除 Entry 和按鈕
        oil_entry.destroy()
        concentration_entry.destroy()
        qty_entry.destroy()
        add_qty_button.destroy()
        sub_qty_button.destroy()
        remove_button.destroy()
        
        # 更新後面的 Entry 和按鈕的列數
        for i in range(row, len(self.oil_ctrlist)+1):
            oil_entry, concentration_var,concentration_entry, qty,qty_entry, add_qty_button, sub_qty_button, remove_button = self.oil_ctrlist[i-1]
            oil_entry.grid(row=i, column=1, padx=5, pady=5)
            concentration_entry.grid(row=i, column=2, padx=5, pady=5)
            qty_entry.grid(row=i, column=3, padx=5, pady=5)
            add_qty_button.config(command=lambda qty=qty: qty.set(qty.get()+1))
            add_qty_button.grid(row=i, column=5, padx=5, pady=5)
            sub_qty_button.config(command=lambda qty=qty: self.sub_qty_bound(qty))
            sub_qty_button.grid(row=i, column=4, padx=5, pady=5)
            remove_button.config(command=lambda row=i: self.remove_eo(row))
            remove_button.grid(row=i, column=6, padx=5, pady=5)
        self.add_button.grid(row= len(self.oil_ctrlist)+2, column=2, padx=5, pady=5)
    def sub_qty_bound(self,qty):
        if(qty.get()-1)>=0:
            qty.set(qty.get()-1)
    def get_piechart_data(self):
        concentraion_dict={}
        total_oil = 0
        try:
            for oil_ctr in self.oil_ctrlist:
                oil_entry,concentration_var, concentration_entry, qty,qty_entry, add_qty_button, sub_qty_button, remove_button = oil_ctr
                total_oil+=concentration_var.get()/100*qty.get()
            for oil_ctr in self.oil_ctrlist:
                oil_entry,concentration_var, concentration_entry, qty,qty_entry, add_qty_button, sub_qty_button, remove_button = oil_ctr
                if total_oil==0:
                    return {}
                concentration = concentration_var.get()*qty.get()/100/total_oil
                concentraion_dict[oil_entry.get()]=concentration
        except:
            pass
        finally:
            return concentraion_dict