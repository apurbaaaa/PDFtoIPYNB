import fitz  # PyMuPDF
import nbformat as nbf

def pdf_to_ipynb(pdf_path, ipynb_path):
    doc = fitz.open(pdf_path)
    notebook = nbf.v4.new_notebook()
    cells = []

    for page in doc:
        text = page.get_text()
        if text.strip():
            cells.append(nbf.v4.new_markdown_cell(text))

    notebook['cells'] = cells

    with open(ipynb_path, 'w', encoding='utf-8') as f:
        nbf.write(notebook, f)

    print(f"Converted {pdf_path} to {ipynb_path}")

# Example usage
pdf_to_ipynb("topformADNIfinal.pdf", "code.ipynb")
