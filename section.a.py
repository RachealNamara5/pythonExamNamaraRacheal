
# No1,a.i
def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "E"
    else:
        return "Fail"

def main():
    percentage = float(input("put student's  score in percentage: "))
    grade = calculate_grade(percentage)
    print(f"The student's grade is: {grade}")

if __name__ == "__main__":
    main()
calculate_grade(75)

#a(ii)
def celiciusToFahrenheit():

    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius ")

    option = int(input("Select your choice (1 or 2): "))

    if option == 1:
        celsius =  float(input("Enter temperature in Celsius : "))
        fahrenheit  = (9/5 * celsius) + 32
        print(f"{celsius}° C is equal to {fahrenheit}°F")

    elif option == 2:
        fahrenheit =  float(input("Enter temperature in Fahrenheit : "))
        celsius  = 5/9 * (fahrenheit -32 )
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid option!") 


celiciusToFahrenheit()



#b(1)
base = int(input('Enter the base of the triangle: '))
height = int(input('Enter the height of the triangle: '))

def areaOfTriangle(b,h):

    area = (1/2) * b * h

    print(int(area))

areaOfTriangle(base,height)


#b.ii
def sumOfItems():

    numbers = [9,2,3,5,8]
    sum = 0

    for number in numbers:
        sum += number
    print("The sum of items in the list is:  " + str(sum))  
#calling the function
sumOfItems()