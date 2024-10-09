import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import time

st.title('Dashboard Analisis Penyewaan Sepeda')
st.write('')

day = pd.read_csv('Data/day.csv')
hour = pd.read_csv('Data/hour.csv')
st.header('Korelasi Pearson Antar Variable')

histogram = {
    'season':'Data/histogram_musim.png',
    'yr':'Data/histogram_tahun.png',
    'mnth':'Data/histogram_bulan.png',
    'hour':'Data/histogram_jam.png',
    'holiday':'Data/histogram_holiday.png',
    'weekday':'Data/histogram_hari.png',
    'workingday':'Data/histogram_hari.png',
    'weathersit':'Data/histogram_cuaca.png',
    'temp':'Data/histogram_suhu_udara.png',
    'atemp':'Data/histogram_suhu_yg_dirasakan',
    'hum':'Data/histogram_kelembapan.png',
    'windspeed':'Data/histogram_kecepatan_angin.png',
    'casual':'Data/histogram_penyewa_no_membership.png',
    'registered':'Data/histogram_penyewa_membership.png',
    'cnt':'Data/histogram_penyewa_sepeda.png'
}

# MEMILIH DATASET
option_heatmap = st.selectbox('Pilih Heatmap:',['day','hour'])

fig , ax = plt.subplots(figsize=(14,8))
# MEMBUAT HEATMAP DAY
if option_heatmap == 'day':
    corr_day = day.drop(columns=['instant','dteday']).corr()
    sns.heatmap(corr_day,annot=True,cmap='coolwarm')
    plt.title('Tabel Heatmap Untuk Faktor Penyewa Sepeda Per hari',pad=20)
    st.pyplot(fig)
else:  # MEMBUAT HEATMAP HOUR 
    corr_hour  = hour.drop(['instant','dteday'],axis=1).corr(method='pearson')
    sns.heatmap(data=corr_hour,annot=True,cmap='coolwarm')
    plt.title('Tabel Heatmap Untuk Faktor Penyewa Sepeda Setiap Jam',pad=20)
    st.pyplot(fig)

st.write('')

st.sidebar.header('Nama  : Aliffa Agnur')
st.sidebar.header('Email : m211b4ky0393@bangkit.academy')
st.write('')
st.write('')

#Membuat Analisis Histogram
st.header('Visualisasi Histogram untuk setiap Variable')
output_histogram = st.empty()
option_histogram = st.sidebar.selectbox('Pilih Histogram: ',['season','yr','mnth','hour','holiday','weekday','workingday','weathersit','temp','atemp','hum','windspeed','casual','registered','cnt'])
output_histogram.image(image=histogram[option_histogram])

st.sidebar.write('')
tombol = st.sidebar.button("Grafik jumlah penyewa sepeda setiap hari")

st.write('')

if tombol == True :

    with st.spinner('Loading kaka...'):
        st.write('')
        st.header('Tren Banyaknya Penyewa Sepeda')
        line_chart = st.empty()
        fig , ax = plt.subplots(figsize=(9,6))
        ax.plot(day['dteday'],day['cnt'])
        ax.set_title("Tren banyaknya penyewa Sepeda Setiap Hari")
        ax.set_xlabel('Tanggal')
        ax.set_ylabel('Jumlah Penyewa Sepeda')
        line_chart.pyplot(fig)
        st.write('')

#Banyaknya Penyewa Sepeda Tiap Tahun
st.header('Pertumbuhan Banyaknya Penyewa Sepeda Tiap Tahun')

col1 , col2 = st.columns(2) # MENAMPILKAN 2 KOLOM DALAM 1 BARIS

fig , ax = plt.subplots()

 # MEMVISUALISASIKAN HASIL DARI STREAMLIT LANGSUNG
with col1:
    jumlah_penyewa_per_tahun = day.groupby('yr')['cnt'].sum().reset_index()
    sns.barplot(data=jumlah_penyewa_per_tahun,x='yr',y=jumlah_penyewa_per_tahun['cnt'])
    plt.title('Jumlah Penyewa Sepeda Setiap Tahun')
    plt.ylabel('Total Penyewa Sepeda')
    plt.xlabel('Tahun')
    plt.xticks(ticks=[0,1],labels=['Tahun Pertama','Tahun Kedua'])
    st.pyplot(fig)

with col2:
    rata2_penyewa_per_tahun = day.groupby('yr')['cnt'].mean().reset_index()
    sns.barplot(data=rata2_penyewa_per_tahun,x='yr',y='cnt')
    plt.title('Rata-rata Penyewa Sepeda Per Tahun')
    plt.ylabel('Total Penyewa Sepeda')
    plt.xlabel('Tahun')
    plt.xticks(ticks=[0,1],labels=['Tahun Pertama','Tahun Kedua'])
    st.pyplot(fig)

st.write('')
st.image('./Data/piechart_banyaknya_penyewa_sepeda_pertahun.png')

st.write('')
st.write('')

st.header("Musim Dengan Penyewa Sepeda Terbanyak")
biggest_season = day.groupby('season')['cnt'].sum().reset_index()
# MENGUBAH NILAI MUSIM MENJADI NAMA-NAMA MUSIM 
biggest_season.loc[biggest_season['season'] == 1 , 'season'] = 'Winter Season'
biggest_season.loc[biggest_season['season'] == 2 , 'season'] = 'Spring Season'
biggest_season.loc[biggest_season['season'] == 3 , 'season'] = 'Summer Season'
biggest_season.loc[biggest_season['season'] == 4 , 'season'] = 'Autumn Season'

# MENGUBAH NAMA KOLOM
biggest_season = biggest_season.rename({'cnt':'Total Penyewa'},axis=1)
biggest_season   #MENAMPILKANNYA DI DASHBOARD

fig , ax = plt.subplots(ncols=1,nrows=1,figsize=(10,7))
ax.pie(biggest_season['Total Penyewa'],autopct='%1.1f%%',labels=['Winter','Spring','Summer','Fall'],shadow=True,explode=(0,0,0.1,0))
ax.set_title('Musim dengan penyewa sepeda terbanyak')
st.pyplot(fig)

st.write('')
st.write('')


class PeringatanKeras(Exception): # Class untuk Melempar Kesalahan
    pass

# PILIH DATASET
choose_dataset = st.selectbox('Pilih Dataset : ',['day','hour'])

# MEMILIH KOLOM BERDASARKAN SELECTBOX YG DIPILIH
if choose_dataset == 'day':
    selected_columns = st.multiselect("Pilih kolom yg ingin ditampilkan: ",options=day.columns.tolist()) # MEMILIH KOLOM2 DAY
else:
    selected_columns = st.multiselect('Pilih kolom yg ingin ditampilkan:', options=hour.columns.tolist()) # MEMILIH KOLOM2 HOUR

num_rows = st.number_input("Masukkan jumlah sample yg ingin ditampilkan : ",min_value=1,value=5)  #INPUT JUMLAH SAMPLE

# JIKA SUDAH MEMILIH SETIDAKNYA 1 KOLOM 
if selected_columns:
    if choose_dataset == 'day':
        assert num_rows <= len(day) , "Input melebihi jumlah data! wkwkwk"  # JIKA INPUT MELEBIHI JUMLAH SAMPLE DAY
        st.dataframe(day[selected_columns].head(num_rows)) # MENAMPILKAN DATAFRAME NYA BERDASARKAN KOLOM DAN BANYAKNYA SAMPLE YG DIINPUT
    else:
        assert num_rows <= len(hour) , "Aduh ketinggian inputan nya aowkwok"  # JIKA INPUT MELEBIHI JUMLAH SAMPLE HOUR
        st.dataframe(hour[selected_columns].head(num_rows)) # MENAMPILKAN DATAFRAME BERDASARKAN KOLOM DAN JUMLAH SAMPLE YG DI INPUT

else: # JIKA BELUM MEMILIH KOLOM APAPUN
    raise PeringatanKeras('Pilih kolom dulu untuk menampilkan dataset nya!')

