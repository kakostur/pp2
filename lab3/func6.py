def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = reversed(words)
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

user_input = input()

print(reverse_sentence(user_input))
