print('''     .--,
           ( (`  ,--.
      ,--.  ) )\  `) ).--,
       `) )/ /) ) ( (( (`
       / /( (.  "-.) )) )
   ,-.( ( /          / /,--,
    `) \ ` ==.    .==  ( (`
    ( (_) ~6~      ~6~ _) )
     \_ (      )(      )_/
    ,-,\ \     ^^     /\ ,-.
   ( (_/ /\    __,   /\ \_) )
    '._.' _\  /__/  /_ '._.'
      .--`  \ `    /  `--.
             '----' ''')

print("Welcome to Medusa's temple. There is no turning back. Only the brave have a place inside.")
print("Your loved ones have turned to stone, and to break this curse, you must find Medusa's Tear Crystal.")

# First choice
choice1 = input('At the entrance of the temple, there are corridors branching to the left and right. The right side looks brighter—will you enter and search for clues, or will you go left and proceed quietly? Type "left" or "right": ').lower()

if choice1 == "right":
    print("Uh-oh! Medusa's snakes noticed you on the bright path. Game over.")
else:
    print("The darkness is a bit unsettling, but you're on the right path.")
    print("As you move deeper into the temple, you come across two more paths—one leading upward, the other downward.")

    # Second choice
    choice2 = input('Do you want to climb upward or descend into the unknown below? Type "up" or "down": ').lower()

    if choice2 == "up":
        print("You ascend upward, each step echoing through the narrow stone passages.")
        print("At the top, you discover a chamber filled with ancient statues, their eyes eerily lifeless.")
        print("Among them, you notice a hidden pedestal with an old, cracked mirror resting upon it.")

        # Third choice
        choice3 = input("Do you approach the mirror, or continue searching the chamber? Type 'approach mirror' or 'search further': ").lower()

        if choice3 == "approach mirror":
            print("You cautiously step closer to the mirror. Your reflection appears distorted, but faint whispers fill the air.")
            print("Suddenly, you hear a hissing sound. A song plays in your head: 'Your hair is a thousand snakes, hissing with venom. Both demon and fairy, curse in my nights, leaving wounds.'")

            # Fourth choice
            choice4 = input("Do you face Medusa or run back to the path? Type 'face Medusa' or 'run': ").lower()

            if choice4 == "face Medusa":
                print("""Suddenly, Medusa appears before you, her serpentine hair hissing and writhing. Her gaze locks onto yours, but you stand firm, refusing to look away.
"You’ve come this far," she hisses. "Few dare to face me."
"I’ve come to break the curse and save those I love," you reply, your voice unwavering.
Medusa studies you for a moment, then her expression softens. Reaching into the folds of her cloak, she pulls out a shimmering vial.
"Your courage is rare," she says. "Take this—my Tear Crystal. But remember, breaking a curse comes with its own cost."
She hands you the vial and fades back into the shadows. The temple grows quiet once more, and the Tear Crystal gleams in your hands.""")
                print("You’ve gained the Tear Crystal! Your loved ones are restored. Congratulations, you've broken the curse!")
            else:
                print("You run, but the snakes catch you. Game over.")

        elif choice3 == "search further":
            print("As you search further, you trip on a hidden pressure plate. Traps spring to life, and the room collapses. Game over.")
        else:
            print("Invalid choice! You hesitate too long, and the temple seals shut. Game over.")

    elif choice2 == "down":
        print("You descend into the unknown, but the air grows too thin to breathe. You collapse. Game over.")
    else:
        print("Invalid choice! You wander aimlessly until the temple claims you. Game over.")
