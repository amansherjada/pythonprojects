def mad_libs_generator():

    story = (
        "Once upon a time, in a {adjective} land, there lived a {noun}. "
        "This {noun} was known for its {adjective} personality and its love for {plural_noun}. "
        "One day, the {noun} decided to {verb} {adverb} with its friends. "
        "They had a {adjective} time together, laughing and sharing {plural_noun}. "
        "It was a day that the {noun} would never forget."
    )

    print("Hello guys, let's play Mad Libs.")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    plural_noun = input("Enter a plural noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    mad_lib = story.format(adjective=adjective, noun=noun, plural_noun=plural_noun, verb=verb, adverb=adverb)

    print("\nMad Lib Result:")
    print(mad_lib)

mad_libs_generator()


