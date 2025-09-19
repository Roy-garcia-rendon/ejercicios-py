import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# 1. Cargar dataset de reseñas
(X_train, y_train), (X_test, y_test) = keras.datasets.imdb.load_data(num_words=10000)

# 2. Rellenar secuencias para que todas tengan el mismo largo
X_train = keras.preprocessing.sequence.pad_sequences(X_train, maxlen=200)
X_test = keras.preprocessing.sequence.pad_sequences(X_test, maxlen=200)

# 3. Definir modelo
modelo = keras.Sequential([
    layers.Embedding(10000, 32, input_length=200),  # convierte palabras en vectores
    layers.LSTM(64),                                # capa recurrente (procesa secuencias)
    layers.Dense(1, activation="sigmoid")           # salida binaria (positivo/negativo)
])

# 4. Compilar
modelo.compile(optimizer="adam",
               loss="binary_crossentropy",
               metrics=["accuracy"])

# 5. Entrenar
modelo.fit(X_train, y_train, epochs=3, batch_size=64, validation_split=0.2)

# 6. Evaluar
loss, acc = modelo.evaluate(X_test, y_test)
print(f"Precisión en prueba: {acc*100:.2f}%")
