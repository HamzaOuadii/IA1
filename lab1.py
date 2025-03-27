from datetime import date
import streamlit as st
from PIL import Image
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

st.title("Analyse des Ventes - Beans & Pods")

st.sidebar.title('Analyse BeansDataSet')
menu = st.sidebar.selectbox('Navigation', ['Accueil', 'Aperçu des données', 'Corrélation', 'Visualisation', 'Statistiques'])

col= ['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']

path = 'BeansDataSet.csv'  
data = pd.read_csv(path)  

if menu == 'Accueil':
    st.header(" Bienvenue dans l'analyse des données des haricots")
    st.markdown("""
        <div style='text-align:center;'>
        <p style='color:blue'> Projet d'analyse de données avec Streamlit </p>
        </div>
    """, unsafe_allow_html=True)
    st.subheader(' Aperçu des données')
    st.dataframe(data)

if menu == 'Aperçu des données':
    st.subheader('Aperçu des données')
    st.write(data.head())

if menu == 'Corrélation':
    st.subheader(" Corrélation de Pearson")
    correlation_matrice = data[col].corr()
    st.write(correlation_matrice)
    st.subheader(" Corrélation de Spearman")
    correlation_matrice_spearm = data[col].corr("spearman")
    st.write(correlation_matrice_spearm)
    st.write("La matrice de corrélation montre la relation entre les différentes colonnes numériques.")
    plt.figure(figsize=(10, 6))

    sns.heatmap(correlation_matrice, annot=True, cmap='coolwarm', fmt='.3f')
    plt.title('Matrice de correlation Pearson')
    st.pyplot(plt)

    st.subheader("Relation entre les ventes de Robusta et Espresso")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Robusta', y='Espresso', data=data, hue='Channel', palette='Set2')
    plt.title('Relation entre les ventes de Robusta et Espresso')
    plt.xlabel('Ventes de Robusta')
    plt.ylabel('Ventes de Espresso')
    plt.legend(title='Canal')
    st.pyplot(plt)

if menu == 'Visualisation':
    st.subheader("Ventes par Canal")
    sales_by_channel = data.groupby('Channel').sum()
    st.bar_chart(sales_by_channel.T)

    st.subheader("Ventes par Région")
    sales_by_region = data.groupby('Region').sum()
    st.bar_chart(sales_by_region.T)

    st.subheader("Relation entre les ventes de Robusta et Espresso")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Robusta', y='Espresso', data=data, hue='Channel', palette='Set2')
    plt.title('Relation entre les ventes de Robusta et Espresso')
    plt.xlabel('Ventes de Robusta')
    plt.ylabel('Ventes de Espresso')
    plt.legend(title='Canal')
    st.pyplot(plt)


if menu == 'Statistiques':
    st.subheader("Statistiques descriptives")
    st.write(data.describe())
    
    st.subheader("Histogrammes :")
    data.hist(bins=15,figsize=(15,10),layout=(3,3))
    plt.suptitle('Histogramme')
    st.pyplot(plt.gcf())

    st.subheader("Boîte à Moustaches")
    data.plot(kind='box', layout=(3,3), subplots=True, sharex=False, sharey=False, figsize=(15,15))
    st.pyplot(plt.gcf())

    st.subheader('Graphe de densite')
    data.plot(kind='density',layout=(3,3),subplots=True,sharex=False,sharey=False,figsize=(15,15))
    st.pyplot(plt.gcf())

    st.subheader('Pairplot')
    fig=sns.pairplot(data,hue='Cappuccino')
    st.pyplot(fig)


