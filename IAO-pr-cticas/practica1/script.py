import pandas as pd

def rm_main(input0):
    """
    Esta función toma un DataFrame de RapidMiner (input0),
    realiza conversiones y cálculos sobre los datos de embalses,
    e incluye la columna con el AGUA_ACTUAL de la siguiente semana como variable a predecir.
    """

    # 1. Convertir la columna 'FECHA' a formato datetime.
    df = input0
    df['FECHA'] = pd.to_datetime(df['FECHA'], format='%m/%d/%y %H:%M:%S', errors='coerce')

    # 2. Convertir las columnas AGUA_ACTUAL y AGUA_TOTAL a numérico.
    # Primero, aplicar el reemplazo de coma por punto SOLO a las celdas que sean de tipo string.
    if df['AGUA_ACTUAL'].dtype == 'object':
        df['AGUA_ACTUAL'] = df['AGUA_ACTUAL'].str.replace(',', '.')

    if df['AGUA_TOTAL'].dtype == 'object':
        df['AGUA_TOTAL'] = df['AGUA_TOTAL'].str.replace(',', '.')

    # Convertir las columnas a tipo numérico
    df['AGUA_ACTUAL'] = pd.to_numeric(df['AGUA_ACTUAL'], errors='coerce')
    df['AGUA_TOTAL'] = pd.to_numeric(df['AGUA_TOTAL'], errors='coerce')

    # 3. Extraer el AÑO y la SEMANA de la columna FECHA.
    df['AÑO'] = df['FECHA'].dt.year
    df['SEMANA'] = df['FECHA'].dt.isocalendar().week

    # 4. Filtro opcional: Selecciona embalses específicos.
    embalses_filtrados = [ "Bao",]  # Modificar esta lista según se necesite
    df_filtrado = df[df['EMBALSE_NOMBRE'].isin(embalses_filtrados)]

    # 5. Calcular el cambio semanal del volumen de agua (AGUA_ACTUAL).
    df_filtrado['Cambio_semanal'] = df_filtrado['AGUA_ACTUAL'].diff()

    # 6. Calcular la tasa de cambio (%) semana a semana.
    df_filtrado['Tasa_cambio'] = (df_filtrado['Cambio_semanal'] / df_filtrado['AGUA_ACTUAL'].shift(1)) * 100

    # 7. Calcular el promedio del volumen de agua de las últimas 4 semanas (promedio móvil).
    df_filtrado['Promedio_4_semanas'] = df_filtrado['AGUA_ACTUAL'].rolling(window=4).mean()

    # 8. AGREGAR: Columna a predecir (AGUA_ACTUAL de la siguiente semana).
    df_filtrado['AGUA_SIGUIENTE_SEMANA'] = df_filtrado['AGUA_ACTUAL'].shift(-1)

    # 9. Devolver el DataFrame filtrado y con los cálculos a RapidMiner.
    return df_filtrado


