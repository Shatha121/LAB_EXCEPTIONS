def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f"Temperature in Fahrenheit: {round(fahrenheit, 2)} F"


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return f"Temperature in Celsius: {round(celsius, 2)} C"

def main():
    while True: 
        user_input = input("Enter a temperature and its unit (e.g., '25 C' or '77 F'): ")
        try:
            split_user_input = user_input.split()
            number = float(split_user_input[0])
                
            if split_user_input[1] == "C":
                print(celsius_to_fahrenheit(number))
                break
            elif split_user_input[1] == "F":
                print(fahrenheit_to_celsius(number))
                break
            else:
                raise TypeError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError:
            print("Invalid temperature value, Please try again")
        except TypeError as e:
            print(e)
        
main()

