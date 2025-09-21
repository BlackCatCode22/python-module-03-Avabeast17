# work_ex_6_5.py homework

numbers = []

while True:
    line = input("Enter a number: ")
    if line.lower() == "done":
        break
    try:
        num = float(line)
        numbers.append(num)
    except ValueError:
        print("Invalid input")
        continue

if numbers:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
else:
    print("No numbers entered.")
