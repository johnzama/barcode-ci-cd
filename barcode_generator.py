import barcode
from barcode.writer import ImageWriter

# Function to generate barcode
def generate_barcode(data, filename):
    EAN = barcode.get_barcode_class('ean13')  # You can choose different formats like 'code128'
    ean = EAN(data, writer=ImageWriter())
    ean.save(filename)
    print(f"Barcode generated and saved as {filename}.png")

if __name__ == "__main__":
    data = input("Enter 12 digits for EAN-13 barcode: ")
    generate_barcode(data, "my_barcode")

