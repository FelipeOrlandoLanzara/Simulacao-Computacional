from tkinter import *
from tkinter.ttk import *
import graphics as gr
import calculate_particules as cp
from PIL import Image, ImageTk


def show():
    return clicked.get()


def checkParticle(root, window):
    particle = show()
    if particle == "Escolha a partícula":
        # se entrar nessa condição, não abre a janela
        label = Label(root, text="Escolha uma partícula")
        label.pack()
    elif particle == "Elétron":
        window(root)
    elif particle == "Próton":
        window(root)


# Principal
class RootWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Main menu")
        self.geometry("1000x600")
        options = [
            "Escolha a partícula",
            "Elétron",
            "Próton"
        ]
        global clicked
        # initial menu text
        clicked = StringVar()
        clicked.set("Escolha a partícula")

        # Create Dropdown menu
        drop = OptionMenu(self, clicked, *options)
        drop.pack()
        drop.place(x=500, y=400, anchor="center")
        # Create button, it will change label text
        self.plot_btn()

        # Create Label
        self.plot_label()

    def plot_btn(self):
        simu_btn = Button(self, text="Simulação")
        simu_btn.bind("<Button>", lambda e: Simulation(self))
        simu_btn.pack()
        simu_btn.place(x=500, y=500, anchor="center")
        poco_btn = Button(self, text="Poço")
        poco_btn.bind("<Button>", lambda e: checkParticle(self, Poco))
        poco_btn.pack()
        poco_btn.place(x=300, y=500, anchor="center")
        outrosimbolo_btn = Button(self, text="ψ")
        outrosimbolo_btn.bind("<Button>", lambda e: checkParticle(self, Psi_simbolo))
        outrosimbolo_btn.pack()
        outrosimbolo_btn.place(x=700, y=500, anchor="center")

    def plot_label(self):
        Label(self, text=" ").pack()
        func_onda = Label(self, text="Caixa 1D - Determinação da função de onda quântica \ne outros parâmetros")
        func_onda.pack()
        func_onda.place(x=300, y=100, anchor="center")
        trid = Label(self, text="Caixa 1D - Cálculo dos parâmetros da caixa e partícula, \ndada a função de onda")
        trid.pack()
        trid.place(x=800, y=100, anchor="center")

        explic = Label(self,
                       text="O 'Poço de potencial infinito' ou 'Partícula na caixa' é um conceito da física quântica "
                            "que \n"
                            "descreve o comportamento de uma partícula confinada em um espaço unidimensional. A \n"
                            "partícula fica presa dentro de uma caixa com paredes impenetráveis, e seu movimento e \n"
                            "energia são quantizados, resultando em níveis de energia discretos.")
        explic.pack()
        explic.place(x=500, y=200, anchor="center")


class Simulation(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.frame_index = None
        self.canvas_image = None
        self.photo = None
        self.image = None
        self.title("Simulação")
        self.geometry("1000x600")
        self.canvas = None
        self.gif()
        self.mainloop()

    def gif(self):
        self.canvas = Canvas(self, width=900, height=600)
        self.canvas.pack()
        self.image = Image.open('Simulacao.gif')
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas_image = self.canvas.create_image(0, 0, anchor=NW, image=self.photo)
        self.frame_index = 0
        self.animate_gif()

    def animate_gif(self):
        # vai atualizando a imagem que está sendo exibida com o proximo quadro do GIF
        self.image.seek(self.frame_index)
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfigure(self.canvas_image, image=self.photo)
        self.frame_index += 1
        # forma uma animação ao dar um delay para definir o próximo quadro
        if self.frame_index >= self.image.n_frames:
            self.frame_index = 0
        delay = self.image.info['duration']
        self.canvas.after(delay, self.animate_gif)


class Poco(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.maior_prob = None
        self.menor_prob = None
        self.nf = None
        self.ni = None
        self.l_caixa = None
        self.resultado = None
        self.title("Determinação da função de onda quântica e outros parâmetros confinado em " + show())
        self.geometry("1000x600")
        self.plot_labels()
        self.plot_entry()
        self.plot_btn()

    def plot_labels(self):
        # Create Label
        larg = Label(self, text="Largura da caixa(L):")
        larg.pack()
        larg.place(x=150, y=100, anchor="center")
        ni = Label(self, text="ni da particula:")
        ni.pack()
        ni.place(x=150, y=175, anchor="center")
        nf = Label(self, text="nf da particula:")
        nf.pack()
        nf.place(x=150, y=250, anchor="center")
        prob = Label(self, text="Probabilidade(a<=x<=b):")
        prob.pack()
        prob.place(x=150, y=325, anchor="center")
        menor = Label(self, text="Menor:")
        menor.pack()
        menor.place(x=150, y=400, anchor="center")
        maior = Label(self, text="Maior:")
        maior.pack()
        maior.place(x=150, y=475, anchor="center")
        meters = Label(self, text="Metros")
        meters.pack()
        meters.place(x=310, y=100, anchor="center")
        proba = Label(self, text="Metros")
        proba.pack()
        proba.place(x=310, y=475, anchor="center")
        probabili = Label(self, text="Metros")
        probabili.pack()
        probabili.place(x=310, y=400, anchor="center")


        # Labels for answers
        func_onda_i = Label(self, text="Função de onda inicial:")
        func_onda_i.pack()
        func_onda_i.place(x=500, y=75, anchor="center")
        func_onda_f = Label(self, text="Função de onda final:")
        func_onda_f.pack()
        func_onda_f.place(x=500, y=125, anchor="center")
        energia_i = Label(self, text="Energia inicial:")
        energia_i.pack()
        energia_i.place(x=500, y=175, anchor="center")
        energia_f = Label(self, text="Energia final:")
        energia_f.pack()
        energia_f.place(x=500, y=225, anchor="center")
        energia_foton = Label(self, text="Energia do fóton:")
        energia_foton.pack()
        energia_foton.place(x=500, y=275, anchor="center")
        comprimento = Label(self, text="Comprimento de onda do foton:")
        comprimento.pack()
        comprimento.place(x=500, y=325, anchor="center")
        frquencia = Label(self, text="Frequência do fóton:")
        frquencia.pack()
        frquencia.place(x=500, y=375, anchor="center")
        veloc_inicial = Label(self, text="Velocidade inicial da partiucla:")
        veloc_inicial.pack()
        veloc_inicial.place(x=800, y=125, anchor="center")
        veloc_final = Label(self, text="Velocidade final da partiucla:")
        veloc_final.pack()
        veloc_final.place(x=800, y=175, anchor="center")
        comprimento_ni = Label(self, text="Comprimento de onda no nivel inicial:")
        comprimento_ni.pack()
        comprimento_ni.place(x=800, y=225, anchor="center")
        comprimento_nf = Label(self, text="Comprimento de onda no nivel final:")
        comprimento_nf.pack()
        comprimento_nf.place(x=800, y=275, anchor="center")
        probabilidade_i = Label(self, text="Probabilidade(a<=x<=b) no nivel inicial:")
        probabilidade_i.pack()
        probabilidade_i.place(x=800, y=325, anchor="center")
        probabilidade_f = Label(self, text="Probabilidade(a<=x<=b) no nivel final:")
        probabilidade_f.pack()
        probabilidade_f.place(x=800, y=375, anchor="center")

    def plot_output_labels(self):
        if self.resultado is not None:
            func_onda_i_out = Label(self,
                                    text="ψi(x)=" + str(f'{self.resultado[0]:.3e}') + "*sin(" + str(f'{self.resultado[1]:.3e}') + "*x)",
                                    font=("Arial", 10))
            func_onda_i_out.pack()
            func_onda_i_out.place(x=500, y=100, anchor="center")
            func_onda_f_out = Label(self, text="ψf(x)=" + str(f'{self.resultado[2]:.3e}') + "*sin("+str(f'{self.resultado[3]:.3e}')+"*x)", font=("Arial", 10))
            func_onda_f_out.pack()
            func_onda_f_out.place(x=500, y=150, anchor="center")
            energia_i_out = Label(self, text="Ei=" + str(f'{self.resultado[4]:.3e}') + "J  =" + str(f'{self.resultado[5]:.3e}') + "eV",
                                  font=("Arial", 10))
            energia_i_out.pack()
            energia_i_out.place(x=500, y=200, anchor="center")
            energia_f_out = Label(self, text="Ef=" + str(f'{self.resultado[6]:.3e}') + "J  =" + str(f'{self.resultado[7]:.3e}') + "eV",
                                  font=("Arial", 10))
            energia_f_out.pack()
            energia_f_out.place(x=500, y=250, anchor="center")
            energia_foton_out = Label(self, text="Eγ=" + str(f'{self.resultado[8]:.3e}') + "eV", font=("Arial", 10))
            energia_foton_out.pack()
            energia_foton_out.place(x=500, y=300, anchor="center")
            comprimento_out = Label(self, text="λ=" + str(f'{self.resultado[9]:.3e}') + "m", font=("Arial", 10))
            comprimento_out.pack()
            comprimento_out.place(x=500, y=350, anchor="center")
            frquencia_out = Label(self, text="f=" + str(f'{self.resultado[10]:.3e}') + "Hz", font=("Arial", 10))
            frquencia_out.pack()
            frquencia_out.place(x=500, y=400, anchor="center")
            veloc_inicial_out = Label(self, text="Vi=" + str(f'{self.resultado[11]:.3e}') + "m/s", font=("Arial", 10))
            veloc_inicial_out.pack()
            veloc_inicial_out.place(x=800, y=150, anchor="center")
            veloc_final_out = Label(self, text="Vf=" + str(f'{self.resultado[12]:.3e}') + "m/s", font=("Arial", 10))
            veloc_final_out.pack()
            veloc_final_out.place(x=800, y=200, anchor="center")
            comprimento_ni_out = Label(self, text="λi=" + str(f'{self.resultado[13]:.3}') + "m", font=("Arial", 10))
            comprimento_ni_out.pack()
            comprimento_ni_out.place(x=800, y=250, anchor="center")
            comprimento_nf_out = Label(self, text="λf=" + str(f'{self.resultado[14]:.3e}') + "m", font=("Arial", 10))
            comprimento_nf_out.pack()
            comprimento_nf_out.place(x=800, y=300, anchor="center")
            probabilidade_i_out = Label(self, text="P(a<=x<=b)=" + str(f'{self.resultado[15]:.3e}') + "%", font=("Arial", 10))
            probabilidade_i_out.pack()
            probabilidade_i_out.place(x=800, y=350, anchor="center")
            probabilidade_f_out = Label(self, text="P(a<=x<=b)=" + str(f'{self.resultado[16]:.3e}') + "%", font=("Arial", 10))
            probabilidade_f_out.pack()
            probabilidade_f_out.place(x=800, y=400, anchor="center")

    def plot_entry(self):
        self.l_caixa = Entry(self, width=10)
        self.l_caixa.pack()
        self.l_caixa.place(x=250, y=100, anchor="center")
        self.ni = Entry(self, width=10)
        self.ni.pack()
        self.ni.place(x=250, y=175, anchor="center")
        self.nf = Entry(self, width=10)
        self.nf.pack()
        self.nf.place(x=250, y=250, anchor="center")
        self.menor_prob = Entry(self, width=10)
        self.menor_prob.pack()
        self.menor_prob.place(x=250, y=400, anchor="center")
        self.maior_prob = Entry(self, width=10)
        self.maior_prob.pack()
        self.maior_prob.place(x=250, y=475, anchor="center")

    def plot_btn(self):
        calc_btn = Button(self, text="Calcular")
        calc_btn.bind("<Button>", lambda e: self.calcular())
        calc_btn.pack()
        calc_btn.place(x=500, y=550, anchor="center")
        graph_btn = Button(self, text="Gráfico")
        graph_btn.bind("<Button>", lambda e: self.showGrafico())
        graph_btn.pack()
        graph_btn.place(x=650, y=550, anchor="center")

    def calcular(self):
        if clicked.get() == "Próton":
            self.resultado = cp.ptotal1(float(self.l_caixa.get()), float(self.ni.get()), float(self.nf.get()),
                                        float(self.menor_prob.get()), float(self.maior_prob.get()))
        elif clicked.get() == "Elétron":
            self.resultado = cp.etotal1(float(self.l_caixa.get()), float(self.ni.get()), float(self.nf.get()), float(self.menor_prob.get()),
                                        float(self.maior_prob.get()))
        self.plot_output_labels()

    def showGrafico(self):
        gr.grafico_funcao_onda_ni(float(self.l_caixa.get()), float(self.ni.get()))
        gr.grafico_funcao_onda_ni(float(self.l_caixa.get()), float(self.nf.get()))
        gr.grafico_funcao_onda_probabilidade_ni(float(self.l_caixa.get()), float(self.ni.get()))
        gr.grafico_funcao_onda_probabilidade_ni(float(self.l_caixa.get()), float(self.nf.get()))


class Psi_simbolo(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.resultado = None
        self.xp = None
        self.k = None
        self.a = None
        self.title("Determinação da função de onda quântica e outros parâmetros confinado em " + show())
        self.geometry("1000x600")
        self.plot_labels()
        self.plot_entry()
        self.plot_btn()

    def plot_labels(self):
        # Create Label
        al = Label(self, text="A:")
        al.pack()
        al.place(x=240, y=100, anchor="center")
        kl = Label(self, text="K:")
        kl.pack()
        kl.place(x=240, y=175, anchor="center")
        xpl = Label(self, text="xp:")
        xpl.pack()
        xpl.place(x=240, y=250, anchor="center")

        # labels for answers
        largural = Label(self, text="Largura da caixa")
        largural.pack()
        largural.place(x=700, y=100, anchor="center")
        nivel_ql = Label(self, text="Nivel quantico da particula")
        nivel_ql.pack()
        nivel_ql.place(x=700, y=175, anchor="center")
        probabilidade_l = Label(self, text="Probabilidade de encontrar a particula")
        probabilidade_l.pack()
        probabilidade_l.place(x=700, y=250, anchor="center")

    def plot_entry(self):
        self.a = Entry(self, width=10)
        self.a.pack()
        self.a.place(x=300, y=100, anchor="center")
        self.k = Entry(self, width=10)
        self.k.pack()
        self.k.place(x=300, y=175, anchor="center")
        self.xp = Entry(self, width=10)
        self.xp.pack()
        self.xp.place(x=300, y=250, anchor="center")

    def plot_btn(self):
        calc_btn = Button(self, text="Calcular")
        calc_btn.bind("<Button>", lambda e: self.calcular())
        calc_btn.pack()
        calc_btn.place(x=350, y=550, anchor="center")

    def calcular(self):
        if clicked.get() == "Próton":
            self.resultado = cp.ptotal2(float(self.a.get()), float(self.k.get()), float(self.xp.get()))
        elif clicked.get() == "Elétron":
            self.resultado = cp.etotal2(float(self.a.get()), float(self.k.get()), float(self.xp.get()))
        self.plot_output_labels()

    def plot_output_labels(self):
        largura_out = Label(self, text="L=" + str(f'{self.resultado[0]:.3e}') + "m", font=("Arial", 10))
        largura_out.pack()
        largura_out.place(x=700, y=125, anchor="center")
        nivel_q_out = Label(self, text="n=" + str(f'{self.resultado[1]:.3e}'), font=("Arial", 10))
        nivel_q_out.pack()
        nivel_q_out.place(x=700, y=200, anchor="center")
        probabilidade_out = Label(self, text="P(a<=x<=b)=" + str(f'{self.resultado[2]:.3e}') + "%", font=("Arial", 10))
        probabilidade_out.pack()
        probabilidade_out.place(x=700, y=275, anchor="center")


def main():
    # Create object
    root = RootWindow()
    # Execute tkinter
    root.mainloop()


if __name__ == '__main__':
    main()