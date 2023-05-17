import streamlit as st
import time
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Aplikasi Perhitungan Sifat Koligatif Larutan", ['Halaman Utama', 'Penurunan Tekanan Uap (ΔP)', 'Penurunan Titik Beku (ΔTf)', 'Kenaikan Titik Didih (ΔTb)', 'Tekanan Osmosis (π)'], default_index=0)

#Halaman Utama
if selected == 'Halaman Utama':
    st.title('Halaman Utama')
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Sifat Koligatif Larutan", "Penurunan Tekanan Uap (ΔP)", "Penurunan Titik Beku (ΔTf)", "Kenaikan Titik Didih (ΔTb)", "Tekanan Osmosis (π)"])
    with tab1:
        st.header("Sifat Koligatif Larutan")
        st.write("Sifat koligatif larutan adalah sifat larutan yang tidak bergantung kepada jenis zat, tetapi hanya bergantung pada konsentrasi larutan. Sifat koligatif terdiri dari penurunan tekanan uap jenuh (ΔP), kenaikan titik didih larutan (ΔTb), penurunan titik beku larutan (ΔTf), dan tekanan osmotik larutan (π).")
        koligatif = Image.open('D:\webapps_using_streamlit\sifatkoligatif.jpg')
        st.image(koligatif, use_column_width=True)
    with tab2:
        st.header("Penurunan Tekanan Uap (ΔP)")
        st.write("Penurunan tekanan up (ΔP) adalah penurunan tekanan uap pelarut yang ditimbulkan ole zat terlarut, pada suhu konstan.")
        tekanan_uap = Image.open('D:\webapps_using_streamlit\TekananUap.jpg')
        st.image(tekanan_uap, use_column_width=True)
    with tab3:
        st.header("Penurunan Titik Beku (ΔTf)")
        st.write("Penurunan titik beku (ΔTf) adalah selisih titik didih pelarut dengan larutannya pada P konstan.")
        titik_beku = Image.open('D:\webapps_using_streamlit\TitikBeku.jpg')
        st.image(titik_beku, use_column_width=True)
    with tab4:
        st.header("Kenaikan Titik Didih (ΔTb)")
        st.write("Kenaikan titik didih (ΔTb) adalah selisih titik didih larutan dengan pelarutnya pada P konstan.")
        titik_didih = Image.open('D:\webapps_using_streamlit\TitikDidih.jpg')
        st.image(titik_didih, use_column_width=True)
    with tab5:
        st.header("Tekanan Osmosis (π)")
        st.write("Tekanan osmotik (π) adalah tekanan hidrostatik yang mempertahankan kesetimbangan osmotik larutan dengan pelarut murninya agar osmosis terhenti.")
        osmosis = Image.open('D:\webapps_using_streamlit\osmosis.jpg')
        st.image(osmosis, use_column_width=True)
        

#Penurunan Tekanan Uap
if selected == 'Penurunan Tekanan Uap (ΔP)':
    st.title('Perhitungan Penurunan Tekanan Uap (ΔP)')
    Jenis_larutan = st.selectbox(
    'Pilih jenis larutan',
    ('Larutan Non Elektrolit', 'Larutan Elektrolit'), index=0)
    if Jenis_larutan == 'Larutan Non Elektrolit':
        nt = st.number_input('Mol zat terlarut (nt)')
        np = st.number_input('Mol zat pelarut (np)')
        P = st.number_input('Tekanan uap jenuh pelarut murni (P°)')
        if st.button('Hasil Perhitungan'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            delta_P = (nt/(nt+np))*P
            st.success(f'Penurunan Tekanan Uap (ΔP) adalah {delta_P:.2f} mmHg')
    if Jenis_larutan == 'Larutan Elektrolit':
        nt = st.number_input('Mol zat terlarut (nt)')
        np = st.number_input('Mol zat pelarut (np)')
        P = st.number_input('Tekanan uap jenuh pelarut murni (P°)')
        n = st.number_input('Jumlah ion', value=0)
        alfa = st.number_input('Derajat ionisasi')
        if st.button('Hasil Perhitungan'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            delta_P = (nt/(nt+np))*P*(1+(n-1)*alfa)
            st.success(f'Penurunan Tekanan Uap (ΔP) adalah {delta_P:.2f} mmHg')

#Penurunan Titik Beku
if selected == 'Penurunan Titik Beku (ΔTf)':
    st.title('Perhitungan Penurunan Titik Beku (ΔTf)')
    Jenis_larutan = st.selectbox(
    'Pilih jenis larutan',
    ('Larutan Non Elektrolit', 'Larutan Elektrolit'), index=0)
    if Jenis_larutan == 'Larutan Non Elektrolit':
        massa = st.number_input('Massa zat terlarut (gram)')
        Mr = st.number_input('Massa molekul relatif zat terlarut (Mr)')
        P = st.number_input('Massa zat pelarut P (gram)')
        Kf = st.number_input('Tetapan penurunan titik beku zat pelarut (Kf)')
        if st.button('Hasil Perhitungan'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            delta_Tf = ((massa/Mr)*(1000/P))*Kf
            st.success(f'Penurunan Titik Beku (ΔTf) adalah {delta_Tf:.2f} °C')
    if Jenis_larutan == 'Larutan Elektrolit':
        massa = st.number_input('Massa zat terlarut (gram)')
        Mr = st.number_input('Massa molekul relatif zat terlarut (Mr)')
        P = st.number_input('Massa zat pelarut P (gram)')
        Kf = st.number_input('Tetapan penurunan titik beku zat pelarut (Kf)')
        n = st.number_input('Jumlah ion', value=0)
        alfa = st.number_input('Derajat ionisasi')
        if st.button('Hasil Perhitungan'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            delta_Tf = ((massa/Mr)*(1000/P))*Kf*(1+(n-1)*alfa)
            st.success(f'Penurunan Titik Beku (ΔTf) adalah {delta_Tf:.2f} °C')

#Kenaikan Titik Didih
if selected == 'Kenaikan Titik Didih (ΔTb)':
    st.title('Perhitungan Kenaikan Titik Didih (ΔTb)')
    Jenis_larutan = st.selectbox(
    'Pilih jenis larutan',
    ('Larutan Non Elektrolit', 'Larutan Elektrolit'), index=0)
    if Jenis_larutan == 'Larutan Non Elektrolit':
        massa = st.number_input('Massa zat terlarut (gram)')
        Mr = st.number_input('Massa molekul relatif zat terlarut (Mr)')
        P = st.number_input('Massa zat pelarut P (gram)')
        Kb = st.number_input('Tetapan kenaikan titik didih zat pelarut (Kb)')
        if st.button('Hasil Perhitungan'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            delta_Tb = ((massa/Mr)*(1000/P))*Kb
            st.success(f'Kenaikan Titik Didih (ΔTb) adalah {delta_Tb:.2f} °C')
    if Jenis_larutan == 'Larutan Elektrolit':
        massa = st.number_input('Massa zat terlarut (gram)')
        Mr = st.number_input('Massa molekul relatif zat terlarut (Mr)')
        P = st.number_input('Massa zat pelarut P (gram)')
        Kb = st.number_input('Tetapan kenaikan titik didih zat pelarut (Kb)')
        n = st.number_input('Jumlah ion', value=0)
        alfa = st.number_input('Derajat ionisasi')
        if st.button('Hasil Perhitungan'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            delta_Tb = ((massa/Mr)*(1000/P))*Kb*(1+(n-1)*alfa)
            st.success(f'Kenaikan Titik Didih (ΔTf) adalah {delta_Tb:.2f} °C')
            
#Tekanan Osmosis
if selected == 'Tekanan Osmosis (π)':
    st.title('Perhitungan Tekanan Osmosis (π)')
    Jenis_larutan = st.selectbox(
    'Pilih jenis larutan',
    ('Larutan Non Elektrolit', 'Larutan Elektrolit'), index=0)
    if Jenis_larutan == 'Larutan Non Elektrolit':
        massa = st.number_input('Massa zat terlarut (gram)')
        Mr = st.number_input('Massa molekul relatif zat terlarut (Mr)')
        V = st.number_input('Volume larutan (mL)')
        T = st.number_input('Suhu mutlak (K)')
        if st.button('Hasil Perhitungan'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            phi = ((massa/Mr)*(1000/V))*0.082*T
            st.success(f'Kenaikan Tekanan Osmosis (π) adalah {phi:.2f} atm')
    if Jenis_larutan == 'Larutan Elektrolit':
        massa = st.number_input('Massa zat terlarut (gram)')
        Mr = st.number_input('Massa molekul relatif zat terlarut (Mr)')
        V = st.number_input('Volume larutan (mL)')
        T = st.number_input('Suhu mutlak (K)')
        n = st.number_input('Jumlah ion', value=0)
        alfa = st.number_input('Derajat ionisasi')
        if st.button('Hasil Perhitungan'):
            progress_text = "Operasi sedang dalam proses. Harap tunggu."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.005)
                my_bar.progress(percent_complete + 1, text=progress_text)
            phi = ((massa/Mr)*(1000/V))*0.082*T*(1+(n-1)*alfa)
            st.success(f'Kenaikan Tekanan Osmosis (π) adalah {phi:.2f} atm')