import streamlit as st

st.title("Quiz")
st.write("Jawab Pertanyaan dibawah ini dengan True atau False!")

with st.form("quiz1"):
    betul = 0
    
    soal1 = st.radio(
        "1. SSL Certifcate adalah sertifikat digital yang mengotentifikasi identitas situs web dan memungkinkan koneksi terenkripsi",
        ["True", "False"]
    )
    kunci1 = "True"

    if soal1 == kunci1:
        betul += 1


    soal2 = st.radio(
        "2. SSL Certifcate tidak digunakan dalam kegiatan transaksi online",
        ["True", "False"]
    )
    kunci2 = "False"

    if soal2 == kunci2:
        betul += 1
    
    soal3 = st.radio(
        "3. HTTPS merupakan singkatan dari HyperText Transfer Protocol Science",
        ["True", "False"]
    )
    kunci3 = "False"

    if soal3 == kunci3:
        betul += 1

    soal4 = st.radio(
        "4. Kunci Public, Subdomain terkait, dan otoritas sertifikat termasuk beberapa detail yang disertakan dalam SSL Certificate",
        ["True", "False"]
    )
    kunci4 = "True"

    if soal4 == kunci4:
        betul += 1

    soal5 = st.radio(
        "5. EV SSL (Sertifikat Validasi Diperpanjang) dianggap sebagai sertifikat SSL Multi-Doman",
        ["True", "False"]
    )
    kunci5 = "False"

    if soal5 == kunci5:
        betul += 1


    submit = st.form_submit_button("Submit")

    if submit:
        nilai = betul * 20
        st.success(f"Skor kamu adalah {nilai}!")


st.write('Let\'s Celebrate!')
Gift = st.button("Click Me!")
if Gift:
    st.balloons()