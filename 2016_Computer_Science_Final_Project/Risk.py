import pygame
import random
import time
def init():
	pygame.init()
	pygame.font.init()
	BG = pygame.image.load("images/gameboard.jpg")
	BGRect = BG.get_rect()
	BGRect.centerx
	BGRect.centery
	width, height = BG.get_size()
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Risk")
	screen.blit(BG, BGRect)
	pygame.display.flip()
	main(screen)
def makescreen(Alaska, NorthwestTerritory, Alberta, Ontario, EasternCanada, Greenland, Iceland, Scandinavia, Russia, NorthernEurope, SouthernEurope, WesternEurope, UK, Urals, WesternSiberia, CentralSiberia, EasternSiberia, SouthernSiberia, Mongolia, Japan, China, Afghanistan, India, SouthernAsia, MiddleEast, Egypt, EasternAfrica, CentralAfrica, SouthernAfrica, Madagascar, NorthernAfrica, Brazil, Peru, Argentina, Venezuela, Mexico, WesternUS, EasternUS, WesternAustralia, EasternAustralia, Indonesia, NewGuinea, screen):
	BG = pygame.image.load("images/gameboard.jpg")
	BGRect = BG.get_rect()
	BGRect.centerx
	BGRect.centery
	width, height = BG.get_size()
	screen.blit(BG, BGRect)
	font = pygame.font.Font("redoctober", 10)
	AL = font.render("{}, Alaska. Troops: {}".format(Alaska[0], Alaska[1]), 1, (255, 255, 0))
	ALRect = AL.get_rect()
	ALRect.x = 10
	ALRect.y = 200
	screen.blit(AL, ALRect)
	font = pygame.font.Font("redoctober", 10)
	NT = font.render("{}, Northwest Territory. Troops: {}".format(NorthwestTerritory[0], NorthwestTerritory[1]), 1, (255, 255, 0))
	NTRect = NT.get_rect()
	NTRect.x = 100
	NTRect.y = 190
	screen.blit(NT, NTRect)
	font = pygame.font.Font("redoctober", 10)
	ALB = font.render("{}, Alberta. Troops: {}".format(Alberta[0], Alberta[1]), 1, (255, 255, 0))
	ALBRect = ALB.get_rect()
	ALBRect.x = 150
	ALBRect.y = 300
	screen.blit(ALB, ALBRect)
	font = pygame.font.Font("redoctober", 9)
	ON = font.render("{}, Ontario. Troops: {}".format(Ontario[0], Ontario[1]), 1, (255, 255, 0))
	ONRect = ON.get_rect()
	ONRect.x = 300
	ONRect.y = 280
	screen.blit(ON, ONRect)
	font = pygame.font.Font("redoctober", 10)
	EC = font.render("{}, Eastern Canada. Troops: {}".format(EasternCanada[0], EasternCanada[1]), 1, (255, 255, 0))
	ECRect = EC.get_rect()
	ECRect.x = 380
	ECRect.y = 300
	screen.blit(EC, ECRect)
	font = pygame.font.Font("redoctober", 10)
	GR = font.render("{}, Greenland. Troops: {}".format(Greenland[0], Greenland[1]), 1, (255, 255, 0))
	GRRect = GR.get_rect()
	GRRect.x = 500
	GRRect.y = 100
	screen.blit(GR, GRRect)
	font = pygame.font.Font("redoctober", 9)
	IC = font.render("{}, Iceland. Troops: {}".format(Iceland[0], Iceland[1]), 1, (255, 255, 0))
	ICRect = IC.get_rect()
	ICRect.x = 590
	ICRect.y = 235
	screen.blit(IC, ICRect)
	font = pygame.font.Font("redoctober", 10)
	SC = font.render("{}, Scandinavia. Troops: {}".format(Scandinavia[0], Scandinavia[1]), 1, (255, 255, 0))
	SCRect = SC.get_rect()
	SCRect.x = 660
	SCRect.y = 200
	screen.blit(SC, SCRect)
	font = pygame.font.Font("redoctober", 12)
	RUS = font.render("{}, Russia. Troops: {}".format(Russia[0], Russia[1]), 1, (255, 255, 0))
	RUSRect = RUS.get_rect()
	RUSRect.x = 797
	RUSRect.y = 311
	screen.blit(RUS, RUSRect)
	font = pygame.font.Font("redoctober", 10)
	NE = font.render("{}, N Europe. Troops: {}".format(NorthernEurope[0], NorthernEurope[1]), 1, (255, 255, 0))
	NERect = NE.get_rect()
	NERect.x = 670
	NERect.y = 350
	screen.blit(NE, NERect)
	font = pygame.font.Font("redoctober", 10)
	SE = font.render("{}, S Europe. Troops: {}".format(SouthernEurope[0], SouthernEurope[1]), 1, (255, 255, 0))
	SERect = SE.get_rect()
	SERect.x = 680
	SERect.y = 410
	screen.blit(SE, SERect)
	font = pygame.font.Font("redoctober", 10)
	WE = font.render("{}, W Europe. Troops: {}".format(WesternEurope[0], WesternEurope[1]), 1, (255, 255, 0))
	WERect = WE.get_rect()
	WERect.x = 570
	WERect.y = 450
	screen.blit(WE, WERect)
	font = pygame.font.Font("redoctober", 11)
	UK = font.render("{}, UK. Troops: {}".format(UK[0], UK[1]), 1, (255, 255, 0))
	UKRect = UK.get_rect()
	UKRect.x = 590
	UKRect.y = 330
	screen.blit(UK, UKRect)
	font = pygame.font.Font("redoctober", 10)
	UR = font.render("{}, Urals. Troops: {}".format(Urals[0], Urals[1]), 1, (255, 255, 0))
	URRect = UR.get_rect()
	URRect.x = 960
	URRect.y = 270
	screen.blit(UR, URRect)
	font = pygame.font.Font("redoctober", 10)
	WS = font.render("{}, W Siberia. Troops: {}".format(WesternSiberia[0], WesternSiberia[1]), 1, (255, 255, 0))
	WSRect = WS.get_rect()
	WSRect.x = 1050
	WSRect.y = 230
	screen.blit(WS, WSRect)
	font = pygame.font.Font("redoctober", 10)
	CS = font.render("{}, Central Siberia. Troops: {}".format(CentralSiberia[0], CentralSiberia[1]), 1, (255, 255, 0))
	CSRect = CS.get_rect()
	CSRect.x = 1200
	CSRect.y = 200
	screen.blit(CS, CSRect)
	font = pygame.font.Font("redoctober", 10)
	ES = font.render("{}, E Siberia. Troops: {}".format(EasternSiberia[0], EasternSiberia[1]), 1, (255, 255, 0))
	ESRect = ES.get_rect()
	ESRect.x = 1350
	ESRect.y = 250
	screen.blit(ES, ESRect)
	font = pygame.font.Font("redoctober", 10)
	SouthernS = font.render("{}, S Siberia. Troops: {}".format(SouthernSiberia[0], SouthernSiberia[1]), 1, (255, 255, 0))
	SouthernSRect = CS.get_rect()
	SouthernSRect.x = 1170
	SouthernSRect.y = 300
	screen.blit(SouthernS, SouthernSRect)
	font = pygame.font.Font("redoctober", 10)
	MO = font.render("{}, Mongolia. Troops: {}".format(Mongolia[0], Mongolia[1]), 1, (255, 255, 0))
	MORect = MO.get_rect()
	MORect.x = 1200
	MORect.y = 375
	screen.blit(MO, MORect)
	font = pygame.font.Font("redoctober", 10)
	JA = font.render("{}, Japan. Troops: {}".format(Japan[0], Japan[1]), 1, (255, 255, 0))
	JARect = JA.get_rect()
	JARect.x = 1320
	JARect.y = 425
	screen.blit(JA, JARect)
	font = pygame.font.Font("redoctober", 11)
	CH = font.render("{}, China. Troops: {}".format(China[0], China[1]), 1, (255, 255, 0))
	CHRect = CH.get_rect()
	CHRect.x = 1100
	CHRect.y = 470
	screen.blit(CH, CHRect)
	font = pygame.font.Font("redoctober", 10)
	AF = font.render("{}, Afghanistan. Troops: {}".format(Afghanistan[0], Afghanistan[1]), 1, (255, 255, 0))
	AFRect = AF.get_rect()
	AFRect.x = 900
	AFRect.y = 400
	screen.blit(AF, AFRect)
	font = pygame.font.Font("redoctober", 10)
	IN = font.render("{}, India. Troops: {}".format(India[0], India[1]), 1, (255, 255, 0))
	INRect = IN.get_rect()
	INRect.x = 1000
	INRect.y = 575
	screen.blit(IN, INRect)
	font = pygame.font.Font("redoctober", 10)
	SA = font.render("{}, S Asia. Troops: {}".format(SouthernAsia[0], SouthernAsia[1]), 1, (255, 255, 0))
	SARect = SA.get_rect()
	SARect.x = 1120
	SARect.y = 585
	screen.blit(SA, SARect)
	font = pygame.font.Font("redoctober", 11)
	ME = font.render("{}, Middle East. Troops: {}".format(MiddleEast[0], MiddleEast[1]), 1, (255, 255, 0))
	MERect = ME.get_rect()
	MERect.x = 800
	MERect.y = 525
	screen.blit(ME, MERect)
	font = pygame.font.Font("redoctober", 10)
	EG = font.render("{}, Egypt. Troops: {}".format(Egypt[0], Egypt[1]), 1, (255, 255, 0))
	EGRect = EG.get_rect()
	EGRect.x = 715
	EGRect.y = 575
	screen.blit(EG, EGRect)
	font = pygame.font.Font("redoctober", 10)
	EAF = font.render("{}, E Africa. Troops: {}".format(EasternAfrica[0], EasternAfrica[1]), 1, (255, 255, 0))
	EAFRect = EAF.get_rect()
	EAFRect.x = 760
	EAFRect.y = 700
	screen.blit(EAF, EAFRect)
	font = pygame.font.Font("redoctober", 10)
	CAF = font.render("{}, Central Africa. Troops: {}".format(CentralAfrica[0], CentralAfrica[1]), 1, (255, 255, 0))
	CAFRect = CAF.get_rect()
	CAFRect.x = 650
	CAFRect.y = 775
	screen.blit(CAF, CAFRect)
	font = pygame.font.Font("redoctober", 10)
	SAF = font.render("{}, S Africa. Troops: {}".format(SouthernAfrica[0], SouthernAfrica[1]), 1, (255, 255, 0))
	SAFRect = SAF.get_rect()
	SAFRect.x = 675
	SAFRect.y = 900
	screen.blit(SAF, SAFRect)
	font = pygame.font.Font("redoctober", 10)
	MA = font.render("{}, Madagascar. Troops: {}".format(Madagascar[0], Madagascar[1]), 1, (255, 255, 0))
	MARect = MA.get_rect()
	MARect.x = 800
	MARect.y = 910
	screen.blit(MA, MARect)
	font = pygame.font.Font("redoctober", 11)
	NAF = font.render("{}, N Africa. Troops: {}".format(NorthernAfrica[0], NorthernAfrica[1]), 1, (255, 255, 0))
	NAFRect = NAF.get_rect()
	NAFRect.x = 590
	NAFRect.y = 625
	screen.blit(NAF, NAFRect)
	font = pygame.font.Font("redoctober", 11)
	BR = font.render("{}, Brazil. Troops: {}".format(Brazil[0], Brazil[1]), 1, (255, 255, 0))
	BRRect = BR.get_rect()
	BRRect.x = 350
	BRRect.y = 700
	screen.blit(BR, BRRect)
	font = pygame.font.Font("redoctober", 10)
	PE = font.render("{}, Peru. Troops: {}".format(Peru[0], Peru[1]), 1, (255, 255, 0))
	PERect = PE.get_rect()
	PERect.x = 260
	PERect.y = 750
	screen.blit(PE, PERect)
	font = pygame.font.Font("redoctober", 10)
	AR = font.render("{}, Argentina. Troops: {}".format(Argentina[0], Argentina[1]), 1, (255, 255, 0))
	ARRect = AR.get_rect()
	ARRect.x = 300
	ARRect.y = 900
	screen.blit(AR, ARRect)
	font = pygame.font.Font("redoctober", 10)
	VE = font.render("{}, Venezuela. Troops: {}".format(Venezuela[0], Venezuela[1]), 1, (255, 255, 0))
	VERect = VE.get_rect()
	VERect.x = 250
	VERect.y = 600
	screen.blit(VE, VERect)
	font = pygame.font.Font("redoctober", 10)
	MEX = font.render("{}, Mexico. Troops: {}".format(Mexico[0], Mexico[1]), 1, (255, 255, 0))
	MEXRect = MEX.get_rect()
	MEXRect.x = 200
	MEXRect.y = 475
	screen.blit(MEX, MEXRect)
	font = pygame.font.Font("redoctober", 10)
	WUS = font.render("{}, W US. Troops: {}".format(WesternUS[0], WesternUS[1]), 1, (255, 255, 0))
	WUSRect = WUS.get_rect()
	WUSRect.x = 180
	WUSRect.y = 375
	screen.blit(WUS, WUSRect)
	font = pygame.font.Font("redoctober", 10)
	EUS = font.render("{}, E US. Troops: {}".format(EasternUS[0], EasternUS[1]), 1, (255, 255, 0))
	EUSRect = EUS.get_rect()
	EUSRect.x = 300
	EUSRect.y = 420
	screen.blit(EUS, EUSRect)
	font = pygame.font.Font("redoctober", 10)
	WAUS = font.render("{}, W Australia. Troops: {}".format(WesternAustralia[0], WesternAustralia[1]), 1, (255, 255, 0))
	WAUSRect = WAUS.get_rect()
	WAUSRect.x = 1150
	WAUSRect.y = 890
	screen.blit(WAUS, WAUSRect)
	font = pygame.font.Font("redoctober", 10)
	EAUS = font.render("{}, E Australia. Troops: {}".format(EasternAustralia[0], EasternAustralia[1]), 1, (255, 255, 0))
	EAUSRect = EAUS.get_rect()
	EAUSRect.x = 1250
	EAUSRect.y = 850
	screen.blit(EAUS, EAUSRect)
	font = pygame.font.Font("redoctober", 10)
	IND = font.render("{}, Indonesia. Troops: {}".format(Indonesia[0], Indonesia[1]), 1, (255, 255, 0))
	INDRect = WAUS.get_rect()
	INDRect.x = 1150
	INDRect.y = 710
	screen.blit(IND, INDRect)
	font = pygame.font.Font("redoctober", 10)
	NG = font.render("{}, New Guinea. Troops: {}".format(NewGuinea[0], NewGuinea[1]), 1, (255, 255, 0))
	NGRect = NG.get_rect()
	NGRect.x = 1300
	NGRect.y = 730
	screen.blit(NG, NGRect)
	pygame.display.flip()
def main(screen):
	Alaska = ["Unclaimed", 0]
	NorthwestTerritory = ["Unclaimed", 0]
	Alberta = ["Unclaimed", 0]
	Ontario = ["Unclaimed", 0]
	EasternCanada = ["Unclaimed", 0]
	Greenland = ["Unclaimed", 0]
	Iceland = ["Unclaimed", 0]
	Scandinavia = ["Unclaimed", 0]
	Russia = ["Unclaimed", 0]
	NorthernEurope = ["Unclaimed", 0]
	SouthernEurope = ["Unclaimed", 0]
	WesternEurope = ["Unclaimed", 0]
	UK = ["Unclaimed", 0]
	Urals = ["Unclaimed", 0]
	WesternSiberia = ["Unclaimed", 0]
	CentralSiberia = ["Unclaimed", 0]
	EasternSiberia = ["Unclaimed", 0]
	SouthernSiberia = ["Unclaimed", 0]
	Mongolia = ["Unclaimed", 0]
	Japan = ["Unclaimed", 0]
	China = ["Unclaimed", 0]
	Afghanistan = ["Unclaimed", 0]
	India = ["Unclaimed", 0]
	SouthernAsia = ["Unclaimed", 0]
	MiddleEast = ["Unclaimed", 0]
	Egypt = ["Unclaimed", 0]
	EasternAfrica = ["Unclaimed", 0]
	CentralAfrica = ["Unclaimed", 0]
	SouthernAfrica = ["Unclaimed", 0]
	Madagascar = ["Unclaimed", 0]
	NorthernAfrica = ["Unclaimed", 0]
	Brazil = ["Unclaimed", 0]
	Peru = ["Unclaimed", 0]
	Argentina = ["Unclaimed", 0]
	Venezuela = ["Unclaimed", 0]
	Mexico = ["Unclaimed", 0]
	WesternUS = ["Unclaimed", 0]
	EasternUS = ["Unclaimed", 0]
	WesternAustralia = ["Unclaimed", 0]
	EasternAustralia = ["Unclaimed", 0]
	Indonesia = ["Unclaimed", 0]
	NewGuinea = ["Unclaimed", 0]
	makescreen(Alaska, NorthwestTerritory, Alberta, Ontario, EasternCanada, Greenland, Iceland, Scandinavia, Russia, NorthernEurope, SouthernEurope, WesternEurope, UK, Urals, WesternSiberia, CentralSiberia, EasternSiberia, SouthernSiberia, Mongolia, Japan, China, Afghanistan, India, SouthernAsia, MiddleEast, Egypt, EasternAfrica, CentralAfrica, SouthernAfrica, Madagascar, NorthernAfrica, Brazil, Peru, Argentina, Venezuela, Mexico, WesternUS, EasternUS, WesternAustralia, EasternAustralia, Indonesia, NewGuinea, screen)
	print("Welcome to Risk! You will be using this terminal for controlling the game!\nThis is a four player game!")
	print("IMPORTANT NOTES: In this version, it is more modern. This means that a mechanic known as paratroopers is implemented. This mechanic allows for up to 3 troops to attack any province from another province. This means you have to be more defensive with your land.")
	p1 = input("Player 1, please input the country you wish to be: ")
	p2 = input("Player 2, please input the country you wish to be: ")
	p3 = input("Player 3, please input the country you wish to be: ")
	p4 = input("Player 4, please input the country you wish to be: ")
	c = random.randint(1, 4)
	print("Player {} goes first!".format(c))
	while True:
		makescreen(Alaska, NorthwestTerritory, Alberta, Ontario, EasternCanada, Greenland, Iceland, Scandinavia, Russia, NorthernEurope, SouthernEurope, WesternEurope, UK, Urals, WesternSiberia, CentralSiberia, EasternSiberia, SouthernSiberia, Mongolia, Japan, China, Afghanistan, India, SouthernAsia, MiddleEast, Egypt, EasternAfrica, CentralAfrica, SouthernAfrica, Madagascar, NorthernAfrica, Brazil, Peru, Argentina, Venezuela, Mexico, WesternUS, EasternUS, WesternAustralia, EasternAustralia, Indonesia, NewGuinea, screen)
		if c == 1:
			print("{}'s turn".format(p1))
			rrate = 3
			if Alaska[0] == NorthwestTerritory[0] and NorthwestTerritory[0] == Ontario[0] and Ontario[0] == EasternCanada[0] and EasternCanada[0] == EasternUS[0] and EasternUS[0] == Mexico[0] and Mexico[0] == WesternUS[0] and WesternUS[0] == Alberta[0] and Alberta[0] == Greenland[0] and Greenland[0] == p1:
				rrate = rrate + 5
			if Venezuela[0] == Brazil[0] and Brazil[0] == Peru[0] and Peru[0] == Argentina[0] and Argentina[0] == p1:
				rrtate = rrate + 2
			if NorthernEurope[0] == UK[0] and UK[0] == Iceland[0] and Iceland[0] == WesternEurope[0] and WesternEurope[0] == SouthernEurope[0] and SouthernEurope[0] == Scandinavia[0] and Scandinavia[0] == Russia[0] and Russia[0] == p1:
				rrate = rrate + 5
			if MiddleEast[0] == India[0] and India[0] == SouthernAsia[0] and SouthernAsia[0] == China[0] and China[0] == Afghanistan[0] and Afghanistan[0] == Urals[0] and Urals[0] == EasternSiberia[0] and EasternSiberia[0] == CentralSiberia[0] and CentralSiberia[0] == WesternSiberia[0] and WesternSiberia[0] == SouthernSiberia[0] and SouthernSiberia[0] == p1:
				rrate = rrate + 7
			if Egypt[0] == EasternAfrica[0] and EasternAfrica[0] == CentralAfrica[0] and CentralAfrica[0] == SouthernAfrica[0] and SouthernAfrica[0] == NorthernAfrica[0] and NorthernAfrica[0] == Madagascar[0] and Madagascar[0] == p1:
				rrate = rrate + 3
			if NewGuinea[0] == Indonesia[0] and Indonesia[0] == WesternAustralia[0] and WesternAustralia[0] == EasternAustralia[0] and EasternAustralia[0] == p1:
				rrate = rrate + 2
			print("Your current rate of getting armies per turn is: {} armies/turn".format(rrate)) 
			t = 1
			while t <= rrate:
				attack = input("{}, please place your  new army(armies) in a territory(input territory name)(note, anything that has as N E W or S in front of the territory name, please write Northern, Eastern, Western, or Southern, and then the name): ".format(p1))
				if attack == "Alaska" and (Alaska[0] == "Unclaimed" or Alaska[0] == p1):
					Alaska[0] = p1
					Alaska[1] =  Alaska[1] + 1
				elif attack == "Northwest Territory" and (NorthwestTerritory[0] == "Unclaimed" or NorthwestTerritory[0] == p1):
					NorthwestTerritory[0] = p1
					NorthwestTerritory[1] =  NorthwestTerritory[1] + 1
				elif attack == "Alberta" and (Alberta[0] == "Unclaimed" or Alberta[0] == p1):
					Alberta[0] = p1
					Alberta[1] =  Alberta[1] + 1
				elif attack == "Ontario" and (Ontario[0] == "Unclaimed" or Ontario[0] == p1):
					Ontario[0] = p1
					Ontario[1] =  Ontario[1] + 1
				elif attack == "Eastern Canada" and (EasternCanada[0] == "Unclaimed" or EasternCanada[0] == p1):
					EasternCanada[0] = p1
					EasternCanada[1] =  EasternCanada[1] + 1
				elif attack == "Greenland" and (Greenland[0] == "Unclaimed" or Greenland[0] == p1):
					Greenland[0] = p1
					Greenland[1] = Greenland[1] + 1
				elif attack == "Iceland" and (Iceland[0] == "Unclaimed" or Iceland[0] == p1):
					Iceland[0] = p1
					Iceland[1] = Iceland[1] + 1
				elif attack == "Scandinavia" and (Scandinavia[0] == "Unclaimed" or Scandinavia[0] == p1):
					Scandinavia[0] = p1
					Scandinavia[1] = Scandinavia[1] + 1
				elif attack == "Russia" and (Russia[0] == "Unclaimed" or Russia[0] == p1):
					Russia[0] = p1
					Russia[1] = Russia[1] + 1
				elif attack == "Northern Europe" and (NorthernEurope[0] == "Unclaimed" or NorthernEurope[0] == p1):
					NorthernEurope[0] = p1
					NorthernEurope[1] = NorthernEurope[1] + 1
				elif attack == "Southern Europe" and (SouthernEurope[0] == "Unclaimed" or SouthernEurope[0] == p1):
					SouthernEurope[0] = p1
					SouthernEurope[1] = SouthernEurope[1] + 1
				elif attack == "Western Europe" and (WesternEurope[0] == "Unclaimed" or WesternEurope[0] == p1):
					WesternEurope[0] = p1
					WesternEurope[1] = WesternEurope[1] + 1
				elif attack == "UK" and (UK[0] == "Unclaimed" or UK[0] == p1):
					UK[0] = p1
					UK[1] = UK[1] + 1
				elif attack == "Urals" and (Urals[0] == "Unclaimed" or Urals[0] == p1):
					Urals[0] = p1
					Urals[1] = Urals[1] + 1
				elif attack == "Western Siberia" and (WesternSiberia[0] == "Unclaimed" or WesternSiberia[0] == p1):
					WesternSiberia[0] = p1
					WesternSiberia[1] = WesternSiberia[1] + 1
				elif attack == "Central Siberia" and (CentralSiberia[0] == "Unclaimed" or CentralSiberia[0] == p1):
					CentralSiberia[0] = p1
					CentralSiberia[1] = CentralSiberia[1] + 1
				elif attack == "Eastern Siberia" and (EasternSiberia[0] == "Unclaimed" or EasternSiberia[0] == p1):
					EasternSiberia[0] = p1
					EasternSiberia[1] = EasternSiberia[1] + 1
				elif attack == "Southern Siberia" and (SouthernSiberia[0] == "Unclaimed" or SouthernSiberia[0] == p1):
					SouthernSiberia[0] = p1
					SouthernSiberia[1] = SouthernSiberia[1] + 1
				elif attack == "Mongolia" and (Mongolia[0] == "Unclaimed" or Mongolia[0] == p1):
					Mongolia[0] = p1
					Mongolia[1] = Mongolia[1] + 1
				elif attack == "Japan" and (Japan[0] == "Unclaimed" or Japan[0] == p1):
					Japan[0] = p1
					Japan[1] = Japan[1] + 1
				elif attack == "China" and (China[0] == "Unclaimed" or China[0] == p1):
					China[0] = p1
					China[1] = China[1] + 1
				elif attack == "Afghanistan" and (Afghanistan[0] == "Unclaimed" or Afghanistan[0] == p1):
					Afghanistan[0] = p1
					Afghanistan[1] = Afghanistan[1] + 1
				elif attack == "India" and (India[0] == "Unclaimed" or India[0] == p1):
					India[0] = p1
					India[1] = India[1] + 1
				elif attack == "Southern Asia" and (SouthernAsia[0] == "Unclaimed" or SouthernAsia[0] == p1):
					SouthernAsia[0] = p1
					SouthernAsia[1] = SouthernAsia[1] + 1
				elif attack == "Middle East" and (MiddleEast[0] == "Unclaimed" or MiddleEast[0] == p1):
					MiddleEast[0] = p1
					MiddleEast[1] = MiddleEast[1] + 1
				elif attack == "Egypt" and (Egypt[0] == "Unclaimed" or Egypt[0] == p1):
					Egypt[0] = p1
					Egypt[1] = Egypt[1] + 1
				elif attack == "Eastern Africa" and (EasternAfrica[0] == "Unclaimed" or EasternAfrica[0] == p1):
					EasternAfrica[0] = p1
					EasternAfrica[1] = EasternAfrica[1] + 1
				elif attack == "Central Africa" and (CentralAfrica[0] == "Unclaimed" or CentralAfrica[0] == p1):
					CentralAfrica[0] = p1
					CentralAfrica[1] = CentralAfrica[1] + 1
				elif attack == "Southern Africa" and (SouthernAfrica[0] == "Unclaimed" or SouthernAfrica[0] == p1):
					SouthernAfrica[0] = p1
					SouthernAfrica[1] = SouthernAfrica[1] + 1
				elif attack == "Madagascar" and (Madagascar[0] == "Unclaimed" or Madagascar[0] == p1):
					Madagascar[0] = p1
					Madagascar[1] = Madagascar[1] + 1
				elif attack == "Northern Africa" and (NorthernAfrica[0] == "Unclaimed" or NorthernAfrica[0] == p1):
					NorthernAfrica[0] = p1
					NorthernAfrica[1] = NorthernAfrica[1] + 1
				elif attack == "Brazil" and (Brazil[0] == "Unclaimed" or Brazil[0] == p1):
					Brazil[0] = p1
					Brazil[1] = Brazil[1] + 1
				elif attack == "Peru" and (Peru[0] == "Unclaimed" or Peru[0] == p1):
					Peru[0] = p1
					Peru[1] = Peru[1] + 1
				elif attack == "Argentina" and (Argentina[0] == "Unclaimed" or Argentina[0] == p1):
					Argentina[0] = p1
					Argentina[1] = Argentina[1] + 1
				elif attack == "Venezuela" and (Venezuela[0] == "Unclaimed" or Venezuela[0] == p1):
					Venezuela[0] = p1
					Venezuela[1] = Venezuela[1] + 1
				elif attack == "Mexico" and (Mexico[0] == "Unclaimed" or Mexico[0] == p1):
					Mexico[0] = p1
					Mexico[1] = Mexico[1] + 1
				elif attack == "Western US" and (WesternUS[0] == "Unclaimed"or WesternUS[0] == p1):
					WesternUS[0] = p1
					WesternUS[1] = WesternUS[1] + 1
				elif attack == "Eastern US" and (EasternUS[0] == "Unclaimed" or EasternUS[0] == p1):
					EasternUS[0] = p1
					EasternUS[1] = EasternUS[1] + 1
				elif attack == "Western Australia" and (WesternAustralia[0] == "Unclaimed" or WesternAustralia[0] == p1):
					WesternAustralia[0] = p1
					WesternAustralia[1] = WesternAustralia[1] + 1
				elif attack == "Eastern Australia" and (EasternAustralia[0] == "Unclaimed" or EasternAustralia[0] == p1):
					EasternAustralia[0] = p1
					EasternAustralia[1] = EasternAustralia[1] + 1
				elif attack == "Indonesia" and (Indonesia[0] == "Unclaimed" or Indonesia[0] == p1):
					Indonesia[0] = p1
					Indonesia[1] = Indonesia[1] + 1
				elif attack == "New Guinea" and (NewGuinea[0] == "Unclaimed" or NewGuinea[0] == p1):
					NewGuinea[0] = p1
					NewGuinea[1] = NewGuinea[1] + 1
				else:
					print("Please input it exactly as you see it/Sorry, this territory is claimed already.")
					t -= 1
				t += 1
				makescreen(Alaska, NorthwestTerritory, Alberta, Ontario, EasternCanada, Greenland, Iceland, Scandinavia, Russia, NorthernEurope, SouthernEurope, WesternEurope, UK, Urals, WesternSiberia, CentralSiberia, EasternSiberia, SouthernSiberia, Mongolia, Japan, China, Afghanistan, India, SouthernAsia, MiddleEast, Egypt, EasternAfrica, CentralAfrica, SouthernAfrica, Madagascar, NorthernAfrica, Brazil, Peru, Argentina, Venezuela, Mexico, WesternUS, EasternUS, WesternAustralia, EasternAustralia, Indonesia, NewGuinea, screen)
			attack = ""
			attack2 = ""
			while attack != "N":
				print("You can move troops now.")
				print("NOTE: While moving, please do not put any spaces between names of territories(EX: WesternSiberia)")
				attack = input("Input territory to move too(input N to skip moving troops): ")
				if attack == "N":
					continue
				attack2 = input("Input territory to move from: ")
				amt = int(input("Input amount: "))
				if (eval("{}".format(attack))[0] == p1 or eval("{}".format(attack))[0] == "Unclaimed") and eval("{}".format(attack2))[0] == p1:
					eval("{}".format(attack))[1] = eval("{}".format(attack))[1] + amt
					eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - amt
				else:
					print("You cannot do that!")
				if eval("{}".format(attack2))[1] == 0:
					eval("{}".format(attack2))[0] = "Unclaimed"
				makescreen(Alaska, NorthwestTerritory, Alberta, Ontario, EasternCanada, Greenland, Iceland, Scandinavia, Russia, NorthernEurope, SouthernEurope, WesternEurope, UK, Urals, WesternSiberia, CentralSiberia, EasternSiberia, SouthernSiberia, Mongolia, Japan, China, Afghanistan, India, SouthernAsia, MiddleEast, Egypt, EasternAfrica, CentralAfrica, SouthernAfrica, Madagascar, NorthernAfrica, Brazil, Peru, Argentina, Venezuela, Mexico, WesternUS, EasternUS, WesternAustralia, EasternAustralia, Indonesia, NewGuinea, screen)
			turnbool = 1
			while turnbool == 1:
				turnbool = 0
				print("NOTE: While attacking, please do not put any spaces between names of territories(EX: WesternSiberia)")
				attack = input("Please input territory to attack(input N to skip attacking this turn): ")
				if attack == "N":
					continue
				attack2 = input("Please input territory with which to attack from: ")
				army = int(input("Please input amount of armies(Max 3): "))
				if eval("{}".format(attack2))[0] == p1 and eval("{}".format(attack))[0] != p1 and army <= 3 and (eval("{}".format(attack2))[1] - army) > -1 and eval("{}".format(attack))[0] != "Unclaimed":
					if army == 1 and eval("{}".format(attack))[1] == 1:
						diceA = random.randint(1, 6)
						diceD = random.randint(1, 6)
						if diceA > diceD:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA <= diceD:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 1 and eval("{}".format(attack))[1] >= 2:
						diceA = random.randint(1, 6)
						diceD = [random.randint(1, 6), random.randint(1, 6)]
						diceD.sort(reverse=True)
						if diceA > diceD[0]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA <= diceD[0]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 2 and eval("{}".format(attack))[1] == 1:
						diceA = [random.randint(1, 6), random.randint(1, 6)]
						diceD = random.randint(1, 6)
						diceA.sort(reverse=True)
						if diceA[0] > dice:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 2 and eval("{}".format(attack))[1] >= 2:
						diceA = [random.randint(1, 6), random.randint(1, 6)]
						diceD = [random.randint(1, 6), random.randint(1, 6)]
						diceA.sort(reverse=True)
						diceD.sort()
						if diceA[0] > diceD[0]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD[0]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
						if diceA[1] > diceD[1]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[1] <= diceD[1]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 3 and eval("{}".format(attack))[1] == 1:
						diceA = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
						diceD = random.randint(1, 6)
						diceA.sort(reverse=True)
						if diceA[0] > diceD:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 3 and eval("{}".format(attack))[1] >= 2:
						diceA = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
						diceD = [random.randint(1, 6), random.randint(1, 6)]
						diceA.sort(reverse=True)
						diceD.sort(reverse=True)
						if diceA[0] > diceD[0]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD[0]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
						if diceA[1] > diceD[1]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[1] <= diceD[1]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
				else:
					print("You cannot attack from someone else's territory/You cannot attack yourself/You are sending more armies then possible/You cannot attack an unclaimed territory!")
					turnbool = 1
				if eval("{}".format(attack))[1] == 0:
					eval("{}".format(attack))[0] = eval("{}".format(attack2))[0]
					eval("{}".format(attack))[1] = eval("{}".format(attack))[1] + army
					eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - army
				if eval("{}".format(attack2))[1] == 0:
					eval("{}".format(attack2))[0] = "Unclaimed"
		if c == 2:
			print("{}'s turn".format(p2))
			rrate = 3
			if Alaska[0] == NorthwestTerritory[0] and NorthwestTerritory[0] == Ontario[0] and Ontario[0] == EasternCanada[0] and EasternCanada[0] == EasternUS[0] and EasternUS[0] == Mexico[0] and Mexico[0] == WesternUS[0] and WesternUS[0] == Alberta[0] and Alberta[0] == Greenland[0] and Greenland[0] == p2:
				rrate = rrate + 5
			if Venezuela[0] == Brazil[0] and Brazil[0] == Peru[0] and Peru[0] == Argentina[0] and Argentina[0] == p2:
				rrtate = rrate + 2
			if NorthernEurope[0] == UK[0] and UK[0] == Iceland[0] and Iceland[0] == WesternEurope[0] and WesternEurope[0] == SouthernEurope[0] and SouthernEurope[0] == Scandinavia[0] and Scandinavia[0] == Russia[0] and Russia[0] == p2:
				rrate = rrate + 5
			if MiddleEast[0] == India[0] and India[0] == SouthernAsia[0] and SouthernAsia[0] == China[0] and China[0] == Afghanistan[0] and Afghanistan[0] == Urals[0] and Urals[0] == EasternSiberia[0] and EasternSiberia[0] == CentralSiberia[0] and CentralSiberia[0] == WesternSiberia[0] and WesternSiberia[0] == SouthernSiberia[0] and SouthernSiberia[0] == p2:
				rrate = rrate + 7
			if Egypt[0] == EasternAfrica[0] and EasternAfrica[0] == CentralAfrica[0] and CentralAfrica[0] == SouthernAfrica[0] and SouthernAfrica[0] == NorthernAfrica[0] and NorthernAfrica[0] == Madagascar[0] and Madagascar[0] == p2:
				rrate = rrate + 3
			if NewGuinea[0] == Indonesia[0] and Indonesia[0] == WesternAustralia[0] and WesternAustralia[0] == EasternAustralia[0] and EasternAustralia[0] == p2:
				rrate = rrate + 2
			print("Your current rate of getting armies per turn is: {} armies/turn".format(rrate)) 
			t = 1
			while t <= rrate:
				attack = input("{}, please place your  new army(armies) in a territory(input territory name)(note, anything that has as N E W or S in front of the territory name, please write Northern, Eastern, Western, or Southern, and then the name): ".format(p2))
				if attack == "Alaska" and (Alaska[0] == "Unclaimed" or Alaska[0] == p2):
					Alaska[0] = p2
					Alaska[1] =  Alaska[1] + 1
				elif attack == "Northwest Territory" and (NorthwestTerritory[0] == "Unclaimed" or NorthwestTerritory[0] == p2):
					NorthwestTerritory[0] = p2
					NorthwestTerritory[1] =  NorthwestTerritory[1] + 1
				elif attack == "Alberta" and (Alberta[0] == "Unclaimed" or Alberta[0] == p2):
					Alberta[0] = p2
					Alberta[1] =  Alberta[1] + 1
				elif attack == "Ontario" and (Ontario[0] == "Unclaimed" or Ontario[0] == p2):
					Ontario[0] = p2
					Ontario[1] =  Ontario[1] + 1
				elif attack == "Eastern Canada" and (EasternCanada[0] == "Unclaimed" or EasternCanada[0] == p2):
					EasternCanada[0] = p2
					EasternCanada[1] =  EasternCanada[1] + 1
				elif attack == "Greenland" and (Greenland[0] == "Unclaimed" or Greenland[0] == p2):
					Greenland[0] = p2
					Greenland[1] = Greenland[1] + 1
				elif attack == "Iceland" and (Iceland[0] == "Unclaimed" or Iceland[0] == p2):
					Iceland[0] = p2
					Iceland[1] = Iceland[1] + 1
				elif attack == "Scandinavia" and (Scandinavia[0] == "Unclaimed" or Scandinavia[0] == p2):
					Scandinavia[0] = p2
					Scandinavia[1] = Scandinavia[1] + 1
				elif attack == "Russia" and (Russia[0] == "Unclaimed" or Russia[0] == p2):
					Russia[0] = p2
					Russia[1] = Russia[1] + 1
				elif attack == "Northern Europe" and (NorthernEurope[0] == "Unclaimed" or NorthernEurope[0] == p2):
					NorthernEurope[0] = p2
					NorthernEurope[1] = NorthernEurope[1] + 1
				elif attack == "Southern Europe" and (SouthernEurope[0] == "Unclaimed" or SouthernEurope[0] == p2):
					SouthernEurope[0] = p2
					SouthernEurope[1] = SouthernEurope[1] + 1
				elif attack == "Western Europe" and (WesternEurope[0] == "Unclaimed" or WesternEurope[0] == p2):
					WesternEurope[0] = p2
					WesternEurope[1] = WesternEurope[1] + 1
				elif attack == "UK" and (UK[0] == "Unclaimed" or UK[0] == p2):
					UK[0] = p2
					UK[1] = UK[1] + 1
				elif attack == "Urals" and (Urals[0] == "Unclaimed" or Urals[0] == p2):
					Urals[0] = p2
					Urals[1] = Urals[1] + 1
				elif attack == "Western Siberia" and (WesternSiberia[0] == "Unclaimed" or WesternSiberia[0] == p2):
					WesternSiberia[0] = p2
					WesternSiberia[1] = WesternSiberia[1] + 1
				elif attack == "Central Siberia" and (CentralSiberia[0] == "Unclaimed" or CentralSiberia[0] == p2):
					CentralSiberia[0] = p2
					CentralSiberia[1] = CentralSiberia[1] + 1
				elif attack == "Eastern Siberia" and (EasternSiberia[0] == "Unclaimed" or EasternSiberia[0] == p2):
					EasternSiberia[0] = p2
					EasternSiberia[1] = EasternSiberia[1] + 1
				elif attack == "Southern Siberia" and (SouthernSiberia[0] == "Unclaimed" or SouthernSiberia[0] == p2):
					SouthernSiberia[0] = p2
					SouthernSiberia[1] = SouthernSiberia[1] + 1
				elif attack == "Mongolia" and (Mongolia[0] == "Unclaimed" or Mongolia[0] == p2):
					Mongolia[0] = p2
					Mongolia[1] = Mongolia[1] + 1
				elif attack == "Japan" and (Japan[0] == "Unclaimed" or Japan[0] == p2):
					Japan[0] = p2
					Japan[1] = Japan[1] + 1
				elif attack == "China" and (China[0] == "Unclaimed" or China[0] == p2):
					China[0] = p2
					China[1] = China[1] + 1
				elif attack == "Afghanistan" and (Afghanistan[0] == "Unclaimed" or Afghanistan[0] == p2):
					Afghanistan[0] = p2
					Afghanistan[1] = Afghanistan[1] + 1
				elif attack == "India" and (India[0] == "Unclaimed" or India[0] == p2):
					India[0] = p2
					India[1] = India[1] + 1
				elif attack == "Southern Asia" and (SouthernAsia[0] == "Unclaimed" or SouthernAsia[0] == p2):
					SouthernAsia[0] = p2
					SouthernAsia[1] = SouthernAsia[1] + 1
				elif attack == "Middle East" and (MiddleEast[0] == "Unclaimed" or MiddleEast[0] == p2):
					MiddleEast[0] = p2
					MiddleEast[1] = MiddleEast[1] + 1
				elif attack == "Egypt" and (Egypt[0] == "Unclaimed" or Egypt[0] == p2):
					Egypt[0] = p2
					Egypt[1] = Egypt[1] + 1
				elif attack == "Eastern Africa" and (EasternAfrica[0] == "Unclaimed" or EasternAfrica[0] == p2):
					EasternAfrica[0] = p2
					EasternAfrica[1] = EasternAfrica[1] + 1
				elif attack == "Central Africa" and (CentralAfrica[0] == "Unclaimed" or CentralAfrica[0] == p2):
					CentralAfrica[0] = p2
					CentralAfrica[1] = CentralAfrica[1] + 1
				elif attack == "Southern Africa" and (SouthernAfrica[0] == "Unclaimed" or SouthernAfrica[0] == p2):
					SouthernAfrica[0] = p2
					SouthernAfrica[1] = SouthernAfrica[1] + 1
				elif attack == "Madagascar" and (Madagascar[0] == "Unclaimed" or Madagascar[0] == p2):
					Madagascar[0] = p2
					Madagascar[1] = Madagascar[1] + 1
				elif attack == "Northern Africa" and (NorthernAfrica[0] == "Unclaimed" or NorthernAfrica[0] == p2):
					NorthernAfrica[0] = p2
					NorthernAfrica[1] = NorthernAfrica[1] + 1
				elif attack == "Brazil" and (Brazil[0] == "Unclaimed" or Brazil[0] == p2):
					Brazil[0] = p2
					Brazil[1] = Brazil[1] + 1
				elif attack == "Peru" and (Peru[0] == "Unclaimed" or Peru[0] == p2):
					Peru[0] = p2
					Peru[1] = Peru[1] + 1
				elif attack == "Argentina" and (Argentina[0] == "Unclaimed" or Argentina[0] == p2):
					Argentina[0] = p2
					Argentina[1] = Argentina[1] + 1
				elif attack == "Venezuela" and (Venezuela[0] == "Unclaimed" or Venezuela[0] == p2):
					Venezuela[0] = p2
					Venezuela[1] = Venezuela[1] + 1
				elif attack == "Mexico" and (Mexico[0] == "Unclaimed" or Mexico[0] == p2):
					Mexico[0] = p2
					Mexico[1] = Mexico[1] + 1
				elif attack == "Western US" and (WesternUS[0] == "Unclaimed"or WesternUS[0] == p2):
					WesternUS[0] = p2
					WesternUS[1] = WesternUS[1] + 1
				elif attack == "Eastern US" and (EasternUS[0] == "Unclaimed" or EasternUS[0] == p2):
					EasternUS[0] = p2
					EasternUS[1] = EasternUS[1] + 1
				elif attack == "Western Australia" and (WesternAustralia[0] == "Unclaimed" or WesternAustralia[0] == p2):
					WesternAustralia[0] = p2
					WesternAustralia[1] = WesternAustralia[1] + 1
				elif attack == "Eastern Australia" and (EasternAustralia[0] == "Unclaimed" or EasternAustralia[0] == p2):
					EasternAustralia[0] = p2
					EasternAustralia[1] = EasternAustralia[1] + 1
				elif attack == "Indonesia" and (Indonesia[0] == "Unclaimed" or Indonesia[0] == p2):
					Indonesia[0] = p2
					Indonesia[1] = Indonesia[1] + 1
				elif attack == "New Guinea" and (NewGuinea[0] == "Unclaimed" or NewGuinea[0] == p2):
					NewGuinea[0] = p2
					NewGuinea[1] = NewGuinea[1] + 1
				else:
					print("Please input it exactly as you see it/Sorry, this territory is claimed already.")
					t -= 1
				t += 1
				makescreen(Alaska, NorthwestTerritory, Alberta, Ontario, EasternCanada, Greenland, Iceland, Scandinavia, Russia, NorthernEurope, SouthernEurope, WesternEurope, UK, Urals, WesternSiberia, CentralSiberia, EasternSiberia, SouthernSiberia, Mongolia, Japan, China, Afghanistan, India, SouthernAsia, MiddleEast, Egypt, EasternAfrica, CentralAfrica, SouthernAfrica, Madagascar, NorthernAfrica, Brazil, Peru, Argentina, Venezuela, Mexico, WesternUS, EasternUS, WesternAustralia, EasternAustralia, Indonesia, NewGuinea, screen)
			attack = ""
			attack2 = ""
			while attack != "N":
				print("You can move troops now.")
				print("NOTE: While moving, please do not put any spaces between names of territories(EX: WesternSiberia)")
				attack = input("Input territory to move too(input N to skip moving troops): ")
				if attack == "N":
					continue
				attack2 = input("Input territory to move from: ")
				amt = int(nput("Input amount: "))
				if (eval("{}".format(attack))[0] == p2 or eval("{}".format(attack))[0] == "Unclaimed") and eval("{}".format(attack2))[0] == p2:
					eval("{}".format(attack))[1] = eval("{}".format(attack))[1] + amt
					eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - amt
				else:
					print("You cannot do that!")
				if eval("{}".format(attack2))[1] == 0:
					eval("{}".format(attack2))[0] = "Unclaimed"
				makescreen(Alaska, NorthwestTerritory, Alberta, Ontario, EasternCanada, Greenland, Iceland, Scandinavia, Russia, NorthernEurope, SouthernEurope, WesternEurope, UK, Urals, WesternSiberia, CentralSiberia, EasternSiberia, SouthernSiberia, Mongolia, Japan, China, Afghanistan, India, SouthernAsia, MiddleEast, Egypt, EasternAfrica, CentralAfrica, SouthernAfrica, Madagascar, NorthernAfrica, Brazil, Peru, Argentina, Venezuela, Mexico, WesternUS, EasternUS, WesternAustralia, EasternAustralia, Indonesia, NewGuinea, screen)
			turnbool = 1
			while turnbool == 1:
				turnbool = 0
				print("NOTE: While attacking, please do not put any spaces between names of territories(EX: WesternSiberia)")
				attack = input("Please input territory to attack(input N to skip attacking this turn): ")
				if attack == "N":
					continue
				attack2 = input("Please input territory with which to attack from: ")
				army = int(input("Please input amount of armies(Max 3): "))
				if eval("{}".format(attack2))[0] == p2 and eval("{}".format(attack))[0] != p2 and army <= 3 and (eval("{}".format(attack2))[1] - army) > -1 and eval("{}".format(attack))[0] != "Unclaimed":
					if army == 1 and eval("{}".format(attack))[1] == 1:
						diceA = random.randint(1, 6)
						diceD = random.randint(1, 6)
						if diceA > diceD:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA <= diceD:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 1 and eval("{}".format(attack))[1] >= 2:
						diceA = random.randint(1, 6)
						diceD = [random.randint(1, 6), random.randint(1, 6)]
						diceD.sort(reverse=True)
						if diceA > diceD[0]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA <= diceD[0]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 2 and eval("{}".format(attack))[1] == 1:
						diceA = [random.randint(1, 6), random.randint(1, 6)]
						diceD = random.randint(1, 6)
						diceA.sort(reverse=True)
						if diceA[0] > diceD:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 2 and eval("{}".format(attack))[1] >= 2:
						diceA = [random.randint(1, 6), random.randint(1, 6)]
						diceD = [random.randint(1, 6), random.randint(1, 6)]
						diceA.sort(reverse=True)
						diceD.sort()
						if diceA[0] > diceD[0]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD[0]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
						if diceA[1] > diceD[1]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[1] <= diceD[1]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 3 and eval("{}".format(attack))[1] == 1:
						diceA = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
						diceD = random.randint(1, 6)
						diceA.sort(reverse=True)
						if diceA[0] > diceD:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 3 and eval("{}".format(attack))[1] >= 2:
						diceA = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
						diceD = [random.randint(1, 6), random.randint(1, 6)]
						diceA.sort(reverse=True)
						diceD.sort(reverse=True)
						if diceA[0] > diceD[0]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD[0]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
						if diceA[1] > diceD[1]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[1] <= diceD[1]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
				else:
					print("You cannot attack from someone else's territory/You cannot attack yourself/You are sending more armies then possible/You cannot attack an unclaimed territory!")
					turnbool = 1
				if eval("{}".format(attack))[1] == 0:
					eval("{}".format(attack))[0] = eval("{}".format(attack2))[0]
					eval("{}".format(attack))[1] = eval("{}".format(attack))[1] + army
					eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - army
				if eval("{}".format(attack2))[1] == 0:
					eval("{}".format(attack2))[0] = "Unclaimed"
			
		if c == 3:
			print("{}'s turn".format(p3))
			rrate = 3
			if Alaska[0] == NorthwestTerritory[0] and NorthwestTerritory[0] == Ontario[0] and Ontario[0] == EasternCanada[0] and EasternCanada[0] == EasternUS[0] and EasternUS[0] == Mexico[0] and Mexico[0] == WesternUS[0] and WesternUS[0] == Alberta[0] and Alberta[0] == Greenland[0] and Greenland[0] == p3:
				rrate = rrate + 5
			if Venezuela[0] == Brazil[0] and Brazil[0] == Peru[0] and Peru[0] == Argentina[0] and Argentina[0] == p3:
				rrtate = rrate + 2
			if NorthernEurope[0] == UK[0] and UK[0] == Iceland[0] and Iceland[0] == WesternEurope[0] and WesternEurope[0] == SouthernEurope[0] and SouthernEurope[0] == Scandinavia[0] and Scandinavia[0] == Russia[0] and Russia[0] == p3:
				rrate = rrate + 5
			if MiddleEast[0] == India[0] and India[0] == SouthernAsia[0] and SouthernAsia[0] == China[0] and China[0] == Afghanistan[0] and Afghanistan[0] == Urals[0] and Urals[0] == EasternSiberia[0] and EasternSiberia[0] == CentralSiberia[0] and CentralSiberia[0] == WesternSiberia[0] and WesternSiberia[0] == SouthernSiberia[0] and SouthernSiberia[0] == p3:
				rrate = rrate + 7
			if Egypt[0] == EasternAfrica[0] and EasternAfrica[0] == CentralAfrica[0] and CentralAfrica[0] == SouthernAfrica[0] and SouthernAfrica[0] == NorthernAfrica[0] and NorthernAfrica[0] == Madagascar[0] and Madagascar[0] == p3:
				rrate = rrate + 3
			if NewGuinea[0] == Indonesia[0] and Indonesia[0] == WesternAustralia[0] and WesternAustralia[0] == EasternAustralia[0] and EasternAustralia[0] == p3:
				rrate = rrate + 2
			print("Your current rate of getting armies per turn is: {} armies/turn".format(rrate))
			t = 1
			while t <= rrate:
				attack = input("{}, please place your  new army(armies) in a territory(input territory name)(note, anything that has as N E W or S in front of the territory name, please write Northern, Eastern, Western, or Southern, and then the name): ".format(p3))
				if attack == "Alaska" and (Alaska[0] == "Unclaimed" or Alaska[0] == p3):
					Alaska[0] = p3
					Alaska[1] =  Alaska[1] + 1
				elif attack == "Northwest Territory" and (NorthwestTerritory[0] == "Unclaimed" or NorthwestTerritory[0] == p3):
					NorthwestTerritory[0] = p3
					NorthwestTerritory[1] =  NorthwestTerritory[1] + 1
				elif attack == "Alberta" and (Alberta[0] == "Unclaimed" or Alberta[0] == p3):
					Alberta[0] = p3
					Alberta[1] =  Alberta[1] + 1
				elif attack == "Ontario" and (Ontario[0] == "Unclaimed" or Ontario[0] == p3):
					Ontario[0] = p3
					Ontario[1] =  Ontario[1] + 1
				elif attack == "Eastern Canada" and (EasternCanada[0] == "Unclaimed" or EasternCanada[0] == p3):
					EasternCanada[0] = p3
					EasternCanada[1] =  EasternCanada[1] + 1
				elif attack == "Greenland" and (Greenland[0] == "Unclaimed" or Greenland[0] == p3):
					Greenland[0] = p3
					Greenland[1] = Greenland[1] + 1
				elif attack == "Iceland" and (Iceland[0] == "Unclaimed" or Iceland[0] == p3):
					Iceland[0] = p3
					Iceland[1] = Iceland[1] + 1
				elif attack == "Scandinavia" and (Scandinavia[0] == "Unclaimed" or Scandinavia[0] == p3):
					Scandinavia[0] = p3
					Scandinavia[1] = Scandinavia[1] + 1
				elif attack == "Russia" and (Russia[0] == "Unclaimed" or Russia[0] == p3):
					Russia[0] = p3
					Russia[1] = Russia[1] + 1
				elif attack == "Northern Europe" and (NorthernEurope[0] == "Unclaimed" or NorthernEurope[0] == p3):
					NorthernEurope[0] = p3
					NorthernEurope[1] = NorthernEurope[1] + 1
				elif attack == "Southern Europe" and (SouthernEurope[0] == "Unclaimed" or SouthernEurope[0] == p3):
					SouthernEurope[0] = p3
					SouthernEurope[1] = SouthernEurope[1] + 1
				elif attack == "Western Europe" and (WesternEurope[0] == "Unclaimed" or WesternEurope[0] == p3):
					WesternEurope[0] = p3
					WesternEurope[1] = WesternEurope[1] + 1
				elif attack == "UK" and (UK[0] == "Unclaimed" or UK[0] == p3):
					UK[0] = p3
					UK[1] = UK[1] + 1
				elif attack == "Urals" and (Urals[0] == "Unclaimed" or Urals[0] == p3):
					Urals[0] = p3
					Urals[1] = Urals[1] + 1
				elif attack == "Western Siberia" and (WesternSiberia[0] == "Unclaimed" or WesternSiberia[0] == p3):
					WesternSiberia[0] = p3
					WesternSiberia[1] = WesternSiberia[1] + 1
				elif attack == "Central Siberia" and (CentralSiberia[0] == "Unclaimed" or CentralSiberia[0] == p3):
					CentralSiberia[0] = p3
					CentralSiberia[1] = CentralSiberia[1] + 1
				elif attack == "Eastern Siberia" and (EasternSiberia[0] == "Unclaimed" or EasternSiberia[0] == p3):
					EasternSiberia[0] = p3
					EasternSiberia[1] = EasternSiberia[1] + 1
				elif attack == "Southern Siberia" and (SouthernSiberia[0] == "Unclaimed" or SouthernSiberia[0] == p3):
					SouthernSiberia[0] = p3
					SouthernSiberia[1] = SouthernSiberia[1] + 1
				elif attack == "Mongolia" and (Mongolia[0] == "Unclaimed" or Mongolia[0] == p3):
					Mongolia[0] = p3
					Mongolia[1] = Mongolia[1] + 1
				elif attack == "Japan" and (Japan[0] == "Unclaimed" or Japan[0] == p3):
					Japan[0] = p3
					Japan[1] = Japan[1] + 1
				elif attack == "China" and (China[0] == "Unclaimed" or China[0] == p3):
					China[0] = p3
					China[1] = China[1] + 1
				elif attack == "Afghanistan" and (Afghanistan[0] == "Unclaimed" or Afghanistan[0] == p3):
					Afghanistan[0] = p3
					Afghanistan[1] = Afghanistan[1] + 1
				elif attack == "India" and (India[0] == "Unclaimed" or India[0] == p3):
					India[0] = p3
					India[1] = India[1] + 1
				elif attack == "Southern Asia" and (SouthernAsia[0] == "Unclaimed" or SouthernAsia[0] == p3):
					SouthernAsia[0] = p3
					SouthernAsia[1] = SouthernAsia[1] + 1
				elif attack == "Middle East" and (MiddleEast[0] == "Unclaimed" or MiddleEast[0] == p3):
					MiddleEast[0] = p3
					MiddleEast[1] = MiddleEast[1] + 1
				elif attack == "Egypt" and (Egypt[0] == "Unclaimed" or Egypt[0] == p3):
					Egypt[0] = p3
					Egypt[1] = Egypt[1] + 1
				elif attack == "Eastern Africa" and (EasternAfrica[0] == "Unclaimed" or EasternAfrica[0] == p3):
					EasternAfrica[0] = p3
					EasternAfrica[1] = EasternAfrica[1] + 1
				elif attack == "Central Africa" and (CentralAfrica[0] == "Unclaimed" or CentralAfrica[0] == p3):
					CentralAfrica[0] = p3
					CentralAfrica[1] = CentralAfrica[1] + 1
				elif attack == "Southern Africa" and (SouthernAfrica[0] == "Unclaimed" or SouthernAfrica[0] == p3):
					SouthernAfrica[0] = p3
					SouthernAfrica[1] = SouthernAfrica[1] + 1
				elif attack == "Madagascar" and (Madagascar[0] == "Unclaimed" or Madagascar[0] == p3):
					Madagascar[0] = p3
					Madagascar[1] = Madagascar[1] + 1
				elif attack == "Northern Africa" and (NorthernAfrica[0] == "Unclaimed" or NorthernAfrica[0] == p3):
					NorthernAfrica[0] = p3
					NorthernAfrica[1] = NorthernAfrica[1] + 1
				elif attack == "Brazil" and (Brazil[0] == "Unclaimed" or Brazil[0] == p3):
					Brazil[0] = p3
					Brazil[1] = Brazil[1] + 1
				elif attack == "Peru" and (Peru[0] == "Unclaimed" or Peru[0] == p3):
					Peru[0] = p3
					Peru[1] = Peru[1] + 1
				elif attack == "Argentina" and (Argentina[0] == "Unclaimed" or Argentina[0] == p3):
					Argentina[0] = p3
					Argentina[1] = Argentina[1] + 1
				elif attack == "Venezuela" and (Venezuela[0] == "Unclaimed" or Venezuela[0] == p3):
					Venezuela[0] = p3
					Venezuela[1] = Venezuela[1] + 1
				elif attack == "Mexico" and (Mexico[0] == "Unclaimed" or Mexico[0] == p3):
					Mexico[0] = p3
					Mexico[1] = Mexico[1] + 1
				elif attack == "Western US" and (WesternUS[0] == "Unclaimed"or WesternUS[0] == p3):
					WesternUS[0] = p3
					WesternUS[1] = WesternUS[1] + 1
				elif attack == "Eastern US" and (EasternUS[0] == "Unclaimed" or EasternUS[0] == p3):
					EasternUS[0] = p3
					EasternUS[1] = EasternUS[1] + 1
				elif attack == "Western Australia" and (WesternAustralia[0] == "Unclaimed" or WesternAustralia[0] == p3):
					WesternAustralia[0] = p3
					WesternAustralia[1] = WesternAustralia[1] + 1
				elif attack == "Eastern Australia" and (EasternAustralia[0] == "Unclaimed" or EasternAustralia[0] == p3):
					EasternAustralia[0] = p3
					EasternAustralia[1] = EasternAustralia[1] + 1
				elif attack == "Indonesia" and (Indonesia[0] == "Unclaimed" or Indonesia[0] == p3):
					Indonesia[0] = p3
					Indonesia[1] = Indonesia[1] + 1
				elif attack == "New Guinea" and (NewGuinea[0] == "Unclaimed" or NewGuinea[0] == p3):
					NewGuinea[0] = p3
					NewGuinea[1] = NewGuinea[1] + 1
				else:
					print("Please input it exactly as you see it/Sorry, this territory is claimed already.")
					t -= 1
				t += 1
				makescreen(Alaska, NorthwestTerritory, Alberta, Ontario, EasternCanada, Greenland, Iceland, Scandinavia, Russia, NorthernEurope, SouthernEurope, WesternEurope, UK, Urals, WesternSiberia, CentralSiberia, EasternSiberia, SouthernSiberia, Mongolia, Japan, China, Afghanistan, India, SouthernAsia, MiddleEast, Egypt, EasternAfrica, CentralAfrica, SouthernAfrica, Madagascar, NorthernAfrica, Brazil, Peru, Argentina, Venezuela, Mexico, WesternUS, EasternUS, WesternAustralia, EasternAustralia, Indonesia, NewGuinea, screen)
			attack = ""
			attack2 = ""
			while attack != "N":
				print("You can move troops now.")
				print("NOTE: While moving, please do not put any spaces between names of territories(EX: WesternSiberia)")
				attack = input("Input territory to move too(input N to skip moving troops): ")
				if attack == "N":
					continue
				attack2 = input("Input territory to move from: ")
				amt = int(input("Input amount: "))
				if (eval("{}".format(attack))[0] == p3 or eval("{}".format(attack))[0] == "Unclaimed") and eval("{}".format(attack2))[0] == p3:
					eval("{}".format(attack))[1] = eval("{}".format(attack))[1] + amt
					eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - amt
				else:
					print("You cannot do that!")
				if eval("{}".format(attack2))[1] == 0:
					eval("{}".format(attack2))[0] = "Unclaimed"
				makescreen(Alaska, NorthwestTerritory, Alberta, Ontario, EasternCanada, Greenland, Iceland, Scandinavia, Russia, NorthernEurope, SouthernEurope, WesternEurope, UK, Urals, WesternSiberia, CentralSiberia, EasternSiberia, SouthernSiberia, Mongolia, Japan, China, Afghanistan, India, SouthernAsia, MiddleEast, Egypt, EasternAfrica, CentralAfrica, SouthernAfrica, Madagascar, NorthernAfrica, Brazil, Peru, Argentina, Venezuela, Mexico, WesternUS, EasternUS, WesternAustralia, EasternAustralia, Indonesia, NewGuinea, screen)
			turnbool = 1
			while turnbool == 1:
				turnbool = 0
				print("NOTE: While attacking, please do not put any spaces between names of territories(EX: WesternSiberia)")
				attack = input("Please input territory to attack(input N to skip attacking this turn): ")
				if attack == "N":
					continue
				attack2 = input("Please input territory with which to attack from: ")
				army = int(input("Please input amount of armies(Max 3): "))
				if eval("{}".format(attack2))[0] == p3 and eval("{}".format(attack))[0] != p3 and army <= 3 and (eval("{}".format(attack2))[1] - army) > -1 and eval("{}".format(attack))[0] != "Unclaimed":
					if army == 1 and eval("{}".format(attack))[1] == 1:
						diceA = random.randint(1, 6)
						diceD = random.randint(1, 6)
						if diceA > diceD:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA <= diceD:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 1 and eval("{}".format(attack))[1] >= 2:
						diceA = random.randint(1, 6)
						diceD = [random.randint(1, 6), random.randint(1, 6)]
						diceD.sort(reverse=True)
						if diceA > diceD[0]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA <= diceD[0]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 2 and eval("{}".format(attack))[1] == 1:
						diceA = [random.randint(1, 6), random.randint(1, 6)]
						diceD = random.randint(1, 6)
						diceA.sort(reverse=True)
						if diceA[0] > dice:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 2 and eval("{}".format(attack))[1] >= 2:
						diceA = [random.randint(1, 6), random.randint(1, 6)]
						diceD = [random.randint(1, 6), random.randint(1, 6)]
						diceA.sort(reverse=True)
						diceD.sort()
						if diceA[0] > diceD[0]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD[0]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
						if diceA[1] > diceD[1]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[1] <= diceD[1]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 3 and eval("{}".format(attack))[1] == 1:
						diceA = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
						diceD = random.randint(1, 6)
						diceA.sort(reverse=True)
						if diceA[0] > diceD:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 3 and eval("{}".format(attack))[1] >= 2:
						diceA = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
						diceD = [random.randint(1, 6), random.randint(1, 6)]
						diceA.sort(reverse=True)
						diceD.sort(reverse=True)
						if diceA[0] > diceD[0]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD[0]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
						if diceA[1] > diceD[1]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[1] <= diceD[1]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
				else:
					print("You cannot attack from someone else's territory/You cannot attack yourself/You are sending more armies then possible/You cannot attack an unclaimed territory!")
					turnbool = 1
				if eval("{}".format(attack))[1] == 0:
					eval("{}".format(attack))[0] = eval("{}".format(attack2))[0]
					eval("{}".format(attack))[1] = eval("{}".format(attack))[1] + army
					eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - army
				if eval("{}".format(attack2))[1] == 0:
					eval("{}".format(attack2))[0] = "Unclaimed"
		if c == 4:
			print("{}'s turn".format(p4))
			rrate = 3
			if Alaska[0] == NorthwestTerritory[0] and NorthwestTerritory[0] == Ontario[0] and Ontario[0] == EasternCanada[0] and EasternCanada[0] == EasternUS[0] and EasternUS[0] == Mexico[0] and Mexico[0] == WesternUS[0] and WesternUS[0] == Alberta[0] and Alberta[0] == Greenland[0] and Greenland[0] == p4:
				rrate = rrate + 5
			if Venezuela[0] == Brazil[0] and Brazil[0] == Peru[0] and Peru[0] == Argentina[0] and Argentina[0] == p4:
				rrtate = rrate + 2
			if NorthernEurope[0] == UK[0] and UK[0] == Iceland[0] and Iceland[0] == WesternEurope[0] and WesternEurope[0] == SouthernEurope[0] and SouthernEurope[0] == Scandinavia[0] and Scandinavia[0] == Russia[0] and Russia[0] == p4:
				rrate = rrate + 5
			if MiddleEast[0] == India[0] and India[0] == SouthernAsia[0] and SouthernAsia[0] == China[0] and China[0] == Afghanistan[0] and Afghanistan[0] == Urals[0] and Urals[0] == EasternSiberia[0] and EasternSiberia[0] == CentralSiberia[0] and CentralSiberia[0] == WesternSiberia[0] and WesternSiberia[0] == SouthernSiberia[0] and SouthernSiberia[0] == p4:
				rrate = rrate + 7
			if Egypt[0] == EasternAfrica[0] and EasternAfrica[0] == CentralAfrica[0] and CentralAfrica[0] == SouthernAfrica[0] and SouthernAfrica[0] == NorthernAfrica[0] and NorthernAfrica[0] == Madagascar[0] and Madagascar[0] == p4:
				rrate = rrate + 3
			if NewGuinea[0] == Indonesia[0] and Indonesia[0] == WesternAustralia[0] and WesternAustralia[0] == EasternAustralia[0] and EasternAustralia[0] == p4:
				rrate = rrate + 2
			print("Your current rate of getting armies per turn is: {} armies/turn".format(rrate))
			t = 1
			while t <= rrate:
				attack = input("{}, please place your  new army(armies) in a territory(input territory name)(note, anything that has as N E W or S in front of the territory name, please write Northern, Eastern, Western, or Southern, and then the name): ".format(p4))
				if attack == "Alaska" and (Alaska[0] == "Unclaimed" or Alaska[0] == p4):
					Alaska[0] = p4
					Alaska[1] =  Alaska[1] + 1
				elif attack == "Northwest Territory" and (NorthwestTerritory[0] == "Unclaimed" or NorthwestTerritory[0] == p4):
					NorthwestTerritory[0] = p4
					NorthwestTerritory[1] =  NorthwestTerritory[1] + 1
				elif attack == "Alberta" and (Alberta[0] == "Unclaimed" or Alberta[0] == p4):
					Alberta[0] = p4
					Alberta[1] =  Alberta[1] + 1
				elif attack == "Ontario" and (Ontario[0] == "Unclaimed" or Ontario[0] == p4):
					Ontario[0] = p4
					Ontario[1] =  Ontario[1] + 1
				elif attack == "Eastern Canada" and (EasternCanada[0] == "Unclaimed" or EasternCanada[0] == p4):
					EasternCanada[0] = p4
					EasternCanada[1] =  EasternCanada[1] + 1
				elif attack == "Greenland" and (Greenland[0] == "Unclaimed" or Greenland[0] == p4):
					Greenland[0] = p4
					Greenland[1] = Greenland[1] + 1
				elif attack == "Iceland" and (Iceland[0] == "Unclaimed" or Iceland[0] == p4):
					Iceland[0] = p4
					Iceland[1] = Iceland[1] + 1
				elif attack == "Scandinavia" and (Scandinavia[0] == "Unclaimed" or Scandinavia[0] == p4):
					Scandinavia[0] = p4
					Scandinavia[1] = Scandinavia[1] + 1
				elif attack == "Russia" and (Russia[0] == "Unclaimed" or Russia[0] == p4):
					Russia[0] = p4
					Russia[1] = Russia[1] + 1
				elif attack == "Northern Europe" and (NorthernEurope[0] == "Unclaimed" or NorthernEurope[0] == p4):
					NorthernEurope[0] = p4
					NorthernEurope[1] = NorthernEurope[1] + 1
				elif attack == "Southern Europe" and (SouthernEurope[0] == "Unclaimed" or SouthernEurope[0] == p4):
					SouthernEurope[0] = p4
					SouthernEurope[1] = SouthernEurope[1] + 1
				elif attack == "Western Europe" and (WesternEurope[0] == "Unclaimed" or WesternEurope[0] == p4):
					WesternEurope[0] = p4
					WesternEurope[1] = WesternEurope[1] + 1
				elif attack == "UK" and (UK[0] == "Unclaimed" or UK[0] == p4):
					UK[0] = p4
					UK[1] = UK[1] + 1
				elif attack == "Urals" and (Urals[0] == "Unclaimed" or Urals[0] == p4):
					Urals[0] = p4
					Urals[1] = Urals[1] + 1
				elif attack == "Western Siberia" and (WesternSiberia[0] == "Unclaimed" or WesternSiberia[0] == p4):
					WesternSiberia[0] = p4
					WesternSiberia[1] = WesternSiberia[1] + 1
				elif attack == "Central Siberia" and (CentralSiberia[0] == "Unclaimed" or CentralSiberia[0] == p4):
					CentralSiberia[0] = p4
					CentralSiberia[1] = CentralSiberia[1] + 1
				elif attack == "Eastern Siberia" and (EasternSiberia[0] == "Unclaimed" or EasternSiberia[0] == p4):
					EasternSiberia[0] = p4
					EasternSiberia[1] = EasternSiberia[1] + 1
				elif attack == "Southern Siberia" and (SouthernSiberia[0] == "Unclaimed" or SouthernSiberia[0] == p4):
					SouthernSiberia[0] = p4
					SouthernSiberia[1] = SouthernSiberia[1] + 1
				elif attack == "Mongolia" and (Mongolia[0] == "Unclaimed" or Mongolia[0] == p4):
					Mongolia[0] = p4
					Mongolia[1] = Mongolia[1] + 1
				elif attack == "Japan" and (Japan[0] == "Unclaimed" or Japan[0] == p4):
					Japan[0] = p4
					Japan[1] = Japan[1] + 1
				elif attack == "China" and (China[0] == "Unclaimed" or China[0] == p4):
					China[0] = p4
					China[1] = China[1] + 1
				elif attack == "Afghanistan" and (Afghanistan[0] == "Unclaimed" or Afghanistan[0] == p4):
					Afghanistan[0] = p4
					Afghanistan[1] = Afghanistan[1] + 1
				elif attack == "India" and (India[0] == "Unclaimed" or India[0] == p4):
					India[0] = p4
					India[1] = India[1] + 1
				elif attack == "Southern Asia" and (SouthernAsia[0] == "Unclaimed" or SouthernAsia[0] == p4):
					SouthernAsia[0] = p4
					SouthernAsia[1] = SouthernAsia[1] + 1
				elif attack == "Middle East" and (MiddleEast[0] == "Unclaimed" or MiddleEast[0] == p4):
					MiddleEast[0] = p4
					MiddleEast[1] = MiddleEast[1] + 1
				elif attack == "Egypt" and (Egypt[0] == "Unclaimed" or Egypt[0] == p4):
					Egypt[0] = p4
					Egypt[1] = Egypt[1] + 1
				elif attack == "Eastern Africa" and (EasternAfrica[0] == "Unclaimed" or EasternAfrica[0] == p4):
					EasternAfrica[0] = p4
					EasternAfrica[1] = EasternAfrica[1] + 1
				elif attack == "Central Africa" and (CentralAfrica[0] == "Unclaimed" or CentralAfrica[0] == p4):
					CentralAfrica[0] = p4
					CentralAfrica[1] = CentralAfrica[1] + 1
				elif attack == "Southern Africa" and (SouthernAfrica[0] == "Unclaimed" or SouthernAfrica[0] == p4):
					SouthernAfrica[0] = p4
					SouthernAfrica[1] = SouthernAfrica[1] + 1
				elif attack == "Madagascar" and (Madagascar[0] == "Unclaimed" or Madagascar[0] == p4):
					Madagascar[0] = p4
					Madagascar[1] = Madagascar[1] + 1
				elif attack == "Northern Africa" and (NorthernAfrica[0] == "Unclaimed" or NorthernAfrica[0] == p4):
					NorthernAfrica[0] = p4
					NorthernAfrica[1] = NorthernAfrica[1] + 1
				elif attack == "Brazil" and (Brazil[0] == "Unclaimed" or Brazil[0] == p4):
					Brazil[0] = p4
					Brazil[1] = Brazil[1] + 1
				elif attack == "Peru" and (Peru[0] == "Unclaimed" or Peru[0] == p4):
					Peru[0] = p4
					Peru[1] = Peru[1] + 1
				elif attack == "Argentina" and (Argentina[0] == "Unclaimed" or Argentina[0] == p4):
					Argentina[0] = p4
					Argentina[1] = Argentina[1] + 1
				elif attack == "Venezuela" and (Venezuela[0] == "Unclaimed" or Venezuela[0] == p4):
					Venezuela[0] = p4
					Venezuela[1] = Venezuela[1] + 1
				elif attack == "Mexico" and (Mexico[0] == "Unclaimed" or Mexico[0] == p4):
					Mexico[0] = p4
					Mexico[1] = Mexico[1] + 1
				elif attack == "Western US" and (WesternUS[0] == "Unclaimed"or WesternUS[0] == p4):
					WesternUS[0] = p4
					WesternUS[1] = WesternUS[1] + 1
				elif attack == "Eastern US" and (EasternUS[0] == "Unclaimed" or EasternUS[0] == p4):
					EasternUS[0] = p4
					EasternUS[1] = EasternUS[1] + 1
				elif attack == "Western Australia" and (WesternAustralia[0] == "Unclaimed" or WesternAustralia[0] == p4):
					WesternAustralia[0] = p4
					WesternAustralia[1] = WesternAustralia[1] + 1
				elif attack == "Eastern Australia" and (EasternAustralia[0] == "Unclaimed" or EasternAustralia[0] == p4):
					EasternAustralia[0] = p4
					EasternAustralia[1] = EasternAustralia[1] + 1
				elif attack == "Indonesia" and (Indonesia[0] == "Unclaimed" or Indonesia[0] == p4):
					Indonesia[0] = p4
					Indonesia[1] = Indonesia[1] + 1
				elif attack == "New Guinea" and (NewGuinea[0] == "Unclaimed" or NewGuinea[0] == p4):
					NewGuinea[0] = p4
					NewGuinea[1] = NewGuinea[1] + 1
				else:
					print("Please input it exactly as you see it/Sorry, this territory is claimed already.")
					t -= 1
				t += 1
				makescreen(Alaska, NorthwestTerritory, Alberta, Ontario, EasternCanada, Greenland, Iceland, Scandinavia, Russia, NorthernEurope, SouthernEurope, WesternEurope, UK, Urals, WesternSiberia, CentralSiberia, EasternSiberia, SouthernSiberia, Mongolia, Japan, China, Afghanistan, India, SouthernAsia, MiddleEast, Egypt, EasternAfrica, CentralAfrica, SouthernAfrica, Madagascar, NorthernAfrica, Brazil, Peru, Argentina, Venezuela, Mexico, WesternUS, EasternUS, WesternAustralia, EasternAustralia, Indonesia, NewGuinea, screen)
			attack = ""
			attack2 = ""
			while attack != "N":
				print("You can move troops now.")
				print("NOTE: While moving, please do not put any spaces between names of territories(EX: WesternSiberia)")
				attack = input("Input territory to move too(input N to skip moving troops): ")
				if attack == "N":
					continue
				attack2 = input("Input territory to move from: ")
				amt = int(input("Input amount: "))
				if (eval("{}".format(attack))[0] == p4 or eval("{}".format(attack))[0] == "Unclaimed") and eval("{}".format(attack2))[0] == p4:
					eval("{}".format(attack))[1] = eval("{}".format(attack))[1] + amt
					eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - amt
				else:
					print("You cannot do that!")
				if eval("{}".format(attack2))[1] == 0:
					eval("{}".format(attack2))[0] = "Unclaimed"
				makescreen(Alaska, NorthwestTerritory, Alberta, Ontario, EasternCanada, Greenland, Iceland, Scandinavia, Russia, NorthernEurope, SouthernEurope, WesternEurope, UK, Urals, WesternSiberia, CentralSiberia, EasternSiberia, SouthernSiberia, Mongolia, Japan, China, Afghanistan, India, SouthernAsia, MiddleEast, Egypt, EasternAfrica, CentralAfrica, SouthernAfrica, Madagascar, NorthernAfrica, Brazil, Peru, Argentina, Venezuela, Mexico, WesternUS, EasternUS, WesternAustralia, EasternAustralia, Indonesia, NewGuinea, screen)
			turnbool = 1
			while turnbool == 1:
				turnbool = 0
				print("NOTE: While attacking, please do not put any spaces between names of territories(EX: WesternSiberia)")
				attack = input("Please input territory to attack(input N to skip attacking this turn): ")
				if attack == "N":
					continue
				attack2 = input("Please input territory with which to attack from: ")
				army = int(input("Please input amount of armies(Max 3): "))
				if eval("{}".format(attack2))[0] == p4 and eval("{}".format(attack))[0] != p4 and army <= 3 and (eval("{}".format(attack2))[1] - army) > -1 and eval("{}".format(attack))[0] != "Unclaimed":
					if army == 1 and eval("{}".format(attack))[1] == 1:
						diceA = random.randint(1, 6)
						diceD = random.randint(1, 6)
						if diceA > diceD:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA <= diceD:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 1 and eval("{}".format(attack))[1] >= 2:
						diceA = random.randint(1, 6)
						diceD = [random.randint(1, 6), random.randint(1, 6)]
						diceD.sort(reverse=True)
						if diceA > diceD[0]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA <= diceD[0]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 2 and eval("{}".format(attack))[1] == 1:
						diceA = [random.randint(1, 6), random.randint(1, 6)]
						diceD = random.randint(1, 6)
						diceA.sort(reverse=True)
						if diceA[0] > dice:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 2 and eval("{}".format(attack))[1] >= 2:
						diceA = [random.randint(1, 6), random.randint(1, 6)]
						diceD = [random.randint(1, 6), random.randint(1, 6)]
						diceA.sort(reverse=True)
						diceD.sort()
						if diceA[0] > diceD[0]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD[0]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
						if diceA[1] > diceD[1]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[1] <= diceD[1]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 3 and eval("{}".format(attack))[1] == 1:
						diceA = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
						diceD = random.randint(1, 6)
						diceA.sort(reverse=True)
						if diceA[0] > diceD:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
					if army == 3 and eval("{}".format(attack))[1] >= 2:
						diceA = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
						diceD = [random.randint(1, 6), random.randint(1, 6)]
						diceA.sort(reverse=True)
						diceD.sort(reverse=True)
						if diceA[0] > diceD[0]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[0] <= diceD[0]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
						if diceA[1] > diceD[1]:
							eval("{}".format(attack))[1] = eval("{}".format(attack))[1] - 1
						elif diceA[1] <= diceD[1]:
							eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - 1
				else:
					print("You cannot attack from someone else's territory/You cannot attack yourself/You are sending more armies then possible/You cannot attack an unclaimed territory!")
					turnbool = 1
				if eval("{}".format(attack))[1] == 0:
					eval("{}".format(attack))[0] = eval("{}".format(attack2))[0]
					eval("{}".format(attack))[1] = eval("{}".format(attack))[1] + army
					eval("{}".format(attack2))[1] = eval("{}".format(attack2))[1] - army
				if eval("{}".format(attack2))[1] == 0:
					eval("{}".format(attack2))[0] = "Unclaimed"
			
		if c == 4:
			c = 1
		else:
			c += 1
		if Alaska[0] == NorthwestTerritory[0] and NorthwestTerritory[0] == Ontario[0] and Ontario[0] == EasternCanada[0] and EasternCanada[0] == EasternUS[0] and EasternUS[0] == Mexico[0] and Mexico[0] == WesternUS[0] and WesternUS[0] == Alberta[0] and Alberta[0] == Greenland[0] and Greenland[0] == Venezuela[0] == Brazil[0] and Brazil[0] == Peru[0] and Peru[0] == Argentina[0] and Argentina[0] == NorthernEurope[0] == UK[0] and UK[0] == Iceland[0] and Iceland[0] == WesternEurope[0] and WesternEurope[0] == SouthernEurope[0] and SouthernEurope[0] == Scandinavia[0] and Scandinavia[0] == Russia[0] and Russia[0] == MiddleEast[0] == India[0] and India[0] == SouthernAsia[0] and SouthernAsia[0] == China[0] and China[0] == Afghanistan[0] and Afghanistan[0] == Urals[0] and Urals[0] == EasternSiberia[0] and EasternSiberia[0] == CentralSiberia[0] and CentralSiberia[0] == WesternSiberia[0] and WesternSiberia[0] == SouthernSiberia[0] and SouthernSiberia[0] == Egypt[0] == EasternAfrica[0] and EasternAfrica[0] == CentralAfrica[0] and CentralAfrica[0] == SouthernAfrica[0] and SouthernAfrica[0] == NorthernAfrica[0] and NorthernAfrica[0] == Madagascar[0] and Madagascar[0] == NewGuinea[0] == Indonesia[0] and Indonesia[0] == WesternAustralia[0] and WesternAustralia[0] == EasternAustralia[0] and EasternAustralia[0] == p2:
			BG = pygame.image.load("images/win.png")
			BGRect = BG.get_rect()
			BGRect.centerx
			BGRect.centery
			width, height = BG.get_size()
			screen = pygame.display.set_mode((width, height))
			screen.blit(BG, BGRect)
			font = pygame.font.Font("redoctober", 40)
			WIN = font.render("Congratulations {}! ^C to exit".format(p1), 1, (255, 255, 0))
			WINRect = WIN.get_rect()
			WINRect.x = BGRect.x/2
			WINRect.y = BGRect.y/2
			screen.blit(WIN, WINRect)
			pygame.display.flip()
			while True:
				pass
		if Alaska[0] == NorthwestTerritory[0] and NorthwestTerritory[0] == Ontario[0] and Ontario[0] == EasternCanada[0] and EasternCanada[0] == EasternUS[0] and EasternUS[0] == Mexico[0] and Mexico[0] == WesternUS[0] and WesternUS[0] == Alberta[0] and Alberta[0] == Greenland[0] and Greenland[0] == Venezuela[0] == Brazil[0] and Brazil[0] == Peru[0] and Peru[0] == Argentina[0] and Argentina[0] == NorthernEurope[0] == UK[0] and UK[0] == Iceland[0] and Iceland[0] == WesternEurope[0] and WesternEurope[0] == SouthernEurope[0] and SouthernEurope[0] == Scandinavia[0] and Scandinavia[0] == Russia[0] and Russia[0] == MiddleEast[0] == India[0] and India[0] == SouthernAsia[0] and SouthernAsia[0] == China[0] and China[0] == Afghanistan[0] and Afghanistan[0] == Urals[0] and Urals[0] == EasternSiberia[0] and EasternSiberia[0] == CentralSiberia[0] and CentralSiberia[0] == WesternSiberia[0] and WesternSiberia[0] == SouthernSiberia[0] and SouthernSiberia[0] == Egypt[0] == EasternAfrica[0] and EasternAfrica[0] == CentralAfrica[0] and CentralAfrica[0] == SouthernAfrica[0] and SouthernAfrica[0] == NorthernAfrica[0] and NorthernAfrica[0] == Madagascar[0] and Madagascar[0] == NewGuinea[0] == Indonesia[0] and Indonesia[0] == WesternAustralia[0] and WesternAustralia[0] == EasternAustralia[0] and EasternAustralia[0] == p2:
			BG = pygame.image.load("images/win.png")
			BGRect = BG.get_rect()
			BGRect.centerx
			BGRect.centery
			width, height = BG.get_size()
			screen = pygame.display.set_mode((width, height))
			screen.blit(BG, BGRect)
			font = pygame.font.Font("redoctober", 450)
			WIN = font.render("Congratulations {}! ^C to exit".format(p2), 1, (255, 255, 0))
			WINRect = WIN.get_rect()
			WINRect.x = BGRect.x/2
			WINRect.y = BGRect.y/2
			screen.blit(WIN, WINRect)
			pygame.display.flip()
			while True:
				pass
		if Alaska[0] == NorthwestTerritory[0] and NorthwestTerritory[0] == Ontario[0] and Ontario[0] == EasternCanada[0] and EasternCanada[0] == EasternUS[0] and EasternUS[0] == Mexico[0] and Mexico[0] == WesternUS[0] and WesternUS[0] == Alberta[0] and Alberta[0] == Greenland[0] and Greenland[0] == Venezuela[0] == Brazil[0] and Brazil[0] == Peru[0] and Peru[0] == Argentina[0] and Argentina[0] == NorthernEurope[0] == UK[0] and UK[0] == Iceland[0] and Iceland[0] == WesternEurope[0] and WesternEurope[0] == SouthernEurope[0] and SouthernEurope[0] == Scandinavia[0] and Scandinavia[0] == Russia[0] and Russia[0] == MiddleEast[0] == India[0] and India[0] == SouthernAsia[0] and SouthernAsia[0] == China[0] and China[0] == Afghanistan[0] and Afghanistan[0] == Urals[0] and Urals[0] == EasternSiberia[0] and EasternSiberia[0] == CentralSiberia[0] and CentralSiberia[0] == WesternSiberia[0] and WesternSiberia[0] == SouthernSiberia[0] and SouthernSiberia[0] == Egypt[0] == EasternAfrica[0] and EasternAfrica[0] == CentralAfrica[0] and CentralAfrica[0] == SouthernAfrica[0] and SouthernAfrica[0] == NorthernAfrica[0] and NorthernAfrica[0] == Madagascar[0] and Madagascar[0] == NewGuinea[0] == Indonesia[0] and Indonesia[0] == WesternAustralia[0] and WesternAustralia[0] == EasternAustralia[0] and EasternAustralia[0] == p3:
			BG = pygame.image.load("images/win.png")
			BGRect = BG.get_rect()
			BGRect.centerx
			BGRect.centery
			width, height = BG.get_size()
			screen = pygame.display.set_mode((width, height))
			screen.blit(BG, BGRect)
			font = pygame.font.Font("redoctober", 40)
			WIN = font.render("Congratulations {}! ^C to exit".format(p3), 1, (255, 255, 0))
			WINRect = WIN.get_rect()
			WINRect.x = BGRect.x/2
			WINRect.y = BGRect.y/2
			screen.blit(WIN, WINRect)
			pygame.display.flip()
			while True:
				pass
		if Alaska[0] == NorthwestTerritory[0] and NorthwestTerritory[0] == Ontario[0] and Ontario[0] == EasternCanada[0] and EasternCanada[0] == EasternUS[0] and EasternUS[0] == Mexico[0] and Mexico[0] == WesternUS[0] and WesternUS[0] == Alberta[0] and Alberta[0] == Greenland[0] and Greenland[0] == Venezuela[0] == Brazil[0] and Brazil[0] == Peru[0] and Peru[0] == Argentina[0] and Argentina[0] == NorthernEurope[0] == UK[0] and UK[0] == Iceland[0] and Iceland[0] == WesternEurope[0] and WesternEurope[0] == SouthernEurope[0] and SouthernEurope[0] == Scandinavia[0] and Scandinavia[0] == Russia[0] and Russia[0] == MiddleEast[0] == India[0] and India[0] == SouthernAsia[0] and SouthernAsia[0] == China[0] and China[0] == Afghanistan[0] and Afghanistan[0] == Urals[0] and Urals[0] == EasternSiberia[0] and EasternSiberia[0] == CentralSiberia[0] and CentralSiberia[0] == WesternSiberia[0] and WesternSiberia[0] == SouthernSiberia[0] and SouthernSiberia[0] == Egypt[0] == EasternAfrica[0] and EasternAfrica[0] == CentralAfrica[0] and CentralAfrica[0] == SouthernAfrica[0] and SouthernAfrica[0] == NorthernAfrica[0] and NorthernAfrica[0] == Madagascar[0] and Madagascar[0] == NewGuinea[0] == Indonesia[0] and Indonesia[0] == WesternAustralia[0] and WesternAustralia[0] == EasternAustralia[0] and EasternAustralia[0] == p4:
			BG = pygame.image.load("images/win.png")
			BGRect = BG.get_rect()
			BGRect.centerx
			BGRect.centery
			width, height = BG.get_size()
			screen = pygame.display.set_mode((width, height))
			screen.blit(BG, BGRect)
			font = pygame.font.Font("redoctober", 40)
			WIN = font.render("Congratulations {}! ^C to exit".format(p4), 1, (255, 255, 0))
			WINRect = WIN.get_rect()
			WINRect.x = BGRect.x/2
			WINRect.y = BGRect.y/2
			screen.blit(WIN, WINRect)
			pygame.display.flip()
			while True:
				pass
init()
