import tkinter as tk 
from tkinter import ttk, messagebox

class RestrauntOrder:
    
    def __init__(self,root):
        self.root = root
        self.root.title(
             "Uber Eats")
    
        self.menu_items = {
            "Loaded Fries": 3,
            "Burger Combo": 4,
            "Large Drink": 2,
            "Supreme Pizza": 5,
            
        }
        self.exchange_rate = 300
        self.setup_background(root)
        
        frame = ttk.Fram(root)
        frame.place (realx = 5.5, rely = .5,
                     anchor=tk.CENTER)
        
        ttk.Label(frame,
                  text = "Welcome to Uber Eats",
                  font = ("Noto Sans Mono", 20, "bold")).grid(row = 0
                                                              columnspam = 3,
                                                              padx = 10,
                                                              pady = 10)

        self.menu_labels = {}
        self.menu_quantities = {}
        
        for i, (item, price) in enumerate(self.menu_items.items(),start = 1):
            label = ttk.Label(frame
                              text = f"{item} (${price}):",
                              font = ("Noto Sans Mono"),12)     
            label.grid(row = 1, column = 0, padx = 10, pady = 5)
            self.menu_labels[item] = label
            
            quantity_entry =  ttk.Entry(frame, width = 5)
            quantity_entry.grid(row = 1, column = 1, padx = 10, pady = 5)
            self.menu_quantities[item] = quantity_entry
            
        self.currency_var = tk.StringVar()
        ttk.Label(frame, text = "Currency: ",
                  font = ("Noto Sans Mono", 12)).grid(row = len(self.menu_items) + 1,
                                                      column = 0
                                                      padx = 10
                                                      pady = 5)