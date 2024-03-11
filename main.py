#Import Library
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Membuat Title
st.title("Dashboard")

#Membuat Subheader
st.subheader("Proyek Analisis Data : [Bike Sharing Dataset]")

#Membuat text
st.text("Nama : Hashimatul Zaria")
st.text("Email: m206d4kx2421@bangkit.academy")
st.text("ID Dicoding: hashimatul_zaria_m206d4kx2421_0Gk8")
st.markdown("---")


# Load data
@st.cache
def load_data():
    bike_df = pd.read_csv('cleaned_data.csv')  # Ganti 'data.csv' dengan nama file data Anda
    return bike_df
bike_df = load_data()
# Tampilkan data
st.write(bike_df.head(5))

st.markdown("---")
#Membuat Header
st.header("Pertanyaan 1")
st.write("Bagaimana perbandingan rata-rata jumlah pengguna sepeda acak dan pengguna sepeda terdaftar.")

# Data dummy
data = {
    'categories': ['Casual', 'Registered'],
    'avg_counts': [bike_df['casual'].mean(), bike_df['registered'].mean()]  
}
# Convert data menjadi DataFrame
df_plot = pd.DataFrame(data)
# Pembuatan plot
plt.figure(figsize=(8, 5))
bars = plt.bar(df_plot['categories'], df_plot['avg_counts'], color=['blue', 'green'])
plt.xlabel('Kategori Pengguna Sepeda')
plt.ylabel('Rata-rata Jumlah Pengguna Sepeda')
plt.title('Rata-rata Jumlah Pengguna Sepeda Casual dan Terdaftar')
plt.grid(axis='y')
# Tampilkan plot menggunakan plt.show()
plt.show()
# Tampilkan plot menggunakan st.pyplot()
st.pyplot()
# Membandingkan rata-rata jumlah pengguna sepeda acak dan terdaftar
rerata_casual = bike_df['casual'].mean()
rerata_registered = bike_df['registered'].mean()
st.write("Rata-rata pengguna sepeda acak:", rerata_casual)
st.write("Rata-rata jumlah pengguna sepeda terdaftar:", rerata_registered)

st.markdown("#### Conclution pertanyaan 1 :")
st.write("Perbandingan rata-rata jumlah pengguna sepeda acak dan pengguna sepeda terdaftar dihasilkan bahwa rata-rata pengguna sepeda acak adalah 848.1764705882352 dan rata-rata jumlah pengguna sepeda terdaftar adalah 3656.172366621067. Dapat disimpulkan bahwa nilai rata-rata penggunaan sepeda terdaftar lebih tinggi dari rata-rata penggunaan sepeda secara acak. Maka, pengunjung banyak menggunakan sepeda yang terdaftar daripada menggunakan sepeda secara acak.")


st.markdown("---")
#Membuat Header
st.header("Pertanyaan 2")
st.write("Bagaimana pola perubahan penggunaan sepeda selama tahun ('yr') berdasarkan tiap bulannya.")

# Mengelompokkan data berdasarkan tahun dan bulan
year = bike_df.groupby(['yr', 'mnth'])['cnt'].mean().unstack()
# Pembuatan plot
plt.figure(figsize=(12, 6))
year.T.plot(kind='line', marker='o')
plt.title('Penggunaan Sepeda Selama Tahun')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pengguna Sepeda')
plt.xticks(range(1, 13))
plt.legend(['Tahun 0', 'Tahun 1'])
plt.grid(True)
# Tampilkan plot menggunakan st.pyplot()
st.pyplot()

st.markdown("#### Conclution pertanyaan 2 :")
st.write("Pola perubahan penggunaan sepeda selama tahun ('yr') berdasarkan tiap bulannya adalah pada tahun 0 di bulan 0-6 memilki kenaikan angka penggunaan sepeda, sedangkan pada bulan 7-12 angka penggunaan sepeda menurun. Kemudian pada tahun 1 di bulan 1-6 angka penggunaan sepeda itu meningkat, sedangkan pada bulan 7 memilki penurunan angka penggunaan sepeda, kemudian pada bulan 8-9 memiliki kenaikan angka penggunaan sepeda, dan penurunan angka penggunaan sepeda menurun kembali di bulan 10-12")
