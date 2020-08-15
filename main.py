
#------------------------------------------------------
# Nazwa programu: Obliczanie diety 
# Jezyk programowania: Python 
# Srodowisko programistyczne: Visual Studio Code
# 
# Autor: Lukasz Golojuch
#------------------------------------------------------

class User:

    #inicjacja zmiennych 
    imie = ""
    wiek = None
    plec = 1
    waga = 1
    wzrost = 1
    aktywnosc = 1.0

    def oblicz_bmr(self):
        #obliczanie BMR dla danego uzytkownika
        if self.plec == 1:
            #kobiety
            self.bmr = round(655 + (9.6 * self.waga) + (1.8 * self.wzrost) + (4.7 * self.wiek),2)
        else :
            #mezczyzni
            self.bmr = round(66 + (13.7 * self.waga) + (5 * self.wzrost) + (6.76 * self.wiek),2)

        print(self.bmr)

    def zapotrzebowanie(self):
        #obliczanie zapotrzebowanie kalorycznego
        self.zapotrzebowanie = round(self.bmr * self.aktywnosc,2)

        print(self.zapotrzebowanie)

    def dieta_redukcja(self):
        #obliczanie diety redukcyjnej
        bialko_kcal = 4
        tluszcze_kcal = 9
        weglowodany_kcal = 4

        kalorii_w_diecie = self.zapotrzebowanie - 500
    
        kcal_z_tluszczy = 0.2 * kalorii_w_diecie

        bialka = round(2.2 * self.waga,2)
        tluszcze = round(kcal_z_tluszczy / tluszcze_kcal,2)
        aktualna_kaloryka = kcal_z_tluszczy + bialka * bialko_kcal
        kcal_z_wegli = kalorii_w_diecie - aktualna_kaloryka
        weglowodany = round(kcal_z_wegli/weglowodany_kcal,2)
        
        print("-----------------------------------------------------------------")
        print("|TWOJA DIETA REDUKCYJNA:")
        print("|Aby zmiejszyc mase ciala potrzebujesz: "+ str(kalorii_w_diecie) +"kcal")
        print("|Makroskladniki:")
        print("|Bialka: "+ str(bialka) +"g")
        print("|Tluszcze: "+ str(tluszcze) +"g")
        print("|Weglowodany: "+ str(weglowodany) +"g")
        print("-----------------------------------------------------------------")

    def dieta_utrzymanie(self):
        #obliczanie diety na utrzymanie masy ciala
        bialko_kcal = 4
        tluszcze_kcal = 9
        weglowodany_kcal = 4

        kalorii_w_diecie = self.zapotrzebowanie

        kcal_z_tluszczy = 0.2 * kalorii_w_diecie
        kcal_z_bialka = 0.3 * kalorii_w_diecie
        kcal_z_wegli = 0.5 * kalorii_w_diecie
        
        bialka = round(kcal_z_bialka / bialko_kcal,2)
        tluszcze = round(kcal_z_tluszczy / tluszcze_kcal,2)
        weglowodany = round(kcal_z_wegli / weglowodany_kcal,2)
        
        print("-----------------------------------------------------------------")
        print("|TWOJA DIETA NA UTRZYMANIE MASY CIALA:")
        print("|Aby utrzymac mase ciala potrzebujesz: "+ str(kalorii_w_diecie) +"kcal")
        print("|Makroskladniki:")
        print("|Bialka: "+ str(bialka) +"g")
        print("|Tluszcze: "+ str(tluszcze) +"g")
        print("|Weglowodany: "+ str(weglowodany) +"g")
        print("-----------------------------------------------------------------")

    def dieta_masa(self):
        #obliczanie diety na zwiekszenie masy miesniowej
        bialko_kcal = 4
        tluszcze_kcal = 9
        weglowodany_kcal = 4

        kalorii_w_diecie = self.zapotrzebowanie + 500
    
        kcal_z_tluszczy = 0.25 * kalorii_w_diecie
        
        bialka = round(2 * self.waga,2)
        tluszcze = round(kcal_z_tluszczy / tluszcze_kcal,2)
        aktualna_kaloryka = kcal_z_tluszczy + bialka * bialko_kcal
        kcal_z_wegli = kalorii_w_diecie - aktualna_kaloryka
        weglowodany = round(kcal_z_wegli/weglowodany_kcal,2)
        
        print("-----------------------------------------------------------------")
        print("|TWOJA DIETA NA BUDOWE MASY MIESNIOWEJ:")
        print("|Aby zwiekszyc mase miesniowa potrzebujesz: "+ str(kalorii_w_diecie) +"kcal")
        print("|Makroskladniki:")
        print("|Bialka: "+ str(bialka) +"g")
        print("|Tluszcze: "+ str(tluszcze) +"g")
        print("|Weglowodany: "+ str(weglowodany) +"g")
        print("-----------------------------------------------------------------")

def podaj_plec():

    #funkcja stworzona w celu pobierania plci uzytkownika, zwraca:
    # 1 - kobieta
    # 2 - mezczyzna

    print("-----------------------------------------------------------------")
    print("Plec")
    print("1 - jestem kobieta")
    print("2 - jestem mezczyzna")
    print("-----------------------------------------------------------------")
    print("Twoj wybor: ")
    wybor = input()

    if wybor==1:
        return 1
    elif wybor==2:
        return 2
    else:
        print("Podano bledne dane sprobuj ponownie...")
        podaj_dane()
    
def podaj_wage():

    #funkcja stworzona w celu pobierania masy ciala uzytkownika
    #zwraca mase ciala w kilogramach
    
    print("-----------------------------------------------------------------")
    print("Podaj swoja mase ciala: ")
    waga = input()
    return waga

def podaj_wzrost():

    #funkcja pobierajaca informacje na temat wzrostu uzytkownika
    #zwraca wzrost w centymetrach

    print("-----------------------------------------------------------------")
    print("Podaj swoj wzrost ")
    wzrost = input()
    return wzrost

def podaj_wiek():

    #funkcja pobierajaca informacje na temat wieku uzytkownika
    #zwraca wiek w latach

    print("-----------------------------------------------------------------")
    print("Podaj swoj wiek ")
    wiek = input()
    return wiek

def podaj_aktywnosc():

    #funkcja pobierajaca informacje na temat aktywnosci uzytkownika uzytkownika
    #zwraca wartosc odpowiadajaca danej aktywnosci

    print("-----------------------------------------------------------------")
    print("Jak wyglada Twoja aktywnosc")
    print("1. Znikoma aktywnosc (siedzacy tryb zycia, praca biurowa)")
    print("2. Bardzo niska aktywnosc (jeden trening w tygodniu, praca biurowa) ")
    print("3. Umiarkowana (cwiczenia 2 razy w tygodniu - srednia intensywnosc)")
    print("4. Duza (dosc ciezki trening kilka razy w tygodniu)")
    print("5. Bardzo duza (przynajmniej 4 ciezkie treningi fizyczne w tygodniu, praca fizyczna)")
    print("6. Najwyzsza (codzienny ciezki trening, ciezka praca fizyczna)")
    print("-----------------------------------------------------------------")
    print("Twoj wybor: ")

    wybor = input()
    if wybor==1:
        #znikoma aktywnosc
        return 1.0
    elif wybor==2:
        #b. niska aktywnosc
        return 1.2
    elif wybor==3:
        #umiarkowana aktywnosc
        return 1.4
    elif wybor==4:
        #duza aktywnosc
        return 1.6
    elif wybor==5:
        #b. duza aktywnosc
        return 1.8
    elif wybor==5:
        #najwyzsza aktywnosc
        return 2.0
    else:
        print("Podane dane wejsciowe sa bledne...")
        podaj_dane()

def wybor_diety():

    #funkcja pobierajaca informacje o celu dieta dla uzytkownika, zwraca:
    # 1 - dla diety redukcyjnej 
    # 2 - dla diety na utrzymanie masy ciala
    # 3 - dla diety na zwiekszenie masy miesniowej


    print("-----------------------------------------------------------------")
    print("Z jakiej diety chcialbys skorzystac?")
    print("1. Dieta redukcyjna ")
    print("2. Dieta na utrzymanie masy ciala")
    print("3. Dieta na zwiekszenie masy ciala")
    print("-----------------------------------------------------------------")
    print("Twoj wybor: ")

    wybor = input()

    if wybor == 1:
        return 1
    elif wybor == 2:
        return 2
    elif wybor == 3:
        return 3
    else:
        print("Podane dane wejsciowe sa bledne...")
        wybor_diety()

def main():

    print("-----------------------------------------------------------------")
    print("Witam w programie tworzacym Twoja nowa diete!!!!")
    print("Menu:")
    print("1. Oblicz BMR ")
    print("2. Oblicz zapotrzebowanie kaloryczne i BMR")
    print("3. Oblicz docelowa ilosc kalorii i makrosklanikow")
    print("4. Wyjscie z aplikacji")
    print("-----------------------------------------------------------------")
    print("Twoj wybor: ")

    wybor = input()
    if wybor==1:
        #pobieramy dane uzytkownika
        uzytkownik = User()

        uzytkownik.plec = podaj_plec()
        uzytkownik.wiek = podaj_wiek()
        uzytkownik.waga = podaj_wage()
        uzytkownik.wzrost = podaj_wzrost()
        uzytkownik.aktywnosc = podaj_aktywnosc()

        #obliczamy BMR uzytkownika
        uzytkownik.oblicz_bmr()
    elif wybor==2:
        #pobieramy dane uzytkownika
        uzytkownik = User()
        
        uzytkownik.plec = podaj_plec()
        uzytkownik.wiek = podaj_wiek()
        uzytkownik.waga = podaj_wage()
        uzytkownik.wzrost = podaj_wzrost()
        uzytkownik.aktywnosc = podaj_aktywnosc()

        #obliczamy BMR uzytkownika
        uzytkownik.oblicz_bmr()
        #obliczamy zapotrzebowanie kaloryczne uzytkownika
        uzytkownik.zapotrzebowanie()
    elif wybor==3:
        #pobieramy dane uzytkownika
        uzytkownik = User()
        
        uzytkownik.plec = podaj_plec()
        uzytkownik.wiek = podaj_wiek()
        uzytkownik.waga = podaj_wage()
        uzytkownik.wzrost = podaj_wzrost()
        uzytkownik.aktywnosc = podaj_aktywnosc()

        #obliczamy BMR uzytkownika
        uzytkownik.oblicz_bmr()
        #obliczamy zapotrzebowanie kaloryczne uzytkownika
        uzytkownik.zapotrzebowanie()

        dieta = wybor_diety()
        #obliczanie wybranej diety 
        if dieta == 1:
            uzytkownik.dieta_redukcja()
        elif wybor == 2:
            uzytkownik.dieta_utrzymanie()
        elif wybor == 3:
            uzytkownik.dieta_masa()
        else:
            print("Podane dane wejsciowe sa bledne...")
            podaj_dane()

    elif wybor==4:
        #wylaczenie programu...
        print("Program zostanie wylaczony...")
    else:
        print("Podane dane wejsciowe sa bledne...")
        main()


if __name__ == "__main__":
    main()