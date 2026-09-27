import pandas as pd
import streamlit as st

# 1. Configuração da página web
st.set_page_config(page_title="Dashboard de Fundos", layout="wide")

# Título principal do Dashboard na página web
st.title("📊 Painel de Controle - Fundos de Investimento")
st.markdown("---")

# 2. Carregar os dados (mesma lógica do Pandas que vocês já conhecem)
df = pd.read_csv('Dados.csv')
df.columns = df.columns.str.strip()

# Criamos os fundos únicos para os filtros cadastrais
df_fundos = df.drop_duplicates(subset=['nomeFundo'])

# 3. Criando uma barra lateral de filtros (Sidebar)
st.sidebar.header("🔍 Filtros do Painel")
fundo_selecionado = st.sidebar.selectbox(
    "Selecione o Fundo para análise detalhada:",
    options=df_fundos['nomeFundo'].tolist()
)

# Filtrando a linha do fundo escolhido pelo usuário na barra lateral
dados_fundo = df_fundos[df_fundos['nomeFundo'] == fundo_selecionado].iloc[0]

# 4. EXIBINDO OS DADOS NO DASHBOARD VISUAL
# Vamos dividir a tela em 3 colunas visuais usando o Streamlit
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Fundo Selecionado", value=dados_fundo['nomeFundo'])
    st.write(f"**Razão Social:** {dados_fundo['DENOM_SOCIAL']}")
    st.write(f"**CNPJ Fundo:** {dados_fundo['CNPJ_FUNDO']}")

with col2:
    # Formatando o PL de forma bonita
    pl_bruto = float(dados_fundo['pl'])
    pl_formatado = f"R$ {pl_bruto:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    
    st.metric(label="Patrimônio Líquido (PL)", value=pl_formatado)
    st.write(f"**Tipo de Carteira:** {dados_fundo['tipoCarteira']}")
    st.write(f"**Condomínio:** {dados_fundo['CONDOM']}")

with col3:
    st.metric(label="Público-Alvo", value=dados_fundo['PUBLICO_ALVO'])
    st.write(f"**Gestor:** {dados_fundo['gestor']}")
    st.write(f"**Custodiante:** {dados_fundo['CUSTODIANTE']}")

st.markdown("---")

# 5. BÔNUS: Exibir a tabela completa de dados brutos na página se o usuário quiser
st.subheader("📋 Visualização da Base de Dados Filtrada")
st.dataframe(df_fundos[['CNPJ_FUNDO', 'nomeFundo', 'tipoCarteira', 'pl', 'gestor']], use_container_width=True)
