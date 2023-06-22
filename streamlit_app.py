from game_of_life_functions import create_grid, update_grid
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import time


# Functions
def plot0(grid):

    plt.style.use('dark_background')
    fig0, ax0 = plt.subplots()
    plot0 = st.pyplot(fig0)
    ax0.imshow(grid, cmap='binary_r')
    ax0.set_xticks([])
    ax0.set_yticks([])
    ax0.set_xticklabels([])
    ax0.set_yticklabels([])
    ax0.spines['top'].set_visible(False)
    ax0.spines['bottom'].set_visible(False)
    ax0.spines['left'].set_visible(False)
    ax0.spines['right'].set_visible(False)
    plot0.pyplot(fig0)


def ani1(grid):
    plt.style.use('dark_background')
    fig1, ax1 = plt.subplots()
    plot1 = st.pyplot(fig1)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    ax1.spines['top'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_grid = np.roll(np.roll(grid, i, axis=0), j, axis=1)

            ax1.clear()
            ax1.imshow(new_grid, cmap='binary_r')

            # Hide the ticks and tick labels on both axes
            ax1.set_xticks([])
            ax1.set_yticks([])
            ax1.set_xticklabels([])
            ax1.set_yticklabels([])

            # Hide the spines (borders) of the plot
            ax1.spines['top'].set_visible(False)
            ax1.spines['bottom'].set_visible(False)
            ax1.spines['left'].set_visible(False)
            ax1.spines['right'].set_visible(False)

            plot1.pyplot(fig1)

            time.sleep(0.5)


def run_da_game(rows_cols, probability):

    grid = create_grid(rows_cols, probability)

    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    plot = st.pyplot(fig)

    while True:
        # Update the grid
        grid = update_grid(grid)

        # Clear the previous plot
        ax.clear()

        # Show the updated grid
        ax.imshow(grid, cmap='binary_r')

        # Hide the ticks and tick labels on both axes
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        # Hide the spines (borders) of the plot
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)

        plot.pyplot(fig)

        # Delay between frames (adjust as needed)
        time.sleep(0.1)

# end Functions

# Text
title = 'Jogo da vida de Conway'
topico_0 = 'Introdução'
texto_0 = 'Na década de 1940, John von Neumann, interessado em estudar como sistemas simples\n'\
          'podem evoluir de forma complexa e padronizada, criou o conceito de autômato celular.\n'\
          'Um autômato celular é modelo computacional composto por uma grade de células regular com\n'\
          'um número finito de dimensões. Cada célula possui um número fixo de vizinhas e assume um\n'\
          'estado discreto a cada etapa. A evolução do sistema se dá a partir de um conjunto de regras\n'\
          'que determina o novo estado de uma célula a partir do estado atual de suas vizinhas.\n'\
          'O jogo da vida é um autômato celular bidimensional criado por John Conway em 1970.\n'\
          'Cada célula tem até oito células vizinhas fixas e deve assumir um estado (morta ou vida) a\n'\
          'cada etapa da evolução do sistema.'
topico_1 = 'Quem foi John Conway?'
texto_1 = 'Jhon Horton Conway foi um grande matemático e cientista da computação inglês.\n' \
        'Nascido em Liverpool, passou sua carreira na universidade de Cambridge, onde foi\n' \
        'aluno doutorando e professor e pesquisador. John conway deixou um legaddo duradou,\n' \
        'nos campos em que atuo, o seu trabalho com o jogo da vida lhe rendeu grandes frutos \n' \
        'e reconhecimento.'
topico_2 = 'Regras do jogo da vida'
texto_2 = 'As regras do Jogo da Vida são as seguintes: uma célula viva com menos de dois\n' \
        'vizinhos vivos morre por solidão; uma célula viva com dois ou três vizinhos vivos\n' \
        'permanece viva; uma célula viva com mais de três vizinhos vivos morre de \n' \
        'superpopulação; uma célula morta com exatamente três vizinhos vivos se torna viva.\n' \
        'Com base nessas regras simples, padrões complexos e interessantes podem surgir no jogo,\n' \
        'incluindo osciladores,espaçonaves e estruturas estáveis.'
topico_3 = 'Aplicações do jogo da vida'
texto_3 ='Modelagem de padrões biológicos: O Jogo da Vida pode ser usado para modelar o \n' \
        'comportamento de populações biológicas. Células vivas e mortas podem representar\n' \
        'organismos, e as regras do jogo podem simular a competição, a reprodução e a \n' \
        'sobrevivência desses organismos. Padrões complexos,como osciladores e espaçonaves,\n' \
        'podem emergir e fornecer insights sobre a dinâmica das populações biológicas.\n' \
        'Simulação de sistemas físicos: O Jogo da Vida pode ser usado para simular sistemas\n' \
        'físicos, como a propagação de ondas ou a interação de partículas. As células podem\n' \
        'representar pontos no espaço e as regras do jogo podem representar as interações\n' \
        'entre esses pontos. Isso permite estudar o comportamento coletivo desses sistemas e\n' \
        'observar como padrões se desenvolvem ao longo do tempo.\n' \
        'Teste de algoritmos de computação paralela: O Jogo da Vida é frequentemente usado \n' \
        'como um problema de teste para algoritmos de computação paralela. O jogo pode ser\n' \
        'dividido em várias regiões independentes, permitindo que diferentes partes sejam\n' \
        'processadas simultaneamente em diferentes threads ou processadores.Isso torna o jogo\n' \
        'um excelente exemplo para estudar técnicas de programação paralela\n' \
        'e distribuída.'
subsection_1 ='Explicando o codigo'
subsubsection_1 ='CRIANDO UMA "GRID"'
exp_1 = 'Idealmente é necessario definirmos uma "grid" aonde definiremos quais pontos\n' \
                'estão ativos, por simplicidade neste exercício vamos gerar aleatoriamente\n' \
                'os pontos, de forma que celulas com valor de 0 serão consideradas ligadas\n' \
                'e -1 desligadas. Observe o codigo abaixo:'
code_1 = '''
import numpy as np 

def create_grid(rows_cols, P):
    return np.random.choice([0, 1], size=(rows_cols, rows_cols), p=[1-P, P])
'''
exp_1_2 = 'Aqui geramos com a função "random.choice" do numpy, uma "grid" de pontos que são\n' \
        '0 ou 1 e possuem dimenção rows_cols X rows_cols\n' \
        'e probabilidade P dos pontos estarem ligados.'
code_1_2 = '''
grid = create_grid(5, 0.2)
grid.show()
'''
subsubsection_1_2 = 'ACHANDO VIZINHOS'
exp_1_3 = 'O proximo passo agora seria aplicar as regras do jogo de Conway.\n' \
        'Segundo o jogo se uma celula ativa esta cercada por 2 ou 3 outras\n' \
        'celulas vivas ela pode continuar vivendo, caso contrario morre,\n' \
        'se uma celula morta esta cercada por 3 vivas ela é ligada.\n' \
        'Logo o passo logico agora seria criar uma função que conta\n' \
        'as celulas vivas na vizinhança de um quadrado e aplica as\n' \
        'condições do jogo.'
code_1_3 = '''
def update_grid(grid):
    neighbours = np.zeros_like(grid)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbours += np.roll(np.roll(grid, i, axis=0), j, axis=1)

    new_grid = np.where((grid == 1) & ((neighbours < 2) | (neighbours > 3)), 0, grid)
    new_grid = np.where((grid == 0) & (neighbours == 3), 1, new_grid)

    return new_grid
'''
exp_1_4 = 'Vamos olhar mais de perto o que eu considero a parte mais importante deste codigo,\n' \
        'para contar os vizinhos de maneira rapida e eficiente resolvi pegar a matrix da grid\n' \
        'e mudar ela inteira em um movimento circular para que possamos somar os valores\n' \
        'laterais, a explicação visual a baixo ajudara a entender melhor. Segue o sequite\n' \
        'codigo que mostra visualmente o que esta acontecendo:'
code_1_4 = '''
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_grid = np.roll(np.roll(grid, i, axis=0), j, axis=1)
'''
exp_1_5 = 'Agora que vimos como podemos somar valores\n' \
        'vizinhos vamos estabelecer nossas regras.'
code_1_5 = '''
    new_grid = np.where((grid == 1) & ((neighbours < 2) | (neighbours > 3)), 0, grid)
    new_grid = np.where((grid == 0) & (neighbours == 3), 1, new_grid)
'''
exp_1_6 = 'Nesta primeira linha estabelecemos se nossa celula esta ligada\n' \
         ' e não tem 2 e nem 3 vizinhos proximos faça ela ser desligada\n' \
         'e caso contrario apenas retorne o valor dela ( ela possui 2 ou 3 vizinhos),\n' \
         'se ela esta deligada e tem 3 vizinhos ativos ela se torna ligada\n' \
         'caso contrario apenas retorna seu valor. Agora vamos aplicar tudo\n' \
         'e rodar o nosso jogo.'

subsection_2 = 'O Jogo da vida de Conway!'

link = 'Download para Windows: https://drive.google.com/file/d/1R5AscSyugvoo3TKQ5MjTdkF7-C0aqMnx/view?usp=sharing'
# end text

# Site code
st.title(title)
st.subheader(topico_0)
st.text(texto_0)
st.subheader(topico_1)
st.text(texto_1)
st.subheader(topico_2)
st.text(texto_2)
st.subheader(topico_3)
st.text(texto_3)

st.subheader(subsection_1)
st.markdown(subsubsection_1)
st.text(exp_1)
st.code(code_1)
st.text(exp_1_2)
st.code(code_1_2)

with st.form('form'):
    button0 = False
    grid = create_grid(5, 0.2)
    button0 = st.form_submit_button('Roda!')
    if button0 is True:
        plot0(grid)
        button0 =False

st.markdown(subsubsection_1_2)
st.text(exp_1_3)
st.code(code_1_3)
st.text(exp_1_4)
st.code(code_1_4)

with st.form('form1'):
    button = st.form_submit_button('Roda')
    reset = False
    grid = np.zeros((10, 10))
    grid[2, 2] = 1
    grid[5, 6] = 1
    grid[5, 4] = 1
    grid[4, 5] = 1
    grid[6, 5] = 1

    if button is True:
        ani1(grid)
        reset = False
    else:
        plot0(grid)

    reset = st.form_submit_button('Reseta')
    if reset is True:
        button = False


st.text(exp_1_5)
st.code(code_1_5)
st.text(exp_1_6)

st.subheader(subsection_2)

with st.form('form2'):
    rows_cols = st.slider('Qual a dimenção da sua grid?', 0, 100)
    probability = st.slider('Qual a probabilidade das celulas estarem ligadas ?', min_value=0.0, max_value=1.0, step=0.05)
    submit_button = st.form_submit_button('VAI RODAAAA!')
    if submit_button and rows_cols != 0:
        run_da_game(rows_cols, probability)


st.markdown(link)
# End site code
