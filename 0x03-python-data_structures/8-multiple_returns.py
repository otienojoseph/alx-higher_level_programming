#!/usr/bin/python3

def multiple_returns(sentence):
    len_of_sentence = len(sentence)

    if sentence == "":
        return (len_of_sentence, None)
    else:
        return (len_of_sentence, sentence[0])
