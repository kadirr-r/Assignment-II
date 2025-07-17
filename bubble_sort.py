def bubbleSort(numbers):
    size = len(numbers)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if numbers[j] > numbers[j + 1]:
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
    return numbers
