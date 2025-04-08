import pandas as pd
import matplotlib.pyplot as plt

# Charger les données filtrées
chemin = "../tmp/donnee_filtrees.csv"
df = pd.read_csv(chemin)
clean_df2 = df[df["valeurfonc_sum_cod121"].notna() & df["sbati_sum_cod121"].notna()]
clean_df2["departement"] = clean_df2["codgeo"].astype(str).str[:2]

idf = ["75", "77", "78", "91", "92", "93", "94", "95"]
idf_clean_df2 = clean_df2[clean_df2["departement"].isin(idf)]
grouped_sum = idf_clean_df2.groupby(["year", "departement"]).agg(
    valeurfonc_totale=("valeurfonc_sum_cod121", "sum"),
    surface_totale=("sbati_sum_cod121", "sum")
).reset_index()

# Calcul du prix moyen global au m²
grouped_sum["pxm2_global"] = grouped_sum["valeurfonc_totale"] / grouped_sum["surface_totale"]
pivot_global = grouped_sum.pivot(index="year", columns="departement", values="pxm2_global")

# Tracer le graphique
plt.figure(figsize=(12, 6))
for col in pivot_global.columns:
    plt.plot(pivot_global.index, pivot_global[col], label=f'Département {col}')

plt.title("Évolution du prix moyen au m² (valeur foncière / surface) des appartements en Île-de-France")
plt.xlabel("Année")
plt.ylabel("Prix moyen global au m² (€)")
plt.legend(title="Département")
plt.grid(True)
plt.tight_layout()
plt.show()
