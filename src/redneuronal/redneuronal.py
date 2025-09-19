import numpy as np

# 1. Datos de entrenamiento
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])
y = np.array([[0],
              [1],
              [1],
              [0]])

# 2. Inicializar pesos aleatorios
np.random.seed(1)
pesos1 = 2 * np.random.random((2, 4)) - 1  # capa oculta (2 entradas -> 4 neuronas)
pesos2 = 2 * np.random.random((4, 1)) - 1  # capa salida (4 neuronas -> 1 salida)

# 3. Función sigmoide y su derivada
def sigmoide(x):
    return 1 / (1 + np.exp(-x))

def sigmoide_derivada(x):
    return x * (1 - x)

# 4. Entrenamiento
for _ in range(10000):
    # Forward propagation
    capa1 = X
    capa2 = sigmoide(np.dot(capa1, pesos1))
    salida = sigmoide(np.dot(capa2, pesos2))

    # Error
    error = y - salida

    # Backpropagation
    ajuste2 = error * sigmoide_derivada(salida)
    error_capa2 = ajuste2.dot(pesos2.T)
    ajuste1 = error_capa2 * sigmoide_derivada(capa2)

    # Actualización de pesos
    pesos2 += capa2.T.dot(ajuste2)
    pesos1 += capa1.T.dot(ajuste1)

# 5. Resultado
print("Salida después de entrenar:")
print(salida)
