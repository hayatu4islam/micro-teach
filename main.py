# main.py
# This program asks the users their name and their year of birth and return the age.

def getName():
    name = input("Enter your name: ")
    return name

def getAge():
    yob = input("Enter year of birth: ")
    age = 2024 - int(yob)
    return age

def main():
    print("Hello, Welcome to Age Calculator Application")
    name = getName()
    age = getAge()
    print()
    print(f"Hello {name}! You are {age} years old")


if __name__ == "__main__":
    main()
