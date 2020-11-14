import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
random_num = random.randint(0, (len(names) - 1))
random_person = names[random_num]
print(f"{random_person} is going to buy the meal today!")
