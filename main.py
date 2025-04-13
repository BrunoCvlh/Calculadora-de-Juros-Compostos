import streamlit as st
import time

import streamlit as st

def main():
    st.title("Calculadora de Juros Compostos")
    capitalInicial = st.number_input("Digite o capital inicial (se houver):", value=0.0)
    aportesMensais = st.number_input("Digite o valor dos aportes mensais:")
    taxaDeJurosAnual = st.slider("Escolha a taxa de juros anual:", 0.04, 0.20, 0.12)
    st.write(f"Taxa média sugerida: 12%")
    tempoEmMeses = st.number_input("Digite o tempo do investimento (em meses):", value=0)

    if tempoEmMeses > 0:
        taxaMensal = taxaDeJurosAnual / 12
        calculoDoInvestimentoFinal = capitalInicial * (1 + taxaMensal) ** tempoEmMeses + aportesMensais * (((1 + taxaMensal) ** tempoEmMeses - 1) / taxaMensal)
        valorDosJuros = calculoDoInvestimentoFinal - capitalInicial - (aportesMensais * tempoEmMeses) 

        tempoMesesX = list(range(1, tempoEmMeses + 1))
        capitalEmMesesY = []
        capitalAtual = capitalInicial

        for _ in range(tempoEmMeses):
            capitalAtual = capitalAtual * (1 + taxaMensal) + aportesMensais
            capitalEmMesesY.append(capitalAtual)

        if capitalInicial > 0 or aportesMensais > 0:
            st.write(f'''Seus rendimentos totais serão de R$ {calculoDoInvestimentoFinal:.2f}
                        \nValor total investido: R$ {capitalInicial + (aportesMensais * tempoEmMeses):.2f}
                        \nJuros acumulados: R$ {valorDosJuros:.2f}''')
            data = {'Meses': tempoMesesX, 'Valor Acumulado': capitalEmMesesY}
            st.line_chart(data, x='Meses', y='Valor Acumulado')
        else:
            st.warning("Por favor, insira valores para visualizar o gráfico.")
    else:
        st.info("Insira um período de tempo para ver a projeção do investimento.")
    st.write("- Criado por Bruno Carvalho")

main()
