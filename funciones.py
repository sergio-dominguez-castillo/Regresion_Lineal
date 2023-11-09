# -*- coding: utf-8 -*-
"""
Created on 01/11/23

@author: Sergio dominguez

"""
# importar librerias
import pandas as pd
import seaborn as sns
import scipy.stats as st
import numpy as np
import statsmodels.api as sm
from scipy import stats
import matplotlib as plt
import matplotlib.pyplot as plt

def Graficar_Regresion(df_data_x,df_data_y,prediccion,columna_x,columna_y,especie):
    """
    Realizar una prueba de hipótesis para comparar media de muestra aleatoria de columna earn con media_hipotetica    
    Args:
        df_data_x (Pandas.Serie): columnas del df para regresion lineal predictor.
        df_data_y (Pandas.Serie): columnas del df para regresion lineal variable de respuesta.
        columna_x (string): nombre columna para eje x
        columna_y (string): nombre columna para eje y
        especie (string): nombre de la especie de pez

        
    Returns:
        none
       
    """
    print(f"-------------Especie -> {especie}  -----------")
    # Realizar la regresión lineal
    #plt.figure(figsize=(12,12))
    plt.scatter(df_data_x, df_data_y, label="Datos reales", color='blue', alpha=0.5)
    plt.scatter(df_data_x, prediccion, label='Predicciones', color='red', alpha=0.5)
    plt.plot(df_data_x, prediccion, color='red', label="Regresión Lineal")
    plt.title(f"Regresión lineal entre el {columna_x} y el {columna_y} de la especie de peces -> {especie} ")
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.legend()
    # Calcular los valores de la regresión lineal. Ya veremos el significado de los parámetros
    slope, intercept, r_value, p_value, std_err = stats.linregress(df_data_x, df_data_y)
    slope_p, intercept_p, r_value_p, p_value_p, std_err_p = stats.linregress(df_data_x, prediccion)
    # Mostrar el gráfico completo
    plt.show()
    print("----------------------------------------------")
    print("-----Datos Reales   -> Prediccion-------------")
    print(f"Pendiente: {slope}   -> {slope_p}")
    print(f"Intercepto: {intercept}  -> {intercept_p}")
    print(f"Error estándar: {std_err}  -> {std_err_p}")
    print(f"Coef. de correlación: {r_value}  -> {r_value_p}")
    print("----------------------------------------------")
    
    # Mostrar un gráfico de los residuos
    residuals = df_data_y - (slope * df_data_x + intercept)
    residuals_p = prediccion - (slope_p * df_data_x + intercept_p)
    # Mostrar un gráfico de los residuos
    plt.figure()
    plt.scatter(df_data_x, residuals, label="Datos reales", color='blue', alpha=0.5)
    plt.scatter(df_data_x, residuals_p, label='Predicciones', color='red', alpha=0.5)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.title(f"Gráfico de Residuos de la especie de peces -> {especie} ")
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.legend()
    plt.show()

    print("----------------------------------------------")
