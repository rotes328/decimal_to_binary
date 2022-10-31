NEGATIVE_ERROR = 2
ZERO_ERROR = 3

def decimal_to_binary(decimal_number):
    if decimal_number < 0:
        return(NEGATIVE_ERROR)
    elif decimal_number == 0:
        return(ZERO_ERROR)
    binary_array = []
    while decimal_number > 0:
        binary_array.append(decimal_number % 2)
        decimal_number //= 2
    return_str = ""
    binary_array.reverse()
    for element in binary_array:
        return_str += str(element)
    return return_str

def main():
    number = int(input("What is the number in decimal? "))

    binary = decimal_to_binary(number)
    if binary == 2:
        print("Negative not allowed.")
    elif binary == 3:
        print("Binary is 0.")
    else:
        print(f"Binary is {binary}.")

if __name__ == "__main__":
    main()