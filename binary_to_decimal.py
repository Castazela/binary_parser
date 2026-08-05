def binary_to_decimal(number: str) -> int:
    binary = [int(x) for x in list(number)]
    binary = binary[::-1]
    decimal = []
    for i in range(len(binary)):
        equation = binary[i]*(2**i)
        decimal.append(equation)
    decimal = sum(decimal)
    return decimal
