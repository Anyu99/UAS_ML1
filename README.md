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
    #### 1.Strategi Pemilihan Peminjam yang Lebih Cermat:
    - Menyusun strategi yang lebih ketat dalam memilih peminjam dengan menganalisis secara rinci keadaan keuangan, riwayat kredit, dan faktor-faktor lain yang berkontribusi terhadap risiko kredit.
    - Memanfaatkan teknologi untuk mengintegrasikan data keuangan terkini dari berbagai sumber dan menganalisisnya secara cepat dan efisien.<br>
    #### 2.Penggunaan Tools Analisis dan Clustering:
    - Menggunakan alat dan platform analisis data canggih untuk mengelompokkan pelanggan ke dalam segmen-segmen berdasarkan perilaku kredit, memungkinkan identifikasi pola-pola risiko yang berbeda di antara kelompok-kelompok ini.
          
## Data Understanding
Gambaran Umum Dataset:
Dataset asli berisi 1000 entri dengan 20 atribut kategorial/simbolik yang disiapkan oleh Prof. Hofmann. Dalam dataset ini, setiap entri mewakili seseorang yang mengajukan kredit di sebuah bank. Setiap orang diklasifikasikan sebagai risiko kredit baik atau buruk berdasarkan serangkaian atribut. Tautan ke dataset asli dapat ditemukan di bawah ini.

Dataset: [German Credit Risk](https://www.kaggle.com/datasets/uciml/german-credit).

## Content
Beberapa kolom diabaika, karena menurut saya, entah itu tidak penting atau deskripsi mereka ambigu. Atribut-atribut yang dipilih adalah"

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

1. Data preparatation yang pertama kali dilakukan adalah pengisian nilai Null dengan unknown
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

2. setelah itu penghapusan kolom yang tidak dipakai dan penentuan fitur kategorinya:

```
df.drop('Unnamed: 0', axis=1, inplace=True)
categorical_features = ['Sex', 'Job', 'Housing', 'Saving accounts', 'Checking account', 'Purpose',]
```

3. selanjutnya adalah pemilihan atribut yang akan digunakan dalam proses modeling:

```
num_df = df[['Age', 'Duration', 'Credit amount']]
num_df.head()
```

pada kasus ini, atribut yang digunakan hanyalah umur, durasi kredit dan jumlah kredit yang di ajukan.

4. setelah pemilihan atribut maka selanjutnya adalah proses scaling data agar range nilai datasetnya tidak terlalu jauh menggunakan library StandarScaler:

```
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
num_df_scaled = scaler.fit_transform(num_df)
```

## Modeling
Model yang dibuat menggunakan metode clustering dengan algoritma K-Means:
1. Tahap pertama pada modeling adalah pendeklarasian model lalu model fitting menggunakan dataset yang sudah di scaling:
```
inertia = []
num_clusters = list(range(1,10))

for k in num_clusters:
    #membuat model dengan range k
    kmeans = KMeans(n_clusters = k, n_init=10)
    #fit model
    kmeans.fit(num_df_scaled)
    #tambahkan SSE dalam klaster k ke dalam daftar
    inertia.append(kmeans.inertia_)
```
2.  selanjutnya mencari nilai K untuk pembagian cluster menggunakan elbow:
```
# mencari elbow spot
cost_kneed = KneeLocator(x = num_clusters , y = inertia , S = 1.0 , curve = 'convex' , direction = 'decreasing' , online = True)
K_cost_c3 = cost_kneed.elbow
print('Elbow at k = {} clusters'.format(K_cost_c3))

#Plot grafik
plt.plot(num_clusters , inertia , 'o-')
plt.xlabel('Number of Clusters')
plt.ylabel('SSE')
#plot garis vertikal di elbow spot
plt.axvline(x=K_cost_c3, color='black', label='axvline-fullheight', ls='--', linewidth=3)
```
![image](https://github.com/Anyu99/UAS_ML1/assets/136258491/ec54ef61-60ec-42f4-9f0b-3a0dfd2a73a3)

berdasarkan hasil pengecekan tersebut dapat dilihat jika cluster terbaik ada pada 3 cluster.

## Evaluation
Evaluasi yang dilakukan dalam proses clustering adalah penggunaan elbow yang mana sudah dilakukan pada proses modeling, cluster optimal yang didapatkan ada pada 3 cluster.

selanjutnya adalah melakukan labeling pada setiap dataset berdasarkan hasil clusternya:
```
df_clustered = df[['Age', 'Duration', 'Credit amount']]
df_clustered['Labels'] = clusters
```
adapun 5 baris pertama setelah dilakukan proses labeling seperti dbawah ini:

![image](https://github.com/Anyu99/UAS_ML1/assets/136258491/25db7791-63fa-4bda-a157-fbaa487c86cf)

lalu dibuat visualisasi pembagian clusternya sesuai dengan cluster yang dibagi yaitu menjadi 3 cluster atau 3 kelompok:

![image](https://github.com/Anyu99/UAS_ML1/assets/136258491/47cb642b-8c8d-4fad-ba2e-5581661ceead)

berdasarkan hasil tersebut dapat dilihat pembagian dataset menjadi 3 kelompok berdasarkan kemiripan dari setiap datanya. terdapat 3 kelompok yang dapat dibedakan berdasarkan warna yang ditampilkan yaitu kuning, hijau dan ungu.

## Deployment
[Aplikasi Pembagian Cluster German Credit Risk](https://uasml1-vdmm8bcsenwixnbjddedi9.streamlit.app/)

1. Sidebar:

![image](https://github.com/Anyu99/UAS_ML1/assets/136258491/93269eb2-de9f-4367-9a2f-688e1290c62e)

didalam sidebar, terdapat slider yang berfungsi untuk memilih berapa cluster dataset akan dibagi.

2. Main Page:

![image](https://github.com/Anyu99/UAS_ML1/assets/136258491/2aa9fe02-4f48-420b-a5cd-fb41f886989e)

pada bagian main page terdapat isi dataset dan juga button fungsi dimana dapat menampilkan visualisasi hasil cluster yang telah diproses oleh sistem

3. Pemilihan tampilan visualisasi hasil cluster:

![image](https://github.com/Anyu99/UAS_ML1/assets/136258491/e351ff62-6942-4e0b-b534-4a9d39855689)

dari 3 pilihan visualisasi tersebut bisa dipilih data apa yang ingin di tampilkan lalu klik button "Proses Klasterisasi Tampilan Plot"

4. contoh hasil visualisasi:

![image](https://github.com/Anyu99/UAS_ML1/assets/136258491/bcc20738-ee2b-416c-a182-4c3ff5d0c207)

![image](https://github.com/Anyu99/UAS_ML1/assets/136258491/2df1ba52-97d5-42a5-b57e-a15676251197)

![image](https://github.com/Anyu99/UAS_ML1/assets/136258491/2b1a6f1f-7bd7-44d7-b573-6862f66c84d0)



