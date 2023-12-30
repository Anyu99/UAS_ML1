import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

df = pd.read_excel('dataset.xlsx')
df = df.drop(['Unnamed: 0','Sex','Job','Housing','Saving accounts','Checking account','Purpose'],axis=1)

# Header Interface
st.header("Isi dataset")
st.write(df)

# Create the slider for selecting the number of clusters (K)
st.sidebar.subheader("Nilai jumlah K")
n_clust = st.sidebar.slider("Pilih jumlah cluster: ", 2, 5, 2, 1)

# Create a selection box for scatter plot type
selected_plot = st.selectbox("Pilih Visualisasi Klasterisasi Data:", 
                             ["Umur dan Saldo Kredit", 
                              "Umur dan Durasi Pemakaian Kredit", 
                              "Umur, Durasi Pemakaian Kredit dan Saldo Kredit"])

# Scatter plot functions
def plot_Age_vs_Credit(n_clust):
    kmean = KMeans(n_clusters=n_clust, n_init=10).fit(df)
    df['Labels'] = kmean.labels_

    st.subheader('Umur dan Saldo Kredit')
    fig, ax = plt.subplots(figsize=(10, 5))

    sns.scatterplot(x=df['Age'], y=df['Credit amount'], hue=df['Labels'], palette=sns.color_palette('hls', n_colors=n_clust), ax=ax)
    st.pyplot(fig)

def plot_Age_vs_Duration(n_clust):
    kmean = KMeans(n_clusters=n_clust, n_init=10).fit(df)
    df['Labels'] = kmean.labels_

    st.subheader('Umur dan Durasi Pemakaian Kredit')
    fig, ax = plt.subplots(figsize=(10, 5))

    sns.scatterplot(x=df['Age'], y=df['Duration'], hue=df['Labels'], palette=sns.color_palette('hls', n_colors=n_clust), ax=ax)
    st.pyplot(fig)

def plot_Age_vs_Duration_vs_Credit(n_clust, df):
    kmean = KMeans(n_clusters=n_clust, n_init=10).fit(df[['Age', 'Duration', 'Credit amount']])
    df['Labels'] = kmean.labels_

    st.subheader('Umur, Durasi Pemakaian Kredit dan Saldo Kredit')

    # 2D scatter plot
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(x=df['Age'], y=df['Duration'], hue=df['Credit amount'], ax=ax)
    plt.title('2D Scatter Plot')
    plt.xlabel('Umur')
    plt.ylabel('Durasi Pemakaian Kredit')
    st.pyplot(fig)

    # 3D scatter plot
    fig2 = plt.figure()
    ax = fig2.add_subplot(111, projection='3d')
    ax.scatter(xs=df['Credit amount'], ys=df['Duration'], zs=df['Age'], c=df['Labels'])
    plt.title('Hasil Clustering')
    ax.set_xlabel('Total Selisih Hari Belanja')
    ax.set_ylabel('Durasi Pemakaian Kredit')
    ax.set_zlabel('Umur')
    st.pyplot(fig2)

if st.button("Proses Klasterisasi dan Tampilkan Plot"):
    clusters = []
    for i in range(1, 11):
        km = KMeans(n_clusters=i, n_init=10).fit(df)
        clusters.append(km.inertia_)

    # Display the elbow plot
    st.subheader("Mencari Elbow")
    st.line_chart(clusters, use_container_width=True)

    if selected_plot == "Umur dan Saldo Kredit":
        plot_Age_vs_Credit(n_clust)
    elif selected_plot == "Umur dan Durasi Pemakaian Kredit":
        plot_Age_vs_Duration(n_clust)
    elif selected_plot == "Umur, Durasi Pemakaian Kredit dan Saldo Kredit":
        plot_Age_vs_Duration_vs_Credit(n_clust, df)