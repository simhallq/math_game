from numpy import random
import time


def generate_question(type):

    if type == "approx_multi":
        return random.randint(1e2, 1e4), random.randint(1e2, 1e4)


def check_answer(type, answer, a, b):
    if type == "approx_multi":
        return (answer <= a * b * 1.1) or (answer >= a * b * 0.9)


def main():
    n_questions = 20
    n_correct = 0

    for i in range(n_questions):
        a, b = generate_question("approx_multi")
        print(f"Question: {a}*{b}")
        start = time.time()
        answer = int(input("Answer: "))
        end = time.time()
        if check_answer("approx_multi", answer, a, b):
            n_correct += 1
            print(f"Correct! Took {end-start:.2f} seconds")
        else:
            print(f"Incorrect! Exact answer is {a*b}, you answered {answer}")

    pass


if __name__ == "__main__":
    main()
