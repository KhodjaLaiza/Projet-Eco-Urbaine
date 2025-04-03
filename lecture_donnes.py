import pandas as pd
import os

folder_path = "donnees"

files = [f for f in os.listdir(folder_path) if f.endswith(".xlsx")]

all_data = []

for file in files:
    file_path = os.path.join(folder_path, file)  # Chemin complet du fichier
    
    annee = None
    for part in file.split("_"):
        if part.isdigit() and len(part) == 4 and part.startswith("20"):
            annee = int(part)
            break
    
    df_dict = pd.read_excel(io=file_path, sheet_name=["Bâti", "Non bâti", "Ensemble des maisons", "Ensemble des appartements"])  
    
    for sheet_name, df in df_dict.items():
        if "codegeo" in df.columns:
            df = df[df["codegeo"].astype(str).str.startswith(("75", "91", "92", "93", "94", "95", "77", "78"))]
            df["fichier"] = file
            df["feuille"] = sheet_name
            df["annee"] = annee  # Ajouter l'année extraite

            all_data.append(df)  # Ajouter le dataframe à la liste
if all_data:
    # Concaténer tous les DataFrames en un seul
    final_df = pd.concat(all_data, ignore_index=True)

    # Sauvegarde en CSV
    final_df.to_csv("idf_data.csv", index=False, encoding="utf-8")

    print("✅ Le fichier CSV a été créé : idf_data.csv")
else:
    print("❌ Aucune donnée valide trouvée. Vérifie tes fichiers Excel.")

print(df.head())
