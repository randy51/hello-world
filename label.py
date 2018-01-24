#import tkinter as tk

# if you are still working under a Python 2 version, 
# comment out the previous line and uncomment the following line
import Tkinter as tk

root = tk.Tk()
root.title("Max Calculator")
#root.geometry("200x200")
w = tk.Label(root,text="Enter 5 RM").grid(row = 0, column = 0, pady=(30,0))
weight = tk.Entry(root).grid(row=0, column=1, padx =(0,10), pady=(30,0))
w1 = tk.Label(root,text="1 RM       ").grid(row=1, column=0, pady=(0,30))
weight1 = tk.Entry(root).grid(row=1, column=1, padx =(0,10),  pady=(0,30))


root.mainloop()
 







