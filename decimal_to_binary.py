def decimal_to_binary(number: str) -> int:
    nb = int(number)
    binary = []
    while nb != 0:
        binary.append(nb % 2)
        nb = int(nb/2)
    return int(''.join(map(str, binary)))
