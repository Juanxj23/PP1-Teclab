import pandas as pd
import os

#  Rutas
excel_path = r"C:\Users\USUARIO\OneDrive\AyR Store Data\Registro de ventas.xlsx"
csv_path = r"C:\Users\USUARIO\OneDrive\AyR Store Data\Project\AyR_Ventas.csv"

#  Leer Excel
df_excel = pd.read_excel(excel_path)
df_excel.columns = df_excel.columns.str.strip().str.lower()

# sincronizamos
if os.path.exists(csv_path):
    df_csv = pd.read_csv(csv_path, encoding='latin1', sep=';')
    df_csv.columns = df_csv.columns.str.strip().str.lower()

    # Convertir columna 'fecha' a solo fecha si existe
    if 'fecha' in df_csv.columns:
        df_csv['fecha'] = pd.to_datetime(df_csv['fecha'], errors='coerce').dt.date

    # Concatenar y eliminar duplicados
    df_combinado = pd.concat([df_csv, df_excel], ignore_index=True)
    df_final = df_combinado.drop_duplicates()

    # Guardar CSV actualizado
    df_final.to_csv(csv_path, index=False, sep=';', encoding='latin1')
    print("✅ Datos nuevos agregados sin duplicar.")
else:
    # Crear CSV desde Excel
    df_excel.to_csv(csv_path, index=False, sep=';', encoding='latin1')
    print("✅ CSV creado a partir del Excel.")
