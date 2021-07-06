import altair as alt
import dateutil
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

df = pd.read_csv("Vendas.csv")
df['Data Venda'] = df['Data Venda'].apply(dateutil.parser.parse, dayfirst=True)
df.rename(columns={df.columns[12]: 'precoCusto'}, inplace=True)

st.sidebar.title('Menu')
selected_page = st.sidebar.selectbox('Selecione o tipo de relatório', [
    'Vendas por ano', 'Vendas por categoria', 'Vendas de categoria por ano', 'Vendas de ano por categoria',
    'Produtos mais vendidos por fabricante', 'Vendas das lojas por categoria',
    'Produtos com maiores venda', 'Produtos com menores vendas', 'Produtos mais rentáveis', 'Vendas por lojas',
    'Vendedores com maior valor de vendas'
])

if selected_page == 'Vendas por ano':
    st.title('Relatório de vendas por ano')
    sales_by_years = df.groupby(df['Data Venda'].dt.strftime('%Y'))['ValorVenda'].sum()
    st.subheader('Vendas por ano')
    st.bar_chart(sales_by_years, use_container_width=True)

elif selected_page == 'Vendas por categoria':

    st.title('Relatório de vendas por categoria')

    sales_by_categories = df.groupby(['Categoria'])['ValorVenda'].sum()
    st.bar_chart(sales_by_categories, use_container_width=True)

elif selected_page == 'Vendas de ano por categoria':
    st.title('Relatório de vendas de categoria por ano')

    """
    Celulares(AZUL) \n
    Eletrodomesticos(Amarelo) \n
    Eletroportaateis(Vermelho) \n
    Eletronicos(Verde) \n
    """

    sales_by_categories_and_years = df.groupby([df['Data Venda'].dt.year, 'Categoria'])['ValorVenda'].sum()
    sales_by_categories_and_years = sales_by_categories_and_years.to_frame().reset_index()
    # labels = sales_by_categories_and_years['Data Venda'].to_numpy()

    celulares = sales_by_categories_and_years.loc[sales_by_categories_and_years['Categoria'] == 'Celulares'][
        'ValorVenda'].values
    eletrodomesticos = \
        sales_by_categories_and_years.loc[sales_by_categories_and_years['Categoria'] == 'Eletrodomestico'][
            'ValorVenda'].values
    eletroportateis = \
        sales_by_categories_and_years.loc[sales_by_categories_and_years['Categoria'] == 'Eletroportateis'][
            'ValorVenda'].values
    eletronicos = sales_by_categories_and_years.loc[sales_by_categories_and_years['Categoria'] == 'Eletronicos'][
        'ValorVenda'].values
    labels = ['2014', '2015', '2016', '2017', '2018', '2019']

    x1 = np.arange(len(labels))
    x2 = [x + 0.15 for x in x1]
    x3 = [x + 0.15 for x in x2]
    x4 = [x + 0.15 for x in x3]

    fig, ax = plt.subplots(figsize=(10, 7))

    # Plota as barras
    plt.bar(x1, celulares, width=0.15, label='Celulares', color='b')
    plt.bar(x2, eletrodomesticos, width=0.15, label='Eletrodomesticos', color='y')
    plt.bar(x3, eletroportateis, width=0.15, label='Eletroportateis', color='r')
    plt.bar(x4, eletronicos, width=0.15, label='Eletronicos', color='g')

    # coloca o nome dos meses como label do eixo x

    plt.xticks([x + 0.30 for x in range(len(celulares))], labels)

    plt.title('Vendas de categoria por ano')
    st.pyplot(fig)

elif selected_page == 'Vendas de categoria por ano':
    st.title('Relatório de vendas de categoria por ano')

    """
    2014(AZUL) \n
    2015(Amarelo) \n
    2016(Vermelho) \n
    2017(Verde) \n
    2018(Cinza) \n
    2019(Rosa)
    """
    # D - Vendas por ano e categoria
    sales_by_years_and_categories = df.groupby(['Categoria', df['Data Venda'].dt.year])['ValorVenda'].sum()
    sales_by_years_and_categories = sales_by_years_and_categories.to_frame().reset_index()
    # labels = sales_by_categories_and_years['Data Venda'].to_numpy()

    date1 = sales_by_years_and_categories.loc[sales_by_years_and_categories['Data Venda'] == 2014][
        'ValorVenda'].values
    date2 = sales_by_years_and_categories.loc[sales_by_years_and_categories['Data Venda'] == 2015][
        'ValorVenda'].values
    date3 = sales_by_years_and_categories.loc[sales_by_years_and_categories['Data Venda'] == 2016][
        'ValorVenda'].values
    date4 = sales_by_years_and_categories.loc[sales_by_years_and_categories['Data Venda'] == 2017][
        'ValorVenda'].values
    date5 = sales_by_years_and_categories.loc[sales_by_years_and_categories['Data Venda'] == 2018][
        'ValorVenda'].values
    date6 = sales_by_years_and_categories.loc[sales_by_years_and_categories['Data Venda'] == 2019][
        'ValorVenda'].values
    labels = ['Celulares', 'Eletroportateis', 'Eletronicos', 'Eletrodomesticos']

    x1 = np.arange(len(labels))
    x2 = [x + 0.15 for x in x1]
    x3 = [x + 0.15 for x in x2]
    x4 = [x + 0.15 for x in x3]
    x5 = [x + 0.15 for x in x4]
    x6 = [x + 0.15 for x in x5]

    fig, ax = plt.subplots(figsize=(10, 7))

    # Plota as barras
    plt.bar(x1, date1, width=0.15, label='2014', color='b')
    plt.bar(x2, date2, width=0.15, label='2015', color='y')
    plt.bar(x3, date3, width=0.15, label='2016', color='r')
    plt.bar(x4, date4, width=0.15, label='2017', color='g')
    plt.bar(x5, date5, width=0.15, label='2018', color='#495550')
    plt.bar(x6, date6, width=0.15, label='2019', color='#FA08E5')

    # coloca o nome dos meses como label do eixo x

    plt.xticks([x + 0.50 for x in range(len(labels))], labels)

    plt.title('Vendas de categoria por ano')
    st.pyplot(fig)

elif selected_page == 'Produtos mais vendidos por fabricante':

    # F - Produtos mais vendidos por cada fabricante
    most_selling_products = df.groupby(['Fabricante', 'Produto']).agg({'ValorVenda': 'count'}).sort_values(
        ['ValorVenda'], ascending=True)
    most_selling_products = most_selling_products.reset_index()
    most_selling_products.set_index("Fabricante")
    most_selling_products["Quantidade"] = most_selling_products['ValorVenda']
    chart = (
        alt.Chart(
            most_selling_products,
            title='Produtos mais vendidos por cada fabricante',
        )
            .mark_bar()
            .encode(
            x=alt.X("Quantidade", title="Valor de venda"),
            y=alt.Y(
                "Produto",
                sort=alt.EncodingSortField(field="stars", order="descending"),
                title="",
            ),
            color=alt.Color(
                "Fabricante",
                legend=alt.Legend(title="Fabricante"),
                scale=alt.Scale(scheme="category10"),
            ),
            tooltip=["Produto", "Quantidade", "Fabricante"],
        )
    )

    st.altair_chart(chart, use_container_width=True)

elif selected_page == 'Vendas das lojas por categoria':
    """
        Celulares(AZUL) \n
        Eletrodomesticos(Amarelo) \n
        Eletroportaateis(Vermelho) \n
        Eletronicos(Verde) \n
        """
    sales_by_categories_by_store = df.groupby(['Loja', 'Categoria'])['ValorVenda'].sum()
    sales_by_categories_by_store = sales_by_categories_by_store.to_frame().reset_index()

    celulares = sales_by_categories_by_store.loc[sales_by_categories_by_store['Categoria'] == 'Celulares'][
        'ValorVenda'].values
    eletrodomesticos = \
        sales_by_categories_by_store.loc[sales_by_categories_by_store['Categoria'] == 'Eletrodomestico'][
            'ValorVenda'].values
    eletroportateis = \
        sales_by_categories_by_store.loc[sales_by_categories_by_store['Categoria'] == 'Eletroportateis'][
            'ValorVenda'].values
    eletronicos = sales_by_categories_by_store.loc[sales_by_categories_by_store['Categoria'] == 'Eletronicos'][
        'ValorVenda'].values
    labels = ['AL1312', 'BA7783', 'GA7751', 'JB6325', 'JP8825', 'R1296', 'RG7742RG7742']

    x1 = np.arange(len(labels))
    x2 = [x + 0.15 for x in x1]
    x3 = [x + 0.15 for x in x2]
    x4 = [x + 0.15 for x in x3]

    fig, ax = plt.subplots(figsize=(10, 7))

    # Plota as barras
    plt.bar(x1, celulares, width=0.15, label='Celulares', color='b')
    plt.bar(x2, eletrodomesticos, width=0.15, label='Eletrodomesticos', color='y')
    plt.bar(x3, eletroportateis, width=0.15, label='Eletroportateis', color='r')
    plt.bar(x4, eletronicos, width=0.15, label='Eletronicos', color='g')

    # coloca o nome dos meses como label do eixo x

    plt.xticks([x + 0.30 for x in range(len(celulares))], labels)

    plt.title('Vendas das lojas por categoria')
    st.pyplot(fig)

elif selected_page == 'Produtos com maiores venda':
    st.subheader('Ranking dos produtos com maiores venda no geral')

    ranking_most_selling_products = df.groupby(['Produto']).agg({'ValorVenda': 'count'}).sort_values(['ValorVenda'],
                                                                                                     ascending=False)
    ranking_most_selling_products = ranking_most_selling_products.reset_index()
    st.table(ranking_most_selling_products)
    st.subheader('Ranking dos produtos com maiores venda por loja')

    ranking_most_selling_products_by_store = df.groupby(['Loja', 'Produto']).agg({'ValorVenda': 'count'}).sort_values(
        ['ValorVenda'], ascending=False)
    st.table(ranking_most_selling_products_by_store.reset_index())

elif selected_page == 'Produtos com menores vendas':

    st.subheader('Produtos com menores vendas no geral')

    ranking_least_sold_products = df.groupby(['Produto']).agg({'ValorVenda': 'count'}).sort_values(['ValorVenda'])
    st.table(ranking_least_sold_products.reset_index())
    st.subheader('Produtos com menores vendas por loja')
    ranking_least_sold_products_by_store = df.groupby(['Loja', 'Produto']).agg({'ValorVenda': 'count'}).sort_values(
        ['Loja', 'ValorVenda'])
    st.table(ranking_least_sold_products_by_store.reset_index())

elif selected_page == 'Produtos mais rentáveis':
    st.subheader('ranking dos produtos mais rentáveis no geral')

    df['Lucro'] = df.apply(lambda s: s.ValorVenda - s.precoCusto, axis=1)
    ranking_profitable_products = df.groupby(['Produto']).agg({
        'Lucro': 'sum'
    }).sort_values(['Lucro'], ascending=False)
    print(ranking_profitable_products)
    st.table(ranking_profitable_products.reset_index())

elif selected_page == 'Vendas por lojas':

    # K - Ranking de
    st.subheader('ranking de venda por lojas')

    ranking_most_selling_by_store = df.groupby(['Loja']).agg({'Produto': 'count'}).sort_values(['Produto'],
                                                                                               ascending=False)
    st.table(ranking_most_selling_by_store.reset_index())

elif selected_page == 'Vendedores com maior valor de vendas':
    st.subheader('Ranking de vendedores com maior valor de vendas')

# L - ranking dos v por loja e ano
    ranking_seller_by_store = df.groupby(['Loja', 'ID-Vendedor']).agg({'ValorVenda': 'sum'}).sort_values(
        ['Loja', 'ValorVenda'])
    st.table(ranking_seller_by_store.reset_index())
#
    st.subheader('Ranking de vendedores com maior valor de vendas por ano')

    ranking_seller_by_year = df.groupby([df['Data Venda'].dt.year, 'ID-Vendedor']).agg(
        {'ValorVenda': 'sum'}).sort_values(
        ['Data Venda', 'ValorVenda'])
    st.table(ranking_seller_by_year.reset_index())
