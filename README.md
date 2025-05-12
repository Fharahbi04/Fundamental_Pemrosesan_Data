# Submission Dicoding Fundamental Pemrosesan Data

Proyek ini merupakan bagian dari submission kelas **Fundamental Pemrosesan Data** di Dicoding. Proyek ini melakukan proses ETL (Extract, Transform, Load) terhadap data produk fashion dari situs [Fashion Studio Dicoding](https://fashion-studio.dicoding.dev/).  
Data diambil dari halaman 1 hingga 50, kemudian dibersihkan dan disimpan ke berbagai tujuan.

## Struktur Proyek
```
├── main.py
├── utils/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
├── tests/
│ ├── test_extract.py
│ ├── test_transform.py
│ └── test_load.py
├── products.csv
└── README.md
```
## Fitur 
- **Extract**: Mengambil data produk dari situs menggunakan `requests` dan `BeautifulSoup`.
- **Transform**: Membersihkan dan memformat data menggunakan `pandas`.
- **Load**: Menyimpan data hasil scraping ke:
  - File CSV (`products.csv`)
  - PostgreSQL Database

## Cara Menjalankan
### Jalankan Proses ETL
```
python main.py
```
### Jalankan Unit Test
```
python -m unittest discover tests
```
### Jalankan Test Coverage
```
coverage run -m unittest discover tests
```
### Report Coverage
```
coverage report -m
```

## Konfigurasi Database
Edit bagian load_to_postgresql() di utils/load.py agar sesuai dengan konfigurasi  Anda:
```
username = 'postgres'
password = '2004'
host = 'localhost'
port = '5432'
database = 'etl_db'
```

## Pembuat
- Nama :  Muhammad Fharahbi Fachri
- Email : fharahbi04@gmail.com


