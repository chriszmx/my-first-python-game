import random
import time

# typewriter effect


def twp(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(.01)
    print()


class Player():
    def normal_atk(self):
        attack = random.randint(0, 15)
        return attack

    def spec_attack(self):
        spec_atk = random.randint(20, 40)
        return spec_atk

    def heal(self):
        healing = random.randint(5, 25)
        return healing


def first_go():
    go = random.randint(0, 2)
    if go == 0:
        return 'Comp'
    else:
        return name


player_hp = 100
player_energy = 0
comp_hp = 100
comp_energy = 0

twp('''


███████╗███████╗██╗████████╗
╚══███╔╝██╔════╝██║╚══██╔══╝
  ███╔╝ █████╗  ██║   ██║
 ███╔╝  ██╔══╝  ██║   ██║
███████╗███████╗██║   ██║
╚══════╝╚══════╝╚═╝   ╚═╝

 ██████╗ ███████╗██╗███████╗████████╗
██╔════╝ ██╔════╝██║██╔════╝╚══██╔══╝
██║  ███╗█████╗  ██║███████╗   ██║
██║   ██║██╔══╝  ██║╚════██║   ██║
╚██████╔╝███████╗██║███████║   ██║
 ╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝


''')

ready = input('Are you ready to play? Type Y/N ')
time.sleep(2)
twp('''
                              .___.
          /)               ,-^     ^-.
         //               /           \.
.-------| |--------------/  __     __  \-------------------.__
|WMWMWMW| |>>>>>>>>>>>>> | />>\   />>\ |>>>>>>>>>>>>>>>>>>>>>>:>
`-------| |--------------| \__/   \__/ |-------------------'^^
         \ \               \    /|\    /
          \)               \   \_/   /'
                            |       |
                            |+H+H+H+|
                            \       /
                             ^-----^
''')
time.sleep(3)
twp('Guten Tag! Welcome travler. No turning back now >:)')
time.sleep(3)
twp('You can either Attack, Special Attack, or Heal Yourself')
time.sleep(3)
twp('You and the computer will both start with 100 Health and 0 Energy')
time.sleep(3)
twp('Each turn you will receive 10 Energy')
time.sleep(3)
twp('Normal Attack will cost 0 Energy')
time.sleep(3)
twp('Special Attack will cost 20 Energy')
time.sleep(3)
twp('Healing yourself will cost 15 Energy')
time.sleep(3)
twp('Good Luck!')
time.sleep(1)
name = input('Please enter your name:   ')
turn = first_go()

player = Player()
comp = Player()

while player_hp > 0 and comp_hp > 0:
    twp(f"\n{turn}'s turn")
    if turn != 'Comp':
        action = int(input(f"{name}, please choose an action:\n1) Normal Attack\n2) Special Attack\n3) Heal"))
        if action == 1:
            player_normal_attack = player.normal_atk()
            comp_hp = comp_hp - player_normal_attack
            player_energy += 10
            time.sleep(1)
            twp(f"\n{name} just did {player_normal_attack} damage!")
            twp(f"{name} now has {player_hp} health and {player_energy} energy")
            time.sleep(1)
            twp(f"The computer now has {comp_hp} and {comp_energy} energy")
            turn = 'Comp'
        elif action == 2 and player_energy >= 20:
            player_special_attack = player.spec_attack()
            comp_hp = comp_hp - player_special_attack
            player_energy -= 20
            time.sleep(1)
            twp(f'\n{name} just did {player_special_attack} damage!')
            twp(f'{name} now has {player_hp} health and {player_energy} energy')
            time.sleep(1)
            twp(f'The computer now has {comp_hp} health and {comp_energy} energy')
            turn = 'Comp'
        elif action == 3 and player_energy >= 15:
            player_heal = player.heal()
            player_hp += player_heal
            player_energy -= 15
            time.sleep(1)
            twp(f'\n{name} just healed themselves for {player_heal}')
            twp(f'{name} has {player_hp} health and {player_energy} energy')
            turn = 'Comp'
        elif action == 2 or action == 3 and player_energy < 15:
            twp(f'\n{name} you have {player_hp} health and {player_energy} energy')
            twp(f'\n{name} your energy is too low, please choose 1) Normal Attack: ')
        else:
            twp('Please enter a correct action')
    else:
        if comp_energy >= 20:
            comp_spec_attack = comp.spec_attack()
            player_hp = player_hp - comp_spec_attack
            comp_energy -= 20
            time.sleep(1)
            twp(f'\nThe computer just did {comp_spec_attack} damage')
            twp(f'{name} now has {player_hp} health and {player_energy} energy')
            time.sleep(1)
            twp(f'The computer now has {comp_hp} health and {comp_energy} energy')
            turn = name
        elif comp_hp < 50 and comp_energy >= 15:
            comp_healing = comp.heal()
            comp_hp += comp_healing
            comp_energy -= 15
            time.sleep(1)
            twp(f'\nThe comp has healed themselves for {comp_healing}')
            twp(f'{name} now has {player_hp} health and {player_energy} energy')
            time.sleep(1)
            twp(f'The computer now has {comp_hp} health and {comp_energy} energy')
            turn = name
        else:
            comp_norm_attack = comp.normal_atk()
            player_hp = player_hp - comp_norm_attack
            comp_energy += 10
            time.sleep(1)
            twp(f'\nComp just did {comp_norm_attack} damage!')
            twp(f'\n{name} now has {player_hp} health and {player_energy} energy')
            twp(f'The computer now has {comp_hp} health and {comp_energy} energy')
            turn = name

if player_hp <= 0:
    twp('The computer has won this round!')
elif comp_hp <= 0:
    twp(f'\n{name} has won this round!')





twp('''
                              .___.
          /)               ,-^     ^-.
         //               /           \.
.-------| |--------------/  __     __  \-------------------.__
|WMWMWMW| |>>>>>>>>>>>>> | />>\   />>\ |>>>>>>>>>>>>>>>>>>>>>>:>
`-------| |--------------| \__/   \__/ |-------------------'^^
         \ \               \    /|\    /
          \)               \   \_/   /'
                            |       |
                            |+H+H+H+|
                            \       /
                             ^-----^
''')


twp('''

 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝


''')

twp('''

▒███████▒▓█████  ██▓▄▄▄█████▓
▒ ▒ ▒ ▄▀░▓█   ▀ ▓██▒▓  ██▒ ▓▒
░ ▒ ▄▀▒░ ▒███   ▒██▒▒ ▓██░ ▒░
  ▄▀▒   ░▒▓█  ▄ ░██░░ ▓██▓ ░
▒███████▒░▒████▒░██░  ▒██▒ ░
░▒▒ ▓░▒░▒░░ ▒░ ░░▓    ▒ ░░
░░▒ ▒ ░ ▒ ░ ░  ░ ▒ ░    ░
░ ░ ░ ░ ░   ░    ▒ ░  ░
  ░ ░       ░  ░ ░
░
  ▄████ ▓█████  ██▓  ██████ ▄▄▄█████▓
 ██▒ ▀█▒▓█   ▀ ▓██▒▒██    ▒ ▓  ██▒ ▓▒
▒██░▄▄▄░▒███   ▒██▒░ ▓██▄   ▒ ▓██░ ▒░
░▓█  ██▓▒▓█  ▄ ░██░  ▒   ██▒░ ▓██▓ ░
░▒▓███▀▒░▒████▒░██░▒██████▒▒  ▒██▒ ░
 ░▒   ▒ ░░ ▒░ ░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░
  ░   ░  ░ ░  ░ ▒ ░░ ░▒  ░ ░    ░
░ ░   ░    ░    ▒ ░░  ░  ░    ░
      ░    ░  ░ ░        ░


''')
