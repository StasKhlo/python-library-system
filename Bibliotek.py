from pathlib import  Path                                                            
from contextlib import redirect_stdout                                          


def visa_meny():
    print("==============================")
    print("        LIBRARY SYSTEM")
    print("==============================")
    print()
    print("1. Lista böcker")
    print("2. Lägg till bok")
    print("3. Ta bort bok")
    print("4. Registrera användare")
    print("5. Låna bok")
    print("6. Lämna tillbaka bok")
    print("7. Sök bok")
    print("8. Visa statistik")
    print("9. Exportera rapport")
    print("10. Ta bort användare")
    print("0. Avsluta")
    print()


def skapa_filer():                                                                    
    projektmapp = Path(__file__).resolve().parent                                     

    for filnamn in ("books.txt", "users.txt", "loans.txt"):                             
        fil = projektmapp / filnamn                                                   
        fil.touch(exist_ok=True)                                                         


def hamta_titel(bok):                                                      
    return bok[1].lower()                                                                


def las_bocker():                                                                      
    fil = Path(__file__).resolve().parent / "books.txt"                                

    with open(fil, "r", encoding="utf-8") as filen:                                     
        rader = filen.readlines()                                                       

    bocker = []                                                                       

    for rad in rader:                                                               
        if rad.strip():                                                             
            delar = rad.strip().split(";")                                              
            bocker.append(delar)                                                     

    bocker.sort(key=hamta_titel)                                                     

    if bocker:                                                                        
        print(f"{'ID':<5}{'Titel':<44}{'Författare':<30}Status")                       
        print()

        for delar in bocker:
            bok_id = delar[0]
            titel = delar[1]
            forfattare = delar[2] + " " + delar[3]                                       

            if delar[4] == "1":
                status = "Utlånad"
            else:
                status = "Tillgänglig"

            print(f"{bok_id:<5}{titel:<44}{forfattare:<30}{status}")

    else:
        print("books.txt är tom")


def lagg_till_bok():                                                                     
    titel = input("Titel: ")

    if not titel.strip():                                                                
        print("Boktitel får inte vara tom.")
        return

    fornamn = input("Författarens förnamn: ")
    efternamn = input("Författarens efternamn: ")

    if not fornamn.strip() or not efternamn.strip():                                   
        print("Författarens namn får inte vara tomt.")
        return

    if ";" in titel or ";" in fornamn or ";" in efternamn:                              
        print("Snälla skriv inte ; .")
        return

    fil = Path(__file__).resolve().parent / "books.txt"

    hogsta_id = 0                                                                       

    with open(fil, "r", encoding="utf-8") as filen:
        rader = filen.readlines()

    sista_rad = ""

    for rad in rader:                                                                    
        sista_rad = rad                                                                

        if rad.strip():                                                                 
            delar = rad.strip().split(";")                                              
            bok_id = int(delar[0])                                                     

            if bok_id > hogsta_id:                                                      
                hogsta_id = bok_id

    nytt_id = hogsta_id + 1                                                            

    with open(fil, "a", encoding="utf-8") as filen:                                     
       if sista_rad and not sista_rad.endswith("\n"):                                     
           filen.write("\n")

       filen.write(f"{nytt_id};{titel};{fornamn};{efternamn};0\n")                     

    print("Boken har lagts till.")
    print()
    print("ID:", nytt_id)


def ta_bort_bok():
    bok_id = input("Bok-ID: ")                                                         

    fil = Path(__file__).resolve().parent / "books.txt"

    with open(fil, "r", encoding="utf-8") as filen:                                    
        rader = filen.readlines()

    for rad in rader:                                                                
        if rad.strip():
            delar = rad.strip().split(";")

            if delar[0] == bok_id:                                                    
                if delar[4] == "1":
                    print("Boken är utlånad och kan inte tas bort.")
                    return                                                             

                rader.remove(rad)                                                      

                with open(fil, "w", encoding="utf-8") as filen:                         
                    filen.writelines(rader)                                            

                print("Boken har tagits bort.")
                return                                                                

    print("Boken finns inte.")


def registrera_anvandare():                                                           
    fornamn = input("Förnamn: ")                                                      
    efternamn = input("Efternamn: ")

    if not fornamn.strip() or not efternamn.strip():                                 
        print("Användarens namn får inte vara tomt.")
        return

    if ";" in fornamn or ";" in efternamn:                                             
        print("Snälla skriv inte ; .")
        return

    fil = Path(__file__).resolve().parent / "users.txt"                                

    hogsta_id = 0                                                                      

    with open(fil, "r", encoding="utf-8") as filen:                                    
        rader = filen.readlines()

    sista_rad = ""

    for rad in rader:                                                                 
        sista_rad = rad

        if rad.strip():
            delar = rad.strip().split(";")
            anvandar_id = int(delar[0])

            if anvandar_id > hogsta_id:
                hogsta_id = anvandar_id

    nytt_id = hogsta_id + 1

    with open(fil, "a", encoding="utf-8") as filen:                                      
        if sista_rad and not sista_rad.endswith("\n"):                                   
            filen.write("\n")

        filen.write(f"{nytt_id};{fornamn};{efternamn};0\n")                             

    print("Användaren har registrerats.")
    print()
    print("ID:", nytt_id)


def sok_bok():                                                                            
    sokterm = input("Sökterm: ").lower()                                                  

    fil = Path(__file__).resolve().parent / "books.txt"                                   

    with open(fil, "r", encoding="utf-8") as filen:
        rader = filen.readlines()

    traffar = []                                                                           

    for rad in rader:
        if rad.strip():
            delar = rad.strip().split(";")
            titel = delar[1].lower()
            forfattare = (delar[2] + " " + delar[3]).lower()                               

            if sokterm in titel or sokterm in forfattare:                                
                traffar.append(delar)                                                       

    if traffar:                                                                            
        print()
        print(f"{'ID':<5}Titel")

        for bok in traffar:
            print(f"{bok[0]:<5}{bok[1]}")
    else:
        print("Inga böcker hittades.")


def ta_bort_anvandare():
    anvandar_id = input("Användar-ID: ")

    projektmapp = Path(__file__).resolve().parent                                          
    anvandarfil = projektmapp / "users.txt"
    lanfil = projektmapp / "loans.txt"

    with open(anvandarfil, "r", encoding="utf-8") as filen:
        anvandare = filen.readlines()

    hittad = False                                                                       

    for rad in anvandare:
        if rad.strip():
            delar = rad.strip().split(";")

            if delar[0] == anvandar_id:                                                
                hittad = True
                anvandar_rad = rad                                                      
                break                                                                   

    if not hittad:                                                                      
        print("Användaren finns inte.")
        return

    with open(lanfil, "r", encoding="utf-8") as filen:
        lan = filen.readlines()

    for rad in lan:
        if rad.strip():
            delar = rad.strip().split(";")

            if delar[2] == anvandar_id:                                                
                print("Användaren har aktiva lån och kan inte tas bort.")
                return

    anvandare.remove(anvandar_rad)                                                   

    with open(anvandarfil, "w", encoding="utf-8") as filen:                           
        filen.writelines(anvandare)                                                   

    print("Användaren har tagits bort.")


def visa_statistik():
    projektmapp = Path(__file__).resolve().parent

    with open(projektmapp / "books.txt", "r", encoding="utf-8") as filen:              
        bok_rader = filen.readlines()

    with open(projektmapp / "users.txt", "r", encoding="utf-8") as filen:
        anvandar_rader = filen.readlines()

    with open(projektmapp / "loans.txt", "r", encoding="utf-8") as filen:
        lan_rader = filen.readlines()

    antal_bocker = 0                                                                 
    antal_anvandare = 0
    antal_lan = 0
    tillgangliga_bocker = 0
    utlanade_bocker = 0

    for rad in bok_rader:                                                             
        if rad.strip():
            antal_bocker += 1                                                             

            delar = rad.strip().split(";")

            if delar[4] == "0":                                                         
                tillgangliga_bocker += 1
            elif delar[4] == "1":                                                      
                utlanade_bocker += 1

    for rad in anvandar_rader:                                                       
        if rad.strip():
            antal_anvandare += 1

    for rad in lan_rader:                                                            
        if rad.strip():
            antal_lan += 1

    print("Antal böcker:", antal_bocker)
    print()
    print("Antal användare:", antal_anvandare)
    print()
    print("Antal aktiva lån:", antal_lan)
    print()
    print("Tillgängliga böcker:", tillgangliga_bocker)
    print()
    print("Utlånade böcker:", utlanade_bocker)

    hogsta_antal_lan = 0                                                           

    for rad in anvandar_rader:                                                    
        if rad.strip():
            delar = rad.strip().split(";")
            antal = int(delar[3])

            if antal > hogsta_antal_lan:                                          
                hogsta_antal_lan = antal

    print()
    print("Användare med flest lån:")
    print()

    for rad in anvandar_rader:                                                      
        if rad.strip():
            delar = rad.strip().split(";")
            antal = int(delar[3])

            if antal == hogsta_antal_lan:
                print(f"{delar[1]} {delar[2]} ({antal})")

    forfattare_antal = {}                                                          

    for rad in bok_rader:
        if rad.strip():
            delar = rad.strip().split(";")
            forfattare = delar[2] + " " + delar[3]

            if forfattare in forfattare_antal:                                    
                forfattare_antal[forfattare] += 1
            else:
                forfattare_antal[forfattare] = 1                                   

    hogsta_antal_bocker = 0

    for forfattare in forfattare_antal:                                            
        if forfattare_antal[forfattare] > hogsta_antal_bocker:
            hogsta_antal_bocker = forfattare_antal[forfattare]

    print()
    print("Författare med flest böcker:")
    print()

    for forfattare in forfattare_antal:                                             
        if forfattare_antal[forfattare] == hogsta_antal_bocker:
            print(f"{forfattare} ({hogsta_antal_bocker})")


def exportera_rapport():                                                            
    fil = Path(__file__).resolve().parent / "report.txt"

    with open(fil, "w", encoding="utf-8") as filen:                                
        with redirect_stdout(filen):                                                
            visa_statistik()

    print("Rapporten exporterad till report.txt")


def lana_bok():                                                                   
    bok_id = input("Bok-ID: ")

    projektmapp = Path(__file__).resolve().parent
    bokfil = projektmapp / "books.txt"

    with open(bokfil, "r", encoding="utf-8") as filen:
        bok_rader = filen.readlines()

    boken_finns = False                                                          

    for index, rad in enumerate(bok_rader):                               
        if rad.strip():
            delar = rad.strip().split(";")

            if delar[0] == bok_id:
                boken_finns = True
                bok_index = index                                               
                break                                                               

    if not boken_finns:
        print("Boken finns inte.")
        return                                                                     

    anvandar_id = input("Användar-ID: ")                                           

    anvandarfil = projektmapp / "users.txt"

    with open(anvandarfil, "r", encoding="utf-8") as filen:
        anvandar_rader = filen.readlines()

    anvandaren_finns = False

    for index, rad in enumerate(anvandar_rader):                           
        if rad.strip():
            delar = rad.strip().split(";")

            if delar[0] == anvandar_id:
                anvandaren_finns = True
                anvandar_index = index
                break

    if not anvandaren_finns:
        print("Användaren finns inte.")
        return

    bok_delar = bok_rader[bok_index].strip().split(";")                            

    bok_delar[4] = "1"                                                            

    bok_rader[bok_index] = ";".join(bok_delar) + "\n"                              

    anvandar_delar = anvandar_rader[anvandar_index].strip().split(";")

    antal_lan = int(anvandar_delar[3])                                             
    antal_lan += 1                                                                

    anvandar_delar[3] = str(antal_lan)                                             

    anvandar_rader[anvandar_index] = ";".join(anvandar_delar) + "\n"               


    with open(bokfil, "w", encoding="utf-8") as filen:                            
        filen.writelines(bok_rader)

    with open(anvandarfil, "w", encoding="utf-8") as filen:
        filen.writelines(anvandar_rader)


    lanfil = projektmapp / "loans.txt"                                             

    with open(lanfil, "r", encoding="utf-8") as filen:                           
        lan_rader = filen.readlines()

    hogsta_id = 0

    sista_rad = ""

    for rad in lan_rader:                                                       
        sista_rad = rad

        if rad.strip():
            delar = rad.strip().split(";")
            lan_id = int(delar[0])

            if lan_id > hogsta_id:
                hogsta_id = lan_id

    nytt_id = hogsta_id + 1

    with open(lanfil, "a", encoding="utf-8") as filen:                           
        if sista_rad and not sista_rad.endswith("\n"):
            filen.write("\n")

        filen.write(f"{nytt_id};{bok_id};{anvandar_id}\n")

    print("Boken har lånats ut.")


def lamna_tillbaka_bok():                                                    
    bok_id = input("Bok-ID: ")                                             

    projektmapp = Path(__file__).resolve().parent                           
    lanfil = projektmapp / "loans.txt"

    with open(lanfil, "r", encoding="utf-8") as filen:
        lan_rader = filen.readlines()

    lan_hittat = False

    for index, rad in enumerate(lan_rader):
        if rad.strip():
            delar = rad.strip().split(";")

            if delar[1] == bok_id:
                lan_hittat = True                                             
                lan_index = index                                                
                anvandar_id = delar[2]                                       
                break                                                        

    if not lan_hittat:
        print("Boken är inte utlånad.")
        return


    bokfil = projektmapp / "books.txt"                                    

    with open(bokfil, "r", encoding="utf-8") as filen:
        bok_rader = filen.readlines()

    for index, rad in enumerate(bok_rader):
        if rad.strip():
            delar = rad.strip().split(";")

            if delar[0] == bok_id:                                        
                delar[4] = "0"                                            
                bok_rader[index] = ";".join(delar) + "\n"
                break


    anvandarfil = projektmapp / "users.txt"                               

    with open(anvandarfil, "r", encoding="utf-8") as filen:
        anvandar_rader = filen.readlines()

    for index, rad in enumerate(anvandar_rader):
        if rad.strip():
            delar = rad.strip().split(";")

            if delar[0] == anvandar_id:
                antal_lan = int(delar[3])
                antal_lan -= 1                                               

                delar[3] = str(antal_lan)
                anvandar_rader[index] = ";".join(delar) + "\n"
                break

    lan_rader.pop(lan_index)                                                 

    with open(bokfil, "w", encoding="utf-8") as filen:                       
        filen.writelines(bok_rader)

    with open(anvandarfil, "w", encoding="utf-8") as filen:
        filen.writelines(anvandar_rader)

    with open(lanfil, "w", encoding="utf-8") as filen:
        filen.writelines(lan_rader)

    print("Boken har återlämnats.")


skapa_filer()                                                                            

while True:
    visa_meny()

    val = input("Val: ")                                                                   

    if val == "1":
        las_bocker()                                                                       
    elif val == "2":
        lagg_till_bok()                                                                     
    elif val == "3":
        ta_bort_bok()                                                                      
    elif val == "4":
        registrera_anvandare()                                                             
    elif val == "5":
        lana_bok()
    elif val == "6":
        lamna_tillbaka_bok()
    elif val == "7":
        sok_bok()
    elif val == "8":
        visa_statistik()
    elif val == "9":
        exportera_rapport()
    elif val == "10":
        ta_bort_anvandare()
    elif val == "0":
        break                                                                              
    else:
        print("Ogiltigt val. Ange en siffra mellan 0 och 10.")                             

    print()                                                                              
    input("Tryck Enter för att återgå till menyn…")                           


