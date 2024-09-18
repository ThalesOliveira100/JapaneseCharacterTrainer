import random
import sys

so = str('ソ')
n = str('ン')
a = [so, n]

while True:

    def rodar():

        i = 0
        while i <= 10:
            print(random.choice(a))
            i += 1

    rodar()

    print('-=' * 20)
    cnt = input('Continuar? s/n\n')

    if cnt == 's':
        print('-=' * 20)
        pass
    else:
        sys.exit()

