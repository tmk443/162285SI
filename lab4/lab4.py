import numpy as np

# zad 1
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y_and = np.array([0, 0, 0, 1])
Y_not = np.array([1, 0, 1, 0])
Y = np.array([0, 1, 0, 0])


def perceptron_learn(X, Y, lr=0.1, epochs=100):
    w = np.zeros(X.shape[1])
    b = 0
    for epoch in range(epochs):
        for x, y in zip(X, Y):
            y_pred = np.dot(w, x) + b
            y_pred = 1 if y_pred > 0 else 0
            error = y - y_pred
            w += lr * error * x
            b += lr * error
    return w, b


w_and, b_and = perceptron_learn(X, Y_and)
w_not, b_not = perceptron_learn(X, Y_not)

test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
print("AND:")
for x in test_inputs:
    y_pred = np.dot(x, w_and) + b_and
    y_pred = 1 if y_pred > 0 else 0
    print("{} = {}".format(x, y_pred))

print("NOT:")
for x in test_inputs:
    y_pred = np.dot(x, w_not) + b_not
    y_pred = 1 if y_pred > 0 else 0
    print("{} = {}".format(x, y_pred))

# zad 2


w, b = perceptron_learn(X, Y)

test_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
print("x1 ∧ ¬x2:")
for x in test_inputs:
    y_pred = np.dot(x, w) + b
    y_pred = 1 if y_pred > 0 else 0
    print("{} = {}".format(x, y_pred))
