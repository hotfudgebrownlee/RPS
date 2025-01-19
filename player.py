from abc import ABC, abstractmethod 
import random

class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.choice = ''
        self.winner = False
        self.points = 0
        
    @abstractmethod
    def makeChoice(self):
        pass
    
    def getName(self):
        return self.name
    
    def getChoice(self):
        return self.choice
    
    def setWinner(self):
        self.winner = True
        self.points += 1
        return f'{self.name} wins. '
    
    def resetWinner(self):
        self.winner = False
        
    def isWinner(self):
        return self.winner
    
class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def makeChoice(self):
        print(f'{self.name}, please make a choice.')
        choice = input('[r]ock, [p]aper, [s]cissors, SHOOT! ')
        print(choice.lower()[0])
        while (choice.lower()[0] not in ['r', 'p', 's']):
            match choice.lower()[0]:
                case 'r': 
                    self.choice = 'Rock'
                    print(self.choice)
                case 'p': self.choice = 'Paper'
                case 's': self.choice = 'Scissors'
                case _:
                    print('invalid choice. Choose [r]ock, [p]aper, or [s]cissors.')
                    self.makeChoice()
        print(self.choice)
        # os.system('clear') # clear screen in case of other players
        
class RandomBot(Player):
    def makeChoice(self):
        self.choice = random.choice(['Rock', 'Paper', 'Scissors'])