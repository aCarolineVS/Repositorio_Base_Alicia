import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dashboard Clubes - Brasileirão", page_icon="⚽", layout="wide")

CSV_PATH = "Tabela_Clubes.csv"


# ----------------------------------------------------------------------------
# Carregamento e tratamento dos dados
# ----------------------------------------------------------------------------
@st.cache_data
def carregar_dados(fonte) -> pd.DataFrame:
    df = pd.read_csv(fonte)

    # Remove a coluna de índice exportada pelo pandas, se existir
    df = df.loc[:, ~df.columns.astype(str).str.startswith("Unnamed")]
    df = df.rename(columns={"Pos.": "Posicao"})

    # Idade média usa vírgula decimal ("24,8")
    df["Idade_Media"] = (
        df["Idade_Media"].astype(str).str.replace(",", ".", regex=False).astype(float)
    )

    # "GolsF/S" no formato "30:47" -> gols feitos : gols sofridos
    gols = df["GolsF/S"].astype(str).str.split(":", expand=True).astype(int)
    df["Gols_Feitos"] = gols[0]
    df["Gols_Sofridos"] = gols[1]

    # Métricas derivadas
    df["Jogos"] = df["Vitorias"] + df["Empates"] + df["Derrotas"]
    df["Pontos"] = df["Vitorias"] * 3 + df["Empates"]
    df["Aproveitamento"] = df["Pontos"] / (df["Jogos"] * 3) * 100
    df["Valor_Milhoes"] = df["Valor_total"] / 1_000_000
    df["Media_Valor_Milhoes"] = df["Media_Valor"] / 1_000_000

    return df.sort_values(["Ano", "Posicao"]).reset_index(drop=True)


def fmt_milhoes(v: float) -> str:
    return f"R$ {v:,.1f} mi".replace(",", "X").replace(".", ",").replace("X", ".")


# ----------------------------------------------------------------------------
# Barra lateral
# ----------------------------------------------------------------------------
st.sidebar.title("⚽ Filtros")

try:
    df = carregar_dados(CSV_PATH)
except FileNotFoundError:
    st.error(f"Arquivo '{CSV_PATH}' não encontrado. Coloque-o na mesma pasta do app.py.")
    st.stop()

anos = sorted(df["Ano"].unique())
ano_min, ano_max = st.sidebar.select_slider(
    "Período (anos)", options=anos, value=(anos[0], anos[-1])
)

clubes_todos = sorted(df["Clubes"].unique())
clubes_sel = st.sidebar.multiselect("Clubes", clubes_todos, placeholder="Todos os clubes")

pos_min, pos_max = st.sidebar.slider("Posição final", 1, int(df["Posicao"].max()), (1, int(df["Posicao"].max())))

filtrado = df[
    df["Ano"].between(ano_min, ano_max)
    & df["Posicao"].between(pos_min, pos_max)
]
if clubes_sel:
    filtrado = filtrado[filtrado["Clubes"].isin(clubes_sel)]

if filtrado.empty:
    st.warning("Nenhum dado para os filtros selecionados.")
    st.stop()

# ----------------------------------------------------------------------------
# Cabeçalho e KPIs
# ----------------------------------------------------------------------------
st.title("Dashboard dos Clubes — Campeonato Brasileiro")
st.caption(f"Temporadas {ano_min}–{ano_max} • {len(filtrado)} registros • {filtrado['Clubes'].nunique()} clubes")

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Clubes", filtrado["Clubes"].nunique())
c2.metric("Média de vitórias", f"{filtrado['Vitorias'].mean():.1f}")
c3.metric("Média de gols feitos", f"{filtrado['Gols_Feitos'].mean():.1f}")
c4.metric("Idade média", f"{filtrado['Idade_Media'].mean():.1f} anos")
c5.metric("Valor médio do elenco", fmt_milhoes(filtrado["Valor_Milhoes"].mean()))

st.divider()

# ----------------------------------------------------------------------------
# Abas
# ----------------------------------------------------------------------------
aba_geral, aba_clube, aba_elenco, aba_comp, aba_dados = st.tabs(
    ["📊 Visão geral", "🔎 Análise por clube", "💰 Elenco e valor", "⚖️ Comparar clubes", "📋 Dados"]
)

# ---- Visão geral -----------------------------------------------------------
with aba_geral:
    esq, dir_ = st.columns(2)

    ranking = (
        filtrado.groupby("Clubes")
        .agg(Pontos=("Pontos", "sum"), Temporadas=("Ano", "count"))
        .reset_index()
        .sort_values("Pontos", ascending=False)
        .head(15)
    )
    fig = px.bar(
        ranking.sort_values("Pontos"),
        x="Pontos", y="Clubes", orientation="h", color="Pontos",
        color_continuous_scale="Greens", hover_data=["Temporadas"],
        title="Top 15 clubes por pontos acumulados",
    )
    fig.update_layout(coloraxis_showscale=False, yaxis_title=None)
    esq.plotly_chart(fig, use_container_width=True)

    campeoes = filtrado[filtrado["Posicao"] == 1][["Ano", "Clubes", "Pontos", "Vitorias", "Gols_Feitos"]]
    dir_.subheader("🏆 Campeões por temporada")
    dir_.dataframe(campeoes.rename(columns={"Clubes": "Campeão", "Gols_Feitos": "Gols"}),
                   hide_index=True, use_container_width=True)

    esq2, dir2 = st.columns(2)
    fig = px.scatter(
        filtrado, x="Valor_Milhoes", y="Pontos", color="Posicao", hover_name="Clubes",
        hover_data=["Ano"], color_continuous_scale="RdYlGn_r",
        title="Valor do elenco × Pontos",
        labels={"Valor_Milhoes": "Valor do elenco (R$ mi)"},
    )
    esq2.plotly_chart(fig, use_container_width=True)

    fig = px.scatter(
        filtrado, x="Gols_Feitos", y="Gols_Sofridos", size="Pontos", color="Posicao",
        hover_name="Clubes", hover_data=["Ano"], color_continuous_scale="RdYlGn_r",
        title="Ataque × Defesa (gols feitos × sofridos)",
    )
    dir2.plotly_chart(fig, use_container_width=True)

# ---- Análise por clube -----------------------------------------------------
with aba_clube:
    clube = st.selectbox("Escolha um clube", clubes_todos,
                         index=clubes_todos.index(clubes_sel[0]) if clubes_sel else 0)
    dc = df[(df["Clubes"] == clube) & df["Ano"].between(ano_min, ano_max)]

    if dc.empty:
        st.info("Este clube não disputou o campeonato no período selecionado.")
    else:
        k1, k2, k3, k4 = st.columns(4)
        k1.metric("Temporadas", len(dc))
        k2.metric("Melhor posição", int(dc["Posicao"].min()))
        k3.metric("Pontos (média)", f"{dc['Pontos'].mean():.1f}")
        k4.metric("Aproveitamento médio", f"{dc['Aproveitamento'].mean():.1f}%")

        a, b = st.columns(2)
        fig = px.line(dc, x="Ano", y="Posicao", markers=True, title=f"Posição final — {clube}")
        fig.update_yaxes(autorange="reversed", dtick=1)
        fig.update_xaxes(dtick=1)
        a.plotly_chart(fig, use_container_width=True)

        res = dc.melt(id_vars="Ano", value_vars=["Vitorias", "Empates", "Derrotas"],
                      var_name="Resultado", value_name="Quantidade")
        fig = px.bar(res, x="Ano", y="Quantidade", color="Resultado", title="Vitórias, empates e derrotas",
                     color_discrete_map={"Vitorias": "#2e7d32", "Empates": "#f9a825", "Derrotas": "#c62828"})
        fig.update_xaxes(dtick=1)
        b.plotly_chart(fig, use_container_width=True)

        gols = dc.melt(id_vars="Ano", value_vars=["Gols_Feitos", "Gols_Sofridos"],
                       var_name="Tipo", value_name="Gols")
        fig = px.line(gols, x="Ano", y="Gols", color="Tipo", markers=True, title="Gols feitos × sofridos")
        fig.update_xaxes(dtick=1)
        st.plotly_chart(fig, use_container_width=True)

# ---- Elenco e valor --------------------------------------------------------
with aba_elenco:
    a, b = st.columns(2)

    evol = filtrado.groupby("Ano", as_index=False).agg(
        Valor_Medio=("Valor_Milhoes", "mean"), Idade=("Idade_Media", "mean"),
        Estrangeiros=("Estrangeiros", "mean"),
    )
    fig = px.line(evol, x="Ano", y="Valor_Medio", markers=True,
                  title="Valor médio dos elencos por ano (R$ mi)")
    fig.update_xaxes(dtick=1)
    a.plotly_chart(fig, use_container_width=True)

    fig = px.line(evol, x="Ano", y="Estrangeiros", markers=True,
                  title="Média de jogadores estrangeiros por clube")
    fig.update_xaxes(dtick=1)
    b.plotly_chart(fig, use_container_width=True)

    a, b = st.columns(2)
    fig = px.scatter(filtrado, x="Idade_Media", y="Pontos", color="Posicao", hover_name="Clubes",
                     hover_data=["Ano"], color_continuous_scale="RdYlGn_r",
                     title="Idade média × Pontos")
    a.plotly_chart(fig, use_container_width=True)

    mais_caros = filtrado.nlargest(10, "Valor_total")[["Ano", "Clubes", "Valor_Milhoes", "Posicao"]]
    fig = px.bar(mais_caros.assign(Rotulo=mais_caros["Clubes"] + " (" + mais_caros["Ano"].astype(str) + ")")
                 .sort_values("Valor_Milhoes"),
                 x="Valor_Milhoes", y="Rotulo", orientation="h", color="Posicao",
                 color_continuous_scale="RdYlGn_r", title="10 elencos mais valiosos (R$ mi)")
    fig.update_layout(yaxis_title=None)
    b.plotly_chart(fig, use_container_width=True)

    st.caption("Correlação entre valor do elenco e pontos no recorte atual: "
               f"**{filtrado['Valor_total'].corr(filtrado['Pontos']):.2f}**")

# ---- Comparar clubes -------------------------------------------------------
with aba_comp:
    padrao = clubes_sel[:4] if clubes_sel else ["Flamengo", "Corinthians", "Palmeiras", "Sao Paulo"]
    padrao = [c for c in padrao if c in clubes_todos]
    comp = st.multiselect("Clubes para comparar", clubes_todos, default=padrao)
    metrica = st.selectbox(
        "Métrica",
        ["Pontos", "Posicao", "Vitorias", "Gols_Feitos", "Gols_Sofridos", "Saldo",
         "Aproveitamento", "Valor_Milhoes", "Idade_Media", "Estrangeiros"],
    )
    dcomp = df[df["Clubes"].isin(comp) & df["Ano"].between(ano_min, ano_max)]
    if dcomp.empty:
        st.info("Selecione ao menos um clube com dados no período.")
    else:
        fig = px.line(dcomp, x="Ano", y=metrica, color="Clubes", markers=True,
                      title=f"{metrica} por temporada")
        fig.update_xaxes(dtick=1)
        if metrica == "Posicao":
            fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig, use_container_width=True)

        resumo = dcomp.groupby("Clubes").agg(
            Temporadas=("Ano", "count"), Pontos=("Pontos", "sum"),
            Vitorias=("Vitorias", "sum"), Gols_Feitos=("Gols_Feitos", "sum"),
            Gols_Sofridos=("Gols_Sofridos", "sum"),
            Melhor_Posicao=("Posicao", "min"), Valor_Medio_mi=("Valor_Milhoes", "mean"),
        ).round(1).reset_index()
        st.dataframe(resumo, hide_index=True, use_container_width=True)

# ---- Dados -----------------------------------------------------------------
with aba_dados:
    busca = st.text_input("Buscar clube na tabela")
    tabela = filtrado[[
        "Ano", "Posicao", "Clubes", "Pontos", "Vitorias", "Empates", "Derrotas",
        "Gols_Feitos", "Gols_Sofridos", "Saldo", "Aproveitamento",
        "Qtd_Jogadores", "Idade_Media", "Estrangeiros", "Valor_total", "Media_Valor",
    ]]
    if busca:
        tabela = tabela[tabela["Clubes"].str.contains(busca, case=False, na=False)]

    st.dataframe(
        tabela, hide_index=True, use_container_width=True,
        column_config={
            "Aproveitamento": st.column_config.NumberColumn(format="%.1f%%"),
            "Valor_total": st.column_config.NumberColumn("Valor total (R$)", format="%d"),
            "Media_Valor": st.column_config.NumberColumn("Valor médio (R$)", format="%d"),
        },
    )
    st.download_button(
        "⬇️ Baixar dados filtrados (CSV)",
        tabela.to_csv(index=False).encode("utf-8"),
        file_name="clubes_filtrado.csv", mime="text/csv",
    )
