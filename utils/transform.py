import pandas as pd
import numpy as np
from datetime import datetime
import warnings

# Menonaktifkan peringatan FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)

# Mengaktifkan pengaturan baru sesuai peringatan
pd.set_option('future.no_silent_downcasting', True)

def clean_data(product_list):
    """Membersihkan dan mentransformasi data produk menjadi format yang diinginkan."""
    
    # Mengubah data produk menjadi DataFrame
    df = pd.DataFrame(product_list)

    # Menghapus baris dengan judul yang tidak valid
    df = df[df['title'].str.lower() != 'unknown product']

    # Membersihkan dan mengonversi harga
    df['price'] = df['price'].replace(r'[^\d.]', '', regex=True)
    df['price'] = df['price'].replace('', np.nan)
    df.dropna(subset=['price'], inplace=True)
    df['price'] = df['price'].astype(float) * 16000  # Mengkonversi ke rupiah

    # Membersihkan dan mengonversi rating
    df['rating'] = df['rating'].replace(r'[^0-9.]', '', regex=True)
    df['rating'] = df['rating'].replace('', np.nan)
    df.dropna(subset=['rating'], inplace=True)
    df['rating'] = df['rating'].astype(float)

    # Membersihkan informasi warna (menghapus non-digit)
    df['colors'] = df['colors'].replace(r'\D', '', regex=True)
    df['colors'] = df['colors'].replace('', np.nan)
    df.dropna(subset=['colors'], inplace=True)
    df['colors'] = df['colors'].astype(int)

    # Membersihkan informasi ukuran dan gender
    df['size'] = df['size'].replace(r'Size:\s*', '', regex=True)
    df['gender'] = df['gender'].replace(r'Gender:\s*', '', regex=True)

    # Menghapus baris duplikat dan data yang kosong
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Menambahkan kolom timestamp untuk mencatat waktu pengolahan
    df['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return df