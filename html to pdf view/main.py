import pdfkit
import os


def html_to_pdf(html_file_path: str, output_pdf_path: str = "output.pdf") -> str:
    """
    converts an HTML file (with inline CSS) to a pdf file.
    """
    if not os.path.exists(html_file_path):
        raise FileNotFoundError(f"HTML file {html_file_path} not found.")

    config = None
    
    pdfkit.from_file(html_file_path, output_pdf_path)
    return output_pdf_path

if __name__ == "__main__":
    pdf_path = html_to_pdf("html to pdf view/index.html", "styled_output.pdf")
    print(f"Pdf Generated: {pdf_path}")
