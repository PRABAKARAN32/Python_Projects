import random as rd
class GuessTheNumber:
    def __init__(self):
        self.number = int(input("Enter a number range: "))
        self.random_number = rd.randint(1,self.number)
        self.start_game()

    def start_game(self):
        print("Welcome to Guess the Number! , GAME STARTED.")
        self.get_user_guess()
    def return_result(self,user_guess):
        if(self.random_number == user_guess):
            return f"Congratulations you have guessed the number {user_guess} is Correctly!!.",True
        elif (self.random_number < user_guess):
            return f"Sorry!!, You have guessed the number {user_guess} is Too High!!.",False
        else:
            return f"Sorry!!, You have guessed the number {user_guess} is Too Low!!.", False
    def get_user_guess(self):
        while True:
            try:
                user_number = int(input("Enter the Guess: "))
                return_message, is_correct = self.return_result(user_number)
                if(is_correct):
                    print(return_message)
                    break
                print(return_message)
            except ValueError:
                print("Please enter a valid number")


user1 = GuessTheNumber()




