class Doc:

    cont=0

    def __init__(self, nom, cog,anno=2022):
        self.nom=nom
        self.cog=cog
        self.anno=anno
        self.birth=None

        Doc.cont+= 1
        self.num = Doc.cont

    def getNome(self):
        return self.nom
    
    def getCognome(self):
        return self.cog
    
    def getAnno(self):
        return self.anno
    
    def setBirth(self, anno):
        if anno>self.anno:
            self.birth=self.anno
        else:
            self.birth=anno

    def getBirth(self):
        return self.birth

    def getNum(self):
        return self.num

def main():
    doc1 = Doc("Mario", "Rossi")
    doc1.setBirth(1990)

    doc2 = Doc("Luca", "Bianchi", 2020)
    doc2.setBirth(2025)

    print("Documento 1:")
    print(doc1.getNome(), doc1.getCognome())
    print("Anno rilascio:", doc1.getAnno())
    print("Anno nascita:", doc1.getBirth())
    print("Numero documento:", doc1.getNum())

    print("\nDocumento 2:")
    print(doc2.getNome(), doc2.getCognome())
    print("Anno rilascio:", doc2.getAnno())
    print("Anno nascita:", doc2.getBirth())
    print("Numero documento:", doc2.getNum())

main()