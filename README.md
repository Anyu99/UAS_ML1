# Laporan Proyek Machine Learning
### Nama : Juandhani Abimanyu
### Nim : 211351069
### Kelas : Malam B

## Domain Proyek

Ketika bank menilai risiko kredit, mereka mempertimbangkan sejumlah faktor yang penting. Ini bukan hanya tentang memberikan atau menolak pinjaman. Ini adalah tentang mengelola risiko untuk memastikan keberlanjutan dan stabilitas keuangan bank, serta kepentingan nasabahnya. Penilaian risiko kredit yang baik memainkan peran utama dalam aktivitas perbankan modern, dan itu penting karena:<br> 1. Keberlanjutan Keuangan
- Stabilitas Institusi Keuangan: Mengelola risiko kredit membantu bank mengurangi kemungkinan kegagalan keuangan yang dapat berdampak sistemik.<br>
2. Perlindungan bagi Nasabah dan Bank
- Pencegahan Kerugian: Mencegah risiko kredit buruk membantu melindungi bank dari kerugian besar yang dapat mempengaruhi nasabah dan stabilitas finansial mereka.
Kepercayaan Pelanggan: Memberikan pinjaman hanya kepada mereka yang dapat membayar kembali membantu bank memelihara kepercayaan nasabah.<br>
3. Pengambilan Keputusan yang Bijak
- Pengambilan Keputusan yang Tepat: Analisis risiko kredit yang cermat membantu bank dalam pengambilan keputusan yang lebih akurat tentang pemberian pinjaman.
Kesinambungan Bisnis: Mencegah pinjaman yang tidak terbayar membantu bank menjaga keberlanjutan bisnisnya.<br>
4. Regulasi dan Kepatuhan
- Kepatuhan Regulasi: Kewajiban mematuhi peraturan pemerintah dalam memberikan pinjaman dengan memeriksa dan menilai risiko kredit secara hati-hati.<br>
5. Dampak Ekonomi
- Stabilitas Ekonomi: Melalui manajemen risiko kredit yang efektif, bank membantu mempertahankan stabilitas ekonomi dengan menghindari keruntuhan keuangan besar.<br>

## Business Understanding

Pada kasus analisis risiko kredit dalam konteks perbankan adalah penting untuk memahami tujuan dan latar belakang bisnis di balik analisis ini. Ini melibatkan pemahaman yang komprehensif tentang bagaimana pengelolaan risiko kredit berperan dalam strategi bisnis bank dan dampaknya terhadap keberlanjutan serta kepentingan nasabah dan bank.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Manajemen Risiko yang Efektif: Bagaimana cara bank dapat meningkatkan strategi manajemen risiko kredit guna mengurangi kemungkinan kegagalan keuangan yang dapat berdampak sistemik?
- Kualitas Portofolio Kredit: Bagaimana cara meningkatkan kualitas portofolio kredit untuk melindungi bank dari kerugian besar dan menjaga stabilitas finansial nasabahnya?
- Kepuasan Nasabah: Bagaimana cara memberikan layanan pinjaman yang cerdas untuk menjaga kepercayaan nasabah sambil tetap meminimalkan risiko kredit?

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Mengurangi Risiko Finansial: Tujuan utama adalah mengurangi risiko finansial bank dengan memperbaiki proses penilaian risiko kredit sehingga kegagalan keuangan dapat diminimalkan.
- Meningkatkan Kualitas Portofolio: Memperbaiki kualitas portofolio kredit dengan memberikan pinjaman hanya kepada mereka yang dapat membayar kembali.
- Optimalisasi Layanan Nasabah: Menawarkan layanan pinjaman yang lebih baik dan lebih cerdas kepada nasabah untuk memelihara kepercayaan pelanggan.
    ### Solution statements
    ## 1.Strategi Pemilihan Peminjam yang Lebih Cermat:
    - Menyusun strategi yang lebih ketat dalam memilih peminjam dengan menganalisis secara rinci keadaan keuangan, riwayat kredit, dan faktor-faktor lain yang berkontribusi terhadap risiko kredit.
    - Memanfaatkan teknologi untuk mengintegrasikan data keuangan terkini dari berbagai sumber dan menganalisisnya secara cepat dan efisien.<br>
    ## 2.Penggunaan Tools Analisis dan Clustering:
    - Menggunakan alat dan platform analisis data canggih untuk mengelompokkan pelanggan ke dalam segmen-segmen berdasarkan perilaku kredit, memungkinkan identifikasi pola-pola risiko yang berbeda di antara kelompok-kelompok ini.
          
## Data Understanding
Gambaran Umum Dataset:
Dataset asli berisi 1000 entri dengan 20 atribut kategorial/simbolik yang disiapkan oleh Prof. Hofmann. Dalam dataset ini, setiap entri mewakili seseorang yang mengajukan kredit di sebuah bank. Setiap orang diklasifikasikan sebagai risiko kredit baik atau buruk berdasarkan serangkaian atribut. Tautan ke dataset asli dapat ditemukan di bawah ini.

Dataset: [German Credit Risk](https://www.kaggle.com/datasets/uciml/german-credit).

### Variabel-variabel pada German Credit Risk Dataset adalah sebagai berikut:
- Sex (text: male, female):  Jenis kelamin orang tersebut.
- Age (numeric): Jumlah tahun yang telah dihabiskan sejak kelahiran seseorang.
- Job (numeric: 0 - unskilled and non-resident, 1 - unskilled and resident, 2 - skilled, 3 - highly skilled): Tingkat keahlian atau jenis peketrjaan yang dimiliki oleh individu.
- Housing (text: own, rent, or free): Menggambarkan status tempat tinggal.
- Saving accounts (text - little, moderate, quite rich, rich): Tingkat atau jumlah tabungan yang dimiliki oleh individu.
- Checking account (numeric, in DM - Deutsch Mark): Menggambarkan status atau jumlah uang yang tersedia dalam rekening checking individu.
- Credit amount (numeric, in DM): Besarnya kredit yang diajukan atau diberikan kepada individu.
- Duration (numeric, in month): Menunjukkan periode waktu dalam bulan yang diambil untuk melunasi kredit atau jangka waktu pinjaman.
- Purpose (text: car, furniture/equipment, radio/TV, domestic appliances, repairs, education, business, vacation/others): Mencakup kategori-kategori seperti pembelian mobil, perabot, peralatan rumah tangga, perbaikan, pendidikan, bisnis, liburan, dan tujuan lainnya yang mungkin menjadi alasan seseorang meminjam uang.

### Variabel-variabel yang saya gunakan untuk membuat Tools Analisis dan Clustering sebagi berikut:
- Age (numeric): Jumlah tahun yang telah dihabiskan sejak kelahiran seseorang.
- Duration (numeric, in month): Menunjukkan periode waktu dalam bulan yang diambil untuk melunasi kredit atau jangka waktu pinjaman.
- Credit amount (numeric, in DM): Besarnya kredit yang diajukan atau diberikan kepada individu.

## Data Preparation
Cek dulu nilai yang kosong dalam dataset:
```
df.isnull().sum()
```
Unnamed: 0            0 <br>
Age                   0 <br>
Sex                   0 <br>
Job                   0 <br>
Housing               0 <br>
Saving accounts     183 <br>
Checking account    394 <br>
Credit amount         0 <br>
Duration              0 <br>
Purpose               0 <br>
dtype: int64 <br>
Setelah dilakukan proses pengecekan nilai yang Null terdapat 183 dataset Null pada atribut Saving accounts dan 394 Checking account, maka dari itu perlu dilakukannya processing terhadap atribut tersebut

### mengisi nilai Null denggan unknown
```
df= df.fillna('unknown')
df.isnull().sum()
```
Unnamed: 0          0 <br>
Age                 0 <br>
Sex                 0 <br>
Job                 0 <br>
Housing             0 <br>
Saving accounts     0 <br>
Checking account    0 <br>
Credit amount       0 <br>
Duration            0 <br>
Purpose             0 <br>
dtype: int64 <br>
Perintah df = df.fillna('unknown') digunakan untuk mengisi nilai null (NaN) di dalam DataFrame df dengan string 'unknown'. Ini berarti setiap nilai null yang ada dalam DataFrame akan diganti dengan string 'unknown'.

##Exploratory Data Analysis
Cek distribusi nilai pada atribut Age:
![image](https://github.com/Anyu99/UAS_ML1/assets/136258491/e8af89a0-5999-4dff-9ef6-95936041a69a)

pada visualisasi tersebut dapat disimpulkan jika dominan umur pada dataset adalah >30 tahun

distribusi tempat tinggal:

![image](https://github.com/Anyu99/UAS_ML1/assets/136258491/cb10aba8-fdd4-40e2-a488-82ee767e4ea8)

didalam dataset tersebut tempat tinggal yang ditempati setiap orangnya dominan milik sendiri lalu sewa dan yang paling sedikit free

visualisasi jenis kelamin:
![image](https://github.com/Anyu99/UAS_ML1/assets/136258491/e148e99d-52dc-4fbe-a02d-dd3616f50551)

laki-laki menjadi jenis kelamin terbanyak yang ada di dalam dataset.

jenis barang yang dikreditkan:
![image](https://github.com/Anyu99/UAS_ML1/assets/136258491/57146114-9a79-4620-b749-09982cbc950e)

kebanyakan orang mengajukan kredit untuk pembelian mobil.

distribusi pekerjaan:
![image](https://github.com/Anyu99/UAS_ML1/assets/136258491/89a154f5-d61b-41f5-8ad6-8425d83dce51)

berdasarkan visualisasi tersebut, status pekerjaan terbanyak ada pada kategori 2 (skilled) yaitu orang yang sudah memiliki keahlian lalu kategori 1 (unskilled and resident) untuk mereka yang belum memiliki keahlian dan menetap di daerah yang sama dengan wilayah kerja mereka.

1. Data preparatation yang pertama kali dilakukan adalah merubah tipe data object (Gender, Occupation, BMI Category dan Sleep Disorder) menjadi integer menggunakan library yanng disediakan oleh sklearn yaitu LabelEncoder:
```bash
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

df['gender'] = label_encoder.fit_transform(df['Gender'])
df['Occ'] = label_encoder.fit_transform(df['Occupation'])
df['BMI'] = label_encoder.fit_transform(df['BMI Category'])
df['Sleep'] = label_encoder.fit_transform(df['Sleep Disorder'])
df.head()
```
2. Setelah itu, dikarenakan kolom Person ID tidak akan dipakai maka kolom tersebut perlu dihapus:
```bash
df = df.drop('Person ID', axis=1)
```
3. Dikarenakan pada kolom Blood Pressure terdapat string berupa **/**, maka kolom tersebut perlu dipecah menjadi 2 yaitu BPU (Tekanan Darah Sistolik) dan BPD (Tekanan Darah Diastolik) menggunakan cara:
```bash
df[['BPU', 'BPD']] = df['Blood Pressure'].str.split('/', expand=True)
```

## Modeling
Model yang dibuat menggunakan metode klasifikasi dengan algoritma Logistic Regression:
1. Menetapkan variabel independen (X) dan target variabel dependen (Y):
```bash
X = df[['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level',
        'Stress Level', 'Heart Rate', 'Daily Steps', 'Occ', 'BMI', 'gender', 'BPU', 'BPD']]
Y = df['Sleep']
```
2. Membagi data ke dalam data training dan testing dengan proporsi 60% data digunakan untuk training, 40% untuk testing:
```bash
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.4, stratify=Y, random_state=2)
```
3. Penggunakan algoritma:
```bash
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, Y_train)
```
## Evaluation
Metrik evaluasi yang digunakan adalan akurasi dikarenakan Metrik evaluasi akurasi digunakan untuk mengukur sejauh mana model klasifikasi berhasil dalam memprediksi kelas-kelas dengan benar. Akurasi mengukur jumlah prediksi yang benar (positif dan negatif) dibagi oleh total jumlah prediksi. Metrik ini memberikan gambaran umum tentang seberapa baik model dapat mengklasifikasikan data dengan benar. Dalam rumus matematika, akurasi dihitung sebagai:

$$\text{Akurasi} = \frac{\text{Total Prediksi}}{\text{Jumlah Prediksi Benar}}$$

```bash
# Membuat figure dengan ukuran tertentu
fig = plt.figure(figsize=(10, 8))

# Membuat subplot 3D
ax = fig.add_subplot(111, projection='3d')

# Melakukan scatter plot dengan data yang dimiliki
scatter = ax.scatter(xs=df_clustered['Age'], ys=df_clustered['Credit amount'], zs=df_clustered['Duration'], c=df_clustered['Labels'], cmap='viridis')

# Menambahkan label pada sumbu x, y, dan z
ax.set_xlabel('Umur Nasabah', fontsize=12)
ax.set_ylabel('Total Penggunaan Credit', fontsize=12)
ax.set_zlabel('Durasi', fontsize=12)

# Menambahkan judul pada plot
plt.title('Hasil Clustering', fontsize=14)

# Menyesuaikan ukuran teks untuk tick labels
ax.tick_params(axis='both', which='major', labelsize=10)

# Menampilkan colorbar
plt.colorbar(scatter, ax=ax, label='Labels')

# Menampilkan plot
plt.show()
```
![image](https://github.com/Anyu99/UAS_ML1/assets/136258491/f27e303a-f240-4147-8efe-8f512b192e97)



## Deployment
https://uasml1-vdmm8bcsenwixnbjddedi9.streamlit.app/

