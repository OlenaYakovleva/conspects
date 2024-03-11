# counter = 1
# while True:
#     print(counter)
#     counter += 1
#     if  counter == 10:
#         print("Stop")
#         break
#     #continue
# counter = 0
# while counter <=10:
#     counter +=1
#     if counter % 2 !=1 :
#         continue
#     print(counter)

import random

while True:
    print("Game \"Guess The Number\"")
    print("There is a secret number between 1 and 20.")
    print("You need to guess it.")
    print("Don't worry, i will give you some tips.")
    print()

    secret_number = random.randint(1, 20)
    user_number = 0
    lives = 5
    while lives != 0:
        user_number = int(input("Try to guess: "))
        if user_number < secret_number:
            print(f"My secret number greater than {user_number}.") #greater - більше
            lives -= 1
        elif user_number > secret_number:
            print(f"My secret number lesser than {user_number}.") #lesser - менше
            lives -= 1
        else:
            print(f"Yes! It was {secret_number}!")
            break
    else: #if lives ==0:
        print(f"Sorry, you lost your life ")

    question = input("You want to play again?: ")
    if question =="yes" or "Yes":
        continue  
    else: 
        break

