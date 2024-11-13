secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("Secret Number is "))
while (number - secret_number):
    number = int(input("Wrong! Type again Secret Number is "))

print("Congratulations!!! Your Number is correct")
