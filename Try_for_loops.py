def addEvens(input_list):
    total = 0
    for number in input_list:
        total += number
    return total

def addEvens2(input_list):
    total = 0
    for index in range(len(input_list)):
        total += input_list[index]
    return total

print(addEvens([2,7,14,3,6]))
print(addEvens2([2,7,14,3,6]))
