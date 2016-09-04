#series=list(raw_input("Enter the series : "))
#length=int(raw_input("Enter the length : "))
def slices(series, length):
    numbers = [int(digit) for digit in series]
    if not 1 <= length <= len(numbers):
        raise ValueError("Invalid slice length for this series: " + str(length))
    return [numbers[i:i + length]
            for i in range(len(numbers) - length + 1)]
            
#slices(series, length)