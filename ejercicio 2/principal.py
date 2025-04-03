'''Se requiere que los estudiantes diseñen un módulo independiente que contenga 
implementaciones  de algoritmos  de ordenamiento  simples  (bubble  sort). El 
objetivo es  que,  a  partir de  una  función  principal, se  invoquen los  métodos del 
módulo para ordenar una lista de números y demostrar la correcta separación de 
responsabilidades, fomentando la modularidad y la reutilización del código.'''

from ordenamiento import bubble_sort

def main():
    numeros = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original: ", numeros)
    
    ordenada = bubble_sort(numeros)
    print("Lista ordenada: ", ordenada)

if __name__ == "__main__":
    main()