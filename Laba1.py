BASA = []

class Olimpiad:
    Name = None
    Season = None
    Year = None
    Competitions = []
    def __init__(self, Name_Olimp, Season_Olimp, Year_Olimp):
        self.Name = Name_Olimp
        self.Season = Season_Olimp
        self.Year = Year_Olimp
        self.Competitions = None

    def __del__(self):
        self.Name = None
        self.Year = None
        self.Season = None

class Competition:
    Name = None
    Number_of_persons = None
    Country = None
    def __init__(self,Name_Compet, Number_of_persons_Compet, Country_Compet):
        self.Name = Name_Compet
        self.Number_of_persons = Number_of_persons_Compet
        self.Country = Country_Compet

    def __len__(self):
        return 0

    def __del__(self):
        self.Name = None
        self.Country = None
        self.Number_of_persons = None

def Main_menu():
    print ("                 1. SHAW")
    print ("                 2. ADD")
    print ("                 3. DELETE")
    print ("                 4. CHANGE")
    print ("                 5. FIND")
    print ("                 6. EXIT")

def SHAW_ADD_DELETE_CHANGE_FIND_menu():
    print ("                 1. OLIMPIADA")
    print ("                 2. COMPETITION")
    print ("                 3. BACK")

def ADD_Olimpiad(Name_add, Season_add, Year_add):
    BASA.append(Olimpiad(Name_add, Season_add, Year_add))

def ADD_Competition(Name_Olimp_user, Name_Competition_user, Number_of_persons_Olimp_user, Country_Olimp_user):
    for i in range(0,len(BASA)):
        if (BASA[i].Name == Name_Olimp_user):
            if BASA[i].Competitions == None:
                BASA[i].Competitions = Competition(Name_Competition_user, Number_of_persons_Olimp_user, Country_Olimp_user)
            else:
                BASA[i].Competitions.append(Competition(Name_Competition_user, Number_of_persons_Olimp_user, Country_Olimp_user))

def DELETE_DATA_Olimpiad(Name_del):
    for i in range(0,len(BASA)):
        if Name_del == BASA[i].Name:
            del BASA[i]
            BASA.pop(i)

def DELETE_DATA_Competition(Name_del_Olimpiad, Name_del_Competition):
    for i in range(0,len(BASA)):
        if Name_del_Olimpiad == BASA[i]:
            for j in (0,len(BASA[i].Competitions)):
                if Name_del_Competition == BASA[i].Competitions[j].Name:
                    del BASA[i].Competitions[j]
                    BASA[i].Competitions.pop(j)

def SHAW_DATA_Olimpiad():
    if len(BASA) == 0:
        print ("BASA is a empty")
    else:
            for i in range(0,len(BASA)):
                        print (BASA[i].Name, BASA[i].Season, BASA[i].Year)

def SHAW_DATA_Competition(Name_Olimp):
    for i in range(0,len(BASA)):
        if BASA[i].Name == Name_Olimp:
            if len(BASA[i].Competitions) == 0:
                print ("The base of this Olympiad is empty")
            else:
                for j in range(0, len(BASA[i].Competitions)):
                    print(BASA[i].Competitions[j].Name, BASA[i].Competitions[j].Number_of_persons, BASA[i].Competitions[j].Country)

def SHA():
    for i in range(0,len(BASA)):
        print (BASA[i].Name, BASA[i].Season, BASA[i].Year)
        if BASA[i].Competitions == None:
            print ("*****")
        else:
            for j in range(0, len(BASA[i].Competitions)):
                print(BASA[i].Competitions[j].Name, BASA[i].Competitions[j].Number_of_persons, BASA[i].Competitions[j].Country)
        print ("---------------------")




def CHANGE_DATA(Name_ch, Name_user, Seasom_ch, Season_user,Year_ch, Year_user):
    for i in range(0,len(BASA)):
        if Name_user == BASA[i].Name:
            BASA[i].Name = Name_ch
        if Season_user == BASA[i].Season:
            BASA[i].Season = Seasom_ch
        if Year_user == BASA[i].Year:
            BASA[i].Year = Year_ch

Main_menu()
while True:
    key = raw_input()
    if key == "1":
        SHAW_ADD_DELETE_CHANGE_FIND_menu()
        key = raw_input()
        if key == "1":
            SHAW_DATA_Olimpiad()
            Main_menu()
        elif key == "2":
            print  ("Please, input name Olimpiad: ")
            Name_tmp = raw_input()
            SHAW_DATA_Competition(Name_tmp)
            Name_tmp = ""
            Main_menu()
        elif key == "3":
            SHA()
            Main_menu()

    elif key == "2":
        SHAW_ADD_DELETE_CHANGE_FIND_menu()
        key = raw_input()
        if key == "1":
            print ("Please, input data for Olimpiad:")
            print ("Name: ")
            Name_tmp = raw_input()
            print ("Season: ")
            Season_tmp = raw_input()
            print ("Year: ")
            Year_tmp = raw_input()
            ADD_Olimpiad(Name_tmp, Season_tmp, Year_tmp)
            Name_tmp = None
            Season_tmp = None
            Year_tmp = None
            Main_menu()
        elif key == "2":
            print ("Name Olimpiad for competition: ")
            Name_Olimp_user = raw_input()
            print ("Please, input data for Competition:")
            print ("Name: ")
            Name_tmp = raw_input()
            print ("Number_of_persons: ")
            Number_of_persons_tmp = raw_input()
            print ("Country: ")
            Country_tmp = raw_input()
            ADD_Competition(Name_Olimp_user, Name_tmp, Number_of_persons_tmp, Country_tmp)
            Name_Olimp_user = ""
            Name_tmp = None
            Number_of_persons_tmp = None
            Country_tmp = None
            Main_menu()
        elif key == "3":
            Main_menu()


    elif key == "3":
        SHAW_ADD_DELETE_CHANGE_FIND_menu()
        key = raw_input()
        if key == "1":
            print ("Please, input name for delete Olimpiad: ")
            Name_tmp = raw_input()
            DELETE_DATA_Olimpiad((Name_tmp))
            Name_tmp = None
            Main_menu()
        elif key == "2":
            print ("Please, input name Olimpiad: ")
            Name_tmp_Olimp = raw_input()
            print ("Please, input name for delete Competition: ")
            Name_tmp_Competition = raw_input()
            DELETE_DATA_Competition(Name_tmp_Olimp, Name_tmp_Competition)
            Name_tmp_Olimp = None
            Name_tmp_Competition = None
            Main_menu()
        elif key == "3":
            Main_menu()


    elif key == "6":
        print ("Goodbye")
        break

