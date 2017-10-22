hexadecimal = "10A1"
# It's for Hexadecimal, To Convert to any other base, Change Input to that base and replace 16 with that base;
# List of All HexaDecimal Numbers Each Index corresponds to the value of Hexa Digit
hexadecimal_list = "0123456789ABCDEF" 

decimal = 0;

for j in range(len(hexadecimal)):
    for i in range(len(hexadecimal_list)):
        #used len(hexadecimal)-j-1 to read a number from least to max value;
      if hexadecimal[len(hexadecimal)-j-1] == hexadecimal_list[i]: 
            #calculating the decimal value;
        decimal += (16 ** j) *  i
#16 is the base
print(decimal);
