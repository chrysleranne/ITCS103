def compute_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

def compare_average_length(avg, length, word):
    if length > avg:
        print(f"The length of the word '{word}' is greater than the average.")
    elif length < avg:
        print(f"The length of the word '{word}' is less than the average.")
    else:
        print(f"The length of the word '{word}' is equal to the average.")

word = input("\nHi! Enter any word: ")
length = len(word)

numbers = []
for i in range(length):
    num = int(input(f"\n\tEnter any number {i+1}: "))
    numbers.append(num)

print(f"\n{numbers}")
print(f"The length of the word is {length}")
average = compute_average(numbers)
print(f"The average of the numbers is {average}")

compare_average_length(average, length, word)