import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Cargar dataset Iris
iris = load_iris()
X = iris.data   # características (largo y ancho de pétalos y sépalos)
y = iris.target # etiquetas (0,1,2 especies de flores)

# 2. Normalizar datos (es importante para redes neuronales)
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 3. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Crear el modelo
modelo = keras.Sequential([
    layers.Dense(10, activation="relu", input_shape=(4,)),  # capa oculta con 10 neuronas
    layers.Dense(8, activation="relu"),                     # otra capa oculta
    layers.Dense(3, activation="softmax")                   # capa de salida (3 clases)
])

# 5. Compilar el modelo
modelo.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# 6. Entrenar
modelo.fit(X_train, y_train, epochs=50, batch_size=8, verbose=1)

# 7. Evaluar
loss, acc = modelo.evaluate(X_test, y_test)
print(f"\nPrecisión en datos de prueba: {acc*100:.2f}%")

# 8. Probar con un dato nuevo
nueva_flor = [[5.1, 3.5, 1.4, 0.2]]  # valores de ejemplo
nueva_flor = scaler.transform(nueva_flor)  # normalizar igual que los datos de entrenamiento
prediccion = modelo.predict(nueva_flor)
print("\nPredicción (probabilidades):", prediccion)
print("Clase predicha:", iris.target_names[prediccion.argmax()])
