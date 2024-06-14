# for Loop to print numbers till 99
for i in range(0, 100):
    print(i)
# to print even numbers (0,100,2) here 2 is the step
for eve in range(0, 100, 2):
    print("Even numbers are:", eve)
# to print odd numbers (1,100,2) here 2 is the step , here counter starts from 1
for odd in range(1, 100, 2):
    print("Odd numbers are:", odd)

# break
for counter in range(0, 101):
    print(counter)
    if counter == 6:
        break

print("We have come outside the program")
