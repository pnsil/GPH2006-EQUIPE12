import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


R_moy = []
R_err = []
V_moy = []
V_err = []
for i in range(1, 14):

    FILE = f"C:/Users/C.O.T/Documents/GPH-2006 Électronique et mesures expérimentales/Labo 5 - Transfert de puissance et lignes de transmission/GPH2006-EQUIPE12/lab5 - 25 fev 2026/R - pt1.{i}.lvm"

    df = pd.read_csv(FILE, skiprows=21, delimiter='\t', decimal=',')

    R = df["Untitled"].to_numpy()

    R_moy.append(float(np.mean(R)))
    R_err.append(float(np.std(R, ddof=1) / np.sqrt(len(R))))


    FILE = f"C:/Users/C.O.T/Documents/GPH-2006 Électronique et mesures expérimentales/Labo 5 - Transfert de puissance et lignes de transmission/GPH2006-EQUIPE12/lab5 - 25 fev 2026/V - pt1.{i}.lvm"

    df = pd.read_csv(FILE, skiprows=21, delimiter='\t', decimal=',')

    V = df["Untitled"].to_numpy()

    V_moy.append(float(np.mean(V)))
    V_err.append(float(np.std(V, ddof=1) / np.sqrt(len(V))))

data = sorted(zip(R_moy, R_err, V_moy, V_err))
R_moy, R_err, V_moy, V_err = zip(*data)

R_moy = np.array(R_moy)
R_err = np.array(R_err)
V_moy = np.array(V_moy)
V_err = np.array(V_err)

print('\nR_moy =', R_moy)
print('\nR_err =', R_err)
print('\nV_moy =', V_moy)
print('\nV_err =', V_err)

p_moy = V_moy**2 / R_moy
p_err = p_moy*(2*V_err/V_moy + R_err/R_moy)

print('\np_moy =', p_moy)
print('\np_err =', p_err)

plt.figure(1, dpi=200)
#plt.plot(R_moy, p_moy, color='lightskyblue', linewidth=1.5)
#plt.plot(angle, ratio_courant, '.k', markersize=1)
plt.errorbar(R_moy, p_moy, yerr=p_err, xerr=R_err, fmt='o', linestyle=None, color='k', markersize=0.3, ecolor='k', elinewidth=0.75, capsize=1, capthick=0.75, label='Mesures')
plt.xscale('log')
plt.xlabel('Résistance $R$ [\u03A9]')
plt.ylabel('Puissance moyenne dissipée $p_{moy}$ [W]')
plt.legend(loc='best')
plt.minorticks_on()
plt.savefig('p_moy_vs_R.png', dpi=600)
plt.show()
