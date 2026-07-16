import streamlit as st
import datetime

st.title("🎓 Profil Biodata Mahasiswa")
st.write("Silakan lengkapi biodata berikut")

# Nama & NIM
aldi_nama = st.text_input("Nama Lengkap")
aldi_nim = st.text_input("NIM")

# Jenis Kelamin
aldi_jenis_kelamin = st.radio("Jenis Kelamin", ["Laki-laki", "Perempuan"])

# Tempat & Tanggal Lahir
aldi_tempat_lahir = st.text_input("Tempat Lahir")
aldi_tanggal_lahir = st.date_input(
    "Tanggal Lahir",
    min_value=datetime.date(1990, 1, 1),
    max_value=datetime.date.today()
)

# Alamat
aldi_alamat = st.text_area("Alamat")

# Program Studi & Semester
aldi_prodi = st.selectbox("Program Studi", ["Teknik Komputer", "Teknik Informatika", "Sistem Informasi"])
aldi_semester = st.selectbox("Semester", [1, 2, 3, 4, 5, 6, 7, 8])

# Email & No HP
aldi_email = st.text_input("Email")
aldi_no_hp = st.text_input("No HP")

# Hobi
aldi_hobi = st.multiselect("Hobi", ["Membaca", "Olahraga", "Musik", "Gaming", "Traveling"])

# Upload Foto
aldi_foto = st.file_uploader("Upload Foto", type=["jpg", "png"])

# Tombol Tampilkan Biodata
aldi_tombol = st.button("Tampilkan Biodata")

if aldi_tombol:
    st.subheader("Hasil Biodata")
    st.write("Nama Lengkap:", aldi_nama)
    st.write("NIM:", aldi_nim)
    st.write("Jenis Kelamin:", aldi_jenis_kelamin)
    st.write("Tempat, Tanggal Lahir:", aldi_tempat_lahir, ",", aldi_tanggal_lahir)
    st.write("Alamat:", aldi_alamat)
    st.write("Program Studi:", aldi_prodi)
    st.write("Semester:", aldi_semester)
    st.write("Email:", aldi_email)
    st.write("No HP:", aldi_no_hp)
    st.write("Hobi:", ", ".join(aldi_hobi))
    if aldi_foto is not None:
        st.image(aldi_foto, caption="Foto yang diupload", width=200)