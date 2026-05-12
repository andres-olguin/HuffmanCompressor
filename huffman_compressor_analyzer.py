import heapq
import os

class NodoHuffman:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.freq < otro.freq

def calcular_frecuencias(texto):
    frecuencias = {}
    for caracter in texto:
        frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
    return frecuencias

def construir_arbol(frecuencias):
    heap = [NodoHuffman(char, freq) for char, freq in frecuencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        nodo1 = heapq.heappop(heap)
        nodo2 = heapq.heappop(heap)

        fusionado = NodoHuffman(None, nodo1.freq + nodo2.freq)
        fusionado.izquierda = nodo1
        fusionado.derecha = nodo2
        heapq.heappush(heap, fusionado)

    return heap[0]

def generar_codigos(raiz, codigo_actual="", codigos={}):
    if raiz is None:
        return

    if raiz.char is not None:
        codigos[raiz.char] = codigo_actual

    generar_codigos(raiz.izquierda, codigo_actual + "0", codigos)
    generar_codigos(raiz.derecha, codigo_actual + "1", codigos)
    return codigos

def comprimir(texto):
    if not texto:
        return "", None

    frecuencias = calcular_frecuencias(texto)
    arbol = construir_arbol(frecuencias)
    codigos = generar_codigos(arbol)
    
    texto_comprimido = "".join([codigos[char] for char in texto])
    return texto_comprimido, arbol

def huffman_analysis(texto_original):
    print("--- Analisis de Algoritmo de Huffman ---")
    print(f"Tamaño original: {len(texto_original) * 8} bits")

    comprimido, arbol = comprimir(texto_original)
    print(f"Tamaño comprimido: {len(comprimido)} bits")
    
    ahorro = 100 * (1 - len(comprimido) / (len(texto_original) * 8))
    print(f"Eficiencia de compresion: {ahorro:.2f}%")
    
    return comprimido

# Ejemplo de ejecucion
if __name__ == "__main__":
    mensaje = "Andres Igor - MasterTech SpA - Ingenieria Civil Informatica UNAB"
    resultado = huffman_analysis(mensaje)
