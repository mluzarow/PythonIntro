###############################################################################################
## Introductory Python 2                                                                     ##
##      Functions                                                                            ##
##                                                                                           ##
## Compute the Pythagorean triple given 2 arbitrary integers m and n, with m > n.            ##
## Then, print the values for a, b, and c to the console.  On this occasion, you will use    ##
## functions in order to split up your code.                                                 ##
##                                                                                           ##
## Pythagorean Triple                                                                        ##
## https://en.wikipedia.org/wiki/Pythagorean_triple                                          ##
##                                                                                           ##
## ==== Calculating the Pythagorean Triple====                                               ##
## The Pythagorean Triple cosists of three positive integers a, b, and c, such that          ##
## a^2 + b^2 = c^2.                                                                          ##
##                                                                                           ##
## The Pythagorean Triple can be generated via Euclid's formula, stating                     ##
## a^2 + b^2 = (m^2 - n^2)^2 + (2mn)^2 = (m^2 + n^2)^2 = c^2.                                ##
##                                                                                           ##
## Simplified, this reads:                                                                   ##
## a = m^2 - n^2                                                                             ##
## b = 2mn                                                                                   ##
## c = m^2 + n^2                                                                             ##
###############################################################################################

#region Public Methods
# Our first function is myInput () which takes a string as argument.  Of course, this function
# simply calls input (), so it is not accomplishing much being its own encapsulated function.
# However, notice that we are returning the user's input much like we would in C.
def myInput (myString):
    userInput = input (myString)

    return userInput

# Our calculation function takes in a, b, and c.  The calculations are the same as they have
# been in the past.  The large difference between Python and C in this case is that we are 
# free to return every variable in our calculation all at once.
def calculateTriple (m, n):
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2

    return a, b, c

# Our print function merely prints out the required output.
def myPrint (a, b, c):
    print "Your a is: %d\nYour b is: %d\nYour c is: %d" % (a, b, c)
#endregion Public Methods

#region Main
# On this run of the program, we are seperating the script's functionality, or 
# compartmentalizing.  This is a very useful approach to programming as it
# creates sections of code that can be reused for many different purposes, as well as
# cleaning up general program clutter.  In this case, it is not very necessary as the
# functions "myInput" and "Input" do pretty much the exact same thing. Still, it is an
# important skill to learn.
if __name__ == "__main__":
    m = myInput ("Put in your m: ")
    n = myInput ("Put in your n: ")

    a, b, c = calculateTriple (m, n)

    myPrint (a, b, c)
#endregion Main