Laporan Proyek Machine Learning
Nama : Juandhani Abimanyu
Nim : 211351069
Kelas : Malam B
Domain Proyek
Tidur yang berkualitas sangat penting bagi manusia karena itu adalah saat di mana tubuh dan otak memiliki kesempatan untuk pulih, memperbaiki diri, dan mengembalikan energi. Tidur berkualitas juga berperan dalam menjaga keseimbangan hormon dan mendukung kesehatan mental dan fisik. Kurang tidur atau tidur yang buruk dapat berdampak negatif pada kinerja, konsentrasi, suasana hati, dan bahkan meningkatkan risiko masalah kesehatan seperti penyakit jantung, obesitas, dan gangguan mental. Oleh karena itu, tidur yang berkualitas adalah komponen penting dari gaya hidup sehat dan produktif.

Business Understanding
Bedasarkan penjelasan sebelumnya penting untuk setiap individunya menjaga pola tidur dan hidup sehat, selain dari pada itu penting juga untuk mengetahui kualitas tidur yang selama ini dilakukan, apakah termasuk kedalam ganggunan tidur atau tidak. Maka dari itu perlu dibuatkan sistem yang mudah diakses agar setiap individunya dapat mengetahui kualitas tidurnya, apakah termasuk kedalam ganguan tidur atau tidak.

Bagian laporan ini mencakup:

Problem Statements
Menjelaskan pernyataan masalah latar belakang:

Sulitnya untuk masyarakat umum agar mengetahui kualitas tidurnya
Untuk mengetahui kualitas tidurnya, diperlukannya konsultasi dengan dokter yang mana biayanya tidaklah murah
Tim kesehatan yang harus menganalisis gangguan tidur secara manual
Goals
Menjelaskan tujuan dari pernyataan masalah:

Dapat mempermudah masyarakat umum maupun tim kesehatan dalam melakukan klasifikasi kualitas tidur seseorang
Dapat mempermudah masyarakat umum untuk mengetahui kualitas tidurnya tanpa harus mengeluarkan uang yang besar untuk bertemu dokter
Solution statements
Pembuatan aplikasi yang dapat mempermudah proses klasifikasi kualitas tidur menjadi solusi untuk saat ini. Dengan adanya sistem yang dapat mempermudah dan dapat diakses oleh setiap orang, maka setiap orang dapat mengetahui kualitas tidurnya dan dapat segera menyadari adanya gangguan tidur atau tidak.
Pembuatan aplikasi ini menggunakan dataset yang diambil dari kaggle dan di deploy menggunakan bantuan streamlit. Model yang dibuat menggunakan metode klasifikasi dengan algoritma logistic regression.
Data Understanding
Gambaran Umum Dataset: Dataset Kesehatan dan Gaya Hidup Tidur terdiri dari 400 baris dan 13 kolom, yang mencakup berbagai variabel yang berkaitan dengan tidur dan kebiasaan sehari-hari. Dataset ini mencakup rincian seperti jenis kelamin, usia, pekerjaan, durasi tidur, kualitas tidur, tingkat aktivitas fisik, tingkat stres, kategori BMI, tekanan darah, detak jantung, langkah harian, dan ada tidaknya gangguan tidur.

Fitur Utama Dataset: Metrik Tidur yang komprehensif: Jelajahi durasi, kualitas, dan faktor-faktor yang memengaruhi pola tidur. Faktor Gaya Hidup: Menganalisis tingkat aktivitas fisik, tingkat stres, dan kategori BMI. Kesehatan Kardiovaskular: Memeriksa tekanan darah dan pengukuran detak jantung. Analisis Gangguan Tidur: Mengidentifikasi terjadinya gangguan tidur seperti Insomnia dan Sleep Apnea.

Dataset: Sleep Health and Lifestyle Dataset.

Variabel-variabel pada Sleep Health and Lifestyle Dataset adalah sebagai berikut:
Person ID: Pengenal untuk setiap individu.
Gender: Jenis kelamin orang tersebut (Pria/Wanita).
Age: The age of the person in years.
Occupation: Pekerjaan atau profesi orang tersebut.
Sleep Duration (hours): Jumlah jam orang tersebut tidur per hari.
Quality of Sleep (scale: 1-10): Penilaian subjektif dari kualitas tidur, mulai dari 1 hingga 10.
Physical Activity Level (minutes/day): The number of minutes the person engages in physical activity daily.
Stress Level (scale: 1-10): Jumlah menit orang tersebut melakukan aktivitas fisik setiap hari.
BMI Category: The BMI category of the person (e.g., Underweight, Normal, Overweight).
Blood Pressure (systolic/diastolic): Kategori BMI orang tersebut (misalnya, Berat Badan Kurang, Normal, Berat Badan Berlebih).
Heart Rate (bpm): Denyut jantung istirahat seseorang dalam denyut per menit.
Daily Steps: Jumlah langkah yang dilakukan seseorang per hari.
Sleep Disorder: Ada atau tidaknya gangguan tidur pada orang tersebut (Tidak Ada, Insomnia, Sleep Apnea).
Detail tentang Kolom Gangguan Tidur:

Normal : Individu tidak menunjukkan gangguan tidur tertentu.
Insomnia : Individu mengalami kesulitan untuk tidur atau tetap tertidur, yang menyebabkan tidur yang tidak memadai atau berkualitas buruk.
Sleep Apnea : Individu mengalami henti napas saat tidur, yang mengakibatkan gangguan pola tidur dan potensi risiko kesehatan.
Data Preparation
Cek dulu nilai yang kosong dalam dataset:

df.isnull().sum()
Dikarenakan tidak ada dataset yang kosong kita lanjut

cek korelasi antar atribut

plt.figure(figsize=(10,8))
sns.heatmap(df.corr(),annot=True)
image

Visualisasi jumlah tipe gangguan tidur perkategorinya:

plt.figure(figsize=(3,3))
sns.set(font_scale=0.8)
sns.histplot(data=df, x='Sleep Disorder')
image

Distribusi Kategori BMI:

image

Distribusi Pekerjaan:

image

Data preparatation yang pertama kali dilakukan adalah merubah tipe data object (Gender, Occupation, BMI Category dan Sleep Disorder) menjadi integer menggunakan library yanng disediakan oleh sklearn yaitu LabelEncoder:
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()

df['gender'] = label_encoder.fit_transform(df['Gender'])
df['Occ'] = label_encoder.fit_transform(df['Occupation'])
df['BMI'] = label_encoder.fit_transform(df['BMI Category'])
df['Sleep'] = label_encoder.fit_transform(df['Sleep Disorder'])
df.head()
Setelah itu, dikarenakan kolom Person ID tidak akan dipakai maka kolom tersebut perlu dihapus:
df = df.drop('Person ID', axis=1)
Dikarenakan pada kolom Blood Pressure terdapat string berupa /, maka kolom tersebut perlu dipecah menjadi 2 yaitu BPU (Tekanan Darah Sistolik) dan BPD (Tekanan Darah Diastolik) menggunakan cara:
df[['BPU', 'BPD']] = df['Blood Pressure'].str.split('/', expand=True)
Modeling
Model yang dibuat menggunakan metode klasifikasi dengan algoritma Logistic Regression:

Menetapkan variabel independen (X) dan target variabel dependen (Y):
X = df[['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level',
        'Stress Level', 'Heart Rate', 'Daily Steps', 'Occ', 'BMI', 'gender', 'BPU', 'BPD']]
Y = df['Sleep']
Membagi data ke dalam data training dan testing dengan proporsi 60% data digunakan untuk training, 40% untuk testing:
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.4, stratify=Y, random_state=2)
Penggunakan algoritma:
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, Y_train)
Evaluation
Metrik evaluasi yang digunakan adalan akurasi dikarenakan Metrik evaluasi akurasi digunakan untuk mengukur sejauh mana model klasifikasi berhasil dalam memprediksi kelas-kelas dengan benar. Akurasi mengukur jumlah prediksi yang benar (positif dan negatif) dibagi oleh total jumlah prediksi. Metrik ini memberikan gambaran umum tentang seberapa baik model dapat mengklasifikasikan data dengan benar. Dalam rumus matematika, akurasi dihitung sebagai:

 

from sklearn.metrics import accuracy_score
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
setelah dilakukannya proses pembuatan model, akurasi yang didapatkan adalah 85% yang mana menunjukan jika model yang dibuat memiliki nilai error yang cukup minim yaitu 15%

Deployment
https://uasml1-vdmm8bcsenwixnbjddedi9.streamlit.app/
