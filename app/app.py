import pdfplumber
from dataclasses import dataclass
from pdfplumber.page import Page
from pdfplumber.table import Table as PdfTable


@dataclass
class Row:
    cells: list[str | None]


@dataclass
class Table:
    rows: list[Row]


def extract_pdf(pdf_path: str) -> list[Table]:
    tables = []
    pdf = pdfplumber.open(pdf_path)
    pages = pdf.pages[:]
    for page in pages:
        page_tables = extract_page(page)
        tables.extend(page_tables)        
    
    return tables


def extract_page(page: Page) -> list[Table]:
    pdf_tables = page.find_tables()
    return [extract_table(pdf_table) for pdf_table in pdf_tables]


def extract_table(pdf_table: PdfTable) -> Table:
    rows = [Row(cells) for cells in pdf_table.extract()]

    return Table(rows)


def find_target_tables(tables: list[Table]) -> list[Table] :
    target_tables = []
    for table in tables:
        for row in table.rows:
            for cell in row.cells:
                if cell and 'Площадь' in cell:
                    target_tables.append(table)
    
    return target_tables
