import pandas as pd
import streamlit as st

# 1. Configuração da página web
st.set_page_config(page_title="Dashboard de Fundos", layout="wide")

st.title("Painel de Controle - Fundos de Investimento")
st.markdown("---")

df = pd.read_csv('Dados.csv')
df.columns = df.columns.str.strip()

df_fundos = df.drop_duplicates(subset=['nomeFundo'])

# 2. Barra lateral 
st.sidebar.header("   ")
fundo_selecionado = st.sidebar.selectbox(
    "Fundo:",
    options=df_fundos['nomeFundo'].tolist()
)

dados_fundo = df_fundos[df_fundos['nomeFundo'] == fundo_selecionado].iloc[0]

# 3. Exibição dos dados
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Fundo Selecionado", value=dados_fundo['nomeFundo'])
    st.write(f"**Razão Social:** {dados_fundo['DENOM_SOCIAL']}")
    st.write(f"**CNPJ Fundo:** {dados_fundo['CNPJ_FUNDO']}")

    

with col2:

# 4. Formatando o PL 
    pl_bruto = float(dados_fundo['pl'])
    pl_formatado = f"R$ {pl_bruto:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    
    st.metric(label="Patrimônio Líquido (PL)", value=pl_formatado)
    st.write(f"**Tipo de Carteira:** {dados_fundo['tipoCarteira']}")
    st.write(f"**Condomínio:** {dados_fundo['CONDOM']}")

with col3:
    st.metric(label="Público-Alvo", value=dados_fundo['PUBLICO_ALVO'])
    st.write(f"**Gestor:** {dados_fundo['gestor']}")
    st.write(f"**Custodiante:** {dados_fundo['CUSTODIANTE']}")

    data_exercicio = pd.to_datetime(
    dados_fundo['DT_FIM_EXERC'],
    errors='coerce'
)

data_exercicio_formatada = data_exercicio.strftime('%d/%m/%Y')

    st.write(f"**Exercício Social:** {dados_fundo['DT_FIM_EXERC']}")

st.markdown("---")


