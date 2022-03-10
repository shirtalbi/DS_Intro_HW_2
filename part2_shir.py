
def reverse(sentence, reverse_word):
    sen = sentence.split(" ")
    if type(reverse_word)!= str:
        return ("invalid input")
    if reverse_word not in sen:
        return("The word was not found")
    else:
        for x in sen:
            sen = [x[::-1] if x == reverse_word else x for x in sen]
            return(' '.join(sen))





