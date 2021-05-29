
age=int(input("Please enter you Age"))

print(age)

if( age < 18): 
	print("This person is a Teenager.")
elif(age > 18 and age < 45):
	print("This person is an Adult.")
else:
	print("This person is Senior Citizen.")