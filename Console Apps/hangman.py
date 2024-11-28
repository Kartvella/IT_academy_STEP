import random

# სიტყვების სია, რომელთაგანაც ერთ-ერთი შემთხვევით აირჩევა
# (შეგიძლია სხვადასხვა სიტყვა ამოშალო ან დაამატო)
HANGMAN_WORDS = [
    "python",
    "function",
    "variable",
    "hangman",
    "algorithm",
    "syntax",
    "developer",
    "iteration",
    "recursion",
    "exception",
    "debugging",
    "dictionary",
    "inheritance",
    "polymorphism",
    "encapsulation",
    "abstraction",
    "interface",
    "framework",
    "compilation",
    "runtime"
]

def choose_word() -> str:
    # ფუნქცია ირჩევს შემთხვევით სიტყვას "HANGMAN_WORDS" სიიდან და აბრუნებს ამ სიტყვას
    return random.choice(HANGMAN_WORDS)

def display_word(word: str, guessed_letters: set) -> str:
    # ფუნქცია არგუმენტად იღებს გამოსაცნობ სიტყვასა(str-ის ტიპის)
    # და გამოცნობილი ასოების სეტს
    """
    მისი ლოგიკა:
    ფუნქცია გამოსახავს სიტყვის გამოცნობილ ასოებს (თუ არის, რა თქმა უნდა) ან 
    გამოუცნობელ ასოებს '_'-ის სახით.
    """
    # შედეგი თავიდან არის ცარიელი სტრინგი
    result = ""

    # word-ზე გავაკეთოთ იტერაცია, რათა მივწვდეთ თითოეულ ასოს
    for letter in word:
        # შევამოწმოთ ყოველი ასო არის თუ არა გამოცნობილი ასოების სეტში
        if letter in guessed_letters:
            # თუ არის, მაშინ ასო დავამატოთ result-ს
            result += letter
        else:
            # თუ არ არის, მაშინ დავამატოთ '_'
            result += "_"
    # შემდეგ შევქმათ დაჯოინებული result, რათა გამოსახული სიტყვის ასოები ერთმანეთზე მიტყუპებული არ იყოს
    spaced_result = " ".join(result)

    # და დავაბრუნოთ მოდიფიცირებული შედეგი
    return spaced_result

    # მოცემული ლოგიკის ანალოგია შემდეგი ხაზი, თუმცა, ცხადია, უფრო ჩახლართულიც:
    # return " ".join([letter if letter in guessed_letters else "_" for letter in word])
 
def main():
    # მთავარი ფუნქცია, რომელიც უშვებს "Hangman"-ის თამაშს
    print("Welcome to Hangman!")
    word_to_guess = choose_word()  # ვირჩევთ გამოსაცნობ სიტყვას
    guessed_letters = set()  # ვქმნით გამოცნობილი ასოების სეტს
    attempts = 6  # თამაშის დასაწყისში მცდელობების რაოდენობაა 6

    # იმ დროის განმავლობაში, როდესაც მცდელობების რაოდენობა 0-ზე მეტია:
    while attempts > 0:
        # ვაჩვენოთ სიტყვის ამჟამინდელი "მდგომარეობა"
        print(f"\n{display_word(word_to_guess, guessed_letters)}")
        guess = input("Guess a letter: ").lower()  # მომხმარებელს ვთხოვოთ ერთ ასო

        # თუ guess-ის სიგრძე 1-ზე მეტია ან ანბანური სახის (ანუ ასო) არაა
        if not guess.isalpha() or len(guess) != 1:
            # მაშინ დავპრინტოთ ეს:
            print("Invalid input. Please guess one letter at a time.")
            # და while ლუპი მოქმედებას თავიდან დაიწყებს continue-თი
            continue
        # თუ შეყვანილი ასო გამოცნობილ ასოებთა სეტშია
        # მაგ. ერთი და იგივე ასო თავიდან შევიყვანეთ
        if guess in guessed_letters:
            # ვაჩვენოთ შესაბამისი შეტყობინება:
            print(f"You already guessed '{guess}'.")
        # თუ შეყვანილი ასო გამოსაცნობ სიტყვაშია
        # (ანუ მოთამაშემ ასო სწორად გამოიცნო)
        elif guess in word_to_guess:
            # ამ ასოს დავამატებთ გამოცნობილი ასოების სეტში
            guessed_letters.add(guess)
            # და დაპრინტავთ ამას: 
            print(f"Good guess! '{guess}' is in the word.")
            # თუ set-ად გადაქცეული გამოსაცნობი სიტყვა გამოცნობილი ასოების სეტის იდენტურია
            # (ანუ ყველა ასო გამოცნობილია)
            if set(word_to_guess).issubset(guessed_letters):
                # დავპრინტავთ გამარჯვების შეტყობინებას:
                print(f"Congratulations! You guessed the word: {word_to_guess}")
                # და ლუპიდანაც გამოვალთ, რადგან თამაში დასრულდა
                break
        # თუ მცდელობა არასწორი აღმოჩნდა 
        else:
            # მაშინ გამოცნობილი ასოების სეტს დავამატებთ მოცემულ ასოს
            guessed_letters.add(guess)
            # მცდელობების რაოდენობას ერთით შევამცირებთ
            attempts -= 1
            # და დავპრინტავთ:
            print(f"Wrong guess! You have {attempts} attempts left.")
    # თუ მცდელობები ამოიწურა
    else:
        #  ვაჩვენოთ წაგების შეტყობინება
        print(f"Out of attempts! The word was: {word_to_guess}")
        
# და საბოლოოდ გავუშვათ თამაში
if __name__ == "__main__":
    main()
