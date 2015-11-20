#===============================================================================
#  Joseph Grocholski
# SU5050 Lab 4
# Lists and loops
# 25 September 2015
#===============================================================================

#============================================================================== Part 1 - Lists
# Initialize list
ids = [4353,2314,2956,3382,9362,3900]
# Determine number of elements in list
numItems = len(ids)
print "There are {} items in ids".format(numItems)

# Remove 3382 from list
ids.remove(3382)
print "3382 was removed and the list is now {}".format(ids)

# Get index of 9362
ind = ids.index(9362)
print "The index of 9362 is {}".format(ind)

# Insert 4499 into list after 9362
ids.insert(ind + 1, 4499)
print "4499 was added to the list after 9362: {}".format(ids)

# Add 5566 and 1830 to end of list
ids.append(5566)
ids.append(1830)
print "5566 and 1830 were added to the list: {}".format(ids)

# Sort the list
ids.sort()
print "The sorted list is {}".format(ids)

# Save new variable
ids_new = ids
print "ids_new is {}" .format(ids_new) 


#=============================================================================== Part 2 - Loops
print "\nList of elements of ids_new and their index:"
for element in ids_new :
    print "{} {}".format(ids_new.index(element),element)    

    
# Fibonacci Sequence
def fibonacci(seqLength):
#     Initialize string
    fibStr = "\nFibonacci Sequence:\n"
#    Define first two terms
    fib0 = 0
    fib1 = 1
#     Add terms to list
    fibStr = fibStr + str(fib0)
    fibStr = fibStr + "\n{}".format(fib1)
#     Starting at the third term, calcluate the remaining terms
    for i in range(2,seqLength):
        temp = fib1
        fib1 = fib1 + fib0
        fib0 = temp
        fibStr = fibStr + "\n{}".format(fib1)
#     Return the list of fibonacci values
    return fibStr

#=============================================================================== Test Section
# print fibonacci(10)
#===============================================================================



    