def add_prefix_un(word):
    print(word, "=", 'un' + word)


add_prefix_un('managable')


def make_word_groups(vocab_words):
    string = ''
    for word in vocab_words:
        if word == vocab_words[0]:
            string = word
        else:
            string += (' :: ' + vocab_words[0] + word)
    print(string)


make_word_groups(['en', 'close', 'joy', 'lighten'])


def remove_suffix_ness(word):
    if word[-5] == 'i':
        print(word[:-5] + 'y')
    else:
        print(word[:-4])


remove_suffix_ness("heaviness")
remove_suffix_ness("sadness")


def noun_to_verb(sentence, index):
    sentence_without_dot = sentence[:-1]
    list = sentence_without_dot.split()
    print(list[index] + 'en')


noun_to_verb('I need to make that bright.', -1)
noun_to_verb('It got dark as the sun set.', 2)
