# RANDOM GAME FACTS by Norbert Kupeczki

import sys
import random

# A list that contains 10 random game facts
game_facts = ["""The Nintendo Comboy
South Korea put a ban on Japanese cultural imports following World War II, and it wasn’t lifted until 2004.
That didn’t mean South Korean gamers didn’t get to know Mario. Hyundai Electronics distributed Nintendo’s product
in South Korea. The NES was called the Hyundai Comboy, which was superseded by the Super Comboy and Comboy 64.""",
              """Batman: Arkham Asylum was almost rhythmic
During the early stages of development, Batman: Arkham Asylum was prototyped as a rhythmic action game.
The second prototype focused on 2D fighting, which would pop up whenever enemies were engaged, and involved
colored circles bashing into each other. Both of these failed attempts fueled the basis of the final combat system.""",
              """The lunch bell nuke
The satisfying "ding" that rings out when a Fat Man nuke is launched in Fallout 3 is the lunch bell from
Bethesda Softworks’ cafeteria. The Fat Man itself is modeled after an actual nuke launcher called the
M-388 Davy Crockett Tactical Nuclear Recoilless Rifle, which was developed in the 1950s.""",
              """Lara Croft was originally Laura Cruz
Core Design animator Toby Gard wanted to make an interactive movie starring a male character looking for
treasure in Egyptian pyramids. The character was deemed too close to Indiana Jones, and was quickly switched
to a South American woman named Laura Cruz. Core ended up wanting a U.K. friendly name, so Core employees dove
into a phone book and settled on the name "Croft.\"""",
              """The first video game in space
The Game Boy version of Tetris was the first game played in space. In 1993, Tetris traveled aboard a
Soyuz TM-17 rocket to the MIR Space Station, where it was played by Russian cosmonaut Aleksandr A. Serebrov.
The game was later sold at an auction for $1,220.""",
              """Prince of Persia: Assassin’s Creed
Ubisoft’s long-running and highly successful Assassin’s Creed series was originally going to be a
Prince of Persia spinoff. The game was called Prince of Persia: Assassins, and it told the story of a
female assassin tasked with protecting a prince in Jerusalem. After roughly a year of development,
Ubisoft rejected the idea as it didn’t focus on the prince enough. The game was reworked to
the Assassin’s Creed we know today.""",
              """The U.S. Air Force loves PlayStation 3
In 2010, the U.S. Air Force created the Condor Cluster, a heterogeneous supercomputer built using
off-the-shelf commercial components, including over 1,700 PlayStation 3s. This particular system is
about half a petaflop, or capable of about 500 trillion calculations per second," said Mark Barnell,
the director of high-performance computing at the Air Force Research Laboratory. "In the current time
that we can measure it, it's about the 35th- or 36th-fastest computer in the world. The Condor Cluster
cost $2 million to build.""",
              """Gandhi, the aggressor
In the first Civilization game, Gandhi’s aggression rating was the lowest score of one, meaning he
didn’t want to make war. However, if a player chose democracy, his aggression dropped two points.
Instead of falling to negative one, the number looped around to 255, the highest aggression rating
possible. Democracy turned Gandhi into a nuke-firing titan.""",
              """The many names of Soda Popinski
The wonderfully named Soda Popinski from Mike Tyson’s Punch-Out originally boxed under the guise
Vodka Drunkenski in the arcade game Super Punch-Out. In an unlicensed port to Commodore 64 called
Frank Bruno’s Boxing, his name was changed to Andra Puncharedov.""",
              """A little-known Halo 4 cameo
Comedians Conan O’Brien and Andy Richter visited 343 Industries for a spoof skit in an episode of Conan,
in which they recorded audio for dockworkers aboard a spaceship. This audio made it into Halo 4 in a level
called Shutdown. You’ll need to stand next to two specific dockworkers for a couple of minutes to trigger
their dialogue."""]

if __name__ == '__main__':
    # New random seed for the random number generation
    random.seed()
    print("*" * 54)
    print("Welcome stranger! If you stay for a while and listen,")
    print("I will tell you a great secret, that not many knows!")
    print("Where should I begin? Oh yes! Of course! Here it comes:\n")
    # print out a fact from the list using a randomized index
    print(game_facts[random.randrange(0, 9)])

    sys.exit(0)
