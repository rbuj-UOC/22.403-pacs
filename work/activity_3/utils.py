import concurrent.futures
import pandas as pd


def filtro_media_movil(senal: pd.DataFrame, ventana: int = 5):
    """ Aplica un filtro de media móvil para suavizar la señal. """
    return senal.rolling(window=ventana, min_periods=1).mean()


def detectar_picos(senal: pd.DataFrame, umbral: int = 160) -> list[int]:
    """ Detecta los picos de frecuencia cardíaca por encima del umbral. """
    return senal[senal > umbral].index.tolist()


def procesar_senal_jugador(df: pd.DataFrame, jugador_id: int) -> dict[int, list[int]]:
    """
    Filtra y encuentra picos de frecuencia cardíaca para un jugador específico.

    Args:
        df (pd.DataFrame): DataFrame con datos de frecuencia cardíaca.
        jugador_id (int): ID del jugador a procesar.

    Returns:
        dict: Datos del jugador con frecuencia filtrada y picos detectados.
    """
    datos_jugador = df[df["jugador_id"] == jugador_id].copy()
    datos_jugador["frecuencia_filtrada"] = filtro_media_movil(
        datos_jugador["frecuencia"])
    picos = detectar_picos(datos_jugador["frecuencia_filtrada"])
    return {"jugador_id": jugador_id, "picos": picos}


def procesar_senales_concurrentes(filename: str, chunk: list[int]) -> list[dict[int, list[int]]]:
    """
    Procesa señales de frecuencia cardíaca de jugadores.
    Args:
        filename (str): Ruta al archivo CSV con datos de frecuencia cardíaca.
        chunk (list): Lista de IDs de jugadores a procesar.
    Returns:
        list: Lista de diccionarios con datos de jugadores y picos detectados.
    """
    df = pd.read_csv(filename, sep=',')
    return [procesar_senal_jugador(df, x) for x in chunk]
