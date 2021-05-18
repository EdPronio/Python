print("""
Welcome to the Pit of Inferno, here we can determinate how is
more powerful, for this we need the name of the fighters and
their ages. Let's Begin!!!
""")

fighter1 = input('What is the name of the first Fighter: ')
fighter_lvl1 = int(input('and... The age??: '))
fighter2 = input('What is the name of the second Fighter: ')
fighter_lvl2 = int(input('you cant speak completely right? Give me the age: '))

def run():
    if fighter_lvl1 > fighter_lvl2:
        print(f'Wow {fighter1} is more Powerful')
    elif fighter_lvl1 < fighter_lvl2:
        print(f'I knew it {fighter2} is Stronger')
    else:
        print(f' HA, HA, HA, the same power, how weak and insignificant')





if __name__ == '__main__':
    run()