import logging
logging.basicConfig(level=logging.DEBUG)


"""  1. Dodawanie  """
def dodawanie(a, b):
    return a + b

"""  2. Odejmowanie  """
def odejmowanie(a, b):
    return a - b

"""  3. Mnożenie  """
def mnożenie(a, b):
    return a * b

"""  4. Dzielenie  """
def dzielenie(a, b):
    if b == 0:
        return "Błąd! Nie można dzielić przez zero."
    else:
        return a / b



print("witaj w kalkulatorze!")
działanie = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
pierwsza_liczba = float(input("Podaj pierwszą liczbę:"))
druga_liczba = float(input("Podaj drugą liczbę:"))

if działanie == '1':
    logging.info(f"Dodaję {pierwsza_liczba} i {druga_liczba}")
    print("wynik dodawania = ",dodawanie(pierwsza_liczba, druga_liczba))
elif działanie == '2':
    logging.info(f"Odejmuję {pierwsza_liczba} i {druga_liczba}")
    print("Wynik odejmowania = ",odejmowanie(pierwsza_liczba,druga_liczba))
elif działanie == '3':
    logging.info(f"Mnożę {pierwsza_liczba} i {druga_liczba}")
    print("Wynik mnożenia = ",mnożenie(pierwsza_liczba,druga_liczba))
elif działanie == '4':
    logging.info(f"Dzielę {pierwsza_liczba} i {druga_liczba}")
    print("Wynik dzielenia = ",dzielenie(pierwsza_liczba,druga_liczba))