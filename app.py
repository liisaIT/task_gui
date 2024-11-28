import tkinter as tk
from TaskGui import TaskGui

if __name__ == '__main__':
    window = tk.Tk() # loo põhiaken
    TaskGui(window) # Loo GUI aga anna aken kaasa
    window.mainloop() # viimane rida selles koodis :O, mainloop hoiab akent püsti
