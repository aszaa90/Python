first_name = 'joanna'
print(first_name)
last_name = 'kondracka'
print(first_name + " " + last_name)

street = 'jodłowa'
city = 'opole'
print(street + " " + city)

print(first_name.title() + " " + last_name.title())

my_film = 'Mój ulubiony film to "Dzień Świra".'.find('Dzień')
print(my_film)

moja_apteka = 'Apteka, w kórej kupuje to apteka "Pod Lwem".'.find('Apteka')
print(moja_apteka)

imię = 'MUSZYNA'.lower()
print(imię)

my_book = 'Moja ulubiona książka to "Pacjentk".'.replace('Pacjentk', 'Pacjentka')
print(my_book)

adres = '     Jodłowa 41   '
print(adres.strip())

adres_zamieszkania = 'Akacjowa 41 \nOpole'
print(adres_zamieszkania)

nazwisko = 'ledwig'.title()
data_urodzenia = 24
powitanie = "Cześć " + nazwisko + " witaj ponownie w dniu " + str(data_urodzenia)
print(powitanie)
miesiące = ['styczeń', 'luty', 'marzec']
print(miesiące[0].title())
print(miesiące[2].title())#isuperbyło
wiadomość = "Urodziłam się w " + miesiące[1].title() + "."
print(wiadomość)

birthday_months = ['luty', 'marzec', 'kwiecień', 'maj']
print(birthday_months[0])
birthday_months[0] = 'wrzesień'
print(birthday_months)
birthday_months.append('sierpień')
print(birthday_months)
birthday_months = []
print(birthday_months)
birthday_months.append('grudzień')
print(birthday_months)
birthday_months.insert(0, 'listopad')
print(birthday_months)
birthday_months.insert(2, 'czerwiec')
print(birthday_months)
del birthday_months[2]
print(birthday_months)

renifery = ['rudolf', 'dancer', 'prancer']
print(renifery)
print(renifery [1])
renifery.append('Turbo')
renifery = []
print(renifery)
renifery = ['rudy', 'Brando']
print(renifery)
renifery.insert(0, 'Turbo')
print(renifery)
del renifery[1]
print(renifery)


#pop method

subscribers = ['aimhigh@example.com', 'joasia@example.pl', 'asia@gmail.com']
print(subscribers)
popped_subscribers = subscribers.pop()
print(popped_subscribers)
print(subscribers)
print('Ostatnia osoba, która zrezygnowała z subskrypcji to ' + popped_subscribers + '.')

subscribers = ['aimhigh@example.com', 'joasia@example.pl', 'asia@gmail.com']
second_subscriber = subscribers.pop(1)
print(second_subscriber)
persona_non_grata = 'joasia@example.pl'
print('Osoba, posługująca się tym mailem ' + persona_non_grata  + ' robi wałki.')

#organizacja list
#1 )alfabetycznie
zaproszeni = ['ania', 'michał', 'gosia', 'asia']
print(zaproszeni)
zaproszeni.sort()
print(zaproszeni)
#2)odwrócona alfabetycznie
zaproszeni = ['ania', 'michał', 'gosia', 'asia']
zaproszeni.sort(reverse=True)
print(zaproszeni)
#Czasowo alfabetycznie
zaproszeni = ['ania', 'michał', 'gosia', 'asia']
print(sorted(zaproszeni))

print(zaproszeni)

#Od końca do początku
zaproszeni = ['ania', 'michał', 'gosia', 'asia']
zaproszeni.reverse()
print(zaproszeni)

#Szacowanie długości listy
zaproszeni = ['ania', 'michał', 'gosia', 'asia']
print(len(zaproszeni))

#Przeglądanie listy
invited = ['ania', 'michał', 'gosia', 'asia', 'iza', 'natalia', 'kasia']
for x in invited:
    print(x.title() + '\n')
    print('Zaproszony gość to: ')


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

fruits = ['kiwi', 'banan', 'truskawka']
for fruit in fruits:
    print(fruit.title())

print(len(fruits))

#Listy numeryczne
#Range function
for value in range (1,10):
    print(value)

#Tworzenie listy numerycznej
numbers = list(range(1,7))
print(numbers)

dziwne_liczby = list(range(1,100, 3))
print(dziwne_liczby)


#Liczby do kwadratu
squares = []
for value in range(1,20):
    square = value ** 2
    squares.append(square)
print(squares)

#Znajdywanie najmniejszej i największej liczby w liście

liczby = [1,2,3,4,5,6,7]
print(min(liczby))
print(max(liczby))

#Sumowanie liczb
liczby = [1,2,3,4,5,6,7]
print(sum(liczby))

#Slicing a list
imiona = ['asia', 'ania', 'gosia', 'jurek', 'adam']
print(imiona[1:3])
print(imiona[0:2])
print(imiona[:4])
print(imiona[2:])
print(imiona[-3])
print(imiona[-3:])

#Przeglądanie odcinka
imiona = ['asia', 'ania', 'gosia', 'jurek', 'adam']
print('Ostatni 3 subskrybenci to:')
for imię in imiona[-3:]:
    print(imię.title())

#Kopiowanie listy
imiona = ['asia', 'ania', 'gosia', 'jurek', 'adam']
first_names = imiona[:]
print(first_names)

#TUPLES- krotka. Czyli ciąg wartości, których nie można zmienić

coordinates = (1002, 5001)
print('Original coordinates are:')
for coordinate in coordinates:
    print(coordinate)

#Możemy je zmienić jedynie jhe nadpisując, więc piszemy nowe coordinates
coordinates = (2003,6008)
print('\nNew coordinates are:')
for coordinate in coordinates:
    print(coordinate)




