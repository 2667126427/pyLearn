import matplotlib.pyplot as plt

x = list(range(0, 1001))
y = [i**2 for i in x]
plt.plot(x, y, 'r')
plt.xlabel()
plt.title("Square")
plt.show()