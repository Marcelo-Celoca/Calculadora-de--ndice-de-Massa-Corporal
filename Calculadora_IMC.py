import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Calculadora de Índice de Massa Corporal')
        self.geometry('400x450')

        self.label_titulo = ctk.CTkLabel(self, text='Cálculo de IMC', font=('Roboto', 24, 'bold'))
        self.label_titulo.pack(pady=20)

        self.entry_peso = ctk.CTkEntry(self, placeholder_text='Peso ')
        self.entry_peso.pack(pady=10)

        self.entry_altura = ctk.CTkEntry(self, placeholder_text='Altura ')
        self.entry_altura.pack(pady=10)

        self.btn_calcular = ctk.CTkButton(self, text='Calcular', command=self.calcular_imc)
        self.btn_calcular.pack(pady=20)

        self.label_resultado = ctk.CTkLabel(self, text='', font=('Roboto', 18))
        self.label_resultado.pack(pady=10)

        self.label_classificacao = ctk.CTkLabel(self, text='', font=('Roboto', 18))
        self.label_classificacao.pack(pady=5)

    def calcular_imc(self):
        try:
            peso = float(self.entry_peso.get())
            altura = float(self.entry_altura.get())
            imc = peso / (altura ** 2)

            self.label_resultado.configure(text=f'Seu IMC: {imc:.2f}')

            if imc < 18.5:
                classif = 'Abaixo do peso'
                cor = '#ffcc00'  # Amarelo
            elif 18.5 <= imc < 25:
                classif = 'Peso normal'
                cor = '#00ff00'  # Verde
            elif 25 <= imc < 30:
                classif = 'Sobrepeso'
                cor = '#ff9900'  # Laranja
            else:
                classif = 'Obesidade'
                cor = '#ff0000'  # Vermelho

            self.label_classificacao.configure(text=classif, text_color=cor)

        except ValueError:
            self.label_resultado.configure(text='Erro! Use números e ponto.')


if __name__ == '__main__':
    app = App()
    app.mainloop()
