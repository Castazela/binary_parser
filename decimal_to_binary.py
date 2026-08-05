def decimal_to_binary(number: str) -> str:
    nb = int(number)
    binary = []
    test = [nb]
    while nb != 0:
        binary.append(nb % 2)
        nb = int(nb/2)
        test.append(nb)
    binary = binary[::-1]
    binary = list(map(str, binary))
    return ''.join(binary)
