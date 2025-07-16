def mamultiplication_table():
    x = int(input("Enter number: "))
    for i in range(1, 6):
        for k in range(1 , i + 1):
            print(f"{i} * {k} = {i * k}")
            
def generate_a_multiplication_table():
    x = int(input("Enter Num: "))
    l = []
    for i in range(1, x + 1):
        temp = []
        for y in range(1, i + 1):
            temp.append(i * y)
        l.append(temp)
    print(l)