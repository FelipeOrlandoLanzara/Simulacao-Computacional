from math import *
from scipy import integrate
import numpy as np
import matplotlib.pyplot as grafico
from scipy.interpolate import make_interp_spline


# CRIAÇÃO DOS GRÁFICOS DA FUNÇÃO DE ONDE PARA OS NÍVEIS INICIAL E FINAL DA PARTÍCULA

def grafico_funcao_onda_ni(largura, n):

    def funcao(x, a, k):
        func = (a * np.sin(k * x))
        return func

    k = (n * pi) / largura
    x = np.linspace(0, largura, 100)  # x vai de 0 a 2 com tamanho 10 de lista
    a = sqrt(2 / largura)
    #y = []
    #for i in range(len(x)):
    #    y.append(a * sin(k * x[i]))
    #X_Y_Spline = make_interp_spline(x, y)
    #X_ = np.linspace(x.min(), x.max(), 500)
    #Y_ = X_Y_Spline(X_)
    y = funcao(x, a, k)


    grafico.plot(x, y)
    grafico.ylabel(f'ψ ({n})')
    grafico.xlabel("x (m)")
    grafico.axis(xmin=0, xmax=largura)
    #grafico.axis(ymin=0)
    grafico.text(0.9,
                 0.9,
                 "n = " + str(n),
                 horizontalalignment='right',
                 verticalalignment='top',
                 transform=grafico.gca().transAxes)
    grafico.title(
        "Gráfico da função de onda para os níveis inicial e final da partícula")
    grafico.show()


# CRIAÇÃO DOS GRÁFICOS DE DISTRIBUIÇÃO DE PROBABILIDADE PARA OS NÍVEIS INICIAL E FINAL DA PARTÍCULA

def grafico_funcao_onda_probabilidade_ni(largura, n):
    def funcao(x, a, k):
        func = ((a * np.sin(k * x))**2)
        return func

    k = (n * pi) / largura
    x = np.linspace(0, largura, 100)  # x vai de 0 a 2 com tamanho 10 de lista
    a = sqrt(2 / largura)
    #y = []
    #for i in range(len(x)):
    #    y.append((a * sin(k * x[i])) * (a * sin(k * x[i])))

    #X_Y_Spline = make_interp_spline(x, y)
    #X_ = np.linspace(x.min(), x.max(), 500)
    #Y_ = X_Y_Spline(X_)

    y = funcao(x, a, k)

    grafico.plot(x, y)
    grafico.text(0.9,
                 0.9,
                 "n = " + str(n),
                 horizontalalignment='right',
                 verticalalignment='top',
                 transform=grafico.gca().transAxes)
    grafico.ylabel(f'|ψ ({n})|²')
    grafico.xlabel("x (m)")
    grafico.axis(xmin=0, xmax=largura)
    grafico.title(
        "Gráfico da função de distruibuição de probabilidade para os níveis inicial e final da partícula"
    )
    grafico.show()