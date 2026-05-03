import matplotlib.pyplot as plt

def plotar_comparacao(pontos_orig, pontos_rot):
    
    # Adicionamos o primeiro ponto no final da lista para "fechar" o desenho do triângulo
    triangulo_orig = pontos_orig + [pontos_orig[0]]
    triangulo_rot = pontos_rot + [pontos_rot[0]]

    # Separando X e Y para o Matplotlib
    x_orig = [p[0] for p in triangulo_orig]
    y_orig = [p[1] for p in triangulo_orig]
    
    x_rot = [p[0] for p in triangulo_rot]
    y_rot = [p[1] for p in triangulo_rot]

    plt.figure(figsize=(8, 8))
    
    # Plotando os triângulos original e rotacionado
    plt.plot(x_orig, y_orig, marker='o', color='blue', label='Original', linewidth=2)
    plt.plot(x_rot, y_rot, marker='s', color='red', label='Rotacionado', linewidth=2)

    # Eixos e grade
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    
    # Configurações de exibição
    plt.title('Transformação Linear: Rotação de Triângulo')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.legend()
    plt.axis('equal') 
    
    plt.show()
