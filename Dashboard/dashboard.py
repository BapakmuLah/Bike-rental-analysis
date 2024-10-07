import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import time
st.title('Dashboard Analisis Penyewaan Sepeda')
st.write('')

day = pd.read_csv('Data/day.csv')
hour = pd.read_csv('Data/hour.csv')
st.header('Analisis Korelasi Antar Variable')

heatmap= {
    'day':'Data/heatmap_day.png',
    'hour':'Data/heatmap_hour.png'
}
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

# Membuat Analisis Heatmap
output_heatmap = st.empty()
option_heatmap = st.selectbox('Pilih Heatmap:',['day','hour'])
output_heatmap.image(heatmap[option_heatmap],caption="Terdapat hubungan cukup kuat antara banyaknya penyewa sepeda dengan faktor-faktor lainnya")

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

col1 , col2 = st.columns(2) #menampilkan 2 kolom dalam 1 baris/line

with col1:
    st.image('./Data/barchart_banyaknya_penyewa_sepeda_pertahun.png')

with col2:
    st.image('./Data/barchart_rata2_penyewa_sepeda_pertahun.png')

st.write('')
st.image('./Data/piechart_banyaknya_penyewa_sepeda_pertahun.png')

st.write('')
st.write('')
st.header("Musim Dengan Penyewa Sepeda Terbanyak")
st.image('./Data/piechart_musim_penyewa_sepeda_terbanyak.png')

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
        assert num_rows <= len(day) , "Input melebihi jumlah sample! wkwkwk"  # JIKA INPUT MELEBIHI JUMLAH SAMPLE DAY
        st.dataframe(day[selected_columns].head(num_rows)) # MENAMPILKAN DATAFRAME NYA BERDASARKAN KOLOM DAN BANYAKNYA SAMPLE YG DIINPUT
    else:
        assert num_rows <= len(hour) , "Aduh ketinggian inputan nya aowkwok"  # JIKA INPUT MELEBIHI JUMLAH SAMPLE HOUR
        st.dataframe(hour[selected_columns].head(num_rows)) # MENAMPILKAN DATAFRAME BERDASARKAN KOLOM DAN JUMLAH SAMPLE YG DI INPUT

else: # JIKA BELUM MEMILIH KOLOM APAPUN
    raise PeringatanKeras('Pilih kolom dulu untuk menampilkan dataset nya!')

