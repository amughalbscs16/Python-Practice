
import time
string=input("Enter string:")
start = time.time()
count1=0; count2=0; count3=0; count=0;
while(count<len(string)):
      if(string[count].islower()):
            count1=count1+1
      elif(string[count].isupper()):
            count2=count2+1
      elif(string[count] != ' ' and int(string[count]) >= 0 and int(string[count]) <= 9) :
            count3+=1
      count+=1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)
print("The number of Letters characters is:")
print(count3)
print(count1+count2+count3)
end = time.time()
print(end-start)
