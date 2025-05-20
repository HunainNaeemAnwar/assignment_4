
def main():
    sentence="My [adjective] [noun] can [adjective] ,thanks python"
    print(sentence)
    adjective=input("Enter adjective and Press Enter : ")
    noun=input("Enter noun and Press Enter : ")
    verb=input("Enter verb and Press Enter : ")
    sentence = sentence.replace("[adjective]", adjective)
    sentence = sentence.replace("[noun]", noun)
    sentence = sentence.replace("[verb]", verb)
    print(sentence)

if __name__=="__main__":
    main()