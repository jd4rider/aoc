from utilities import *
        
def main():
    f = open("input.txt", "r")

    final_sum = 0

    #loop through the input
    for x in f:
        #pass line to Utilities Class to find the 
        #number from the first and last occurance of
        #the line
        u = Utilities(x)

        #add the extracted number to total sum
        final_sum += u.num

    print("The Number for day 1 is: " + str(final_sum))

if __name__ == '__main__':
    main()