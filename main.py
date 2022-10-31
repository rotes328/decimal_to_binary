import re


NEGATIVE_ERROR = 2
ZERO_ERROR = 3
BINARY_ERROR = 4


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


def binary_to_decimal(binary_number):
    if not re.match('^[0-1]*$', str(binary_number)):
        return BINARY_ERROR
    reversed = binary_number[::-1]
    i = 1
    return_value = 0
    for element in reversed:
        return_value += (int(element) * i)
        i *= 2
    return str(return_value)


def main():
    decimal_number = int(input("What is the number in decimal? "))
    binary_number = input("What is the number in binary? ")

    binary = decimal_to_binary(decimal_number)
    if binary == NEGATIVE_ERROR:
        print("Negative not allowed.")
    elif binary == ZERO_ERROR:
        print("Binary is 0.")
    else:
        print(f"{decimal_number} in binary is {binary}.")

    decimal = binary_to_decimal(binary_number)
    if decimal == BINARY_ERROR:
        print("Error")
    else:
        print(f"{binary_number} in decimal is {decimal}")


if __name__ == "__main__":
    main()
