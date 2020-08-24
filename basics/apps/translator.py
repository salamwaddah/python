# replace every vowel with letter g - giraffe language
def translate(phrase):
    translation = ""
    vowels = ["a", "e", "i", "o", "u"]
    for char in phrase:
        if char.lower() in vowels:
            char = "g"
        translation += char
    return translation


print(translate(input("Enter a phrase to translate into giraffe language: ")))
