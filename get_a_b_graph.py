import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from data_from_table import ore13_2, ore19, ore26_5, ore37_5, ore53
from indexes import indexes
import pandas as pd

def fit_function(energy, A, b):
    return A * (1 - np.exp(-b * energy))

ores = [ore53(), ore13_2(), ore19(), ore26_5(), ore37_5()]

colors = ['blue', 'green', 'red', 'purple', 'orange']

plt.figure(figsize=(10, 6))
model_predict = []
for i, ore in enumerate(ores):
    params, _ = curve_fit(fit_function, ore.energy, ore.t10,maxfev=5000)
    
    A, b = params
    model_predict.append((A, b))
    energy_fit = np.linspace(min(ore.energy), max(ore.energy), 100)
    t10_fit = fit_function(energy_fit, A, b)

    
    plt.scatter(ore.energy, ore.t10, label=f'Ore {i+1} Data', color=colors[i])
    
    plt.plot(energy_fit, t10_fit, label=f'Ore {i+1} Fit: A={A:.2f}, b={b:.2f}', color=colors[i])

plt.xlabel('Energy, kWth/t')
plt.ylabel('t10 %')
plt.title('t10 vs Energy for Various Ores')
plt.legend()
plt.grid(True)

plt.savefig("result.png")

SG =  2.85


DWI = np.array([])
SCSE = np.array([])
t_a = np.array([])
M_ia = np.array([])
M_ih = np.array([])
M_ic = np.array([])
for A, b in model_predict:
    DWI = np.append(DWI, indexes.getDWi(A, b, SG))
    SCSE = np.append(SCSE, indexes.getSCSE(A, b))
    t_a = np.append(t_a, indexes.gett_a(A, b, SG))
    M_ia = np.append(M_ia, indexes.getM_ia(A, b))
    M_ic = np.append(M_ic, indexes.getM_ic(A, b))
    M_ih = np.append(M_ih, indexes.getM_ih(A, b))

out = pd.DataFrame({"DWI": DWI, "SCSE": SCSE, "t_a": t_a, "M_ia": M_ia, "M_ih": M_ih, "M_ic": M_ic})
out.to_excel("out.xlsx")