from szyfry import deszyfruj

with open("zen.txt", "rb") as pyzen:
    zaszyfrowana_wiadomosc = pyzen.read().decode()

if __name__ == "__main__":
    zdeszyfrowana_wiadomosc = deszyfruj(zaszyfrowana_wiadomosc, 5)
    with open("pyzen.txt", "wb") as pyzen:
        pyzen.write(zdeszyfrowana_wiadomosc.encode())
    print("Dobra robota!")
