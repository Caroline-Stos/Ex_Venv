import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

caminho_dt = os.environ.get('DATA_PATH')

df = pd.read_csv(caminho_dt, sep=';')

plt.plot(df["Mês"], df["Vendas"])
plt.xlabel("Mês")
plt.ylabel("Total de vendas")
plt.title("Vendas - Ano 2023")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
