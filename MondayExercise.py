
def is_dark_brown(row, column):
    if (row + column) % 2 == 0:
        return True
    else:
        return False

print(is_dark_brown(1,1))
print(is_dark_brown(1,2))