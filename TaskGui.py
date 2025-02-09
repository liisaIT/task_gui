# graafiline osa
# II päeva salvestus 11:19

from tkinter import Frame, Text, messagebox
from tkinter.ttk import Combobox, Button, Label, Entry

from Circle import Circle
from Rectangle import Rectangle
from Triangle import Triangle

class TaskGui:
   def __init__(self, main):
       self.main = main
       main.title("Task GUI")
       self.main.geometry("500x500")
       self.main.resizable()

       #teeme ainult need, mida meil korduvalt vaja kasutada
       #Frame
       self.frame = Frame(self.main, background='forestgreen')
       self.frame.pack(fill='both', expand=True)

       #Create Combobox
       self.cmb = Combobox(self.frame, values=['Vali kujund', 'Ring', 'Ristkülik', 'Täisnurkne kolmnurk']) # self.frame!! 11:36 salvestusest
       self.cmb.current(0) # vali esimene valik *Vali kujund
       self.cmb['state'] = 'readonly' # Comboboxi sisu ei ole muudetav
       self.cmb.grid(row=0, column=0, padx=3, pady=3, columnspan=2, sticky='ew')

       # Ujuvad vidinad (Ring ja Ristkülik, kolmnurk)
       # Ring
       self.lbl_circle, self.txt_circle = self.create_circle_widget() #salvestus 12:12, seda ei ole koodis näha, sest
       #see tehakse enne ja selle peale tuleb ristkülik (salvestus 12:24)

       # Ristkülik
       self.lbl_a, self.lbl_b, self.txt_a, self.txt_b = self.create_rectangle_widget()

       #kolmnurk
       self.lbl_ta, self.lbl_tb, self.txt_ta, self.txt_tb = self.create_triangle_widget()

       # Loome nupu - button
       self.btn_submit = self.create_button()

       # Vastuse kast
       self.result = self.create_result()

       # Peidame Ringi ja Ristküliku, Kolmnurga info
       self.forget_circle() # Unusta/peida ring
       self.forget_rectangle() # Unusta/Peida ristkülik
       self.forget_triangle()  # Unusta/Peida kolmnurk

       # #"kuula" Comboboxi muutusi
       self.cmb.bind('<<ComboboxSelected>>', self.changed)
       self.main.bind('<Return>', lambda event=None: self.calculate())

   def create_button(self):
       button = Button(self.frame, text='Näita', command=lambda: self.calculate())
       button['state'] = 'disabled' # nupp on aga klikkida ei saa
       button.grid(row=3, column=0, padx=3, pady=3, columnspan=2, sticky='ew')
       return button

   def create_result(self):
       result = Text(self.frame, height=15, width=25)
       result.grid(row=4, column=0, padx=3, pady=3, columnspan=2, sticky='ew')
       result['state'] = 'disabled'  # kasti kirjutada ei saa
       return result

   def create_circle_widget(self):
       label = Label(self.frame, text='Raadius')
       label.grid(row=1, column=0, padx=3, pady=3, sticky='ew')

       text = Entry(self.frame, width=12)
       text.focus() # teksti kursor raadiuse teksti lahtris
       text.grid(row=1, column=1, padx=3, pady=3, sticky='ew')
       return label, text

   def create_rectangle_widget(self):
       label_a = Label(self.frame, text='Külg a')
       label_a.grid(row=1, column=0, padx=3, pady=3, sticky='ew')

       text_a = Entry(self.frame, width=12)
       text_a.focus() # teksti kursor ristküliku teksti lahtris
       text_a.grid(row=1, column=1, padx=3, pady=3, sticky='ew')

       label_b = Label(self.frame, text='Külg b')
       label_b.grid(row=2, column=0, padx=3, pady=3, sticky='ew')

       text_b = Entry(self.frame, width=12)
       text_b.grid(row=2, column=1, padx=3, pady=3, sticky='ew')

       return label_a, label_b, text_a, text_b

   def create_triangle_widget(self):
       lbl_ta = Label(self.frame, text='Külg a')
       lbl_ta.grid(row=1, column=0, padx=3, pady=3, sticky='ew')

       txt_ta = Entry(self.frame, width=12)
       txt_ta.grid(row=1, column=1, padx=3, pady=3, sticky='ew')

       lbl_tb = Label(self.frame, text='Külg b')
       lbl_tb.grid(row=2, column=0, padx=3, pady=3, sticky='ew')

       txt_tb = Entry(self.frame, width=12)
       txt_tb.grid(row=2, column=1, padx=3, pady=3, sticky='ew')

       return lbl_ta, lbl_tb, txt_ta, txt_tb

   # kodutöö osa 15:20 salvestusest ... luua uus widget.

   def forget_circle(self):
       self.lbl_circle.grid_forget()
       self.txt_circle.grid_forget()
       self.btn_submit['state'] = 'disabled'

   def forget_rectangle(self):   # salvestus alates u 13:25
       self.lbl_a.grid_forget()
       self.lbl_b.grid_forget()
       self.txt_a.grid_forget()
       self.txt_b.grid_forget()
       self.btn_submit['state'] = 'disabled'

   def forget_triangle(self):
       self.lbl_ta.grid_forget()
       self.lbl_tb.grid_forget()
       self.txt_ta.grid_forget()
       self.txt_tb.grid_forget()
       self.btn_submit['state'] = 'disabled'

   def changed(self, event=None):
       combo_index = self.cmb.current() # mitmes valik comboboxist (0, 1, 2, 3)
       #print(combo_index)  # testime, kas see toimib

       if combo_index == 0:  # Kujundi valik
          self.forget_circle()
          self.forget_rectangle()
          self.forget_triangle()
          self.btn_submit['state'] = 'disabled'

       elif combo_index == 1: # Ring
          self.lbl_circle, self.txt_circle = self.create_circle_widget()
          self.forget_rectangle()
          self.forget_triangle()
          self.btn_submit['state'] = 'normal'

       elif combo_index == 2: #ristkülik
          self.lbl_a, self.lbl_b, self.txt_a, self.txt_b = self.create_rectangle_widget()
          self.forget_circle()
          self.forget_triangle()
          self.btn_submit['state'] = 'normal'

       elif combo_index == 3:  # Täisnurkne kolmnurk
           self.lbl_ta, self.lbl_tb, self.txt_ta, self.txt_tb = self.create_triangle_widget()
           self.forget_circle()
           self.forget_rectangle()
           self.btn_submit['state'] = 'normal'


       self.clear_result()

   def clear_result(self):
      self.result.config(state='normal') # tulemuskasti sisu saab muuta
      self.result.delete('1.0', 'end') # tühjendab kastist tulemuse
      self.result.config(state='disabled') # ei saa muuta kasti sisu

   def calculate(self):
      cmb_index = self.cmb.current()
      if cmb_index == 1: # Ring
         try:

            radius = float(self.txt_circle.get().strip())

            circle = Circle(radius)

            self.clear_result()
            self.result.config(state='normal')

            self.result.insert('1.0', str(circle))
            self.result.config(state='disabled')
         except ValueError:
            messagebox.showerror('Oops!', 'Palun sisesta number!')

         self.txt_circle.delete(0, 'end')
         self.txt_circle.focus()

      elif cmb_index == 2:

          try:
              rectangle_a = float(self.txt_a.get().strip())
              rectangle_b = float(self.txt_b.get().strip())

              rectangle = Rectangle(rectangle_a, rectangle_b) # objekti loomine

            # self.lbl_a, self.lbl_b, self.txt_a, self.txt_b = self.create_rectangle_widget()

              self.clear_result()
              self.result.config(state='normal')

             #self.result.insert('1.0', str(rectangle))
              self.result.insert('1.0', repr(rectangle)) # sobib ka repr versioon - mis on Rectangle versioonis.
              self.result.config(state='disabled')

          except ValueError:
              messagebox.showerror('Oops!', 'Palun sisesta number!')

          self.txt_a.delete(0, 'end')
          self.txt_b.delete(0, 'end')
          self.txt_a.focus()


      elif cmb_index == 3:  # Täisnurkne kolmnurk

          try:

              side_a = float(self.txt_ta.get().strip())

              side_b = float(self.txt_tb.get().strip())

              triangle = Triangle(side_a, side_b)

              self.clear_result()

              self.result.config(state='normal')

              self.result.insert('1.0', repr(triangle))

              self.result.config(state='disabled')


          except ValueError:

              messagebox.showerror('Oops!', 'Palun sisesta number!')

          self.txt_ta.delete(0, 'end')

          self.txt_tb.delete(0, 'end')

          self.txt_ta.focus()

