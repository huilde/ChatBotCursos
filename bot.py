
import pandas as pd


df = pd.read_csv('./udemy_courses.csv')
print(df["subject"])

areasDeInteresse = ['Business Finance',
                    'Musical Instruments', 'Graphic Design', 'Web Development']

faixasDePreco = [20, 50, 80, 100, 200, 0]

precoDolar = 5

list_of_column_names = []

for row in df:
    list_of_column_names.append(row)
print("List of column names : ",
      list_of_column_names)


runApp = True
print("Seja bem-vindo ao nosso chatbot de cursos")

print("Qual a sua área de interesse?")
print("1 - Finanças Corporativas \n 2 - Música \n 3 - Design gráfico \n 4- Desenvolvimento web")
areaDeInteresse = 0
while (areaDeInteresse < 1 or areaDeInteresse > 4):
    areaDeInteresse = int(input("Digite uma das opções: "))
    if (areaDeInteresse < 1 or areaDeInteresse > 5):
        print("Digite um valor entre 1 e 4")


print("quanto você deseja Pagar pelo curso?")
print("1 - até 100 reais \n 2 - até 250 reais \n 3 - até 400 reais \n 4 - até 500 reais \n 5 - 1000 reais \n 6 - quero um curso gratuito")
faixaDePreco = 0
while (faixaDePreco < 1 or faixaDePreco > 6):
    faixaDePreco = int(input("Digite uma das opções: "))
    if (faixaDePreco < 1 or faixaDePreco > 6):
        print("Digite um valor entre 1 e 6")

print("quantas horas você estuda por dia?")
print("1 - até 30 minutos \n 2 - até 1 hora \n 3 - até 3 horas \n 4 - + de 3 horas \n")
tempoDeEstudo = 0
while (tempoDeEstudo < 1 or tempoDeEstudo > 4):
    tempoDeEstudo = int(input("Digite uma das opções: "))
    if (tempoDeEstudo < 1 or tempoDeEstudo > 5):
        print("Digite um valor entre 1 e 4")


df_filtrado = df[(df['subject'] == areasDeInteresse[areaDeInteresse-1])
                 & (df['price'] <= faixasDePreco[faixaDePreco-1])]
print(df_filtrado)
