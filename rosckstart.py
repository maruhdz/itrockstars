# div % 3 == 0 => "Rock"
# div % 5 == 0 => "Start"
# div % 3 && div % 5 == 0 => "Rock Start"

#for x in range (51):


x=15

if x%5 == 0 and x%3 == 0:
    print ("Rock Start")
elif x%3 == 0:
    print("Rock")
elif x%5 == 0:
    print ("Start")

