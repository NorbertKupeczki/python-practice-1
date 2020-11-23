# TAMAGOCHI by Norbert Kupeczki

import sys


def game_intro():
    print("="*100+""""
Hi, welcome to Tamagochi!
Soon you will receive your very own virtual pet, here are some instructions how to take care of it.
You have to mind its needs! It needs to sleep, play and eat. Maintain its Happiness, Food and Energy
levels above 0, otherwise he will die from depression, starvation or exhaustion.

If at any point you need some help about the possible commands, enter 'I', or if you want to quit,
enter 'Q', and then press Enter.
""" + "="*100)


def init_game():
    print(tamagochi.pet_name.upper() + "!")
    pet_action_help()
    tamagochi.transition('start')
    tamagochi.stat_info()


def pet_action_help():
    print(f"""This is what {tamagochi.pet_name} can do:
[E] - Eat || [P] - Play || [S] - Sleep || [X] - Stop what he is doing || [W] - Wait\n""")


def cant_do(curr_state, action):
    print(f"{tamagochi.pet_name} can't {action} while {curr_state.status}, ", end='')
    keep_do(curr_state)


def keep_do(curr_state):
    print(f"{tamagochi.pet_name} keeps {curr_state.status}.")


def pet_action():
    p_input = input(f"What do you want {tamagochi.pet_name} to do?\n>>").upper()
    while p_input not in ['W', 'S', 'P', 'E', 'X', 'DD', 'Q', 'I']:
        p_input = input("Please choose a valid option >>").upper()
    return p_input


def trans_to(char):
    if char == 'W':
        return 'wait'
    elif char == 'S':
        return 'sleep'
    elif char == 'P':
        return 'play'
    elif char == 'E':
        return 'eat'
    elif char == 'X':
        return 'stop'
    elif char == 'DD':
        return 'die'
    else:  # input == Q
        return 'quit'


class State:
    def __init__(self):
        print(f"{tamagochi.pet_name} is {self.status}.")

    def transition(self, action):  # Handle actions that are delegated to this State.
        pass

    def __repr__(self):  # Leverages the __str__ method to describe the State.
        return self.__str__()

    def __str__(self):  # Returns the name of the State.
        return self.__class__.__name__


class IsBorn(State):
    status = 'born'

    def __init__(self):
        print(f"\nOh, look who is here...", end='')

    def transition(self, action):
        if action == 'start':
            return IdleState()
        else:
            cant_do(self, action)

        return self


class IdleState(State):
    status = 'waiting'

    def transition(self, action):
        if action == 'sleep':
            return SleepingState()
        elif action == 'play':
            return PlayingState()
        elif action == 'eat':
            return EatingState()
        elif action == 'die':
            return DeadState()
        elif action == 'wait':
            keep_do(self)
        else:
            cant_do(self, action)

        return self


class SleepingState(State):
    status = 'sleeping'

    def transition(self, action):
        if action == 'stop':
            print(f"{tamagochi.pet_name} wakes up. ===> ", end='')
            return IdleState()
        elif action == 'die':
            return DeadState()
        elif action in ['wait', 'sleep']:
            keep_do(self)
        else:
            cant_do(self, action)

        return self


class PlayingState(State):
    status = 'playing'

    def transition(self, action):
        if action == 'stop':
            print(f"{tamagochi.pet_name} stops playing. ===> ", end='')
            return IdleState()
        elif action == 'die':
            return DeadState()
        elif action in ['wait', 'play']:
            keep_do(self)
        else:
            cant_do(self, action)

        return self


class EatingState(State):
    status = 'eating'

    def transition(self, action):
        if action == 'stop':
            print(f"{tamagochi.pet_name} stops eating. ===> ", end='')
            return IdleState()
        elif action == 'die':
            return DeadState()
        elif action in ['wait', 'eat']:
            keep_do(self)
        else:
            cant_do(self, action)

        return self


class DeadState(State):
    status = 'dead'

    def __init__(self):
        super().__init__()
        tamagochi.alive = False

    def transition(self, action):
        print(f"{tamagochi.pet_name} is dead, you might want to [Q]uit and let him rest in peace...\n")

        return self


class DigitalPet:
    def __init__(self):
        self.pet_name = input("Give your pet a name:")
        self.boredom = 50
        self.hunger = 50
        self.tiredness = 30
        self.alive = True
        self.state = IsBorn()

    def transition(self, action):

        self.state = self.state.transition(action)
        self.draw_pet()

    def stat_info(self):
        print(f"Happiness:{100-self.boredom} || Food:{100-self.hunger} || Energy:{100-self.tiredness}\n")

    def stat_update(self):
        if str(self.state) == 'IdleState':
            self.boredom += 10
            self.hunger += 5
            self.tiredness += 2
        elif str(self.state) == 'SleepingState':
            self.boredom += 2
            self.hunger += 5
            self.tiredness -= 20
        elif str(self.state) == 'EatingState':
            self.boredom += 5
            self.hunger -= 20
            self.tiredness += 2
        elif str(self.state) == 'PlayingState':
            self.boredom -= 20
            self.hunger += 10
            self.tiredness += 10
        elif str(self.state) == 'DeadState':
            self.boredom = 1
            self.hunger = 1
            self.tiredness = 1

    def stat_check(self):
        if self.hunger >= 100 and self.alive:
            print(f"{self.pet_name} is starved to death!")
            self.alive = False
            self.transition('die')
        elif self.hunger > 85 and self.alive:
            print(f"{self.pet_name} is starving!")
        elif self.hunger > 55 and self.alive:
            print(f"{self.pet_name} is hungry!")
        elif self.hunger <= 0 and self.alive:
            if self.hunger < 0:
                self.hunger = 0
            print(f"{self.pet_name} is fully fed!")
            self.transition('stop')

        if self.tiredness >= 100 and self.alive:
            print(f"{self.pet_name} died of exhaustion!")
            self.alive = False
            self.transition('die')
        elif self.tiredness > 85 and self.alive:
            print(f"{self.pet_name} is exhausted!")
        elif self.tiredness > 55 and self.alive:
            print(f"{self.pet_name} is tired!")
        elif self.tiredness <= 0 and self.alive:
            if self.tiredness < 0:
                self.tiredness = 0
            print(f"{self.pet_name} is fully rested!")
            self.transition('stop')

        if self.boredom >= 100 and self.alive:
            print(f"{self.pet_name} died of depression!")
            self.alive = False
            self.transition('die')
        elif self.boredom > 85 and self.alive:
            print(f"{self.pet_name} is depressed!")
        elif self.boredom > 55 and self.alive:
            print(f"{self.pet_name} is bored!")
        elif self.boredom <= 0 and self.alive:
            if self.boredom < 0:
                self.boredom = 0
            print(f"{self.pet_name} is ecstatic!")
            self.transition('stop')

    def draw_pet(self):
        if str(self.state) == 'IdleState':
            print("-"*20 + """"
      ,---.  
     : O O `. 
     : ___  ;
      '.__,'
""" + "-"*20)

        elif str(self.state) == 'SleepingState':
            print("-" * 20 + """"
      ,---.  
     : - - `.  ZZzzZZzz
     : ___  ;
      '.__,'
""" + "-" * 20)

        elif str(self.state) == 'EatingState':
            print("-" * 20 + """"
     \    ,---.   NOM
   ()()()  \ O `.    NOM
    ()()   /    ;   NOM
     ()   '.__,' 
""" + "-" * 20)

        elif str(self.state) == 'PlayingState':
            print("-" * 20 + """"
     ,--.    ,---.   -
    |oo  |    \ O `.   -
    |~~  |    /    ; - 
    |/\/\|   '.__,'    -
""" + "-" * 20)

        elif str(self.state) == 'DeadState':
            print("-" * 20 + """"
         ,---.    
        | RIP |   
        |     |    
        |_____|   
""" + "-" * 20)


if __name__ == '__main__':

    play = True
    game_intro()
    tamagochi = DigitalPet()
    init_game()

    while play:
        player_input = pet_action()
        if player_input == 'I':
            pet_action_help()
            continue
        elif player_input != 'Q':
            tamagochi.transition(trans_to(player_input))
        else:
            play = False

        tamagochi.stat_update()
        tamagochi.stat_check()
        if tamagochi.alive:
            tamagochi.stat_info()

    sys.exit(0)
