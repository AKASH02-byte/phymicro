boy_name = input("Boy Name: ")
boy_age = int(input("Boy Age: "))
girl_name = input("Girl Name: ")
girl_age = int(input("Girl Age: "))
# use of abs it prevents the ans in negative
age_diff = abs(boy_age - girl_age)
print(f"{boy_name} loves {girl_name}. Age Difference {age_diff}")