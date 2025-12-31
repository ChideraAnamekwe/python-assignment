import random
from js import document, console

random_number = None
guesses = 0

def log(message):
    console.log(f"[PYTHON LOG] {message}")

def start_game(event=None):
    global random_number, guesses

    top_input = document.getElementById("range")
    output = document.getElementById("output")

    top = top_input.value
    log("Start game clicked")

    if not top or int(top) <= 0:
        output.innerText = "Enter a number greater than 0"
        return

    random_number = random.randint(1, int(top))
    guesses = 0

    output.innerText = "Game started! Make a guess."

def make_guess(event=None):
    global guesses

    output = document.getElementById("output")
    guess_input = document.getElementById("guess")

    if random_number is None:
        output.innerText = "Start the game first!"
        return

    guess = guess_input.value
    if not guess:
        output.innerText = "Enter a valid number"
        return

    guesses += 1
    guess = int(guess)

    if guess == random_number:
        output.innerText = f"🎉 You got it in {guesses} guesses!"
    elif guess > random_number:
        output.innerText = "📉 Too high!"
    else:
        output.innerText = "📈 Too low!"

    guess_input.value = ""

def reset_game(event=None):
    global random_number, guesses

    random_number = None
    guesses = 0

    document.getElementById("range").value = ""
    document.getElementById("guess").value = ""
    document.getElementById("output").innerText = "Game reset. Start again."
