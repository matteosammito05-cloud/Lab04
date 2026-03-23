def somma(n):
    if n == 0:
        return 0
    else:
        return n + somma(n - 1)
    
def main():
    n = int(input("Inserisci un numero: "))
    print("La somma dei primi", n, "numeri è:", somma(n))

main()