class Matrix:
    def __init__(self, table):
        self._table = table
        self._rows = len(table)
        self._cols = len(table[0])

    def get_rows(self):
        return self._rows

    def get_cols(self):
        return self._cols
    
    def __add__(self, other):
        result = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                row.append(self._table[i][j] + other._table[i][j])
            result.append(row)
        return Matrix(result)
    
    def __sub__(self, other):
        result = []
        for i in range(self._rows):
            row = []
            for j in range(self._cols):
                row.append(self._table[i][j] - other._table[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        result = []
        for i in range(self._rows):
            row = []
            for j in range(other._cols):
                somma = 0
                for k in range(self._cols):
                    somma += self._table[i][k] * other._table[k][j]
                row.append(somma)
            result.append(row)
        return Matrix(result)

    def __eq__(self, other):
        return self._table == other._table
    
    def __str__(self):
        s = ""
        for row in self._table:
            s += " ".join(map(str, row)) + "\n"
        return s
    
def main():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])

    print("Matrice 1:")
    print(m1)

    print("Matrice 2:")
    print(m2)

    print("Somma:")
    print(m1 + m2)

    print("Differenza:")
    print(m1 - m2)

    print("Prodotto:")
    print(m1 * m2)

    print("Uguaglianza:")
    print(m1 == m2)


if __name__ == "__main__":
    main()