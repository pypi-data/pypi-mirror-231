import cv2
import os
import sys

def process_image(input_file):
    # Resmi oku
    image = cv2.imread(input_file)

    if image is None:
        print(f"Resim bulunamadı: {input_file}")
        return

    # Resmi siyah-beyaza çevir
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Klasörü oluştur (eğer yoksa)
    os.makedirs("grayimages1", exist_ok=True)

    # Siyah-beyaz resmi kaydet
    output_file = os.path.join("grayimages1", os.path.basename(input_file))
    cv2.imwrite(output_file, gray_image)

def main():
    if len(sys.argv) != 2:
        print("Kullanım: niva source=\"File/Path/example.jpg\"")
        sys.exit(1)

    source = sys.argv[1].split("=")[-1]
    process_image(source)

if __name__ == "__main__":
    main()
