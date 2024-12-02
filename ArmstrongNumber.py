while True:
    num = input("Enter a number (or 'exit' to quit): ")
    if num() == 'exit':
        break
    if num():
        total = sum(int(digit) ** len(num) for digit in num)
        if total == int(num):
            print(num, " is an Armstrong number!")
        else:
            print(num ,"is not an Armstrong number.")
    else:
        print("Invalid input. Try again.")
