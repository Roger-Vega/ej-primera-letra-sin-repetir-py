def first_not_repeating_char(string):
    for char in string:
        if string.count(char) == 1:
            return char
    return '_'

if __name__ == "__main__":
    string = str(input("Ingrese una secuencia de caracteres: "))
    print(first_not_repeating_char(string))
