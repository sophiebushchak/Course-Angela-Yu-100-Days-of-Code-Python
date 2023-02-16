# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

true_t_count = name1.count("t") + name2.count("t")
true_r_count = name1.count("r") + name2.count("r")
true_u_count = name1.count("u") + name2.count("u")
true_e_count = name1.count("e") + name2.count("e")
true_score = true_t_count + true_r_count + true_u_count + true_e_count

love_l_count = name1.count("l") + name2.count("l")
love_o_count = name1.count("o") + name2.count("o")
love_v_count = name1.count("v") + name2.count("v")
love_e_count = true_e_count
love_score = love_l_count + love_o_count + love_v_count + love_e_count

score = int(str(true_score) + str(love_score))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")





