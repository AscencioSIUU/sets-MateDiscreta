numberUniverse = set(range(0, 10))
lettersUniverse = set(chr(c) for c in range(ord('A'), ord('Z') + 1))

def universeValidator(array):
    for element in array:
        if element not in numberUniverse and element not in lettersUniverse:
            print(element)
            break

print(numberUniverse)
genericList = [0, 1, 2, 5, 6, 7, 8, 'A', 'z', 10]
universeValidator(genericList)