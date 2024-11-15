#[Assume all arrays and data has already been set up and stored as per mentioned in the question]

def hosNoValid(n):
    if 1 <= n <= 1000:
        return "Valid"
    else:
        return "Invalid"
#Checks if hospital number is valid

def tempRead(n):
    if 31.6 < Readings[n][1] < 37.2:
        return "Normal"
    else:
        return "Warning"
#Checks if temperature readign is normal

def pulseRead(n):
    if 55.0 < Readings[n][2] < 100.0:
        return "Normal"
    else:
        return "Warning"
#Checks if heart rate readign is normal

n = input("Enter hospital number_ ")
#Asks for hospital number
if hosNoValid(n) == "Valid":
    print(f"Patient name: {Patient[n]}")
    if tempRead(n) == pulseRead(n) == "Warning":
        print("Severe warning")
    print(f"Temperature: {Readings[n][1]}")
    print(f"Heart Rate: {Readings[n][2]}")
else:
    print("Error: Invalid Hospital Number")
#Prints everything out