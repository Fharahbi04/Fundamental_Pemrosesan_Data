import pandas as pd
from sqlalchemy import create_engine

def save_to_csv(df: pd.DataFrame, path="products.csv"):
    try:
        df.to_csv(path, index=False)
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def save_to_postgresql(df, table_name='products'):
    """Menyimpan DataFrame ke PostgreSQL database."""
    try:
        # Ganti info berikut dengan konfigurasi PostgreSQL yang sesuai
        username = 'postgres'
        password = '2004'
        host = 'localhost'
        port = '5432'
        database = 'etl_db'

        # Buat koneksi engine SQLAlchemy
        engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')

        # Menyimpan DataFrame ke dalam tabel PostgreSQL (mengganti jika tabel sudah ada)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data berhasil disimpan ke tabel PostgreSQL '{table_name}'.")

    except Exception as e:
        print(f"Gagal menyimpan data ke PostgreSQL: {e}")