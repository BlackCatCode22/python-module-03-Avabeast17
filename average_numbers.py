# average_numbers.py homework

total = 0
count = 0

while True:
    line = input("Enter a number: ")
    if line.lower() == "done":
        break
    try:
        num = int(line)
    except ValueError:
        print("Invalid input")
        continue
    total = total + num
    count = count + 1

if count > 0:
    average = total / count
    print(total, count, average)
else:
    print("No numbers entered.")
