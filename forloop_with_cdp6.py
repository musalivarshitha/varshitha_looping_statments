input_str = input("Enter a string: ")
even_sum = 0

for char in input_str:
    if char.isdigit() and int(char)%2==0:
      even_sum+=int(char)

print("Sum of even digits:", even_sum)
