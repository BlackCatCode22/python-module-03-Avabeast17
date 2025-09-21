# min_max_numbers.py homework

smallest = None
largest = None

while True:
    line = input("Enter a number: ")
    if line.lower() == "done":
        break
    try:
        num = float(line)
    except ValueError:
        print("Invalid input")
        continue

    if smallest is None or num < smallest:
        smallest = num
    if largest is None or num > largest:
        largest = num

if smallest is not None and largest is not None:
    print("Maximum:", largest)
    print("Minimum:", smallest)
else:
    print("No numbers entered.")
