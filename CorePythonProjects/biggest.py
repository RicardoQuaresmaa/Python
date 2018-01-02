# find biggest
def largest(array, index=0):
    for i, v in enumerate(array):
        if v > array[index]:
            index = i
    
    return index

numbers = raw_input("Numbers (seperate with whitespaces): ").split(" ")
i = largest(numbers)
print("Largest number is {} at index {}.".format(numbers[i], i))