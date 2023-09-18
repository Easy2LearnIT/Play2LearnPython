import random
import time
import threading

anagrams = {
    5: [
        ['abets', 'baste', 'betas', 'beast', 'beats'],
        ['acres', 'cares', 'races', 'scare'],
        ['alert', 'alter', 'later'],
        ['angel', 'angle', 'glean'],
        ['baker', 'brake', 'break'],
        ['bared', 'beard', 'bread', 'debar'],
        ['dater', 'rated', 'trade', 'tread'],
        ['below', 'bowel', 'elbow'],
        ['caret', 'cater', 'crate', 'trace', 'react']
    ],
    6: [
        ['arrest', 'rarest', 'raster', 'raters', 'starer'],
        ['carets', 'caters', 'caster', 'crates', 'reacts', 'recast', 'traces'],
        ['canter', 'nectar', 'recant', 'trance'],
        ['danger', 'gander', 'garden', 'ranged'],
        ['daters', 'trades', 'treads', 'stared']
    ],
    7: [
        ['allergy', 'gallery', 'largely', 'regally'],
        ['aspired', 'despair', 'diapers', 'praised'],
        ['claimed', 'decimal', 'declaim', 'medical'],
        ['dearths', 'hardest', 'hatreds', 'threads', 'trashed'],
        ['detains', 'instead', 'sainted', 'stained']
    ],
    8: [
        ['parroted', 'predator', 'prorated', 'teardrop'],
        ['repaints', 'painters', 'pantries', 'pertains'],
        ['restrain', 'retrains', 'strainer', 'terrains', 'trainers'],
        ['construe', 'counters', 'recounts', 'trounces']
    ]
}

def get_random_word(length):
    word_set = anagrams.get(length)
    if not word_set:
        return None
    return random.choice(word_set)

def display_anagram(anagram):
    print(f"The word is: {anagram}")
    print(f"There are {len(anagram_set)} unguessed anagrams.")
    print(f"You have {time_left} seconds left.")

def countdown_timer():
    global time_left
    while time_left > 0:
        time_left -= 1
        time.sleep(1)

    print("Time is up!")

def play_game(word_length):
    global anagram_set, time_left
    anagram_set = get_random_word(word_length)
    if not anagram_set:
        print("That is not a correct word length. Please try again [5, 6, 7, 8]:")
        return
    time_left = 60

    timer_thread = threading.Thread(target=countdown_timer)
    timer_thread.start()

    while len(anagram_set) > 0:
        print(f"Guess the anagrams for {word_length}-letter words!")
        correct_guesses = []

        anagram = random.choice(anagram_set)
        anagram_set.remove(anagram)
        while time_left > 0 and len(anagram_set) > 0:
            display_anagram(anagram)
            guess = input("Make a guess: ").strip().lower()

            if guess in anagram_set and guess != anagram:
                anagram_set.remove(guess)
                correct_guesses.append(guess)
                print(f"{guess.upper()} is correct!")
            elif guess == anagram or guess in correct_guesses:
                print(f"Sorry, you already got {guess.upper()}. Try again.")
            else:
                print(f"{guess.upper()} is not a valid anagram. Please try again.")


        if len(anagram_set) == 0 and time_left > 0:
            print(f"You got all the anagrams for {anagram}!")
            anagram_set = get_random_word(word_length)
            while anagram in anagram_set:
                anagram_set = get_random_word(word_length)
        else:
            print("Time is up!")
            print(f"Sorry, you didn’t get that last one in on time.")
            print(f"You got {len(anagram_set)} anagrams for {word_length}-letter words!")
            break

if __name__ == "__main__":
    while True:
        word_length = int(input("Please enter a word length [5, 6, 7, 8]: "))
        if word_length not in [5, 6, 7, 8]:
            print("That is not a correct word length. Please try again [5, 6, 7, 8]:")
            continue

        play_game(word_length)
        play_again = input("Press Enter to play again (or type 'exit' to quit): ").strip().lower()
        if play_again == 'exit':
            break
