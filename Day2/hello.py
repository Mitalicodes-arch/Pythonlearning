#git add Day2/
#git commit -m "Day 2 – basic calculator, even/odd, factorial, primes"
#git push
old_age = input("Enter your old age: ")
new_age = old_age + 2  # This will cause an error because old_age is a string
print(new_age)

i = 1
while i <= 10000:
    print(i)
    i = i + 1

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
    print("You can vote")
elif age < 18 and age > 3:
    print("You are in school")
else:
    print("You are a child")

first = input("Enter first number: ")
second = input("Enter second number: ")

sum = int(first) + int(second)
print("The sum is: " + str(sum))

name = "Tony Stark"
print(name.replace("Tony Stark", "Ironman"))
