import math

def criar_matriz_rotacao(angulo):
    """Gera a matriz de rotação 2x2 com base no ângulo fornecido."""
    rad = math.radians(angulo)
    cos = math.cos(rad)
    sin = math.sin(rad)
    
    return [
        [cos, -sin],
        [sin,  cos]
    ]

def multiplicar_matriz_vetor(matriz, vetor):
    resultado = [0, 0]
    for i in range(2):
        for j in range(2):
            resultado[i] += matriz[i][j] * vetor[j]
    return [round(resultado[0], 2), round(resultado[1], 2)]

def existe_triangulo(pontos):
    """Verifica se três pontos formam um triângulo não degenerado (não colineares)."""
    (x1, y1), (x2, y2), (x3, y3) = pontos
    area_dobrada = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    return abs(area_dobrada) > 1e-9

def calcular_determinante_2x2(matriz):
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[1][0]
    d = matriz[1][1]
    
    det = (a * d) - (b * c)
    return round(det, 2)
