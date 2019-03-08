# account balance
k = open("sum.txt", 'r')  # location of the text file
lines = k.readlines()  # i am reading lines here
counter = 0  # counter update each time number is entered
for line in lines:  # taking each line
    conv_int = float(line)  # converting string to float
    counter = counter + conv_int  # update counter
print(counter)
