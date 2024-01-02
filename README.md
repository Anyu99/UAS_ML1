# Laporan Proyek Machine Learning
### Nama : Juandhani Abimanyu
### Nim : 211351069
### Kelas : Malam B

## Domain Proyek

Ketika bank menilai risiko kredit, mereka mempertimbangkan sejumlah faktor yang penting. Ini bukan hanya tentang memberikan atau menolak pinjaman. Ini adalah tentang mengelola risiko untuk memastikan keberlanjutan dan stabilitas keuangan bank, serta kepentingan nasabahnya. Penilaian risiko kredit yang baik memainkan peran utama dalam aktivitas perbankan modern, dan itu penting karena:<br> 1. Keberlanjutan Keuangan
Stabilitas Institusi Keuangan: Mengelola risiko kredit membantu bank mengurangi kemungkinan kegagalan keuangan yang dapat berdampak sistemik.<br>
2. Perlindungan bagi Nasabah dan Bank
Pencegahan Kerugian: Mencegah risiko kredit buruk membantu melindungi bank dari kerugian besar yang dapat mempengaruhi nasabah dan stabilitas finansial mereka.
Kepercayaan Pelanggan: Memberikan pinjaman hanya kepada mereka yang dapat membayar kembali membantu bank memelihara kepercayaan nasabah.<br>
3. Pengambilan Keputusan yang Bijak
Pengambilan Keputusan yang Tepat: Analisis risiko kredit yang cermat membantu bank dalam pengambilan keputusan yang lebih akurat tentang pemberian pinjaman.
Kesinambungan Bisnis: Mencegah pinjaman yang tidak terbayar membantu bank menjaga keberlanjutan bisnisnya.<br>
4. Regulasi dan Kepatuhan
Kepatuhan Regulasi: Kewajiban mematuhi peraturan pemerintah dalam memberikan pinjaman dengan memeriksa dan menilai risiko kredit secara hati-hati.<br>
5. Dampak Ekonomi
Stabilitas Ekonomi: Melalui manajemen risiko kredit yang efektif, bank membantu mempertahankan stabilitas ekonomi dengan menghindari keruntuhan keuangan besar.<br>

## Business Understanding

Bedasarkan penjelasan sebelumnya penting untuk setiap individunya menjaga pola tidur dan hidup sehat, selain dari pada itu penting juga untuk mengetahui kualitas tidur yang selama ini dilakukan, apakah termasuk kedalam ganggunan tidur atau tidak.
Maka dari itu perlu dibuatkan sistem yang mudah diakses agar setiap individunya dapat mengetahui kualitas tidurnya, apakah termasuk kedalam ganguan tidur atau tidak.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Sulitnya untuk masyarakat umum agar mengetahui kualitas tidurnya
- Untuk mengetahui kualitas tidurnya, diperlukannya konsultasi dengan dokter yang mana biayanya tidaklah murah
- Tim kesehatan yang harus menganalisis gangguan tidur secara manual

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Dapat mempermudah masyarakat umum maupun tim kesehatan dalam melakukan klasifikasi kualitas tidur seseorang
- Dapat mempermudah masyarakat umum untuk mengetahui kualitas tidurnya tanpa harus mengeluarkan uang yang besar untuk bertemu dokter
    ### Solution statements
    - Pembuatan aplikasi yang dapat mempermudah proses klasifikasi kualitas tidur menjadi solusi untuk saat ini. Dengan adanya sistem yang dapat mempermudah dan dapat diakses oleh setiap orang, maka setiap orang dapat mengetahui kualitas tidurnya dan dapat segera menyadari adanya gangguan tidur atau tidak.
    - Pembuatan aplikasi ini menggunakan dataset yang diambil dari kaggle dan di deploy menggunakan bantuan streamlit. Model yang dibuat menggunakan metode klasifikasi dengan algoritma logistic regression.
      
## Data Understanding
Gambaran Umum Dataset:
Dataset asli berisi 1000 entri dengan 20 atribut kategorial/simbolik yang disiapkan oleh Prof. Hofmann. Dalam dataset ini, setiap entri mewakili seseorang yang mengajukan kredit di sebuah bank. Setiap orang diklasifikasikan sebagai risiko kredit baik atau buruk berdasarkan serangkaian atribut. Tautan ke dataset asli dapat ditemukan di bawah ini.

Dataset: [German Credit Risk](https://www.kaggle.com/datasets/uciml/german-credit).

### Variabel-variabel pada German Credit Risk Dataset adalah sebagai berikut:.
- Sex (text: male, female):  Jenis kelamin orang tersebut.
- Age (numeric): Jumlah tahun yang telah dihabiskan sejak kelahiran seseorang.
- Job (numeric: 0 - unskilled and non-resident, 1 - unskilled and resident, 2 - skilled, 3 - highly skilled): Tingkat keahlian atau jenis peketrjaan yang dimiliki oleh individu.
- Housing (text: own, rent, or free): Menggambarkan status tempat tinggal.
- Saving accounts (text - little, moderate, quite rich, rich): Tingkat atau jumlah tabungan yang dimiliki oleh individu.
- Checking account (numeric, in DM - Deutsch Mark): Menggambarkan status atau jumlah uang yang tersedia dalam rekening checking individu.
- Credit amount (numeric, in DM): Besarnya kredit yang diajukan atau diberikan kepada individu.
- Duration (numeric, in month): Menunjukkan periode waktu dalam bulan yang diambil untuk melunasi kredit atau jangka waktu pinjaman.
- Purpose (text: car, furniture/equipment, radio/TV, domestic appliances, repairs, education, business, vacation/others): Mencakup kategori-kategori seperti pembelian mobil, perabot, peralatan rumah tangga, perbaikan, pendidikan, bisnis, liburan, dan tujuan lainnya yang mungkin menjadi alasan seseorang meminjam uang.

**Detail tentang Kolom Gangguan Tidur:**
- Normal : Individu tidak menunjukkan gangguan tidur tertentu.
- Insomnia : Individu mengalami kesulitan untuk tidur atau tetap tertidur, yang menyebabkan tidur yang tidak memadai atau berkualitas buruk.
- Sleep Apnea :  Individu mengalami henti napas saat tidur, yang mengakibatkan gangguan pola tidur dan potensi risiko kesehatan.

## Data Preparation
Cek dulu nilai yang kosong dalam dataset:
```
df.isnull().sum()
```
Dikarenakan tidak ada dataset yang kosong kita lanjut

cek korelasi antar atribut
```
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(),annot=True)
```
![image](https://github.com/Anyu99/kualitas-tidur/assets/136258491/a998f7fb-9f26-4834-8018-7045d78c81b2)

Visualisasi jumlah tipe gangguan tidur perkategorinya:
```
plt.figure(figsize=(3,3))
sns.set(font_scale=0.8)
sns.histplot(data=df, x='Sleep Disorder')
```
![image](https://github.com/Anyu99/kualitas-tidur/assets/136258491/62a5d7ac-483c-45c9-8ee4-0acf78057a58)

Distribusi Kategori BMI:

![image](https://github.com/Anyu99/kualitas-tidur/assets/136258491/8605d14a-7afd-442d-b3f8-910f2d3fb4ed)

Distribusi Pekerjaan:

![image](https://github.com/Anyu99/kualitas-tidur/assets/136258491/ac10722a-878a-450f-814e-b315cc972980)

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
from sklearn.metrics import accuracy_score
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
```
setelah dilakukannya proses pembuatan model, akurasi yang didapatkan adalah 85% yang mana menunjukan jika model yang dibuat memiliki nilai error yang cukup minim yaitu 15%

## Deployment
https://uasml1-vdmm8bcsenwixnbjddedi9.streamlit.app/

