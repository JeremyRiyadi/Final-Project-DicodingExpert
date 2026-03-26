# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Dalam konteks bisnis, institusi pendidikan memiliki kepentingan untuk meningkatkan tingkat kelulusan (graduate) dan menurunkan angka dropout, karena hal ini berdampak langsung pada reputasi institusi, keberlanjutan finansial (tuition fees), serta kualitas lulusan yang dihasilkan.

Dengan memanfaatkan data historis mahasiswa seperti latar belakang pendidikan, kondisi finansial, dan performa akademik, institusi dapat mengambil keputusan berbasis data untuk meningkatkan retensi mahasiswa.

### Permasalahan Bisnis

Beberapa permasalahan bisnis yang ingin diselesaikan antara lain:

1. Tingginya angka dropout mahasiswa yang berdampak pada kerugian finansial dan reputasi institusi
2. Kurangnya pemahaman mengenai faktor utama yang menyebabkan mahasiswa gagal menyelesaikan studi
3. Kesulitan dalam mengidentifikasi mahasiswa yang berisiko dropout sejak dini
4. Belum optimalnya strategi intervensi seperti pemberian beasiswa atau bantuan akademik

### Cakupan Proyek
- Analisis eksplorasi data untuk memahami karakteristik mahasiswa berdasarkan status (dropout, enrolled, graduate)
- Mengidentifikasi fitur-fitur yang paling berpengaruh terhadap status mahasiswa, seperti performa akademik, kondisi finansial, dan latar belakang pendidikan
- Membangun model machine learning untuk mengklasifikasikan status mahasiswa
- Evaluasi model untuk menentukan pendekatan terbaik dalam memprediksi risiko dropout
- Pembuatan dashboard (misalnya di Metabase) untuk memvisualisasikan insight penting bagi stakeholder
- Memberikan rekomendasi berbasis data untuk membantu institusi mengurangi dropout dan meningkatkan kelulusan

### Persiapan

Sumber data: student_performance dataset (https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:

```
1. Membuat dan Mengaktifkan Virtual Environment (venv)

Virtual environment digunakan untuk memisahkan dependensi proyek agar tidak bercampur dengan environment global.

Jalankan perintah berikut untuk membuat virtual environment:

py -m venv env

Aktifkan virtual environment:
Windows:
env\Scripts\activate

2. Menginstal Dependensi dari requirements.txt

Setelah virtual environment aktif, instal seluruh pustaka yang dibutuhkan menggunakan file requirements.txt:

pip install -r requirements.txt

```

## Business Dashboard
1. Distribution Status Mahasiswa

→ Mayoritas mahasiswa berstatus Graduate (48.9%), diikuti Dropout (32.1%), dan Enrolled (17.9%)
→ Menunjukkan tingkat kelulusan cukup tinggi, namun angka dropout masih signifikan

2. Status berdasarkan Admission Grade

→ Rata-rata admission grade relatif mirip di semua status (Dropout, Enrolled, Graduate)
→ Artinya, nilai masuk bukan faktor utama yang menentukan mahasiswa akan lulus atau dropout

3. Status berdasarkan Gender

→ Jumlah mahasiswa Graduate paling tinggi pada kedua gender, terutama pada gender female
→ Dropout juga cukup tinggi di kedua gender, menunjukkan tidak ada perbedaan signifikan berdasarkan gender

4. Status berdasarkan Financial Condition (Debtor)

→ Mahasiswa dengan status tidak memiliki hutang (0) mendominasi jumlah graduate
→ Mahasiswa yang memiliki hutang cenderung lebih sedikit yang lulus
→ Faktor finansial berpengaruh terhadap keberhasilan studi

5. Status berdasarkan Marital Status

→ Mahasiswa Single memiliki jumlah graduate tertinggi
→ Status menikah dan lainnya jauh lebih sedikit kontribusinya
→ Hal ini menunjukkan mayoritas mahasiswa aktif adalah belum menikah

6. Status berdasarkan Previous Qualification

→ Mahasiswa dengan nilai 0–7.5 memiliki jumlah graduate paling besar
→ Namun dropout juga cukup tinggi di kategori ini
→ Background akademik sebelumnya memiliki pengaruh, tapi tidak sepenuhnya menentukan hasil akhir

7. Status berdasarkan Scholarship Holder

→ Mahasiswa tanpa beasiswa (0) mendominasi semua status, termasuk graduate dan dropout
→ Mahasiswa dengan beasiswa memiliki proporsi graduate yang cukup baik
→ Beasiswa berpotensi membantu meningkatkan kelulusan

8. Status berdasarkan Tuition Fees Up to Date

→ Mahasiswa yang pembayaran kuliahnya lancar (1) memiliki jumlah graduate paling tinggi
→ Mahasiswa yang menunggak lebih banyak berada di kategori dropout
→ Ini menunjukkan faktor kemampuan membayar biaya kuliah sangat berpengaruh

9. KPI Utama
Total Mahasiswa: 4.424
Graduate: 48.9%
Dropout: 32.1%
Enrolled: 17.9%

Link : http://localhost:3000/public/dashboard/67cdbf40-df73-4784-9583-5f6a3e041a24

## Menjalankan Sistem Machine Learning
Berikut isi bagian **Menjalankan Sistem Machine Learning** yang bisa langsung kamu pakai 👇

---

## Menjalankan Sistem Machine Learning

Prototype sistem machine learning ini dibangun menggunakan **Streamlit** untuk melakukan prediksi status mahasiswa (Dropout, Enrolled, Graduate) berdasarkan input data pengguna

### Cara Menjalankan Prototype

1. **Clone atau download repository proyek**
   Pastikan seluruh file seperti `app.py`, folder `model/`, dan file dependency tersedia

2. **Buat dan aktifkan virtual environment (opsional tapi direkomendasikan)**

   ```
    python -m venv env
    env\Scripts\activate
   ```

3. **Install dependencies**

   ```
    pip install -r requirements.txt
   ```

4. **Jalankan aplikasi Streamlit**

   ```
    streamlit run app.py
   ```

5. **Gunakan aplikasi**

   * Masukkan data mahasiswa melalui form input
   * Klik tombol **Predict**
   * Sistem akan menampilkan hasil prediksi status mahasiswa

---

### Link Akses Prototype

Prototype dapat diakses melalui link berikut: https://final-project-dicodingexpert-nwgjjtnmp6saxawepadyjn.streamlit.app/
Link github : https://github.com/JeremyRiyadi/Final-Project-DicodingExpert

## Conclusion
Berdasarkan hasil analisis, dapat disimpulkan bahwa faktor yang paling berpengaruh terhadap status mahasiswa (dropout, enrolled, graduate) bukan berasal dari kemampuan akademik awal seperti admission grade, melainkan lebih dipengaruhi oleh performa akademik selama perkuliahan dan kondisi finansial mahasiswa

Meskipun tingkat kelulusan sudah tergolong tinggi (48.9%), angka dropout yang masih mencapai 32.1% menunjukkan adanya masalah signifikan dalam retensi mahasiswa. Faktor finansial seperti status hutang (debtor) dan kelancaran pembayaran biaya kuliah (tuition fees) terbukti memiliki pengaruh kuat terhadap kemungkinan mahasiswa menyelesaikan studi. Selain itu, performa akademik selama semester awal juga menjadi indikator penting keberhasilan mahasiswa

Di sisi lain, faktor demografis seperti gender dan marital status tidak menunjukkan pengaruh signifikan terhadap outcome mahasiswa. Hal ini menunjukkan bahwa intervensi yang efektif sebaiknya difokuskan pada aspek akademik dan finansial, bukan pada karakteristik personal

Secara keseluruhan, proyek ini berhasil mengidentifikasi bahwa risiko dropout dapat diprediksi dan dicegah lebih awal dengan memanfaatkan data historis mahasiswa, sehingga institusi dapat mengambil langkah proaktif untuk meningkatkan kelulusan

### Rekomendasi Action Items
- Early Warning System Mahasiswa Berisiko
Mengembangkan sistem deteksi dini berbasis data (misalnya dari nilai semester 1 dan status pembayaran) untuk mengidentifikasi mahasiswa yang berpotensi dropout sejak awal
- Program Bantuan Finansial yang Lebih Tepat Sasaran
Memberikan beasiswa atau skema pembayaran fleksibel kepada mahasiswa yang mengalami kesulitan finansial, terutama yang terindikasi memiliki risiko dropout tinggi
- Monitoring Performa Akademik Semester Awal
Fokus pada evaluasi dan pendampingan mahasiswa di semester 1 dan 2, karena performa di tahap ini sangat menentukan keberhasilan akhir
- Intervensi Akademik (Mentoring / Tutoring)
Menyediakan program bimbingan belajar atau mentoring untuk mahasiswa dengan performa akademik rendah
- Optimalisasi Kebijakan Pembayaran Kuliah
Meninjau ulang sistem pembayaran agar lebih fleksibel tanpa mengurangi stabilitas finansial institusi, guna mengurangi angka dropout akibat kendala biaya
- Dashboard Monitoring untuk Stakeholder
Menggunakan dashboard untuk memantau KPI utama secara real-time, sehingga pihak manajemen dapat mengambil keputusan lebih cepat dan tepat