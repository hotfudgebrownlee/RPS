from player import Player, RandomBot

class RPS:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.logstring = ''
        self.rules = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'}
        self.tie = False
        self.games = 0
        self.startGame()
        
    def logstringAdd(self, string):
        # print(string)
        self.logstring += string
        
    def getSelection(self, player: Player):
        player.makeChoice()
        self.logstringAdd(f'{player.getName()} chose {player.getChoice()}. ')
    
    def scoreGame(self):
        c1 = self.player1.getChoice()
        c2 = self.player2.getChoice()
        if c1 == c2:
            self.tie = True
            self.logstringAdd(f'{c1} ties {c2}. No one wins. ')
        elif self.rules[c1] == c2:
            self.logstringAdd(f'{c1} beats {c2}. {self.player1.setWinner()}')
        else:
            self.logstringAdd(f'{c2} beats {c1}. {self.player2.setWinner()}')
            
    def reset(self):
        self.logstring = ''
        self.tie = False
        self.games += 1
    
    def startGame(self):
        self.reset()
        self.logstringAdd(f'{self.player1.getName()} vs {self.player2.getName()}: ')
        for playerID in [self.player1, self.player2]:
            self.getSelection(playerID)
        self.scoreGame()
        print(self.logstring)
        if (self.tie):
            self.startGame()
        
player1 = RandomBot('bob')
player2 = RandomBot('fred')
rps = RPS(player1, player2)
print(f'Games played: {rps.games}')
print(f'{player1.getName()} wins: {player1.points}')
print(f'{player2.getName()} wins: {player2.points}')