from game_of_life_functions import create_grid, update_grid
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import time


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



title = 'Jogo da vida de Conway'
intro = 'Uma breve introdução sobre quem foi Conway\n' \
        'blabla\n' \
        'more bla bla'
exp_0 = 'Uma breve explicação sobre as regras do jogo\n' \
                'bla bla bla\n' \
                'more bla bla bla'

st.title(title)
st.subheader('Quem foi Conway?')
st.text(intro)
st.subheader('Regras do jogo da vida')
st.text(exp_0)

st.subheader('Explicando o codigo')
st.markdown('CRIANDO UMA "GRID"')
exp_1 = 'Idealmente é necessario definirmos uma "grid" aonde definiremos quais pontos\n' \
                'estão ativos, por simplicidade neste exercício vamos gerar aleatoriamente\n' \
                'os pontos, de forma que celulas com valor de 1 serão consideradas ligadas\n' \
                'e 0 desligadas. Observe o codigo abaixo:'
st.text(exp_1)

code_0 = '''
import numpy as np 

def create_grid(rows_cols, P):
    return np.random.choice([0, 1], size=(rows_cols, rows_cols), p=[1-P, P])
'''
st.code(code_0)
exp_2 = 'Aqui geramos com a função "random.choice" do numpy, uma "grid" de pontos que são\n' \
        '0 ou 1 e possuem dimenção rows_cols X rows_cols\n' \
        'e probabilidade P dos pontos estarem ligados.'
st.text(exp_2)
code_1 = '''
grid = create_grid(5, 0.5)
grid.show()
'''
st.code(code_1)
with st.form('form0'):
    button0 = False
    grid = create_grid(5, 0.2)
    button0 = st.form_submit_button('Roda!')
    if button0 is True:
        plot0(grid)
        button0 =False

st.markdown('ACHANDO VIZINHOS')

exp_3 = 'O proximo passo agora seria aplicar as regras do jogo de Conway.\n' \
        'Segundo o jogo se uma celula ativa esta cercada por 2 ou 3 outras\n' \
        'celulas vivas ela pode continuar vivendo, caso contrario morre,\n' \
        'se uma celula morta esta cercada por 3 vivas ela é ligada.\n' \
        'Logo o passo logico agora seria criar uma função que conta\n' \
        'as celulas vivas na vizinhança de um quadrado e aplica as\n' \
        'condições do jogo.'
st.text(exp_3)

code_2 = '''
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
st.code(code_2)

exp_4 = 'Vamos olhar mais de perto o que eu considero a parte mais importante deste codigo,\n' \
        'para contar os vizinhos de maneira rapida e eficiente resolvi pegar a matrix da grid\n' \
        'e mudar ela inteira em um movimento circular para que possamos somar os valores\n' \
        'laterais, a explicação visual a baixo ajudara a entender melhor. Segue o sequite\n' \
        'codigo que mostra visualmente o que esta acontecendo:'
st.text(exp_4)
code_3 = '''
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_grid = np.roll(np.roll(grid, i, axis=0), j, axis=1)
'''
st.code(code_3)
with st.form('form1'):
    button = st.form_submit_button('Roda')
    reset = False
    grid = np.zeros((5, 5))
    grid[2, 2] = 1

    if button is True:
        ani1(grid)
        reset = False
    else:
        plot0(grid)

    reset = st.form_submit_button('Reseta')
    if reset is True:
        button = False

exp_5 = 'Agora que vimos como podemos somar valores\n' \
        'vizinhos vamos estabelecer nossas regras.'
st.text(exp_5)
code_4 = '''
    new_grid = np.where((grid == 1) & ((neighbours < 2) | (neighbours > 3)), 0, grid)
    new_grid = np.where((grid == 0) & (neighbours == 3), 1, new_grid)
'''
st.code(code_4)
exp_6 = 'Nesta primeira linha estabelecemos se nossa celula esta ligada\n' \
         ' e não tem 2 e nem 3 vizinhos proximos faça ela ser desligada\n' \
         'e caso contrario apenas retorne o valor dela ( ela possui 2 ou 3 vizinhos),\n' \
         'se ela esta deligada e tem 3 vizinhos ativos ela se torna ligada\n' \
         'caso contrario apenas retorna seu valor. Agora vamos aplicar tudo\n' \
         'e rodar o nosso jogo.'
st.text(exp_6)

st.subheader('O Jogo da vida de Conway!')

with st.form('form2'):
    rows_cols = st.slider('Qual a dimenção da sua grid?', 0, 100)
    probability = st.slider('Qual a probabilidade das celulas estarem ligadas ?', min_value=0.0, max_value=1.0, step=0.05)
    submit_button = st.form_submit_button('VAI RODAAAA!')
    if submit_button and rows_cols != 0:
        run_da_game(rows_cols, probability)
        
