import streamlit as st
import pandas as pd
import joblib

# Judul Aplikasi
st.title("Deteksi Kelayakan Kredit")

# Deskripsi singkat
st.write("Masukkan informasi berikut untuk memprediksi kelayakan kredit.")

# Form input
income = st.number_input("Pendapatan (dalam USD)", min_value=0)
age = st.number_input("Umur", min_value=18, max_value=100)
loan_amount = st.number_input("Jumlah Pinjaman", min_value=0)
term = st.selectbox("Jangka Waktu Pinjaman", ["short", "long"])
credit_history = st.selectbox("Riwayat Kredit", ["good", "bad"])
employment_status = st.selectbox("Status Pekerjaan", ["employed", "unemployed"])

# Mapping jika perlu
term_map = {"short": 0, "long": 1}
history_map = {"good": 1, "bad": 0}
employment_map = {"employed": 1, "unemployed": 0}

# Jika tombol diklik
if st.button("Prediksi"):
    # Load model
    model = joblib.load("decision_tree_model.pkl")  # ganti dengan nama file model kamu

    # Buat DataFrame input
    input_data = pd.DataFrame([{
        "income": income,
        "age": age,
        "loan_amount": loan_amount,
        "term": term_map[term],
        "credit_history": history_map[credit_history],
        "employment_status": employment_map[employment_status],
    }])

    # Prediksi
    pred = model.predict(input_data)[0]

    # Output
    if pred == 1:
        st.success("Kredit LAYAK diberikan.")
    else:
        st.error("Kredit TIDAK layak diberikan.")
