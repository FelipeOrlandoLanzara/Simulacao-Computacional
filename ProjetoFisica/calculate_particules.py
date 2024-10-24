from math import *
from scipy import integrate
import numpy as np
import matplotlib.pyplot as grafico
from scipy.interpolate import make_interp_spline

hm = 6.626e-34  # h com massa
h = 4.136e-15  # h sem massa
m = 9.11e-31  # massa do eletron
mp = 1.6726219e-27  # massa do proton
j = 6.242e+18  # 1ev -> j
c = 3e8  # velocidade da luz


# --------------------------------------------------------------------------------
# CAIXA 1D - DETERMINACAO DA FUNCAO DE ONDA QUANTICA E OUTROS PARAMETROS
# CONFINADO EM ELETRON
# EQUAÇÃO DA FUNÇÃO

def funcao(x, a, k):
    func = pow(a * sin(k * x), 2)
    return func


# --------------------------------------------------------------------------------
# CAIXA 1D - DETERMINACAO DA FUNCAO DE ONDA QUANTICA E OUTROS PARAMETROS
# CONFINADO EM ELETRON
# TODAS AS EQUACOES JUNTAS


def etotal1(largura, ni, nf, inf, sup):
    ai = sqrt(2 / largura)
    ki = (ni * pi) / largura
    af = sqrt(2 / largura)
    kf = (nf * pi) / largura
    eji = (ni * ni * hm * hm) / (8 * m * largura * largura)
    evi = eji * j
    ejf = (nf * nf * hm * hm) / (8 * m * largura * largura)
    evf = ejf * j
    efoton = abs(evf - evi)
    comprimento_foton = abs((h * c) / efoton)
    frequencia = abs(efoton / h)
    vi = sqrt((2 * eji) / m)
    vf = sqrt((2 * ejf) / m)
    comprimento_particulai = hm / (m * vi)
    comprimento_particulaf = hm / (m * vf)
    fi = lambda x: (funcao(x, ai, ki))
    integrali, erroi = integrate.quad(fi, inf, sup)
    integrali = integrali * 100
    ff = lambda x: (funcao(x, af, kf))
    integralf, errof = integrate.quad(ff, inf, sup)
    integralf = integralf * 100
    return ai, ki, af, kf, eji, evi, ejf, evf, efoton, comprimento_foton, frequencia, vi, vf, comprimento_particulai, comprimento_particulaf, integrali, integralf


# --------------------------------------------------------------------------------
# CAIXA 1D - DETERMINACAO DA FUNCAO DE ONDA QUANTICA E OUTROS PARAMETROS
# CONFINADO EM PROTON
# TODAS AS EQUACOES JUNTAS


def ptotal1(largura, ni, nf, inf, sup):
    ai = sqrt(2 / largura)
    ki = (ni * pi) / largura
    af = sqrt(2 / largura)
    kf = (nf * pi) / largura
    eji = (ni * ni * hm * hm) / (8 * mp * largura * largura)
    evi = eji * j
    ejf = (nf * nf * hm * hm) / (8 * mp * largura * largura)
    evf = ejf * j
    efoton = abs(evf - evi)
    comprimento_foton = abs((h * c) / efoton)
    frequencia = abs(efoton / h)
    vi = sqrt((2 * eji) / mp)
    vf = sqrt((2 * ejf) / mp)
    comprimento_particulai = hm / (mp * vi)
    comprimento_particulaf = hm / (mp * vf)
    fi = lambda x: (funcao(x, ai, ki))
    integrali, erroi = integrate.quad(fi, inf, sup)
    integrali = integrali * 100
    ff = lambda x: (funcao(x, af, kf))
    integralf, errof = integrate.quad(ff, inf, sup)
    integralf = integralf * 100
    return ai, ki, af, kf, eji, evi, ejf, evf, efoton, comprimento_foton, frequencia, vi, vf, comprimento_particulai, comprimento_particulaf, integrali, integralf


# --------------------------------------------------------------------------------
# CAIXA 1D - CALCULO DOS PARAMETROS DA CAIXA E PARTICULA, DADA A FUNCAO DE ONDA
# CONFINADO EM ELETRON
# TODAS AS EQUACOES JUNTAS


def etotal2(a, k, x):
    largura = 2 / (a * a)
    n = round((k * largura) / pi)
    xp = x * largura
    p = (2 / largura) * pow((sin((n * pi * xp) / largura)), 2)
    return largura, n, p

# --------------------------------------------------------------------------------
# CAIXA 1D - CALCULO DOS PARAMETROS DA CAIXA E PARTICULA, DADA A FUNCAO DE ONDA
# CONFINADO EM PROTON
# TODAS AS EQUACOES JUNTAS


def ptotal2(a, k, x):
    largura = 2 / (a * a)
    n = round((k * largura) / pi)
    xp = x * largura
    p = (2 / largura) * pow((sin((n * pi * xp) / largura)), 2)
    return largura, n, p