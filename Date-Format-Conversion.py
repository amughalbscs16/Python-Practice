date = input("Enter a Data in format MMDDYYYY")
months = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]
Month = int(date[0:2])
print(months[Month-1]+" ",date[2:4],",",date[4:8] );
