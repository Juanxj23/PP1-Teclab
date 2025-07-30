import pandas as pd
import matplotlib.pyplot as plt
import os
########################################## codigo de automatizacion, sacar si no funciona
# Rutas absolutas
#ruta_csv = r"C:\Users\USUARIO\OneDrive\AyR Store Data\Project\AyR_Ventas.csv"
#ruta_excel = r"C:\Users\USUARIO\OneDrive\AyR Store Data\Registro de ventas.xlsx"

#Cargar datos actuales del CSV
#if os.path.exists(ruta_csv):
#    data_csv = pd.read_csv(ruta_csv, encoding='latin1', sep=';')
#else:
#    data_csv = pd.DataFrame()

# Cargar nuevos datos desde el Excel
#data_excel = pd.read_excel(ruta_excel)

# Homogeneizar nombres de columnas (por si acaso)
#data_excel.columns = data_excel.columns.str.strip().str.lower()
#data_csv.columns = data_csv.columns.str.strip().str.lower()

# Paso 3: Concatenar los datos
#data_actualizado = pd.concat([data_csv, data_excel], ignore_index=True)

# Paso 4: Guardar el CSV actualizado
#data_actualizado.to_csv(ruta_csv, sep=';', index=False, encoding='latin1')
#print("✅ Se agregaron correctamente los nuevos datos del Excel al CSV.")

########################################## codigo de automatizacion, sacar si no funciona
archivo = "AyR_Ventas.csv"
data = pd.read_csv(archivo, encoding='latin1', sep=';')
data.columns = data.columns.str.strip().str.lower()

print("Primeras filas del dataset:")
print(data.head())
print("\nInformación del dataset:")
print(data.info())

# EliminO filas con datos nulos
data_limpio = data.dropna()
print("\nCantidad de datos nulos por columna después de limpiar:")
print(data_limpio.isnull().sum())

# Mostrar cantidad de filas antes y después de limpiar
print(f"\nCantidad de filas antes de limpiar: {len(data)}")
print(f"Cantidad de filas después de limpiar: {len(data_limpio)}")

# Agrupamos por cliente y sumamos los ingresos que han generado al emprendimiento
data_limpio['ingreso'] = data_limpio['ingreso'].replace('[\$,\.]', '', regex=True).astype(float)
ingresos_por_cliente = data_limpio.groupby('cliente')['ingreso'].sum()
# Ordenar de mayor a menor
ingresos_ordenados = ingresos_por_cliente.sort_values(ascending=False)
# Cliente con más ingresos
cliente_top = ingresos_ordenados.idxmax()
monto_top = ingresos_ordenados.max()
print(f"\nEl cliente que más compró es: {cliente_top}")
print(f"El monto total de sus compras es: {monto_top:.2f}")

top_5_clientes = ingresos_ordenados.head(5)
plt.figure(figsize=(8, 6))
plt.bar(top_5_clientes.index, top_5_clientes.values, color='skyblue')
plt.title('Top 5 Clientes por Ingresos')
plt.xlabel('Cliente')
plt.ylabel('Total de Ingresos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Ahora vamos a ver cuales son los modelos de zapatillas más vendidos y el que menos salidas ha tenido.
# Contar cuántas veces se vendió cada modelo
conteo_modelos = data_limpio['modelo'].value_counts()
modelo_top = conteo_modelos.idxmax()
ventas_top = conteo_modelos.max()
# Modelo menos vendido (pero que se vendió al menos una vez)
modelo_menos = conteo_modelos.idxmin()
ventas_menos = conteo_modelos.min()
print(f"\nEl modelo más vendido es: {modelo_top} con {ventas_top} ventas.")
print(f"El modelo menos vendido es: {modelo_menos} con {ventas_menos} venta(s).")

# Top 3 modelos más vendidos de las zapatillas
top_3_modelos = conteo_modelos.head(3)
print("\nTop 3 modelos más vendidos:")
print(top_3_modelos)
plt.figure(figsize=(8, 6))
plt.bar(top_3_modelos.index, top_3_modelos.values, color='salmon')
plt.title('Top 3 Modelos de Zapatillas Más Vendidos')
plt.xlabel('Modelo')
plt.ylabel('Cantidad de Ventas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
