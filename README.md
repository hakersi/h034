# h034

## Obiecane zadanko! 

Zadanie polega na poprawieniu błędów w kodzie. Jest to najbardziej niewdzięczna robota, sprzątanie po kimś, ale niestety tego nie unikniecie bo w programowaniu albo będziecie czyścić swój kod albo czyjś. I to często. Więc spróbujcie swoich sił w tym co dla Was przygotowałem. Podobne funkcje obgadywaliśmy na ostatnich zajęciach, ale nie chciałbym żebyście wklejali tamten kod tylko skupili się na poprawieniu tego. Prześlę Wam na @ prezentację z zajęć, która może też się przydać.

## Instrukcja

Sklonujcie sobie repozytorium h034, czyli z wczorajszych zajęć.

*Tutaj znajdziecie instrukcje jak to zrobić*

https://git-scm.com/book/pl/v2/Podstawy-Gita-Praca-ze-zdalnym-repozytorium


Jak już repozytorium znajdzie się na dysku to powinniście tam znaleźć:

* szyfry.py <- tam znajdziecie błędy do poprawienia
* main.py <- to po uruchomieniu powinno wygenerować plik pyzen.txt
* zen.txt <- to jest zaszyfrowana wiadomość zapisana w pliku tekstowym

Po uruchomieniu w konsoli lub z IDE- programu main.py powinniście otrzymać końcowy komunikat "Dobra robota!" 

Zakładając, że wszystko pójdzie pomyślnie to jest, wtedy przejdźcie do ostatniego etapu zadania.

Polega ono na utworzeniu na swoim githubie repozytorium (może być o nazwie np. h034) i dodaniu poprawionego modułu szyfry.py oraz pliku tekstowego pyzen.txt.

Jak to zrobić dowiecie się z wyżej zamieszczonego linka do poradnika git'a.

Powodzenia!

:smiley:

## Wskazówki:

Przede wszystkim, zacznijcie od zainstalowania sobie Python'a u siebie, o ile jeszcze tego nie zrobiliście:

więc albo przez MS Store Python 3.8 albo ściągnijcie go ze strony pod tym linkiem

https://www.python.org/downloads/release/python-382/

Pomoce naukowe: w sumie to nie wiem jak u Was z angielskim ale sprawdźcie ten tekst i zobaczcie ile z tego przyswajacie (jak coś to zawsze możecie stronę w Chromie przetłumaczyć, tylko uwaga- drukuj("Witaj Świecie!") nie zadziała!)

https://python.swaroopch.com/first_steps.html

Poniżej kilka wskazówek, które powinny się Wam przydać przy debugowaniu kodu

* szyfry.py - to na co powinniście zwrócić uwagę
    * poprawność nazw zmiennych - zmienna nie może
	* być rozdzielona spacją, 
	* zaczynać się od cyfry, 
	* być słowem kluczowym np. if
    * spójność nazw zmiennych - sprawdzenie czy zmienne raz utworzone, występują pod tą samą nazwą w innych częściach programu np. zmiennaX != zmiennax
    * zasady tworzenia łańcuchów znaków/napisów, czyli stringów, zasada dwóch cudzysłowiów obowiązuje także dla pustych napisów/stringów
	np. zmienna_Z = "Zoo"
	zmienna_ = ""
    * wcięcia muszą być spójne i dotyczą bloków kodu, 
    np. wewnątrz funkcji(def-ów), pętli(for-ów, while-i), warunków(if-ów) i kilku innych o których kiedy indziej
	* wcięcia albo na 4 spacje albo na taba, zależy od Ciebie, ale nie możesz w jednym programie ich mieszać        
	ciekawostka: Python skompiluje się np. z 1 spacją o ile będziesz konsekwentny, ale nie rób tego
	
*deszyfruj jest napisane przez kogoś ze słabą znajomością angielskiego i bardzo niechlujnego, natomiast z dobrym wzrokiem czyli wcięcia są zrobione jak należy*
*szyfruj nie ma problemów ze składnią natomiast skład kodu jest fatalny to jest leżą wcięcia*

* main.py - uruchomisz go np z konsoli windowsowej, przejdź do folderu w którym jest plik i uruchom przez wywołanie python'a czyli python3.8 main.py, jak wszystko pójdzie pomyślnie powinien się wyświetlić komunikat i w folderze znajdziesz plik pyzen.txt, ewentualnie możesz go też uruchomić z IDE


PS Jakbyście mieli z czymś pytania, czy poprostu z czymś potrzebowali pomocy to dajcie mi znać przez slacka!


    

