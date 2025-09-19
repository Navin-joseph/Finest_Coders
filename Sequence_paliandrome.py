a = int(input("Enter The Number: "))
limit = int(input("Enter The Limit: "))

for i in range(limit):
    b = str(a)[::-1]
    c = int(b)
    a = a+c
    print(f"step {i+1} = {a}")
    if str(a) == str(a)[::-1]:
        print("Found Paliandrome: ",a)
        break
