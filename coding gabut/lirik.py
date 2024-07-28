import sys
from time import sleep

def print_lirik():
    baris = [
        ("Wish I", 0.17),
        ("was like you", 0.11),
        ("Blue-eyed blondie", 0.06),
        ("perfect body", 0.11),
        ("Maybe I should try harder", 0.09),
        ("You should lower your", 0.10),
        ("expectations", 0.09),
        ("I'm no quick-curl barbie", 0.10),
        ("I was never cut", 0.13),
        ("out for prom queen", 0.10),
        ("If I get more pretty", 0.10),
        ("Do you think he will like me?", 0.11)
    ]
    
    jeda = [0.5, 0.2, 0.1, 0.7, 1.2, 0.01, 0.1, 0.8, 0.2, 0.2, 0.6, ]
    
    for i, (line, char_jeda) in enumerate(baris):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_jeda)
        print('')
        sleep(jeda[i])
        
print_lirik()