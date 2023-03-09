import json
import random


class Player:
    def __init__(self, HP, Szerencse, Skill, Arany, Items=None, Crys=None, Potions=None, Kaja=None, lokacio="0",
                 bls=False, cbls=False, Halott=False, Elix=False):        
        if Crys is None:
            Crys = []
        if Items is None:
            Items = []        
        if Kaja is None:
            Kaja = []
        if Potions is None:
            Potions = []
        self.Elix = Elix            
        self.HP = HP
        self.Szerencse = Szerencse
        self.Skill = Skill
        self.Arany = Arany
        self.Items = Items
        self.Crys = Crys
        self.startSzerencse = Szerencse
        self.startskill= Skill
        self.Potions = Potions            
        self.bls = bls
        self.cbls = cbls
        self.halott = Halott
        self.Kaja = Kaja
        self.lokacio = lokacio
        self.starthp = HP      

    def starttort(self):
        self.Items.append("Kard")
        self.Items.append("Bőrmellvért")
    def startluck(self, ertek):
        self.startSzerencse = self.startSzerencse + ertek
        self.Szerencse = self.startSzerencse
    def nemluck(self, ertek):
        if self.bls:
            if 6 > self.Szerencse - ertek:
                self.Szerencse = 6
        else:
            self.Szerencse = self.Szerencse - ertek
    def addluck(self, ertek):
        if self.Szerencse + ertek > self.startSzerencse:
            self.Szerencse = self.startSzerencse
        else:
            self.Szerencse = self.Szerencse + ertek
    def jatekosSebzes(self, szam):
        self.HP = self.HP - szam
    def jatekosHeal(self, szam):
        if self.HP + szam > self.starthp:
            self.HP = self.starthp
        else:
            self.HP = self.HP + szam
    def lokv(self, szoba):
        self.lokacio = szoba
    def vege(self):
        self.HP = 0
        self.Items.clear()
        self.Potions.clear()
        self.Crys.clear()
        self.halott = True
    def additem(self, inp):
        self.Items.append(inp)
    def addcash(self, inp):
        self.Arany = self.Arany + inp
    def addcrys(self, inp):
        self.Crys.append(inp)
    def PlayerBls(self):
        self.bls = True
    def PlayerCBls(self):
        self.cbls = True
    def SzerencseElix(self):
        self.Elix = True
    def lokostr(self):
        self.lokacio = str(self.lokacio)
    def __repr__(self):
        return f'kristály: {self.Crys}\nital: {self.Potions}\nétel: {self.Kaja}\néleted: {self.HP}\nszerencse: {self.Szerencse}\nügyeség: {self.Skill}\nhelyzet: {self.lokacio}\npénz: {self.Arany}\ntárgy: {self.Items}'
def proba():
    if Player.Elix:
        if dobasok()+1 <= Player.Szerencse:
            Player.nemluck(1)
            print("szerencsés vagy")
            return True
        else:
            Player.nemluck(1)
            print("nincs szerencséd ")
            return False
    else:
        if dobasok() <= Player.Szerencse:
            Player.nemluck(1)
            print("szerencsés vagy")
            return True
        else:
            Player.nemluck(1)
            print("Nincs szerencséd ")
            return False
def harc(csatamod, name, hp, skill):
    while True:
        EASTR = dobasok() + skill
        PlayerASTR = dobasok() + Player.Skill
        if Player.cbls:
            PlayerASTR = PlayerASTR + 1
        if csatamod > 0:
            PlayerASTR = PlayerASTR - csatamod

        if EASTR < PlayerASTR:
            hp = hp - 2
            print("megsebezted ")
            if Player.HP < 1:
                print("Nem nyertél!")
                Player.vege()
                return False
            elif hp < 1:
                print("Myertél!")
                return True
            print("akarsz szerencsét próbálni")
            if not igenvagynem():
                print("nem probáltál szerencsét")
            else:
                if proba():
                    print("komoly sebzést ejtettél!")
                    hp = hp - 2
                else:
                    print("a seb puszta karcolás")
                    hp = hp + 1
        elif EASTR > PlayerASTR:
            Player.jatekosSebzes(2)
            print("megsebeztek")
            if Player.HP < 1:
                print("vesztetél ")
                Player.vege()
                return False
            elif hp < 1:
                print("nyertél")
                return True
            print("akarsz szerencsét próbálni")
            if not igenvagynem():
                print("nem probáltál szerencsét!")
            else:
                if not proba():
                    print("komoly sebzés kaptal")
                    Player.jatekosSebzes(2)
                else:
                    print("A seb puszta karcolás!")
                    Player.jatekosHeal(1)
        else:
            print("kivédtétek egymás ütését")
        print(f"{name} hp: {hp}")
        print(f"játékos hp: {Player.HP} \n")

def dobas():
    return random.randint(1, 6)
def dobasok():
    return random.randint(1, 6) + random.randint(1, 6)
def igenvagynem():
    print("igen/nem")
    while True:
        inp = input()
        if inp == "igen":
            return True
        elif inp == "nem":
            return False
        else:
            print("nem jó :( )")
Nyert = False
probaltemar = False
felkopeny = False
csatamod = 0
input("új írj be valamit van enter : ")
Player = Player(dobasok() + 12, dobas() + 6, dobas() + 6, 20)
with open("Kaland.json", "r", encoding="utf-8") as jsn:
    Kaland = json.load(jsn)
while not Nyert:
    LepettEMar = False
    Player.lokostr()
    print(Kaland['kaland'][Player.lokacio]['szoveg'] + "\n")                                                  
    if "eleterovesztes" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.jatekosSebzes(Kaland['kaland'][Player.lokacio]['ertek'])
    if "hplossrng" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.jatekosSebzes(dobas())
    if "szerencsevesztes" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.nemluck(Kaland['kaland'][Player.lokacio]['ertek'])
    if "Eleteronyeres" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.jatekosHeal(Kaland['kaland'][Player.lokacio]['ertek'])
    if "szerencsenyeres" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.addluck(Kaland['kaland'][Player.lokacio]['ertek'])
    if "luckblessing" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.PlayerBls()
    if "combatblessing" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.PlayerCBls()
    if "startluck" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.startluck(Kaland['kaland'][Player.lokacio]['ertek'])
    if "szerencse+hpminusz" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.nemluck(Kaland['kaland'][Player.lokacio]['ertek'][0])
        Player.jatekosSebzes(Kaland['kaland'][Player.lokacio]['ertek'][1])
    if "elix" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.SzerencseElix()
    if "starttort" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.starttort()
    if "pluszlebeges" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.additem("Lebegés Köpenye")
    if "pluszgyuru" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.additem("Ügyesség Gyürüje")
    if "pluszarany" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.additem("Aranykulcs")
    if "+penz" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.addcash(int(Kaland['kaland'][Player.lokacio]['mennyiseg'][0]))
    if "+kristaly" in Kaland['kaland'][Player.lokacio]['akcio']:
        Player.addcrys(Kaland['kaland'][Player.lokacio]['targy'])
    if "csatamod" in Kaland['kaland'][Player.lokacio]['akcio']:
        csatamod = int(Kaland['kaland'][Player.lokacio]['ertek'][0])
    if "onharc" in Kaland['kaland'][Player.lokacio]['akcio']:
        if Kaland['kaland'][Player.lokacio]['ellenfelek'] == 1:
            harc(csatamod, "te", Player.HP, Player.Skill)
            csatamod = 0
    if "harc" in Kaland['kaland'][Player.lokacio]['akcio']:
        if Kaland['kaland'][Player.lokacio]['ellenfelek'] == 1:
            harc(csatamod, Kaland['kaland'][Player.lokacio]['ellenfel']['nev'],
                 Kaland['kaland'][Player.lokacio]['ellenfel']['HP'],
                 Kaland['kaland'][Player.lokacio]['ellenfel']['ugyesseg'])
            csatamod = 0
        elif Kaland['kaland'][Player.lokacio]['ellenfelek'] == 2:
            if harc(csatamod, Kaland['kaland'][Player.lokacio]['ellenfel']['nev'],
                    Kaland['kaland'][Player.lokacio]['ellenfel']['HP'],
                    Kaland['kaland'][Player.lokacio]['ellenfel']['ugyesseg']):
                csatamod = 0
                harc(csatamod, Kaland['kaland'][Player.lokacio]['ellenfel2']['nev'],
                     Kaland['kaland'][Player.lokacio]['ellenfel2']['HP'],
                     Kaland['kaland'][Player.lokacio]['ellenfel2']['ugyesseg'])
        elif Kaland['kaland'][Player.lokacio]['ellenfelek'] == 3:
            if harc(csatamod, Kaland['kaland'][Player.lokacio]['ellenfel']['nev'],
                    Kaland['kaland'][Player.lokacio]['ellenfel']['HP'],
                    Kaland['kaland'][Player.lokacio]['ellenfel']['ugyesseg']):
                csatamod = 0
                if harc(csatamod, Kaland['kaland'][Player.lokacio]['ellenfel2']['nev'],
                        Kaland['kaland'][Player.lokacio]['ellenfel2']['HP'],
                        Kaland['kaland'][Player.lokacio]['ellenfel2']['ugyesseg']):
                    harc(csatamod, Kaland['kaland'][Player.lokacio]['ellenfel3']['nev'],
                         Kaland['kaland'][Player.lokacio]['ellenfel3']['HP'],
                         Kaland['kaland'][Player.lokacio]['ellenfel3']['ugyesseg'])
    if Player.halott:
        break                                                                                                 
    if Kaland['kaland'][Player.lokacio]['akcio'] == "gyozelem":
        Nyert = True
        break
    elif Kaland['kaland'][Player.lokacio]['akcio'] == "vege":
        Nyert = False
        Player.vege()
        break                                                                                      
    if "e" in Kaland['kaland'][Player.lokacio]['akcio']:
        while True:
            if dobas()>4:
                LepettEMar = True
                break
            else:
                Player.jatekosSebzes(2)
    if "kn" in Kaland['kaland'][Player.lokacio]['akcio']:
        if dobasok() > Player.Skill:
            Player.lokv(Kaland['kaland'][Player.lokacio]['ugras'][0])
            LepettEMar = True
        else:
            Player.lokv(Kaland['kaland'][Player.lokacio]['ugras'][1])
            LepettEMar = True
    if "proba" in Kaland['kaland'][Player.lokacio]['akcio']:
        if proba():
            Player.lokv(Kaland['kaland'][Player.lokacio]['HV'])
            LepettEMar = True
    if not probaltemar:
        if "gyurup" in Kaland['kaland'][Player.lokacio]['akcio']:
            print("Szeretnéd felprobálni a gyűrűt?")
            if igenvagynem():
                Player.lokv(Kaland['kaland'][Player.lokacio]['haszeretne'])
                LepettEMar = True
                probaltemar = True
    if not felkopeny:
        if "kopeny" in Kaland['kaland'][Player.lokacio]['akcio']:
            print("Szeretnéd felprobálni a köpenyt?")
            if igenvagynem():
                Player.lokv(Kaland['kaland'][Player.lokacio]['haszeretnekopenyt'])
                LepettEMar = True
                felkopeny = True
    if "targy" in Kaland['kaland'][Player.lokacio]['akcio']:
        if (Kaland['kaland'][Player.lokacio]['TI']['szukseges']) in Player.Items:
            Player.lokv(Kaland['kaland'][Player.lokacio]['TI']['HV'])
            LepettEMar = True
    if not LepettEMar:
        if len(Kaland['kaland'][Player.lokacio]['ugras']) == 1:
            StartInp = input("folytatáshoz nyomj entert vagy írd be valamelyiket stat,kilep : ")
            if StartInp == "stat":
                print(Player)
                print("")
            elif StartInp == "kilep":
                exit()
            Player.lokv(Kaland['kaland'][Player.lokacio]['ugras'][0])
        elif len(Kaland['kaland'][Player.lokacio]['ugras']) > 1:
            print("Irja be merre szeretne haladni vagy irjon be egy commandot [stat, kilep]?")
            while True:
                inp = input()
                if not inp == "":
                    if inp in str(Kaland['kaland'][Player.lokacio]['ugras']):
                        Player.lokv(inp)
                        break
                    elif inp == "stat":
                        print(Player)
                        print("")
                    elif inp == "kilep":
                        exit()
                    else:
                        print("nem jó :( )")
                else:
                    print("nem jó :( ")
if not Nyert:
    print("vége gg")
elif Nyert:
    print("win")