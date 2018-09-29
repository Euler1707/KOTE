
#This fuction will evaluate the burning cost of an oxyfueled part.


def burning(thickness,perimeter,num_torches):

    burn_run_rate = float(95)
    
    feedrate = [11,12,10,9,8,7,6,5,4,3]

    efficiency_mult = 1.4

    if thickness > 0 and thickness <= 0.5: 

        time = perimeter/float(feedrate[0])

        burn_cost = float((efficiency_mult*burn_run_rate/60)*time/num_torches)

        return burn_cost


    elif thickness > 0.5 and thickness <= 0.75: 

        time = perimeter/float(feedrate[1])

        burn_cost = float((efficiency_mult*burn_run_rate/60)*time/num_torches)

        return burn_cost

    elif thickness > 0.75 and thickness <= 1.0: 

        time = perimeter/float(feedrate[2])

        burn_cost = float((efficiency_mult*burn_run_rate/60)*time/num_torches)

        return burn_cost

    elif thickness > 1.0 and thickness <= 1.25: 

        time = perimeter/float(feedrate[3])

        burn_cost = float((efficiency_mult*burn_run_rate/60)*time/num_torches)

        return burn_cost


    elif thickness > 1.25 and thickness <= 1.75: 

        time = perimeter/float(feedrate[4])

        burn_cost = float((efficiency_mult*burn_run_rate/60)*time/num_torches)

        return burn_cost

    elif thickness > 1.75 and thickness <= 2.25:

        time = perimeter/float(feedrate[5])

        burn_cost = float((efficiency_mult*burn_run_rate/60)*time/num_torches)

        return burn_cost

    elif thickness > 2.25 and thickness <= 2.50: 

        time = perimeter/float(feedrate[6])

        burn_cost = float((efficiency_mult*burn_run_rate/60)*time/num_torches)

        return burn_cost
       

    elif thickness > 2.50 and thickness <= 4.0: 

        time = perimeter/float(feedrate[7])

        burn_cost = float((efficiency_mult*burn_run_rate/60)*time/num_torches)

        return burn_cost


    elif thickness > 4.0 and thickness <= 8.0: 

        time = perimeter/float(feedrate[8])

        burn_cost = float((efficiency_mult*burn_run_rate/60)*time/num_torches)

        return burn_cost

    elif thickness > 8.0 and thickness <= 14.0: 

        time = perimeter/float(feedrate[9])

        burn_cost = float((efficiency_mult*burn_run_rate/60)*time/num_torches)

        return burn_cost

    else:

        print "Please enter a thickness between 0 and 14 inches"


            
    
    
