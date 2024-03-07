# Author: Jaden Miguel
# Date: 4/17/19
# Purpose: Assignment #2 - fungi exchange
# prompting user for amounts
shiitakes_amt = int(input("How many shiitakes have you picked up? "))
ports_amt = int(input("How many portobellos have you picked up? "))
print(
    """As you wander carelessly through the forest, passing by a dark
corner- you notice a soup chef coming toward you. He strikes you with his
soup ladle and yells, "what are you doing here!" He peers into your bag
and changes his demeanor. He speaks to you directly, "Would you be willing
to trade some of those mushrooms?" """
)
# prompts user for trade amounts w/ chef
shiitakes_offd = int(input("How many shiitakes are you willing to trade?"))
ports_offd = int(input("How many portobellos are you willing to trade? "))
# if mushrooms are more than found
if shiitakes_offd > shiitakes_amt or ports_offd > ports_amt:
    print("The chef shakes his head and turns away.")
# if mushrooms are equal to zero
elif shiitakes_offd + ports_offd == 0:
    print(
        """The chef looks at you in digust. He says, "Well get out of my
woods then!" """
    )
# first algorithm - less than ten, less than 5
elif shiitakes_offd < 10 and ports_offd < 5:
    rubies = shiitakes_offd * 2
    print("The chef offers you", rubies, "rubies")
    response = input("Do you accept the trade? Y/N: ")
    if response == "y" or "yes" or "Yes":
        print(
            "You make the trade and walk away with",
            rubies,
            "rubies,",
            (shiitakes_amt - shiitakes_offd),
            "shiitakes, and",
            (ports_amt - ports_offd),
            "portobellos.",
        )
    else:
        print("The chef looks at you in disgust. He makes you leave the forest.")
# second algorithm - less than 10, larger or equal to 5
elif shiitakes_offd < 10 and ports_offd >= 5:
    rubies = ports_offd * 3
    print("The chef offers you", rubies, "rubies")
    response = input("Do you accept the trade? Y/N: ")
    if response == "y" or "yes" or "Yes":

        print(
            "You make the trade and walk away with",
            rubies,
            "rubies,",
            (shiitakes_amt - shiitakes_offd),
            "shiitakes, and",
            (ports_amt - ports_offd),
            "portobellos.",
        )
    else:
        print("The chef looks at you in disgust. He makes you leave the forest.")
# third algorithm - multiple of 12, NOT multiple of 24. and ports larger or equal to 20
elif (shiitakes_offd % 12 == 0 and (not shiitakes_offd % 24 == 0)) and (
    ports_offd >= 20
):
    rubies = shiitakes_offd * 4
    print("The chef offers you", rubies, "rubies")
    response = input("Do you accept the trade? Y/N: ")
    if response == "y" or "yes" or "Yes":
        print(
            "You make the trade and walk away with",
            rubies,
            "rubies,",
            (shiitakes_amt - shiitakes_offd),
            "shiitakes, and",
            (ports_amt - ports_offd),
            "portobellos.",
        )
    else:
        print("The chef looks at you in disgust. He makes you leave the forest.")
# fourth algorithm - multiple of 12, NOT multiple of 24. and ports less than 20
elif (shiitakes_offd % 12 == 0 and (not shiitakes_offd % 24 == 0)) and (
    ports_offd < 20
):
    rubies = ports_offd
    print("The chef offers you", rubies, "rubies")
    response = input("Do you accept the trade? Y/N: ")
    if response == "y" or "yes" or "Yes":
        print(
            "You make the trade and walk away with",
            rubies,
            "rubies,",
            (shiitakes_amt - shiitakes_offd),
            "shiitakes, and",
            (ports_amt - ports_offd),
            "portobellos.",
        )
    else:
        print("The chef looks at you in disgust. He makes you leave the forest.")
# for any values outside of parameters
else:
    rubies = shiitakes_offd * 5
    print("The chef offers you", rubies, "rubies")
    response = input("Do you accept the trade? Y/N: ")
    if response == ("y" or "yes" or "Yes"):
        print(
            "You make the trade and walk away with",
            rubies,
            "rubies,",
            (shiitakes_amt - shiitakes_offd),
            "shiitakes, and",
            (ports_amt - ports_offd),
            "portobellos.",
        )
    else:
        print("The chef looks at you in disgust. He makes you leave the forest.")
# who goes into a forest and finds a soup chef?!
