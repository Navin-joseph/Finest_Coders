# Finest_Coders
Palindrome Finder using Reverse-and-Add Method
📌 Description

This Python program takes a number as input and repeatedly applies the Reverse-and-Add process to check if it becomes a palindrome.

A palindrome number is a number that remains the same when reversed (e.g., 121, 1331).

🔄 Reverse-and-Add Process:

Take the given number.

Reverse its digits.

Add the reversed number to the original number.

Repeat until a palindrome is found, or until a given limit of steps.

📝 How It Works

The user enters:

A starting number (a).

A maximum limit of steps (limit).

In each step:

The number is reversed.

It is added to the original number.

The result is checked for palindrome.

If a palindrome is found → the program stops and displays it.

If the limit is reached without finding a palindrome → the program ends.

CODE :

a = int(input("Enter The Number: "))
limit = int(input("Enter The Limit: "))

for i in range(limit):
    b = str(a)[::-1]
    c = int(b)
    a = a+c
    print(f"step {i+1} = {a}")
    if str(a) == str(a)[::-1]:
        print("Found Paliandrome: ", a)
        break

