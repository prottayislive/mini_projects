# a madlibs project using string concatenation
adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
adj3 = input("Adjective: ")
adj4 = input("Adjective: ")
adj5 = input("Adjective: ")
adj6 = input("Adjective: ")
adj7 = input("Adjective: ")
noun1 = input("Noun: ")
noun2 = input("Noun: ")
noun3 = input("Noun: ")
noun4 = input("Noun: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
verb3 = input("Verb: ")
verb4 = input("Verb: ")


def passage():
    """This function contains the passage(s)"""
    madlib = f"I walk through the color jungle. I take out my {adj1} canteen. There's a {adj2} parrot with a\n"\
             f" {adj3} {noun1} in his mouth right there in front of me in the {adj4} \n" \
             f"trees! I gaze at his {adj5} {noun2}. A sudden sound awakes me from my daydream!\n" \
             f" A panther’s {verb1} in front of my head! I {verb2} his {adj6} breath. I remember I have a packet of\n " \
             f"{noun3}  that makes go into a deep slumber! I {verb3} it away from me in front of the {noun4}.Yes he's \n" \
             f"eating it! I {verb4} away through the {adj7} jungle. I meet my parents at the tent. Phew! It’s\n" \
             f" been an exciting day in the jungle."
    print(madlib)


passage()
