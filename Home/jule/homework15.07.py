# def count_words(a):
#
#     return len(a.split())
# print(count_words("Привет мир привет"))



# import re
# def count_numbers(s):
#
#     numbers = re.findall(r'\d+', s)
#     return len(numbers)
# print(count_numbers("6 54 8 64 5 64 6 46 45"))


def get_repeated_words(s):

    words = s.split( )

    word_count = { }
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    repeated = [word for word, count in word_count.items() if count > 1]

    return " ".join(repeated)
print(get_repeated_words("яблоко груша яблоко апельсин груша яблоко"))


