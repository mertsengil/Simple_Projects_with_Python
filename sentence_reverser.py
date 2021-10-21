def sentence_reverser(a):

    L = list(str(a).split(" "))
    lenght = len(L)
    index = lenght - 1
    reversed_sentence = ''

    while (index >=0):
        letter = L[index]
        reversed_sentence += letter + " "
        index = index - 1

    print(reversed_sentence)

a = str(input("enter a sentence:"))
sentence_reverser(a)
        
