from PyPDF2 import PdfReader, PdfWriter

def encrypt_pdf(input_pdf: str, output_pdf: str, password: str):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)
    
    writer.encrypt(password)
    
    with open(output_pdf, 'wb') as out_file:
        writer.write(out_file)
    
    print(f"Encrypted PDF saved as: {output_pdf}")
