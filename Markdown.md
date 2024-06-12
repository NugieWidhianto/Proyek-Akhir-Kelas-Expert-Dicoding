# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Perusahaan Edutech Jaya Jaya Institut menghadapi kesulitan dalam mempertahankan siswa untuk menyelesaikan pendidikan mereka, yang tercermin dari tingginya tingkat siswa yang keluar sebelum lulus. Tingkat dropout yang tinggi dapat mengakibatkan penurunan reputasi institusi dan potensi kehilangan lulusan yang berkualitas. Tujuan proyek ini adalah untuk melakukan analisis faktor-faktor yang berdampak pada dropout dan mengembangkan model prediktif untuk mengidentifikasi siswa yang berisiko tinggi untuk meninggalkan institusi.

## Permasalahan Bisnis
1. **Tingginya Tingkat dan Angka Dropout Pada Institusi:** Jaya Jaya Institut memiliki tingkat dropout yang tinggi. Jumlah siswa yang tidak menyelesaikan pendidikan mereka merupakan masalah serius yang dapat mempengaruhi reputasi dan kinerja institusi.

## Cakupan Proyek
Proyek ini mencakup beberapa aspek utama:
- **Analisis Data Siswa:** Memahami distribusi dan karakteristik data siswa.
- **Preprocessing Data:** Membersihkan dan mempersiapkan data untuk analisis lebih lanjut.
- **Modeling:** Membangun dan mengevaluasi model prediktif menggunakan algoritma Random Forest.
- **Visualisasi Data:** Membuat visualisasi untuk memahami pola dropout berdasarkan berbagai fitur siswa menggunakan PowerBI.

## Persiapan
**Sumber data:**
- Data siswa (data.csv) | Link : https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

**Setup environment:**
1. Buat virtual environment
python -m venv myenv

2. Aktifkan virtual environment
.\myenv\Scripts\activate

3. Install library dari requirements.txt
pip install -r requirements.txt

## Business Dashboard
Dashboard ini menyajikan gambaran visual mengenai data umum seperti jumlah siswa, tingkat kelulusan, dan distribusi dropout berdasarkan variabel seperti nilai semester pertama dan kedua, serta jumlah mata kuliah yang diambil oleh mahasiswa. Visualisasi ini bermanfaat untuk memahami pola dropout, faktor-faktor yang berpengaruh, serta informasi penting dalam dataset kita.

## Conclusion
Berdasarkan analisis yang dilakukan, disimpulkan bahwa faktor-faktor seperti nilai pada semester awal dan semester kedua, serta jumlah mata kuliah yang diambil berpengaruh signifikan terhadap tingkat siswa yang drop out. Model Random Forest yang dikembangkan menunjukkan kemampuan yang baik dalam memprediksi siswa yang berpotensi besar untuk meninggalkan institusi, dengan tingkat akurasi sebesar 76%.

## Rekomendasi Action Items
Berikut beberapa rekomendasi action items yang dapat dilakukan perusahaan guna menyelesaikan permasalahan:

1. **Riset dan Survey tentang Kurikulum yang Diberikan Kepada Mahasiswa:**
Menyarankan untuk melakukan riset mendalam dan survey terhadap kurikulum yang diberikan kepada mahasiswa. Melibatkan mahasiswa dalam penilaian terhadap relevansi, kedalaman, serta keefektifan materi yang diajarkan dapat membantu institusi untuk mengevaluasi kebutuhan dan perbaikan dalam penyusunan kurikulum. Dengan demikian, dapat memastikan bahwa kurikulum yang diselenggarakan sesuai dengan tuntutan perkembangan ilmu di bidang yang diajarkan dan dapat memberikan pengalaman belajar yang lebih bermakna bagi mahasiswa.

2. **Pemberian Pelajaran Tambahan ataupun Perhatian Tambahan Kepada Mahasiswa dengan Nilai Rata-Rata yang Rendah:**
Mengusulkan untuk memberikan perhatian tambahan dan bantuan kepada mahasiswa yang memiliki nilai rata-rata yang rendah. Dengan mengidentifikasi mahasiswa yang berisiko terhadap tingkat dropout dan memberikan bimbingan tambahan, program akademik yang disesuaikan dengan kebutuhan individu, atau pelatihan keterampilan supaya mereka dapat meningkatkan prestasi akademik mereka. Dengan demikian, dapat membantu meningkatkan kesempatan kelulusan mereka dan mengurangi tingkat dropout di institusi tersebut.


## Prediksi dan Penggunaan Model
1. **Pastikan File Berikut Tersedia dalam Satu Folder:**
> model.joblib
> scaler.joblib
Mulai Terminal atau Command Prompt

2. **Arahkan Direktori ke Lokasi Folder yang Berisi app.py, model.joblib, dan scaler.joblib.**

Jalankan Perintah Berikut untuk Memulai Aplikasi Streamlit:
streamlit run app.py

3. **Input Nilai pada Aplikasi Streamlit: Pada halaman aplikasi, akan terdapat formulir input untuk memasukkan nilai pada empat kolom utama:**
> Jumlah kursus yang diambil pada Semester 1: Masukkan jumlah kursus yang diambil pada semester 1 (contoh: 5).
> Rata-rata nilai Semester 1: Masukkan rata-rata nilai pada semester 1 (contoh: 2.5).
> Jumlah kursus yang diambil pada Semester 2: Masukkan jumlah kursus yang diambil pada semester 2 (contoh: 5).
> Rata-rata nilai Semester 2: Masukkan rata-rata nilai pada semester 2 (contoh: 2.5).

4. **Setelah semua nilai input terisi, klik tombol "Prediksi" yang tersedia di halaman aplikasi.**

## Link Streamlit
-  https://proyek-akhir-nugie.streamlit.app/
