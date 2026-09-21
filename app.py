import streamlit as st

# Configuração da página do aplicativo
st.set_page_config(
    page_title="Auxiliar CBDF - Fisioterapia",
    page_icon="🩺",
    layout="centered"
)

def main():
    st.title("🩺 Gerador de Diagnóstico Fisioterapêutico (CBDF)")
    st.subheader("Módulo: Sistema Musculoesquelético (CBDF-D03)")
    st.write("Selecione os achados semiológicos da avaliação para gerar o código oficial e a descrição correspondente.")
    
    st.markdown("---")

    # 1. BLOCO A: Status Estrutural
    st.markdown("### 1. Bloco A: Status Estrutural")
    status_estrutural = st.selectbox(
        "Selecione a condição estrutural principal:",
        options=[
            ("00", "D03.00 - Sem lesão de estrutura"),
            ("01", "D03.01 - Com lesão estrutural aguda"),
            ("02", "D03.02 - Com lesão estrutural crônica")
        ],
        format_func=lambda x: x[1]
    )
    bloco_a_codigo = status_estrutural[0]

    st.markdown("---")
    st.markdown("### 2. Bloco B: Parâmetros Funcionais")

    # Dor (Subcódigo 3)
    dor = st.selectbox(
        "Nível de Dor (Repouso ou Esforço):",
        options=[
            ("0", "0 - Nenhuma dor (0-4%)"),
            ("1", "1 - Leve dor (5-24%)"),
            ("2", "2 - Moderada dor (25-49%)"),
            ("3", "3 - Grave dor (50-95%)"),
            ("4", "4 - Dor insuportável (96-100%)"),
            ("8", "8 - Não especificada"),
            ("9", "9 - Não aplicável")
        ],
        format_func=lambda x: x[1]
    )

    # Mobilidade Articular (Subcódigo 4)
    mobilidade = st.selectbox(
        "Mobilidade Articular (Ativa ou Passiva):",
        options=[
            ("0", "0 - Mobilidade articular completa"),
            ("1", "1 - Leve alteração de mobilidade articular"),
            ("2", "2 - Moderada alteração de mobilidade articular"),
            ("3", "3 - Grave alteração de mobilidade articular"),
            ("4", "4 - Completa alteração de mobilidade articular"),
            ("8", "8 - Não especificada"),
            ("9", "9 - Não aplicável")
        ],
        format_func=lambda x: x[1]
    )

    # Funções Musculares (Subcódigo 5)
    muscular = st.selectbox(
        "Funções Musculares (Força, Tônus ou Resistência):",
        options=[
            ("0", "0 - Funções musculares preservadas"),
            ("1", "1 - Leve redução das funções musculares"),
            ("2", "2 - Moderada redução das funções musculares"),
            ("3", "3 - Grave redução das funções musculares"),
            ("4", "4 - Completa redução das funções musculares"),
            ("8", "8 - Não especificada"),
            ("9", "9 - Não aplicável")
        ],
        format_func=lambda x: x[1]
    )

    st.markdown("---")
    st.markdown("### 3. Bloco C: Segmento / Estrutura Acometida")

    # Segmento Corporal (6º Subcódigo)
    segmento = st.selectbox(
        "Segmento ou Parte do Corpo Acometido:",
        options=[
            ("0", "0 - Afetando Cabeça (ATM, crânio, face)"),
            ("1", "1 - Afetando Coluna (Cervical, torácica, lombar, sacro/cóccix)"),
            ("2", "2 - Afetando Coluna e Membros"),
            ("3", "3 - Afetando Um Segmento Específico (Ombro, cotovelo, punho, quadril, joelho, tornozelo, etc.)"),
            ("4", "4 - Afetando Mais de uma Parte do Corpo (MMII, MMSS, ombros, joelhos, etc.)"),
            ("8", "8 - Não especificada"),
            ("9", "9 - Não aplicável")
        ],
        format_func=lambda x: x[1]
    )

    st.markdown("---")

    # Botão para gerar o diagnóstico
    if st.button("Gerar Código e Descrição CBDF", type="primary"):
        codigo_final = f"CBDF D03.{bloco_a_codigo}.{dor[0]}.{mobilidade[0]}.{muscular[0]}.{segmento[0]}"
        
        st.success("Diagnóstico Fisioterapêutico gerado com sucesso!")
        
        # Caixa destacada com o código oficial
        st.markdown(f"### 📋 Código Oficial:")
        st.code(codigo_final, language="")
        
        # Resumo detalhado para o prontuário
        st.markdown("### 📝 Descrição para o Prontuário:")
        descricao_textual = (
            f"**Diagnóstico:** Deficiência Cinético-Funcional Musculoesquelética\n"
            f"- **Status Estrutural:** {status_estrutural[1]}\n"
            f"- **Dor:** {dor[1]}\n"
            f"- **Mobilidade Articular:** {mobilidade[1]}\n"
            f"- **Funções Musculares:** {muscular[1]}\n"
            f"- **Segmento Acometido:** {segmento[1]}"
        )
        st.info(descricao_textual)

if __name__ == "__main__":
    main()
