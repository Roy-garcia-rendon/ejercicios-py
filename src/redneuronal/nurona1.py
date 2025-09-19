import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# 1. Cargar dataset MNIST
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# 2. Normalizar (0-255 → 0-1)
X_train = X_train / 255.0
X_test = X_test / 255.0

# 3. Definir modelo
modelo = keras.Sequential([
    layers.Flatten(input_shape=(28,28)),      # convertir imagen 28x28 a vector 784
    layers.Dense(128, activation="relu"),     # capa oculta
    layers.Dropout(0.2),                      # prevenir sobreajuste
    layers.Dense(10, activation="softmax")    # salida (10 dígitos)
])

# 4. Compilar
modelo.compile(optimizer="adam",
               loss="sparse_categorical_crossentropy",
               metrics=["accuracy"])

# 5. Entrenar
modelo.fit(X_train, y_train, epochs=5)

# 6. Evaluar
loss, acc = modelo.evaluate(X_test, y_test)
print(f"Precisión en prueba: {acc*100:.2f}%")
