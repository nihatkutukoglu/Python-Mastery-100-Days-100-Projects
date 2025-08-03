# --- PDF TO DOCX ---

from pdf2docx import converter

pdf_path = "sample.pdf"
docx_path = "sample.docx"

cv = converter(pdf_file= pdf_path)
cv.convert(docx_filename=docx_path)
cv.close()



