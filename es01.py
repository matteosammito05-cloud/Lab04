class Squadra:
    def __init__(self, nome):
        self.nome=nome
        self.partite=[]

    def addMatch(self, avv, score):
        self.partite.append((avv, score))

    def getSum(self):
        sum=0
        for row in self.partite:
            sum+=row[1]
        return sum

    def getAverage(self):
        sum=self.getSum
        media=sum/len(self.partite)
        return media

    def getTeams(self):
        teams=[]
        for row in self.partite:
            teams.append(row[0])
        return teams
    
    def getSummary(self):
        sum=self.getSum
        media=self.getAverage
        summary=(sum,media)
        return summary            
            
def main():
    squadra = Squadra("Torino")

    squadra.addMatch("Milano", 67)
    squadra.addMatch("Roma", 67)
    squadra.addMatch("Bologna", 67)

    print("Squadre affrontate:", squadra.getTeams())
    print("Media canestri:", squadra.getAverage())
    print("Riepilogo:", squadra.getSummary())

main()