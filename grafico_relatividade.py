import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# Dados
v_frac = np.linspace(0.01, 0.999, 200)
energy = 1 / np.sqrt(1 - v_frac**2)

# Criar figura
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 10)
line, = ax.plot([], [], color='red', linewidth=2)
point, = ax.plot([], [], 'bo')
text = ax.text(0.7, 8, '', fontsize=12)

ax.set_title("Energia vs Velocidade (animação)", fontsize=14, fontweight='bold')
ax.set_xlabel("Fração da velocidade da luz (v/c)")
ax.set_ylabel("Energia relativa (unidades de mc²)")
ax.grid(True)

def init():
    line.set_data([], [])
    point.set_data([], [])
    text.set_text('')
    return line, point, text

def animate(i):
    x = v_frac[:i]
    y = energy[:i]
    line.set_data(x, y)
    if i > 0:
        point.set_data([x[-1]], [y[-1]]) 
        text.set_text(f"v/c = {x[-1]:.3f}\nEnergia ≈ {y[-1]:.2f}")
    return line, point, text

ani = animation.FuncAnimation(fig, animate, frames=len(v_frac), init_func=init, interval=30, blit=True)

ani.save("energia_velocidade_luz.gif", writer=PillowWriter(fps=30))
