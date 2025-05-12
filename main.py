from utils.extract import fetch_product_data
from utils.transform import clean_data
from utils.load import save_to_csv,save_to_postgresql

def main():
    base_url = 'https://fashion-studio.dicoding.dev/'
    all_products = []

    print(f"Memulai scraping halaman utama: {base_url}")
    try:
        products = fetch_product_data(base_url)
        all_products.extend(products)
    except Exception as e:
        print(f" Gagal scraping halaman utama: {e}")

    # Scrape halaman 2 hingga 50
    for page_number in range(2, 51):
        page_url = f"{base_url}page{page_number}"
        print(f"Scraping halaman {page_number}: {page_url}")
        try:
            products = fetch_product_data(page_url)
            all_products.extend(products)
        except Exception as e:
            print(f"Gagal scraping halaman {page_number}: {e}")

    if not all_products:
        print(" Tidak ada produk yang berhasil di-scrape. Program dihentikan.")
        return

    # Transformasi data hasil scraping
    transformed_data = clean_data(all_products)

    # Menyimpan hasil ke berbagai tujuan
    save_to_csv(transformed_data)
    save_to_postgresql(transformed_data)

if __name__ == '__main__':
    main()