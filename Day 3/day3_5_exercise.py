# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
combined_names = name1 + name2
lowercased_names = combined_names.lower()

t = lowercased_names.count("t")
r = lowercased_names.count("r")
u = lowercased_names.count("u")
e = lowercased_names.count("e")

true = t + r + u + e

l = lowercased_names.count("l")
o = lowercased_names.count("o")
v = lowercased_names.count("v")
e = lowercased_names.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(
        f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
