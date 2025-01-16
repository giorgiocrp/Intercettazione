import numpy as np
from scipy.optimize import fsolve

# Parametri dell'oggetto in movimento
v_t = 250  # velocità dell'oggetto in movimento (m/s)
theta_t = np.radians(45)  # rotta rispetto al nord magnetico (gradi -> radianti)
h_t = 10000  # quota (m)
d_0 = 15000  # distanza iniziale dalla stazione (m)
phi_s = np.radians(60)  # azimuth rispetto alla stazione (gradi -> radianti)

# Parametri dell'oggetto dalla stazione
v_s = 250  # velocità (m/s)

# Posizione iniziale dell'oggetto in movimento
x_t0 = d_0 * np.cos(phi_s)
y_t0 = d_0 * np.sin(phi_s)

# Funzione da risolvere per intercettazione
def equations(vars):
    t, theta_s = vars
    # Posizione dell'oggetto in movimento
    x_t = x_t0 + v_t * t * np.cos(theta_t)
    y_t = y_t0 + v_t * t * np.sin(theta_t)
    # Posizione dell'oggetto dalla stazione
    x_s = v_s * t * np.cos(theta_s)
    y_s = v_s * t * np.sin(theta_s)
    return [
        x_t - x_s,  # Uguaglianza delle coordinate x
        y_t - y_s   # Uguaglianza delle coordinate y
    ]

# Stima iniziale per t e theta_s
initial_guess = [10, np.radians(45)]

# Risoluzione del sistema
solution = fsolve(equations, initial_guess)
t_intercept, theta_s_intercept = solution

# Risultati
theta_s_deg = np.degrees(theta_s_intercept)
if t_intercept<0: 
    print("Intercettazione impossibile")
else:
    print(f"Tempo di intercettazione: {t_intercept:.2f} secondi")
    print(f"Rotta per l'intercettazione: {theta_s_deg:.2f} gradi")
