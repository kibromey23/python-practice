import random
def game():
    while True:  # game loop
        num = random.choice(range(1, 11))

        for i in range(3):  # 3 attempts
            try:
                guess = int(input("Guess a number between 1 and 10: "))

                if guess == num:
                    print("✅ Congratulations! You guessed the number.")
                    break
                else:
                    print(f"❌ Wrong guess. You have {2 - i} tries left.")

            except ValueError:
                print("Please enter a valid number.")

        else:
            # runs if loop didn't break (user failed all attempts)
            print(f"💀 You ran out of tries. The number was {num}")

        # play again logic
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break



game()