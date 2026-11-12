
import streamlit as st
from core.knapsack import knapsack

def main():
    # ========================================
    # CONFIGURAÇÕES DA PÁGINA
    # ========================================

    st.set_page_config(
        page_title="ConectaBairro | Priorizador",
        page_icon="🏘️",
        layout="wide"
    )


    # ========================================
    # INICIALIZAÇÃO DOS DADOS
    # ========================================

    if "necessidades" not in st.session_state:
        st.session_state.necessidades = []

    if "resultado" not in st.session_state:
        st.session_state.resultado = None


    # ========================================
    # FUNÇÕES AUXILIARES
    # ========================================

    def formatar_moeda(valor):
        return (
            f"R$ {valor:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )


    def invalidar_resultado():
        st.session_state.resultado = None


    # ========================================
    # CADASTRO DE NECESSIDADES
    # ========================================

    @st.dialog("Adicionar necessidade")
    def cadastrar_necessidade():

        with st.form("form_necessidade"):

            nome = st.text_input(
                "Nome da necessidade",
                placeholder="Ex: Reforço escolar"
            )

            custo = st.number_input(
                "Custo estimado (R$)",
                min_value=1,
                value=100,
                step=50
            )

            beneficio = st.number_input(
                "Benefício para o bairro",
                min_value=1,
                max_value=10,
                value=5,
                help="Avalie o impacto da necessidade de 1 a 10."
            )

            enviar = st.form_submit_button(
                "Cadastrar necessidade",
                use_container_width=True
            )

            if enviar:

                if not nome.strip():

                    st.error("Informe o nome da necessidade.")

                else:

                    nova_necessidade = {
                        "nome": nome.strip(),
                        "custo": int(custo),
                        "beneficio": int(beneficio)
                    }

                    st.session_state.necessidades.append(
                        nova_necessidade
                    )

                    invalidar_resultado()

                    st.success("Necessidade cadastrada!")
                    st.rerun()


    # ========================================
    # CABEÇALHO
    # ========================================

    st.title("🏘️ ConectaBairro")

    st.subheader("Priorizador de necessidades comunitárias")

    st.write(
        "Cadastre as necessidades do seu bairro e descubra "
        "quais delas podem gerar o maior benefício considerando "
        "os recursos disponíveis."
    )

    st.divider()


    # ========================================
    # ORÇAMENTO
    # ========================================

    st.subheader("💰 Orçamento disponível")

    orcamento = st.number_input(
        "Quanto você tem disponível para investir? (R$)",
        min_value=0,
        value=1000,
        step=50
    )

    # Se o orçamento mudar, o resultado anterior deixa de ser válido.
    if (
        st.session_state.resultado is not None
        and st.session_state.resultado["orcamento"] != int(orcamento)
    ):
        invalidar_resultado()

    st.divider()


    # ========================================
    # LISTAGEM DE NECESSIDADES
    # ========================================

    col_titulo, col_botao = st.columns([3, 1])

    with col_titulo:
        st.subheader("📋 Necessidades cadastradas")

    with col_botao:

        if st.button(
            "➕ Adicionar necessidade",
            use_container_width=True
        ):
            cadastrar_necessidade()


    necessidades = st.session_state.necessidades

    if not necessidades:

        st.info(
            "Nenhuma necessidade cadastrada. "
            "Clique em 'Adicionar necessidade' para começar."
        )

    else:

        # Container com rolagem interna
        with st.container(height=350, border=True):

            for i, necessidade in enumerate(necessidades):

                col_info, col_excluir = st.columns([5, 1])

                with col_info:

                    with st.container(border=True):

                        st.markdown(
                            f"**{necessidade['nome']}**"
                        )

                        c1, c2 = st.columns(2)

                        c1.write(
                            f"💵 Custo: "
                            f"{formatar_moeda(necessidade['custo'])}"
                        )

                        c2.write(
                            f"⭐ Benefício: "
                            f"{necessidade['beneficio']}/10"
                        )

                with col_excluir:

                    st.write("")

                    if st.button(
                        "🗑️",
                        key=f"excluir_{i}",
                        help="Excluir necessidade"
                    ):

                        st.session_state.necessidades.pop(i)

                        invalidar_resultado()

                        st.rerun()


    st.divider()


    # ========================================
    # PRIORIZAÇÃO COM PROGRAMAÇÃO DINÂMICA
    # ========================================

    st.subheader("🧠 Priorização inteligente")

    if st.button(
        "🚀 Priorizar necessidades",
        type="primary",
        use_container_width=True,
        disabled=len(necessidades) == 0
    ):

        custos = [
            necessidade["custo"]
            for necessidade in necessidades
        ]

        beneficios = [
            necessidade["beneficio"]
            for necessidade in necessidades
        ]

        valor_maximo, itens_escolhidos = knapsack(
            custos,
            beneficios,
            int(orcamento)
        )

        custo_total = sum(
            custos[i] for i in itens_escolhidos
        )

        st.session_state.resultado = {
            "orcamento": int(orcamento),
            "itens": itens_escolhidos,
            "beneficio": valor_maximo,
            "custo": custo_total
        }


    # ========================================
    # EXIBIÇÃO DO RESULTADO
    # ========================================

    resultado = st.session_state.resultado

    if resultado is not None:

        st.success("Priorização concluída!")

        # Indicadores do resultado
        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Orçamento disponível",
            formatar_moeda(resultado["orcamento"])
        )

        col2.metric(
            "Valor utilizado",
            formatar_moeda(resultado["custo"])
        )

        col3.metric(
            "Benefício máximo",
            f"{resultado['beneficio']} pontos"
        )

        st.subheader("✅ Necessidades selecionadas")

        if resultado["itens"]:

            for indice in resultado["itens"]:

                necessidade = necessidades[indice]

                with st.container(border=True):

                    st.markdown(
                        f"**{necessidade['nome']}**"
                    )

                    col1, col2 = st.columns(2)

                    col1.write(
                        f"💵 Custo: "
                        f"{formatar_moeda(necessidade['custo'])}"
                    )

                    col2.write(
                        f"⭐ Benefício: "
                        f"{necessidade['beneficio']}/10"
                    )

        else:

            st.warning(
                "Nenhuma necessidade pode ser atendida "
                "com o orçamento disponível."
            )

        # Recursos restantes
        economia = (
            resultado["orcamento"] - resultado["custo"]
        )

        st.info(
            f"💰 Recursos restantes: {formatar_moeda(economia)}"
        )


    # ========================================
    # RODAPÉ
    # ========================================

    st.divider()

    st.caption(
        "ConectaBairro | Priorização de necessidades comunitárias"
    )


# ========================================
# EXECUÇÃO
# ========================================

if __name__ == "__main__":
    main()
