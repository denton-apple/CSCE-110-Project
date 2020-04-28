import matplotlib.pyplot as plt

x_values = list(range(-50,51))
y_values = []

for x in x_values:
    y_values.append(3 * (x ** 2) + 5 * x - 6)
    
plt.xlabel("x - values")
plt.ylabel("y - values")
plt.title("This is a graph of a quadratic")
plt.plot(x_values, y_values, color = 'b')
plt.show()