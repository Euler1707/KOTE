prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for n in prices:
    print n                                                                
    print "price: %s" % prices[n]
    print "stock: %s" % stock[n]
    

total = 0

for n in prices: 
    
    total = total + prices[n]*stock[n]
    

print total


