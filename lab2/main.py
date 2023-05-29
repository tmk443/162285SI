import gradio as gr
import numpy as np
import pandas as pd


def execute_query(name, number):
    try:
        dataframe = pd.read_csv(name, delimiter=' ', header=None)
        dataframe.fillna(0, inplace=True)
        rows = dataframe.iloc[[number - 1], :]

        return rows
    except Exception as e:
        return 'Niepoprawny plik'
