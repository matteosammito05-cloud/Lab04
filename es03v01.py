class Player:
    def __init__(self, nom, cog, eta):
        self.nom=nom
        self.cog=cog
        self.eta=eta

        self._team=None

    def getNome(self):
        return self.nom
    
    def getCognome(self):
        return self.cog
    
    def getEta(self):
        return self.eta
    
    def getTeam(self):
        return self._team
    
    def setTeam(self, team):
        self._team=team

    
class Team:
    def __init__(self, nom, citta):
        self.nom=nom
        self.citta=citta

        self._players=[]

    def getNome(self):
        return self.nom
    
    def getCitta(self):
        return self.citta
    
    def addPlayer(self, player):
        self._players.append(player)

    def getPlayers(self):
        return self._players
    
def main():
    team1=Team("Juventus", "Torino")
    team2=Team("Milan", "Milano")

    player1=Player("Cristiano", "Ronaldo", 36)
    player2=Player("Zlatan", "Ibrahimovic", 39)

    team1.addPlayer(player1)
    team2.addPlayer(player2)

    player1.setTeam(team1)
    player2.setTeam(team2)

    print(f"{player1.getNome()} {player1.getCognome()} gioca nella squadra {player1.getTeam().getNome()}")
    print(f"{player2.getNome()} {player2.getCognome()} gioca nella squadra {player2.getTeam().getNome()}")