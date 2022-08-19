from rich.prompt import Prompt
from rich.console import Console
from random import choice
from word_set import word_list

SQUARES = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect_letter': '⬛'
}

WELCOME_MESSAGE = f'\n[white on blue] WELCOME TO WORDLE-6 [/]\n'
PLAYER_INSTRUCTIONS = "You have 6 guesses to find what 6 letter word am I thinking of. You think you can do it?? Then lets get it started...\n"
GUESS_STATEMENT = "\nEnter your guess"
ALLOWED_GUESSES = 6

def correct_place(letter):
    return f'[black on green]{letter}[/]'


def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'


def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'


def check_guess(guess, answer):
    guessed = []
    wordle_pattern = []
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            guessed += correct_place(letter)
            wordle_pattern.append(SQUARES['correct_place'])
        elif letter in answer:
            guessed += correct_letter(letter)
            wordle_pattern.append(SQUARES['correct_letter'])
        else:
            guessed += incorrect_letter(letter)
            wordle_pattern.append(SQUARES['incorrect_letter'])
    return ''.join(guessed), ''.join(wordle_pattern)


def game(console, chosen_word):
    end_of_game = False
    already_guessed = []
    full_wordle_pattern = []
    all_words_guessed = []

    while not end_of_game:
        guess = Prompt.ask(GUESS_STATEMENT).upper()
        while len(guess) != 6 or guess in already_guessed or guess not in word_list:
            if guess in already_guessed:
                console.print("[red]Oops!!! You've already tried this word\n[/]")
            elif len(guess)!=6:
                console.print('[red]No way. Its not even a 6-letter word XD\n[/]')
            else:
                console.print("[red]Word not in my list. Will learn it later\n[/]")
            guess = Prompt.ask(GUESS_STATEMENT).upper()
        already_guessed.append(guess)
        guessed, pattern = check_guess(guess, chosen_word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)

        console.print(*all_words_guessed, sep="\n")
        if guess == chosen_word or len(already_guessed) == ALLOWED_GUESSES:
            end_of_game = True
    if len(already_guessed) == ALLOWED_GUESSES and guess != chosen_word:
        console.print(f"\n[red]Out of guesses[/]")
        console.print(f'\n[green]Correct Word: {chosen_word}[/]')
        console.print(f"\n[red]You can always try again though...[/]")
    else:
        console.print(f"\n[green]Congratulations!! You guessed the right word in  {len(already_guessed)} guesses :)[/]\n")
    console.print(*full_wordle_pattern, sep="\n")


if __name__ == '__main__':
    console = Console()
    chosen_word = choice(word_list)
    console.print(WELCOME_MESSAGE)
    console.print(PLAYER_INSTRUCTIONS)
    game(console, chosen_word)
