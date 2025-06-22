import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# Tema escuro
plt.style.use('dark_background')

# Dados
v_frac = np.linspace(0.01, 0.999, 200)
gamma = 1 / np.sqrt(1 - v_frac**2)

energia = gamma  # E ~ mc² * γ
tempo = gamma     # Δt = γ * Δt₀

# Criar figura
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 10)

linha_energia, = ax.plot([], [], color='cyan', linewidth=2, label='Energia (E/mc²)')
linha_tempo, = ax.plot([], [], color='magenta', linestyle='--', linewidth=2, label='Dilatação do tempo (Δt/Δt₀)')
ponto, = ax.plot([], [], 'o', color='yellow')
texto = ax.text(0.7, 8, '', fontsize=12, color='white')

# Estética
ax.set_title("Energia e Dilatação do Tempo vs Velocidade", fontsize=14, fontweight='bold', color='white')
ax.set_xlabel("Fração da velocidade da luz (v/c)", color='white')
ax.set_ylabel("Valor relativo (γ)", color='white')
ax.grid(True, linestyle=':', alpha=0.4)
ax.tick_params(colors='white')
ax.legend()

def init():
    linha_energia.set_data([], [])
    linha_tempo.set_data([], [])
    ponto.set_data([], [])
    texto.set_text('')
    return linha_energia, linha_tempo, ponto, texto

def animate(i):
    x = v_frac[:i]
    y1 = energia[:i]
    y2 = tempo[:i]
    linha_energia.set_data(x, y1)
    linha_tempo.set_data(x, y2)
    if i > 0:
        ponto.set_data([x[-1]], [y1[-1]])
        texto.set_text(f"v/c = {x[-1]:.3f}\nγ ≈ {y1[-1]:.2f}")
    return linha_energia, linha_tempo, ponto, texto

ani = animation.FuncAnimation(fig, animate, frames=len(v_frac), init_func=init, interval=30, blit=True)

ani.save("grafico_relatividade_duplo.gif", writer=PillowWriter(fps=30))
