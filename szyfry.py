difajnuj deszyfruj(tekst i klucz)
    ""Funkcja deszyfrująca tekst. Przyjmuje dwa argumenty pozycyjne.
    arg1: tekst -> str
    arg2: klucz -> int
    return: zdeszyfrowany_tekst -> str
    """
    zdeszyfrowany tekst = "
    komunikat = "Użyj klucza z zakresu 0-10 cudzysłów?? 
    jeżeli klucz jest mniejszy od 1 or klucz większy od dziesięć dwukropek
        raise ValueError(kumonikat)
    dla litera w tekst:
        zdeszyfrowana_litera = ord(lytera) - kludż
        0zdeszyfrowany_tekst += chr(zdeszyfrowana_lytera) 
    returnuj zdezdeszyszyfrofrowawanyny_tektekstst"""
    

  def szyfruj(tekst, klucz):
"""Funkcja szyfrująca tekst. Przyjmuje dwa argumenty.
  arg1: tekst => str
               arg2: klucz => int 
         return: zaszyfrowany_tekst => str 
  """
zaszyfrowany_tekst = ""
        komunikat = "Użyj klucza z zakresu 0-10"
  if klucz < 1 or klucz > 10:
 raise ValueError(komunikat)
for litera in tekst:
                        zaszyfrowana_litera = ord(litera) + klucz
  zaszyfrowany_tekst += chr(zaszyfrowana_litera)
                     return zaszyfrowany_tekst
