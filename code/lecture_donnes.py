import pandas as pd
import os


folder = "../input"
files = os.listdir(folder)
all_dfs = []

wanted_sheets = ["Bâti", "Non bâti", "Ensemble des maisons", "Ensemble des appartements"]
city = ("75", "91", "92", "93", "94", "95", "77", "78")

for file in files:
    if not file.startswith("~") and file.endswith(".xlsx"):  # Vérifier l'extension
        year = file.replace(".xlsx", "")
        excel_file = pd.ExcelFile(f"{folder}/{file}", engine="openpyxl")  # Lire les fichiers .xlsx
        sheets = excel_file.sheet_names
        for sheet in wanted_sheets:
            if sheet in sheets:  # Vérifier que la feuille existe
                df = pd.read_excel(f"{folder}/{file}", sheet_name=sheet)
                df = df[df["codgeo"].astype(str).str.startswith(city)]
                df["year"] = int(year)
                df["type_bien"]=sheet
                all_dfs.append(df)
                #liste_df = liste_df.rename(columns=lambda col: f"{col}_{sheet}" if col not in ["codgeo", "libgeo", "année"] else col)

df_final = pd.concat(all_dfs, ignore_index=True, sort=False)

df_final.to_csv("../output/donnee_filtrees.csv", index=False, encoding="utf-8")
print("fichier csv généré avec succées)")

