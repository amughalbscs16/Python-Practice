
#Using While Loop
#python 3.5.2

hexadecimal = "10A1"
# It's for Hexadecimal, To Convert to any other base, Change Input to that base and replace 16 with that base;
# List of All HexaDecimal Numbers Each Index corresponds to the value of Hexa Digit
hexadecimal_list = "0123456789ABCDEF" 

decimal = 0;
i=0;
j=0;
#Loops over each digit in your input.
while(j < len(hexadecimal)):
    print(j)
    #Comparison of each digit with hexadecimal list to find the value/index.
    while (i < len(hexadecimal_list)):
      print(i)
        #used len(hexadecimal)-j-1 to read a number from least to max value;
      if hexadecimal[len(hexadecimal)-j-1] == hexadecimal_list[i]: 
            #calculating the decimal value;
        decimal += (16 ** j) *  i
      i+=1;
    j+=1; i=0;
#16 is the base
print(decimal);


#Using For LOOP

hexadecimal = "10A1"
# It's for Hexadecimal, To Convert to any other base, Change Input to that base and replace 16 with that base;
# List of All HexaDecimal Numbers Each Index corresponds to the value of Hexa Digit
hexadecimal_list = "0123456789ABCDEF" 

decimal = 0;
#Loops over each digit in your input.
for j in range(len(hexadecimal)):
    #Comparison of each digit with hexadecimal list to find the value/index.
    for i in range(len(hexadecimal_list)):
        #used len(hexadecimal)-j-1 to read a number from least to max value;
      if hexadecimal[len(hexadecimal)-j-1] == hexadecimal_list[i]: 
            #calculating the decimal value;
        decimal += (16 ** j) *  i
#16 is the base
print(decimal);
