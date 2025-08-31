import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

true_m = 3
true_c = 2

X = np.linspace(0, 10, 100)
Y = true_m * X + true_c + np.random.randn(*X.shape) * 0.5 

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(optimizer='sgd', loss='mean_squared_error')

history = model.fit(X, Y, epochs=100, verbose=0)

m, c = model.layers[0].get_weights()
print(f"Learned equation: y = {m[0][0]:.2f}x + {c[0]:.2f}")


plt.scatter(X, Y, label="Data")
plt.plot(X, model.predict(X), color="red", label="Fitted Line")
plt.legend()
plt.show()
