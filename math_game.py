import inquirer
from playsound import playsound
from numpy import random
import time
import gtts


class MathGame:
    def __init__(self):
        self.sound_setting = inquirer.prompt(
            [
                inquirer.List(
                    "sound_setting",
                    message="Choose a setting",
                    choices=["Only sound", "Only text", "Sound and text"],
                )
            ]
        )["sound_setting"]
        self.mode = inquirer.prompt(
            [
                inquirer.List(
                    "mode",
                    message="Choose a mode",
                    choices=["Approximate", "Exact"],
                )
            ]
        )["mode"]

        n_rounds = inquirer.prompt(
            [
                inquirer.Text(
                    "n_rounds",
                    message="How many rounds do you want to play? Default is 12",
                    # validate=lambda _, x: x.isdigit() and int(x) > 0,
                )
            ]
        )["n_rounds"]
        if n_rounds.isdigit():
            n_rounds = int(n_rounds)
        else:
            n_rounds = 12

        self.n_rounds = n_rounds

    def generate_question(self):
        if self.mode == "Approximate":
            # TODO change this distribution so more even spread
            return random.randint(1e2, 1e4), random.randint(1e2, 1e4)

    def check_answer(self, answer, a, b):
        if self.mode == "Approximate":
            if (answer <= a * b * 1.1) and (answer >= a * b * 0.9):
                return True
            else:
                return False

    def start_round(self):
        a, b = self.generate_question()

        question = f"{a} gånger {b}? "
        while True:
            if self.sound_setting == "Only text":
                answer = input(question)
            elif self.sound_setting == "Only sound":
                gtts.gTTS(question, lang="sv").save("question.mp3")
                playsound("question.mp3")
                answer = input("Answer: ")
            elif self.sound_setting == "Sound and text":
                gtts.gTTS(question, lang="sv").save("question.mp3")
                playsound("question.mp3")
                answer = input(question)

            if answer.isdigit():
                answer = int(answer)
                if self.check_answer(answer, a, b):
                    print("Correct!")
                    break
                else:
                    print("Wrong! Try again.")
            elif answer == "r" and self.sound_setting != "Only text":
                continue
            elif answer == "q":
                break
            else:
                print("Invalid answer. Try again.")


def main():
    game = MathGame()
    for i in range(game.n_rounds):
        game.start_round()


if __name__ == "__main__":
    main()
