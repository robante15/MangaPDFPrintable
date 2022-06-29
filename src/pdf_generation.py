from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from src.split_list import SplitList

# Set general variables
landscape_mode = True
paper_w, paper_h = 210, 297
# Dr Stone
#manga_size_w, manga_size_h = 114, 178
# Sono Bisque Doll
#manga_size_w, manga_size_h = 146, 210
# The Quintessential Quintuplets
#manga_size_w, manga_size_h = 127, 191
# SpyXFamily
#manga_size_w, manga_size_h = 130, 180
# Plunderer
#manga_size_w, manga_size_h = 145, 208
# Initial D
manga_size_w, manga_size_h = 127, 197
margin, padding = 4.65, 5
width, height = A4

class PDFGeneration():
    # Single/Double, Nombre del archivo izq, Nombre del archivo derecha, Margen, Linea de doblez
    def add_double_page(pdf: canvas.Canvas, left_page, right_page, draw_margin=True, draw_fold_line=True, UNOCUATRO=True):
        # Añade un margen a las páginas que podría funcionar como guía de corte
        if draw_margin:
            pdf.rect(((paper_w/2)-(padding/2)-manga_size_w)*mm, ((paper_h/2) -
                    (manga_size_h/2))*mm, manga_size_w*mm, manga_size_h*mm)

            pdf.rect(((paper_w/2)+(padding/2))*mm, ((paper_h/2) -
                    (manga_size_h/2))*mm, manga_size_w*mm, manga_size_h*mm)

        if UNOCUATRO == True:
            pdf.drawString(40*mm, 7*mm, 'UNO')
            pdf.drawString(240*mm, 7*mm, 'CUATRO')
        else:
            pdf.drawString(40*mm, 7*mm, 'TRES')
            pdf.drawString(240*mm, 7*mm, 'DOS')

        # Añade una linea que indica el centro de la página, donde se va a realizar el doblez
        if draw_fold_line:
            pdf.line((paper_w/2)*mm, ((paper_h/2)-(manga_size_h/2))*mm,
                    (paper_w/2)*mm, ((paper_h/2)+(manga_size_h/2))*mm)

        # Agrega la pagina izquierda y derecha
        pdf.drawImage(left_page, ((paper_w/2)-(padding/2)-manga_size_w)*mm, ((paper_h/2)-(manga_size_h/2))*mm,
                    manga_size_w*mm, manga_size_h*mm)

        pdf.drawImage(right_page, ((paper_w/2)+(padding/2))*mm,
                    ((paper_h/2)-(manga_size_h/2))*mm, manga_size_w*mm, manga_size_h*mm)

        pdf.showPage()


    def add_single_page(pdf: canvas.Canvas, page, draw_margin=True):
        if draw_margin:
            pdf.rect(((paper_w/2)-(padding/2)-manga_size_w)*mm, ((paper_h/2)-(manga_size_h/2))*mm, manga_size_w *
                    2*mm+padding*mm, manga_size_h*mm)

        pdf.drawImage(page, ((paper_w/2)-(padding/2)-manga_size_w)*mm, ((paper_h/2)-(manga_size_h/2))*mm,
                    manga_size_w*2*mm+padding*mm, manga_size_h*mm)
        pdf.showPage()


    def makepdf(source_list : list, pdf_name: str = 'default.pdf'):
        """Genera un PDF a partir de los archivos de imagen contenidos dentro de un folder, ordenandolos para facilitar su impresión

        Args:
            pdf_name (str, optional): Nombre del archivo pdf a generar. Defaults to 'default.pdf'.
            source_folder (str, optional): Directorio de origen de los archivos. Defaults to 'input'.
        """
        pdf = canvas.Canvas('output/'+pdf_name, pagesize=A4)

        if(landscape_mode):
            canvas.Canvas.setPageSize(pdf, (landscape(A4)))
            global width, height
            global paper_w, paper_h
            width, height = landscape(A4)
            paper_w, paper_h = 297, 210
        listado_chunks = SplitList.order_list(source_list)

        for chunk in listado_chunks:
            PDFGeneration.add_double_page(pdf, chunk[0][1]+'/'+chunk[0][0], chunk[1][1]+'/'+chunk[1][0], True, True, True)
            PDFGeneration.add_double_page(pdf, chunk[2][1]+'/'+chunk[2][0], chunk[3][1]+'/'+chunk[3][0], True, True, False)

        pdf.save()

