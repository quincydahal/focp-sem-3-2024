#1
greeting = input("Hello, what is your name? ")
print(f"Hello, {greeting}. Good to meet you!")


#2
temp_in_Celsius = float(input("Enter the temperature in Celsius: "))
temp_in_Fahrenheit = (temp_in_Celsius * 9/5) + 32
print("The temperature in Faharenheit is: ",temp_in_Fahrenheit)


#3
no_of_students = int(input("Enter the number of students: "))
required_size = int(input("Enter the required group size: "))

no_of_groups = no_of_students // required_size
left_over = no_of_students % required_size
print(f"There will be {no_of_groups} groups with {left_over} student left over.")


#4
no_of_sweets = int(input("Enter the number of sweets you have: "))
no_of_students = int(input("Enter the number of students: "))

if no_of_sweets < no_of_students:
    print("!!! Not enought sweets !!!")

else:
    sweets_per_student = no_of_sweets // no_of_students
    remainder = no_of_sweets % no_of_students
    print(f"The students will get {sweets_per_student} number of sweets each and you will have {remainder} number of remaining sweets.")