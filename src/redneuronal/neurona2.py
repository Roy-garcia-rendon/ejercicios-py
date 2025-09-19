import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Cargar dataset de casas
data = fetch_california_housing()
X, y = data.data, data.target

# 2. Normalizar
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 3. Dividir en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Definir modelo
modelo = keras.Sequential([
    layers.Dense(64, activation="relu", input_shape=(X.shape[1],)),
    layers.Dense(64, activation="relu"),
    layers.Dense(1)  # salida: precio estimado
])

# 5. Compilar
modelo.compile(optimizer="adam", loss="mse", metrics=["mae"])

# 6. Entrenar
modelo.fit(X_train, y_train, epochs=20, batch_size=32, verbose=1)

# 7. Evaluar
loss, mae = modelo.evaluate(X_test, y_test)
print(f"Error absoluto medio en prueba: {mae:.2f}")
