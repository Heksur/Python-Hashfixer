                    #########################################
                    #                                       #
                    #     ~This was made by Heksur~         #
                    #                                       #
                    #########################################
from sys import argv
from os.path import exists

script = argv

print """
\t\tThis tool was created to make dividing hashes etc easily.
\t\tIt will make a bash script so name it anything.sh
\t\tBasically it's easy-mode awk. 
\t\tCTRL+C at any time to stop.
"""
filename = raw_input("\t\tHere you insert the in-filename: ")
txt = open(filename)

outfilename = raw_input("\t\tInsert the outfilename you want here: " )
outfile = "AWK Hash Fix.sh"
txt2 = open(outfile, 'w')

print """
\t\tThe following inputs will ask you for the position of what you want to see.
\t\tWhat is its position relevant to the dividing character you'd like to remove?
\t\tExample: user:email:hash:salt:pass  
\t\tYou'd like user and pass? You would type in: 1 (enter) 5 (enter) : (enter) 
"""

first_position = raw_input("\t\tInsert first desired data position: ")
# The position of the second part of the data you'd like to extract.
second_position = raw_input("\t\tInsert second desired data position: ")
# Added a divider, so you can pick the character to replace.
divider = raw_input("\t\tInsert the sign you want to replace: ")

stringed_position = str(first_position)
stringed_position2 = str(second_position)

scripttext = 'awk -F \"'+ divider +'\"  \'{print$' + stringed_position + '"\\t"$' + stringed_position2 + "}' " + filename + " > " + outfilename

scripttext = str(scripttext)
txt2.write(scripttext)

txt.close()
txt2.close()

print "\t\tSucces! Now open the AWK Hash Fix.sh! It will create: " + filename

# It basically just creates a simple bash script that awks the desired character.
# Script-builder for friends :) Enjoy! 
