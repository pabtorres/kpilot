import matplotlib.pyplot as plt
from PIL import Image
import base64
import os


def plot_indicators(df, grupo_rollout_input: str, metrics_dict: dict, output_path: str, webpquality: int, show: bool) -> str:
    name_1, name_2, name_3 = metrics_dict['name_1'], metrics_dict['name_2'], metrics_dict['name_3']
    required_cols = ['Fecha', name_1, name_2, name_3]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Falta la columna requerida: '{col}'")
    
    # Definir el estilo del gráfico
    plt.style.use('seaborn-v0_8-white')

    # Crear una figura con dimensiones duplicadas
    fig = plt.figure(figsize=(10, 6))

    # Generar el gráfico en la figura
    ax = fig.add_subplot()
    ax.grid(False)

    df.plot(x='Fecha', y=[name_1, name_2, name_3], marker='o', linestyle='--', ax=ax)
    plt.axhline(y=0, color='black', linestyle='--') # Línea horizontal en el 0
    plt.xlabel("Fecha")
    plt.ylabel("KPI")
    plt.title(f'Evolución KPIs en Grupo {grupo_rollout_input}')

    # Mostrar los valores numéricos de cada punto en formato porcentual
    for index, row in df.iterrows():
        for column in [name_1, name_2, name_3]:
            value = row[column]
            formatted_value = "{:.2%}".format(value)
            ax.text(row['Fecha'], value + 0.001, formatted_value, ha='center', va='bottom', fontsize=10)

    max_value = df[[name_1, name_2, name_3]].max().max()
    ylim_upper = max_value + 0.005
    min_value = df[[name_1, name_2, name_3]].min().min()
    ylim_bott = min_value - 0.003
    plt.ylim(ylim_bott, ylim_upper)
    plt.xticks(rotation=30, ha='right')

    # Mover la leyenda fuera del gráfico
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

    # Guardar la imagen en un archivo
    plt.savefig(output_path, format='png', dpi=80, bbox_inches='tight')
    if show:
        plt.show()
    plt.close()
    
    # Convertir imagen a WEBP
    with Image.open(output_path) as img:
        img = img.convert('RGB')

        img.save(f"{output_path.split('.')[0]}.webp", "WEBP", quality=webpquality)

    # Leer la imagen en bytes y codificarla en base64
    with open('grafico.webp', 'rb') as image_file:
        image_bytes = image_file.read()
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')

    return image_base64