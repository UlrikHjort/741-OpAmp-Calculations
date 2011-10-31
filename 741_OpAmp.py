#!/usr/bin/python
########################################################################
#                                                                           
#                          741 OpAmp Calculations                                      
#                                                                           
#                         741_OpAmp_Calculations.py                                      
#                                                                           
#                                 MAIN                                      
#                                                                           
#                   Copyright (C) 1998 Ulrik Hoerlyk Hjort                   
#                                                                           
#  741 OpAmp Calculations is free software;  you can  redistribute it                          
#  and/or modify it under terms of the  GNU General Public License          
#  as published  by the Free Software  Foundation;  either version 2,       
#  or (at your option) any later version.                                   
#  741 OpAmp Calculations is distributed in the hope that it will be                           
#  useful, but WITHOUT ANY WARRANTY;  without even the  implied warranty    
#  of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                  
#  See the GNU General Public License for  more details.                    
#  You should have  received  a copy of the GNU General                     
#  Public License  distributed with Yolk.  If not, write  to  the  Free     
#  Software Foundation,  51  Franklin  Street,  Fifth  Floor, Boston,       
#  MA 02110 - 1301, USA.                                                    
########################################################################                                                                          

from Tkinter import *

######################################
#
# Calculate R1
#
#####################################
def calculate_r1():

  r2_val = float(r2_entry.get())
  gain_val = float(gain_entry.get())

  inv = invert.get()
  gain = 0.0
  r1 = 0.0


  if inv == 0: # Non Inverting
     r1 = r2_val / (gain_val - 1)
  else:
     r1 = -r2_val /gain_val

  r1_entry.delete(0, END)
  r1_entry.insert(0, str(r1))



######################################
#
# Calculate R2 
#
#####################################
def calculate_r2():

  r1_val = float(r1_entry.get())
  gain_val = float(gain_entry.get())

  inv = invert.get()
  gain = 0.0
  r2 = 0.0


  if inv == 0: # Non Inverting
     r2 = (gain_val - 1.0) * r1_val
  else:
     r2 = gain_val * - r1_val

  r2_entry.delete(0, END)
  r2_entry.insert(0, str(r2))



######################################
#
# Calculate gain
#     Gain inv     = -R2/R1
#     Gain non inv = 1 + (R2/R1)
#
# Where:
# 
#       R1 is resistance in Ohm
#       R2 is resistance in Ohm
#
#
#####################################
def calculate_gain():
  r1_val = float(r1_entry.get())
  r2_val = float(r2_entry.get())
  
  inv = invert.get()
  gain = 0.0
  if inv == 0: # Non Inverting
     gain = 1 + (r2_val / r1_val)
  else:
     gain = -r2_val / r1_val

  gain_entry.delete(0, END)
  gain_entry.insert(0, str(gain))



##################################
#
# Reset input entries to 0.0
#
##################################
def reset():
   r1_entry.delete(0, END)
   r1_entry.insert(0, str(0.0))
   r2_entry.delete(0, END)
   r2_entry.insert(0, str(0.0))
   gain_entry.delete(0, END)
   gain_entry.insert(0, str(0.0))
   non_inverting.select()



root=Tk()

h_label = Label(root, text="741 OpAmp Calculations:")
h_label.grid(row=0, column=0)

invert = IntVar()

non_inverting = Radiobutton(root, text="Non-Inverting", variable=invert, value=0)
non_inverting.grid(row=0, column=1)

inverting = Radiobutton(root, text="Inverting", variable=invert, value=1)
inverting.grid(row=0, column=2)



r1_label = Label(root, text="R1 (Ohm)")
r1_label.grid(row=1)

r1_entry = Entry(root)
r1_entry.grid(row=1, column=1)

r2_label = Label(root, text="R2 (Ohm)")
r2_label.grid(row=2)

r2_entry = Entry(root)
r2_entry.grid(row=2, column=1)


gain_label = Label(root, text="Gain: ")
gain_label.grid(row=3)

gain_entry = Entry(root)
gain_entry.grid(row=3, column=1)

reset();

button=Button(root, text="Calculate", command=calculate_r1).grid(row=1, column=2);
button=Button(root, text="Calculate", command=calculate_r2).grid(row=2, column=2);
button=Button(root, text="Calculate", command=calculate_gain).grid(row=3, column=2);
button=Button(root, text="reset", command=reset).grid(row=4,column=3);

root.mainloop()
