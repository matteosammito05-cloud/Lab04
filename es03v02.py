class Player:
    def __init__(self, nom, cog, eta):
        self.nom = nom
        self.cog = cog
        self.eta = eta
        self._team = None

    def getNome(self):
        return self.nom
    
    def getCognome(self):
        return self.cog
    
    def getEta(self):
        return self.eta
    
    def getTeam(self):
        return self._team
    
    def setTeam(self, team):
        if self._team is not None:
            if self in self._team._players:
                self._team._players.remove(self)

        self._team = team

        if team is not None:
            if self not in team._players:
                team._players.append(self)


class Team:
    def __init__(self, nom, citta):
        self.nom = nom
        self.citta = citta
        self._players = []

    def getNome(self):
        return self.nom
    
    def getCitta(self):
        return self.citta
    
    def addPlayer(self, player):
        player.setTeam(self)

    def getPlayers(self):
        return self._players
    
def main():
    team1 = Team("Juventus", "Torino")
    player1 = Player("Mario", "Rossi", 25)

    team1.addPlayer(player1)

    print(player1.getTeam().getNome())  # Juventus
    print([p.getNome() for p in team1.getPlayers()])  # ['Mario']

main()