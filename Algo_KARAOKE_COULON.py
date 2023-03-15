import random
song0_Played = False
song1_Played = False
song2_Played = False
song3_Played = False
song4_Played = False

class Player:
    def __init__(self,nickname,song0,song1,song2,song3,song4):

        self.pseudo=nickname
        self.chanson0=song0
        self.chanson1=song1
        self.chanson2=song2
        self.chanson3=song3
        self.chanson4=song4
    song0 = 0
    song1 = 0
    song2 = 0
    song3 = 0
    song4 = 0

    def song0(self):
        song0 = 0
        print("Votre score sur la chanson 0 est de", song0)
        
    def song1(self):
        song1 = 0
        print("Votre score sur la chanson 1 est de", song1)

    def song2(self):
        song2 = 0
        print("Votre score sur la chanson 2 est de", song2)

    def song3(self):
        song3 = 0
        print("Votre score sur la chanson 3 est de", song3)

    def song4(self):
        song4 = 0
        print("Votre score sur la chanson 4 est de", song4)

    
    

    
        return self.pseudo


    def playSong_0(self):
        if song0_Played == False:
            song0 = random.randint(50,100)
            song0_Played = True
            previousScore_0 = song0

        else :
            song0 = random.randint(50,100)
            if song0 < previousScore_0 :
                song0 = previousScore_0
    
    def playSong_1(self):
        if song1_Played == False:
            song1 = random.randint(50,100)
            song1_Played = True
            previousScore_1 = song1

        else: 
            song1 = random.randint(50,100)
            if song1 < previousScore_1 :
                song1 = previousScore_1

    def playSong_2(self):
        if song2_Played == False:
            song2 = random.randint(50,100)
            song2_Played = True
            previousScore_2 = song2

        else: 
            song2= random.randint(50,100)
            if song2 < previousScore_2 :
                song2 = previousScore_2

    def playSong_3(self):
        if song3_Played == False:
            song3 = random.randint(50,100)
            song3_Played = True
            previousScore_3 = song3

        else: 
            song3 = random.randint(50,100)
            if song3 < previousScore_3 :
                song3 = previousScore_3

    def playSong_4(self):
        if song4_Played == False:
            song4 = random.randint(50,100)
            song4_Played = True
            previousScore_4 = song4

        else: 
            song4 = random.randint(50,100)
            if song4 < previousScore_4 :
                song4 = previousScore_4


    def moyenneScore(self):
        total =  song0 += song 1 += song2 += song3 += song4
        moyenne = total/5
        print(moyenne)

    def totalScore(self):
        scoreTotal = song0 += song 1 += song2 += song3 += song4
        print(scoreTotal)

Michel = Player("Michello le rigolo",0,0,0,0,0)   


Michel.playSong_0

print(Michel.song0)