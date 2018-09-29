# This program calculates the weight of a steel plate.

ms_rho = .2836

print "Please enter the thickness (in.) of the plate."

t = input("> ")

print "Please enter the width (in.) of the plate."

w= input("> ")

print "Please enter the length (in.) of the plate."

l= input("> ")

we = ms_rho*t*w*l

print " We have a plate that weights ", we, "lb"


