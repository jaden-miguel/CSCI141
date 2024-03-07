# Name: Jaden Miguel
# Date: 23 April 2019
# Purpose: Lab 3: Conditionals and Boolean Logic. Will check if sunny or cloudy and adjust relative to temperature.

# ask user for inputs
sun_cloud = input("Is it sunny or cloudy? ")
temperature = int(input("What is the temperature? "))

# if sunny
if sun_cloud == "sunny":
    if temperature < 60:
        print("Wear a sweater.")
    elif temperature == 60:
        print("Woo hoo, it is 60 degrees. Wear what you want.")
    elif temperature > 60:
        print("Wear a tee shirt and flip flops.")
# if cloudy
elif sun_cloud == "cloudy":
    if temperature < 40:
        print("Wear a coat and hat.")
    elif 40 <= temperature <= 50:
        if temperature == 50:
            print("A jacket is best.")
        else:
            print("Not quite freezing, but close. Bundle up.")
    elif temperature > 50:
        print("Wear a long sleeved shirt.")
