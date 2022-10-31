def decimal_to_binary(decimal_number):
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

    if int(number) < 0:
        print("Negative not allowed")
        quit()
    if int(number) == 0:
        print("Binary is 0.")
        quit()
    binary = decimal_to_binary(number)
    print(f"Binary is {binary}.")

if __name__ == "__main__":
    main()