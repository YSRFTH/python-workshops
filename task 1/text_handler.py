# text_handler.py
"""
Text handling utilities:
- is_palindrome(text)
- count_vowels(text)
- reverse_text(text)
- remove_punctuation(text)
- capitalize_words(text)
- count_words(text)
- unique_words(text)
"""
import string
def is_palindrome(text: str) -> bool:
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def count_vowels(text: str) -> int:
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)

def reverse_text(text: str) -> str:
    return text[::-1]

def remove_punctuation(text: str) -> str:
    return text.translate(str.maketrans("", "", string.punctuation))

def capitalize_words(text: str) -> str:
    return text.title()

def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def unique_words(text: str) -> set:
    words = text.lower().split()
    return set(words)
