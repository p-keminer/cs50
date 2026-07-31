
def main():

    while True:
        text = input("Prompt ur Text: ")
        if len(text) != 0:
            break
        else:
            print("Prompt ur Text please!")

    cli = calculate_cli(count_letters_whole_(text), count_sentences_whole_(text), count_words_whole_(text))

    if round(cli) < 1:
        print("Before Grade 1")
    elif round(cli) >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {round(cli)}")


# cli function
def calculate_cli(letters, sentences, words):
    return 0.0588 * (letters/words) * 100 - 0.296 * (sentences/words) * 100 - 15.8

# calulator functions
def count_letters_whole_(text):
    letter_counter = 0
    for char in text:
        if char.isalpha():  # return sum(1 for char in text if char.isalpha())
            letter_counter += 1
    return letter_counter


def count_sentences_whole_(text):
    sentences_counter = 0
    for sentences in text:
        if sentences in [".", "!", "?"]: # return text.count(".") + text.count("!") + text.count("?")
            sentences_counter += 1
    return sentences_counter


def count_words_whole_(text):
    return len(text.split())


main()
