# 🔺 Rotacionador de Triângulo

> Projeto de Álgebra Linear I - Transformações Lineares e Rotações em R²

**Autores:** Jhemeson, Júlio, Dassayeff e João Pedro Duarte

---

## 📋 Sobre o Projeto

Este projeto implementa um **rotacionador de triângulos** utilizando conceitos de **Álgebra Linear**, especificamente transformações lineares através de matrizes de rotação. O programa permite ao usuário inserir as coordenadas de um triângulo no plano cartesiano e rotacioná-lo por um ângulo especificado, visualizando graficamente o resultado da transformação.

### 🎯 Objetivos

- Demonstrar a aplicação prática de **matrizes de rotação** em R²
- Implementar operações matriciais **sem bibliotecas externas** (NumPy)
- Visualizar transformações lineares geometricamente
- Verificar a preservação de área através do **determinante**

---

## 🧮 Conceitos Matemáticos

### Matriz de Rotação

Para rotacionar um ponto (x, y) por um ângulo θ em torno da origem, utilizamos a matriz de rotação:

```
R(θ) = | cos(θ)  -sin(θ) |
       | sin(θ)   cos(θ) |
```

### Transformação Linear

A rotação de um ponto é obtida pela multiplicação matriz-vetor:

```
| x' |   | cos(θ)  -sin(θ) |   | x |
| y' | = | sin(θ)   cos(θ) | × | y |
```

### Determinante e Preservação de Área

O **determinante da matriz de rotação é sempre 1**, o que significa que a transformação preserva áreas. Isso é verificado no programa:

```
det(R) = cos²(θ) + sin²(θ) = 1
```

---

## 📁 Estrutura do Projeto

```
Rotacionador-de-Triângulo/
│
├── README.md                          # Este arquivo
├── Rotacionador de Triângulo/
│   ├── main.py                        # Programa principal
│   ├── matematica_manual.py           # Operações matriciais
│   └── graficos.py                    # Visualização gráfica
```

### Descrição dos Módulos

#### 🔹 `main.py`
Arquivo principal que:
- Solicita as coordenadas dos 3 vértices do triângulo
- Valida se os pontos formam um triângulo não degenerado
- Solicita o ângulo de rotação (em graus)
- Aplica a transformação linear
- Exibe os resultados numéricos
- Gera o gráfico comparativo

#### 🔹 `matematica_manual.py`
Implementações matemáticas do zero, sem uso de NumPy:
- `criar_matriz_rotacao(angulo)` — Gera a matriz R(θ) a partir de um ângulo em graus
- `multiplicar_matriz_vetor(matriz, vetor)` — Produto matriz × vetor (aplica a rotação a um ponto)
- `calcular_determinante_2x2(matriz)` — Calcula o determinante de uma matriz 2×2
- `existe_triangulo(pontos)` — Verifica se os três vértices são não colineares (área ≠ 0)

#### 🔹 `graficos.py`
Visualização usando Matplotlib:
- `plotar_comparacao(pontos_orig, pontos_rot)` — Plota o triângulo original e o rotacionado no mesmo plano cartesiano

---

## ⚙️ Instalação e Requisitos

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Dependências

O projeto utiliza apenas uma biblioteca externa:

```bash
matplotlib
```

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/Rotacionador-de-Triangulo.git
   cd Rotacionador-de-Triangulo
   ```

2. **Instale as dependências:**
   ```bash
   pip install matplotlib
   ```

---

## 🚀 Como Executar

1. Navegue até o diretório do projeto:
   ```bash
   cd "Rotacionador de Triângulo"
   ```

2. Execute o programa principal:
   ```bash
   python main.py
   ```

### Exemplo de Uso

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

### Resultado Visual

O programa gera um gráfico mostrando:
- **Triângulo azul (original)** com marcadores circulares
- **Triângulo vermelho (rotacionado)** com marcadores quadrados
- Grade cartesiana para referência
- Eixos X e Y centralizados

---

## 💡 Casos de Teste Sugeridos

### Teste 1: Rotação de 90°
```
Vértices: (0,0), (1,0), (0,1)
Ângulo: 90°
Resultado esperado: Triângulo rotacionado no sentido anti-horário
```

### Teste 2: Rotação de 180°
```
Vértices: (1,1), (3,1), (2,3)
Ângulo: 180°
Resultado esperado: Triângulo invertido em relação à origem
```

### Teste 3: Rotação de 360°
```
Vértices: Quaisquer
Ângulo: 360°
Resultado esperado: Triângulo retorna à posição original
```

---

## 🔬 Detalhes de Implementação

### Por que Implementação Manual?

Este projeto **não utiliza NumPy** intencionalmente para:
1. **Fins didáticos** — Compreender os algoritmos por trás das operações
2. **Transparência** — Cada operação é explícita e verificável
3. **Aprendizado** — Consolidar conceitos de Álgebra Linear na prática

### Validação de Entrada

Antes de aplicar a rotação, o programa verifica se os três vértices são **não colineares** usando a fórmula da área com coordenadas:

```
área_dobrada = x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)
```

Se o resultado for zero (ou muito próximo de zero), os pontos são colineares e não formam um triângulo válido. O usuário é então solicitado a inserir novos valores.

### Arredondamento

Os resultados são arredondados para 2 casas decimais para melhor legibilidade:
```python
return [round(resultado[0], 2), round(resultado[1], 2)]
```

### Ângulos

- **Entrada:** Graus (mais intuitivo para o usuário)
- **Processamento:** Convertido para radianos internamente via `math.radians(angulo)`

---

## 🎓 Conceitos de Álgebra Linear Aplicados

1. **Transformações Lineares** — Mapeamento de R² → R²
2. **Matrizes de Rotação** — Representação de rotações como operadores lineares
3. **Produto Matriz-Vetor** — Aplicação de transformações a pontos
4. **Determinante** — Fator de escala de áreas; det(R) = 1 confirma preservação de área
5. **Ortonormalidade** — Matrizes de rotação preservam ângulos e distâncias

---

## 📄 Licença

Este projeto é de código aberto e está disponível para fins educacionais.

---

## 👥 Contribuidores

- **Jhemeson**
- **Júlio**
- **Dassayeff**
- **João Pedro Duarte**

**Disciplina:** Álgebra Linear I  
**Instituição:** Centro Universitário de Ensino Superior do Amazonas (CIESA)

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela no repositório!**

</div>
