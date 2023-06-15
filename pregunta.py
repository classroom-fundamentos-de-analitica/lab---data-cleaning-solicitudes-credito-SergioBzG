"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------
Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.
"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0, encoding="utf-8")

    df = df.dropna()
    df['sexo'] = df['sexo'].apply(str.lower)
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].apply(str.lower)
    df['idea_negocio'] = df['idea_negocio'].apply(lambda x: x.lower().replace('_', ' ').replace('-', ' ').strip() if type(x) == str else x)
    df['barrio'] = df['barrio'].apply(lambda x: x.lower().replace('_', ' ').replace('-', ' ') if type(x) == str else x)
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(str).apply(lambda x: x.replace('.0', ''))
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], format='%d/%m/%Y', errors='coerce').fillna(
            pd.to_datetime(df['fecha_de_beneficio'], format='%Y/%m/%d', errors='coerce')
        )
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].dt.strftime('%d-%m-%Y')
    df['monto_del_credito'] = df['monto_del_credito'].apply(lambda x: x.replace('$', '').strip().replace(',', '').replace('.00', '') if type(x) == str else x)
    df['línea_credito'] = df['línea_credito'].apply(lambda x: x.lower().replace('_', ' ').replace('-', ' ').strip() if type(x) == str else x)
    df['sexo'].value_counts().to_list()
    df = df.drop_duplicates()
    return df