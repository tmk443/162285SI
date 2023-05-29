import gradio as gr
import pandas as pd


def execute_query(name, number, question):
    try:
        dataframe = pd.read_csv(name, delimiter=' ', header=None)
        temp = 0
        if question == "Ile klas decyzyjnych?":
            temp = len(pd.read_csv('info.txt', header=None).index)
        elif question == "Wielkość każdej klasy decyzyjnej":
            temp = pd.read_csv('info.txt', delimiter=' ', header=None, names=['Nazwa pliku', 'ilość atrybutów', 'liczba obiektów'])

        return [f'Ilość obiektów: {len(dataframe.index)}\nIlość atrybutów: {len(dataframe.columns)}', temp, dataframe.iloc[:number]]
    except Exception as e:
        return [None, None, None]


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            nazwa = gr.Textbox(label="Podaj nazwę pliku")
            liczba = gr.Number(label='Podaj liczbę wierszy', precision=0)
            gowno = gr.Textbox(label="Podaj to gowno")

        with gr.Column():
            data = gr.Textbox(label="informacje")
            answer = gr.Textbox(label="Odpowiedź")
            wynik = gr.Dataframe(label="Wynik")

    btn = gr.Button("Pokaż")
    btn.click(execute_query, inputs=[nazwa, liczba, gowno], outputs=[data, answer, wynik])

demo.launch()
