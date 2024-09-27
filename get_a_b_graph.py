import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from data_from_table import ore13_2, ore19, ore26_5, ore37_5, ore53

def fit_function(energy, A, b):
    return A * (1 - np.exp(-b * energy))

ores = [ore53(), ore13_2(), ore19(), ore26_5(), ore37_5()]

colors = ['blue', 'green', 'red', 'purple', 'orange']

plt.figure(figsize=(10, 6))

for i, ore in enumerate(ores):
    params, _ = curve_fit(fit_function, ore.energy, ore.t10,maxfev=5000)
    
    A, b = params
    
    energy_fit = np.linspace(min(ore.energy), max(ore.energy), 100)
    t10_fit = fit_function(energy_fit, A, b)
    
    plt.scatter(ore.energy, ore.t10, label=f'Ore {i+1} Data', color=colors[i])
    
    plt.plot(energy_fit, t10_fit, label=f'Ore {i+1} Fit: A={A:.2f}, b={b:.2f}', color=colors[i])

plt.xlabel('Energy, kWth/t')
plt.ylabel('t10 %')
plt.title('t10 vs Energy for Various Ores')
plt.legend()
plt.grid(True)

plt.savefig("plot.png")