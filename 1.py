import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(1, 10, 100)
y = (1/x) * np.cos(x**2 + 1/x)
plt.plot(x, y, label='(1/x)*cos(x^2 + 1/x)', color='red', linewidth=4, linestyle='-')
plt.title('Графік функції Y(x) = (1/x)*cos(x^2 + 1/x)', fontsize=14)
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('Y(x)', fontsize=12, color='blue')
plt.legend()
plt.grid(True)
plt.show()
