from __future__ import division
from weight import gross
from Burning import burning

# This program will calculate total cost of fabrication a part.

print "Please Enter the part number of your part."

part_name = raw_input("> ")
print " "

print "Please enter the thickness of your part."
thickness = float(input())
print " "

print "Please enter the net real weight of yout part"
real_w = float(input(" Real weight> "))
print " "

print "Please enter the width of the plate you selected."
width = float(input())
print " "

print "Please enter the length of the plate you selected."
length = float(input())
print " "


#This Fuction was imported from weight. It calculates the weight of the selected plate.
gross(thickness,width,length)   

print "Plate gross weight used =  %f  " % gross(thickness,width,length)
print " "

print "Please enter the number of parts nested on the above selected plate"
nested = float(input())
print " " 

#This is the adjusted weight of the parts after it has been nested.
aw_pc = gross(thickness,width,length)/nested 

print "Please enter material cost per cwt." 
mat_rate = float(input())
print " "

#I could make this an outside fuction also.
part_mat_cost = mat_rate*aw_pc/100 
print "Material cost per piece > % f" % part_mat_cost


print "Please enter the burning perimeter > " 
per = float(input())
print " "

print "How many torches? > " 
num_torches = float(input())
print " "

#This function calculates burning cost.



freight = input("Please enter freight cost in CWT > ")*aw_pc/100
print " "

Markup = input("Mark-up percentage >  ")/100
print " "

mat_resale = mat_cost_pc*(1+Markup/100)
burning_resale = burning(thickness,per,num_torches)*(1+Markup/100)
freight_resale = freight*(1+Markup/100)

total = mat_resale + burning_resale + freight_resale



print "**********************************************************"
print "**********************************************************"
print "******************PRICING SUMMARY*************************"
print "**********************************************************"
print "Material resale %f <<" %mat_resale
print "**********************************************************"
print "**********************************************************"
print "Burning resale %f <<" %burning_resale
print "**********************************************************"
print "**********************************************************"
print "Freight resale %f <<" %freight_resale
print "**********************************************************"
print "**********************************************************"
print "**************TOTAL = %f" %total
print "**********************************************************"
print "**********************************************************"
print "**********************************************************"
print "**********************************************************"




















