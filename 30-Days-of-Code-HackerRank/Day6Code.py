# If you Find Any thing which can help me improve my code do email me on amughal.bscs16seecs@seecs.edu.pk
# Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as
# space-separated strings on a single line (see the Sample below for more detail).
#Sample Input
#2
#Hacker
#Rank

#Sample Output
#Hce akr
#Rn ak

ites=input()        #Number of Strings to Perform Operation On.
ites=int(ites)
for i in range(ites):
    string = input()
    odd=""; even="";
    for j in range(len(string)):   #2nd For
        if (j%2==0):
            even+=string[j]
        elif (j%2==1):
            odd+=string[j]
    #End 2nd for loop
    print(even+" "+odd)
#End 3rd For Loop
