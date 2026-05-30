# 🔺 Rotacionador de Triângulo

> Projeto de Álgebra Linear I — Transformações Lineares e Rotações em R²

**Autores:** Jhemeson, Júlio, Dassayeff e João Pedro Duarte  
**Disciplina:** Álgebra Linear I  
**Instituição:** Centro Universitário de Ensino Superior do Amazonas (CIESA)

---

## 📋 Sobre o Projeto

Este projeto implementa um **rotacionador de triângulos** utilizando conceitos de **Álgebra Linear**, especificamente transformações lineares através de matrizes de rotação em R². O programa solicita as coordenadas dos três vértices de um triângulo no plano cartesiano e um ângulo de rotação, aplica a transformação ponto a ponto e exibe o resultado graficamente.

Toda a matemática é implementada **do zero, sem uso de NumPy**, a fim de tornar cada operação explícita e verificável.

---

## 🧮 Fundamentos Matemáticos

### 1. Matriz de Rotação

Uma rotação de ângulo θ em torno da origem é representada pela matriz ortogonal:

```
R(θ) = | cos(θ)  -sin(θ) |
       | sin(θ)   cos(θ) |
```

No código (`matematica_manual.py`), o ângulo é recebido em graus e convertido para radianos antes de calcular as entradas da matriz:

```python
rad = math.radians(angulo)
cos = math.cos(rad)
sin = math.sin(rad)
```

### 2. Aplicação da Transformação (Produto Matriz × Vetor)

Para rotacionar um ponto `P = [x, y]`, calcula-se o produto matriz-vetor:

```
| x' |   | cos(θ)  -sin(θ) |   | x |
| y' | = | sin(θ)   cos(θ) | × | y |
```

Explicitando as fórmulas escalares:

```
x' = cos(θ) · x  −  sin(θ) · y
y' = sin(θ) · x  +  cos(θ) · y
```

Isso é exatamente o que `multiplicar_matriz_vetor` computa com seu duplo loop `i, j`:

```python
for i in range(2):
    for j in range(2):
        resultado[i] += matriz[i][j] * vetor[j]
```

A transformação é aplicada **individualmente a cada vértice** do triângulo dentro de `main.py`:

```python
for vetor_ponto in pontos:
    novo_ponto = multiplicar_matriz_vetor(matriz_rotacao, vetor_ponto)
    pontos_rotacionados.append(novo_ponto)
```

O resultado de cada vértice é arredondado para 2 casas decimais.

### 3. Determinante e Preservação de Área

O determinante de uma matriz 2×2

```
M = | a  b |      →    det(M) = a·d − b·c
    | c  d |
```

é implementado diretamente em `calcular_determinante_2x2`. Para a matriz de rotação:

```
det(R) = cos(θ)·cos(θ) − (−sin(θ))·sin(θ)
       = cos²(θ) + sin²(θ)
       = 1
```

Isso confirma que **matrizes de rotação são isometrias**: preservam distâncias, ângulos e áreas. O programa exibe esse valor calculado numericamente (e arredondado para 2 casas) como verificação.

> ⚠️ O determinante exibido é `round(det, 2)`. Para ângulos como 45° ou 30°, o valor exato já é 1; para outros ângulos podem surgir erros de ponto flutuante da ordem de 1e-16, que o arredondamento elimina.

### 4. Verificação de Triângulo Não Degenerado

Três pontos são colineares quando a área do triângulo que formariam é zero. A área com sinal é dada por metade do determinante da matriz de coordenadas homogêneas:

```
      | x1  y1  1 |
  A = | x2  y2  1 |   ÷ 2
      | x3  y3  1 |
```

Expandindo pela terceira coluna, obtém-se a expressão usada em `existe_triangulo`:

```
2A = x1·(y2 − y3) + x2·(y3 − y1) + x3·(y1 − y2)
```

Se `|2A| ≤ 1e-9`, os pontos são colineares e o programa rejeita a entrada:

```python
area_dobrada = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
return abs(area_dobrada) > 1e-9
```

---

## 📁 Estrutura do Projeto

```
Rotacionador-de-Triângulo/
│
├── README.md
└── Rotacionador de Triângulo/       ← pasta com espaço no nome
    ├── main.py                      # Ponto de entrada
    ├── matematica_manual.py         # Operações matriciais sem NumPy
    └── graficos.py                  # Visualização com Matplotlib
```

### Descrição dos Módulos

#### `main.py`
Orquestra o fluxo do programa:
- Coleta as coordenadas dos 3 vértices via `input`, com tratamento de `ValueError`
- Chama `existe_triangulo` em loop até receber pontos válidos
- Solicita o ângulo de rotação em graus
- Constrói a matriz de rotação e aplica a transformação a cada vértice
- Exibe o determinante e as coordenadas originais/rotacionadas
- Chama `plotar_comparacao` para gerar o gráfico

#### `matematica_manual.py`
Implementações matemáticas sem dependências externas:

| Função | O que faz |
|---|---|
| `criar_matriz_rotacao(angulo)` | Converte graus → radianos e monta R(θ) como lista de listas |
| `multiplicar_matriz_vetor(matriz, vetor)` | Produto M·v com duplo loop; retorna resultado arredondado a 2 casas |
| `calcular_determinante_2x2(matriz)` | Calcula `a·d − b·c`; retorna arredondado a 2 casas |
| `existe_triangulo(pontos)` | Testa colinearidade pela área com sinal; retorna `bool` |

#### `graficos.py`
Visualização com Matplotlib:
- Fecha cada triângulo adicionando o primeiro vértice ao final da lista
- Plota original em **azul** (marcador `o`) e rotacionado em **vermelho** (marcador `s`)
- Usa `plt.axis('equal')` para manter proporção correta dos eixos

---

## ⚙️ Requisitos e Instalação

- Python 3.7 ou superior
- Matplotlib (única dependência externa)

```bash
pip install matplotlib
```

---

## 🚀 Como Executar

```bash
cd "Rotacionador de Triângulo"
python main.py
```

### Exemplo de Sessão

```
--- ROTACIONADOR DE TRIÂNGULO ---
Vértice 1 - x: 0
Vértice 1 - y: 0
Vértice 2 - x: 4
Vértice 2 - y: 0
Vértice 3 - x: 2
Vértice 3 - y: 3

Digite o ângulo de rotação (em graus): 45

--- RESULTADOS MATEMÁTICOS ---
Determinante da Matriz de Rotação: 1.0
Conclusão: Como o determinante é 1, a área da figura se manteve idêntica!

Coordenadas originais:
[0.0, 0.0]
[4.0, 0.0]
[2.0, 3.0]

Coordenadas após rotação de 45.0°:
[0.0, 0.0]
[2.83, 2.83]
[-0.71, 3.54]

Gerando gráfico comparativo...
```

---

## 💡 Casos de Teste

| Teste | Vértices | Ângulo | Resultado esperado |
|---|---|---|---|
| Rotação 90° | (0,0), (1,0), (0,1) | 90° | Triângulo girado 90° anti-horário |
| Rotação 180° | (1,1), (3,1), (2,3) | 180° | Triângulo espelhado em relação à origem |
| Rotação 360° | Quaisquer | 360° | Coordenadas idênticas às originais (dentro da precisão de 2 casas) |
| Colinearidade | (0,0), (1,1), (2,2) | — | Programa rejeita e pede novos pontos |

---

## 🎓 Conceitos de Álgebra Linear Aplicados

1. **Transformação Linear** — Mapeamento T: R² → R² que preserva adição e multiplicação escalar
2. **Matriz de Rotação** — Representação matricial de uma rotação; pertence ao grupo SO(2)
3. **Produto Matriz-Vetor** — Mecanismo de aplicação de T a cada vértice
4. **Determinante** — Fator de escala de área; `det(R) = 1` confirma que R é isometria
5. **Colinearidade e Área com Sinal** — Uso do determinante de coordenadas homogêneas para validar a entrada
6. **Ortonormalidade** — As colunas de R(θ) formam base ortonormal; daí a preservação de normas e ângulos

---

## 📄 Licença

Projeto de código aberto disponível para fins educacionais.
