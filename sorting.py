largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    if num in ("done", "exit", "quit", "adios", "bye", "bye bye", "tchau") : break
        
    try:
        num = int(num)
    
    except:
        print "Invalid input"
        continue
           
    if smallest == None or largest == None :
        smallest = num
        largest = num
        
    if smallest > num :
        smallest = num
        
    if largest < num :
        largest = num
        
print "Maximum is", largest
print "Minimum is", smallest
