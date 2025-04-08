import pandas as pd
import matplotlib.pyplot as plt

# Charger les données filtrées
chemin = "../tmp/donnee_filtrees.csv"
df = pd.read_csv(chemin)

# Filtrer sur le type "Non bâti"
df_non_bati = df[df["type_bien"] == "Non bâti"]

# Calculer le prix moyen au m² par année (valeur foncière totale / nb de transactions)
df_prix_temps = df_non_bati.groupby("year").agg({
    "valeurfonc_sum_cod2": "sum",
    "nbtrans_cod2": "sum"
}).reset_index()

# Éviter les divisions par zéro
df_prix_temps["prixm2_moyen"] = df_prix_temps["valeurfonc_sum_cod2"] / df_prix_temps["nbtrans_cod2"]

# Tracer le graphique
plt.figure(figsize=(10, 6))
plt.plot(df_prix_temps["year"], df_prix_temps["prixm2_moyen"], marker="o", linestyle="-", color="green")
plt.title("Évolution du prix moyen des terres non bâties en Île-de-France")
plt.xlabel("Année")
plt.ylabel("Prix moyen au m² (€)")
plt.grid(True)
plt.tight_layout()
plt.show()

df_bati = df[df["type_bien"] == "Bâti"]

# Calculer le prix moyen au m² par année
df_prix_bati = df_bati.groupby("year").agg({
    "valeurfonc_sum_cod1": "sum",
    "nbtrans_cod1": "sum"
}).reset_index()

# Calcul du prix moyen
df_prix_bati["prixm2_moyen"] = df_prix_bati["valeurfonc_sum_cod1"] / df_prix_bati["nbtrans_cod1"]

# Tracer le nuage de points
plt.figure(figsize=(10, 6))
plt.plot(df_prix_bati["year"], df_prix_bati["prixm2_moyen"], marker="o", linestyle="-", color="blue")
plt.title("Évolution du prix moyen des biens bâtis en Île-de-France")
plt.xlabel("Année")
plt.ylabel("Prix moyen au m² (€)")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))

# Courbe des terres non bâties
plt.plot(df_prix_temps["year"], df_prix_temps["prixm2_moyen"],
         marker="o", linestyle="-", color="green", label="Non bâti")

# Courbe des biens bâtis
plt.plot(df_prix_bati["year"], df_prix_bati["prixm2_moyen"],
         marker="o", linestyle="-", color="blue", label="Bâti")

# Personnalisation
plt.title("Évolution du prix moyen au m² en Île-de-France")
plt.xlabel("Année")
plt.ylabel("Prix moyen au m² (€)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
