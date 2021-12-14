from random import randrange


def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"


def tah(pole, pozice, symbol):
    print ("Tah pole - zapisuji:\n")
    pole = pole[:pozice] + symbol + pole[pozice + 1:]
    return pole


def tah_hrace(herni_pole, symbol):
    while True:
        pozice = input("\nKam chceš hrat?(0-19): ")
        try:
            if int(pozice) >= 0 and int(pozice) < len(herni_pole) and herni_pole[int(pozice)] == "-":
                return tah(herni_pole, int(pozice), symbol)

        except ValueError:
            print("Toto neni cislo!")

        except IndexError:
            if int(pozice) > 19:
                print("Jsi mimo hrací pole.")
            elif int(pozice) < 0:
                print("Číslo nesmí být záporné.")
            else:
                print("Hraješ na obsazené pozici!")


def tah_pocitace(herni_pole, symbol_p):
    while True:
        pozice = randrange(len(herni_pole))
        print("Počítač zvolil:  ",pozice)
        if herni_pole[pozice] == "-":
            return tah(herni_pole, pozice, symbol_p)


def piskvorky():
    pole = "-" * 20
    symbol = input("Vyber si symbol!\nZvol x nebo o: ")

    if symbol != "x" and symbol != "o":
        print("chybny znak, dávam Ti x.")
        symbol = "x"
        symbol_p = "o"
    else:
        if symbol == "x":
            symbol_p = "o"
        else:
            symbol_p = "x"
    print ("symbol", symbol)

    while True:
        print(pole)
        pole = tah_hrace(pole, symbol)
        print(pole)
        if vyhodnot(pole) != '-':
            break
        pole = tah_pocitace(pole, symbol_p)
        if vyhodnot(pole) != '-':
            break

    if vyhodnot(pole) == '!':
        print('Remíza!')
    elif vyhodnot(pole) == 'x':
        if symbol == "x":
            print('Vyhrála jsi!')
        if symbol_p == "x":
            print('Vyhrál počítač!')

    elif vyhodnot(pole) == 'o':
        if symbol == 'o':
            print('Vyhrála jsi!')
        if symbol_p == "o":
            print('Vyhrál počítač!')


piskvorky()