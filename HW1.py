###############################################################################################
## Introductory Python 1                                                                     ##
##      Data Types / IO                                                                      ##
##                                                                                           ##
## Compute the Pythagorean triple given 2 arbitrary integers m and n, with m > n.            ##
## Then, print the values for a, b, and c to the console.                                    ##
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


#region Main
# This is your "main" function, from which the program will start.  While Python has no real
# Main (), the logic statement "if __name__ == "__main__" is comparing the __name__ variable
# data to the string "__main__", in which the script is asking itself whether or not it
# should run itself. The scripts youe create will always be the boot scripts.
#
# An example in which this is not the case is in the import of Python modules, or otherwise 
# different scripts.  Your main script will be the one running, and the imported modules will
# have that __name__ set to their own script's names, creating a distinction between which
# scripts should be the boot script.
# 
# While this is not necessary in this situation, it is a nice habit to learn.
if __name__ == "__main__":
    # Python does not have staticly typed data types, nor does it have a compiler. Rather,
    # Python uses an interpreter to interpret that code you have written.  Therefore, there
    # is not need for creating a certain amount of integer variables; Python will decide what
    # type of variables 'm' and 'n' are at runtime.
    #
    # Try checking out this conecpt by inputing both integers, floats, and strings as arguments
    # You will find, possibly as the program crashes, that the variables are indeed labeled as
    # integers, floats, and strings in memory at that moment.
    m = input ("Put in your m: ")
    n = input ("Put in your n: ")

    # Much like C, the common algebraic syntax carries over.  In order to produce a exponential
    # calculation, the operator '**' is used.  The operator '^' is already used as a boolean
    # algebra operator, specifically used for "exclusive or" (XOR) comparisons. 
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2

    # Continuing with the theme of Python being a loose language, printing in Python can take
    # many shapes.  As you can see from running the script, all the below print statements
    # are aesthetically identical. However, the approach differs.  Use whichever one you like.
    print "Your a is: ", a, "\nYour b is: ", b, "\nYour c is: ", c
    print "\n"
    print "Your a is: %d\nYour b is: %d\nYour c is: %d" % (a, b, c)
    print "\n"
    print "Your a is: %(first)d\nYour b is: %(second)d\nYour c is: %(third)d" % {"first": a, "second" : b, "third" : c}
    print "\n"
    print "Your a is: {}\nYour b is: {}\nYour c is: {}".format (a, b, c)
    print "\n"
    print "Your a is: " + str (a) + "\nYour b is: " + str (b) + "\nYour c is: " + str (c)
    
    # Unlike C, Python does not require the user to "pre-define" a function.  Python does not
    # if you have a return () or not.  While it certainly exists within Python, it is far less
    # restrictive than in C/++.  In C, you could only send 1 piece of data through your return.
    # There are ways, of course, to mitigate this restriction in C, but in Python it is much
    # simpler to bundle data together and unpack as needed.
    
#endregion Main

# While not a part of Python, #region tags are used in both Microsoft's C# and the Visual Studio
# version of Python.  Of course, if the Python script is used in some other editor, say IDLE,
# the tags will appear as simple comments.  However, in Visual Studio, they do indeed work
# just as they do when writing C# and are a very useful way to organize code.