import streamlit as st
import pandas as pd
import time
from database.index import run
from database.hash_function import find_word_in_buckets, hash_word
from database.read_file import read_file
from database.pages import mount_pages
from database.buckets import Bucket

# Define o estado para persistir os valores entre as execuções
if "metrics" not in st.session_state:
    st.session_state.metrics = None
if "buckets" not in st.session_state:
    st.session_state.buckets = None
if "pages" not in st.session_state:
    st.session_state.pages = None

st.title("Índice Hash Estático")
st.subheader("Projeto Banco de Dados")

# Parâmetros de entrada
with st.sidebar:
    st.header("Parâmetros")
    lines_per_page = st.number_input("Linhas por página", min_value=1, value=100)
    bucket_size = st.number_input("Tamanho do bucket", min_value=1, value=300)

    # Botão para iniciar a construção do índice
    if st.button("Construir Índice"):
        st.info("Construindo índice...")

        start_time_run = time.time()
        st.session_state.metrics = run(
            lines_per_page=lines_per_page, bucket_size=bucket_size
        )
        end_time_run = time.time()
        st.session_state.run_time = end_time_run - start_time_run

        words = read_file("words.txt")
        st.session_state.pages = mount_pages(lines_per_page, words)

        num_words = len(words)
        st.session_state.buckets = Bucket.create_buckets(num_words, bucket_size)

        for page_index, page_words in enumerate(st.session_state.pages):
            for word in page_words:
                bucket_index = hash_word(str(word), len(st.session_state.buckets))
                st.session_state.buckets[bucket_index].add_word(str(word), page_index)

        st.success("Índice construído")
        st.info(f"Tempo construção do índice: {st.session_state.run_time:.4f} segundos")

# Exibe as métricas após a construção do índice
if st.session_state.metrics:
    st.header("Métricas")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Páginas", st.session_state.metrics["Total pages"])
        st.metric("Total de Buckets", st.session_state.metrics["Total Buckets"])
    with col2:
        st.metric("Total de Palavras", st.session_state.metrics["Total words"])
        st.metric(
            "Colisões (%)",
            f'{st.session_state.metrics["Percentage of collisions"]:.2f}%',
        )
    with col3:
        st.metric("Total de Colisões", st.session_state.metrics["Total collisions"])
        st.metric(
            "Overflows (%)",
            f'{st.session_state.metrics["Percentage of bucket overflows"]:.2f}%',
        )

    st.markdown("---")

    # Exibe a primeira e a última página usando colunas
    st.header("Páginas de dados")
    if st.session_state.pages:
        col1, col2 = st.columns(2)

        # Primeira Página
        with col1:
            st.subheader("Página 1")
            first_page_df = pd.DataFrame(
                st.session_state.pages[0], columns=["Palavras"]
            )
            st.table(first_page_df)

        # Última Página
        with col2:
            st.subheader(f"Página {len(st.session_state.pages)}")
            last_page_df = pd.DataFrame(
                st.session_state.pages[-1], columns=["Palavras"]
            )
            st.table(last_page_df)

    st.header("Busca")
    search_word = st.text_input("Digite uma palavra para buscar:")

    if st.button("Buscar com Índice"):
        if search_word:
            if st.session_state.buckets:
                start_time = time.time()
                found_page = find_word_in_buckets(search_word, st.session_state.buckets)
                end_time = time.time()
                search_time = end_time - start_time
                st.session_state.search_time = search_time

                if found_page is not None:
                    st.success(
                        f"Palavra '{search_word}' encontrada na página {found_page + 1}"
                    )
                else:
                    st.warning(f"Palavra '{search_word}' não encontrada")

                # Exibição simplificada de custo e tempo
                st.info("Custo da busca com índice: 1 acesso ao disco (1 página lida)")
                st.info(f"Tempo decorrido: {search_time:.6f} segundos")
            else:
                st.error("Por favor, construa o índice primeiro")
        else:
            st.error("Por favor, digite uma palavra para buscar")

    if st.button("Varredura de Tabela (Table Scan)"):
        if search_word:
            words = read_file("words.txt")
            start_time = time.time()
            pages_read = 0
            found = False

            for page_index, page_words in enumerate(st.session_state.pages):
                pages_read += 1
                if search_word in page_words:
                    end_time = time.time()
                    table_scan_time = end_time - start_time
                    st.session_state.table_scan_time = table_scan_time
                    st.success(
                        f"Palavra '{search_word}' encontrada na página {page_index + 1}"
                    )
                    st.info(f"Custo da Varredura de Tabela: {pages_read} páginas lidas")
                    st.info(f"Tempo decorrido: {table_scan_time:.6f} segundos")
                    found = True
                    break

            if not found:
                end_time = time.time()
                table_scan_time = end_time - start_time
                st.session_state.table_scan_time = table_scan_time
                st.warning(f"Palavra '{search_word}' não encontrada")
                st.info(f"Custo da Varredura de Tabela: {pages_read} páginas lidas")
                st.info(f"Tempo decorrido: {table_scan_time:.6f} segundos")

        else:
            st.error(
                "Por favor, digite uma palavra para realizar a Varredura de Tabela"
            )

    # Exibe a diferença de tempo
    if "search_time" in st.session_state and "table_scan_time" in st.session_state:
        st.subheader("Comparação de Tempo")
        st.write(
            f"Diferença de tempo (Varredura de Tabela - Busca com Índice): {st.session_state.table_scan_time - st.session_state.search_time:.6f} segundos"
        )
