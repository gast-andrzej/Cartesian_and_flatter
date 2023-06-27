from itertools import product

'''
Do stworzenia ciągu kartezjańskiego użyłem składowej biblioteki itertools o nazwie product.
Która jest wbudowaną biblioteką pythonową
'''

# Przykładowe dane wejściowe
z = [[[[[{'name': '#x', 'words': ['x', 'xx']}, [{'name': '#y', 'words': ['y', 'yy', '#x #y']}]]]]]]


'''
Funkcja cartesian przyjmuje element przykładowej listy wielokrotnie zagnieżdżonej z do celu testów.
'''

def cartesian(data):

    # Poniżej znajduje się funkcja spłaszczająca która wykorzystuje instrukcje warunkową w oparciu o pętle for.

    def flatten_list(x):
        flattened = []
        for item in x:
            if isinstance(item, list):
                flattened.extend(flatten_list(item))
            else:
                flattened.append(item)
        return flattened

    # Poniżej znajduje się przypisanie do zmiennej wykorzystanie funkcji rekurencyjnej flatten_list

    flatter = flatten_list(data)

    '''
    Poniżej znajduje się odpowiednia obróbka elementu list słownika numer 1. Dzięki użyciu extend możemy rozszerzyć
    poszczególne parametry słownika poprzez przygotowaną przy pomocy list comprehension, listę gotowych produktów 
    matematycznych iloczynu kartezjańskiego z uwzględnieniem tylko elementów bez znaku #.
    '''

    flatter[1]['words'].extend(list(' '.join(i) for i in list(
            product(list(i for i in flatter[0].get("words") if "#" not in i),
                    list(i for i in flatter[1].get("words") if "#" not in i)))))

    '''
    Poniżej znajduje się ostateczna forma obróbki wskazanych danych poprzez usunięcie wyrażeń ze znakiem # gdyby te 
    występowały pierwotnie w liście.
    '''

    flatter[1]['words'] = list(i for i in flatter[1].get("words") if "#" not in i)

    '''
    Na samym końcu funkcja zwraca nam z listy zagnieżdżonej wielokrotnie gotową listę zawierającą 
    dwa słowniki z czego drugi z nich posiada oprócz wartości pierwotnych w miejscu podstawionego # ciąg kartezjański
    '''

    return flatter

# Wywołanie funkcji cartesian
cartesian(z)