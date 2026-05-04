from matematica_manual import (
    criar_matriz_rotacao, 
    multiplicar_matriz_vetor, 
    calcular_determinante_2x2,
    existe_triangulo
)
from graficos import plotar_comparacao

def main():
    print("--- ROTACIONADOR DE TRIÂNGULO ---")
    
    while True:
        pontos = []
        for i in range(3):
            try:
                x = float(input(f"Vértice {i+1} - x: "))
                y = float(input(f"Vértice {i+1} - y: "))
                pontos.append([x, y])
            except ValueError:
                print("Entrada inválida. Digite um número.")
                break

        if len(pontos) < 3:
            print("\nEntrada incompleta. Vamos tentar novamente.\n")
            continue

        if existe_triangulo(pontos):
            break

        print("\nOs pontos informados são colineares e não formam um triângulo válido.")
        print("Tente novamente com outros pontos.\n")

    try:
        angulo = float(input("\nDigite o ângulo de rotação (em graus): "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    matriz_rotacao = criar_matriz_rotacao(angulo)
 
    pontos_rotacionados = []
    for vetor_ponto in pontos:
        novo_ponto = multiplicar_matriz_vetor(matriz_rotacao, vetor_ponto)
        pontos_rotacionados.append(novo_ponto)

    det = calcular_determinante_2x2(matriz_rotacao)

    print("\n--- RESULTADOS MATEMÁTICOS ---")
    print(f"Determinante da Matriz de Rotação: {det}")
    if det == 1.0:
        print("Conclusão: Como o determinante é 1, a área da figura se manteve idêntica!\n")

    print("Coordenadas originais:")
    for p in pontos:
        print(p)

    print(f"\nCoordenadas após rotação de {angulo}°:")
    for p in pontos_rotacionados:
        print(p)

    print("\nGerando gráfico comparativo...")
    plotar_comparacao(pontos, pontos_rotacionados)

# Executa o programa
if __name__ == "__main__":
    main()
