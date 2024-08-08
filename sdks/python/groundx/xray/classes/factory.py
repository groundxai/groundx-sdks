# coding: utf-8


from typing import Optional

from groundx.xray.classes.filetypes.csv_ft import XRayCSV
from groundx.xray.classes.filetypes.docx_ft import XRayDOCX
from groundx.xray.classes.filetypes.jpg_ft import XRayJPG
from groundx.xray.classes.filetypes.json_ft import XRayJSON
from groundx.xray.classes.filetypes.pdf_ft import XRayPDF
from groundx.xray.classes.filetypes.png_ft import XRayPNG
from groundx.xray.classes.filetypes.pptx_ft import XRayPPTX
from groundx.xray.classes.filetypes.tsv_ft import XRayTSV
from groundx.xray.classes.filetypes.txt_ft import XRayTXT
from groundx.xray.classes.filetypes.xlsx_ft import XRayXLSX
from groundx.xray.classes.filetypes.filetype import FileType
from groundx.xray.classes.document import XRayDocument


def create_xray_document(file_path: str) -> Optional[XRayDocument]:
    xray_document = XRayDocument(file_path)

    if xray_document.file_type == FileType.CSV:
        return XRayCSV(file_path)
    elif xray_document.file_type == FileType.DOCX:
        return XRayDOCX(file_path)
    elif xray_document.file_type == FileType.JPG:
        return XRayJPG(file_path)
    elif xray_document.file_type == FileType.JSON:
        return XRayJSON(file_path)
    elif xray_document.file_type == FileType.PDF:
        return XRayPDF(file_path)
    elif xray_document.file_type == FileType.PNG:
        return XRayPNG(file_path)
    elif xray_document.file_type == FileType.PPTX:
        return XRayPPTX(file_path)
    elif xray_document.file_type == FileType.TSV:
        return XRayTSV(file_path)
    elif xray_document.file_type == FileType.TXT:
        return XRayTXT(file_path)
    elif xray_document.file_type == FileType.XLSX:
        return XRayXLSX(file_path)
