# main.py
import text_handler as th

def run_demo():
    print("Text Handler Demo")
    text = input("Enter a word or a sentence: ").strip()

    print("\nResults:")
    print("Is palindrome?:", th.is_palindrome(text))
    print("Vowels count:", th.count_vowels(text))
    print("Reversed", th.reverse_text(text))
    print("Without punctuation:", th.remove_punctuation(text))
    print("Capitalized words:", th.capitalize_words(text))
    print("Word count:", th.count_words(text))
    print("Unique words:", th.unique_words(text))

if __name__ == '__main__':
    run_demo()
