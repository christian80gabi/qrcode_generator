def print_box_label(box_number='', quantity='', description='', order=''):
    # Importing library
    # import os
    import qrcode
    from reportlab.pdfgen import canvas
    from PyPDF2 import PdfFileWriter, PdfFileReader
    # import io

    qrcode_img = 'QRCode.png'
    pdf_file = 'report.pdf'

    # Data to be encoded
    data = (
        (
            (f'Box Number: {str(box_number)}' + '\n' 'Quantity: ')
            + str(quantity)
            + '\n'
            'Description: '
        )
        + str(description)
        + '\n'
        'Order: '
    ) + str(order)


    img = qrcode.make(data)  # Encoding data using make() function
    img.save(qrcode_img)  # Saving as an image file

    # Print data on a PDF file

    # ---------------------------------------------------------------------------------------------
    c = canvas.Canvas(pdf_file)
    c.drawString(20, 750, f"Box Number: {str(box_number)}")
    c.drawString(20, 700, f"Quantity: {str(quantity)}")
    c.drawString(20, 650, f"Description: {str(description)}")
    c.drawString(20, 600, f"Order: {str(order)}")

    c.drawImage(qrcode_img, 10, 150, width=300, preserveAspectRatio=True, mask='auto')
    c.showPage()
    c.save()
    os.startfile(pdf_file)
    # ---------------------------------------------------------------------------------------------

    #import a module
    from fpdf import FPDF

    pdf = FPDF()

    # Adding a page
    pdf.add_page()

    # set style and size of font 
    pdf.set_font("Arial", size = 50)

    # create cells
    pdf.cell(200, 30, txt = "Ticket", ln = 1, align = 'C')

    pdf.set_font("Arial", size = 15)
    pdf.cell(200, 10, txt=f"Box Number: {str(box_number)}", ln = 2, align = 'L')
    pdf.cell(200, 10, txt=f"Quantity: {str(quantity)}", ln = 3, align = 'L')
    pdf.cell(200, 10, txt=f"Description: {str(description)}", ln = 4, align = 'L')
    pdf.cell(200, 10, txt=f"Order: {str(order)}", ln = 5, align = 'L')

    # add another cell
    pdf.image(qrcode_img, w = 120)

    # save the pdf
    pdf.output(pdf_file)


if __name__ == "__main__":
    print_box_label(box_number='HGHJH868YGH', quantity=12, description='Vente du 30 octobre', order='BUY7YHOJGFJH')
    print('Done')
