def binary_to_decimal(number: str) -> int:
    """
        Converti un nombre binaire en nombre décimal

        Args:
            number (str): le nombre binaire à convertir

        Returns:
            decimal (int): le nombre décimal correspondant au nombre binaire ajouté 

        Example:
            >>> birary_to_decimal(12)
            '1100'
        """
    binary = [int(x) for x in list(number)]
    binary = binary[::-1]
    decimal = []
    for i in range(len(binary)):
        equation = binary[i]*(2**i)
        decimal.append(equation)
    decimal = sum(decimal)
    return decimal
