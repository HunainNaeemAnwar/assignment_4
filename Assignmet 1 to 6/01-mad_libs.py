def mad_libs():
    print("Welcome to the Mad Libs Game!")

    # Get inputs from the user
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    place = input("Enter a place: ")
    exclamation = input("Enter an exclamation: ")

    story = f"{exclamation}! he said {verb} the {adjective} {noun} to the {place}."

    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    mad_libs()
