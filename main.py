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
    data = 'Box Number: ' + str(box_number) + '\n'\
           'Quantity: ' + str(quantity) +  '\n'\
           'Description: ' + str(description) + '\n'\
           'Order: ' + str(order)

    img = qrcode.make(data)  # Encoding data using make() function
    img.save(qrcode_img)  # Saving as an image file

    # Print data on a PDF file

    # ---------------------------------------------------------------------------------------------
    # c = canvas.Canvas(pdf_file)
    # c.drawString(10, 200, "Box Number: " + str(box_number))
    # c.drawString(10, 210, "Quantity: " + str(quantity))
    # c.drawString(10, 220, "Description: " + str(description))
    # c.drawString(10, 240, "Order: " + str(order))
    # c.save()
    # os.startfile(pdf_file)

    # # Add image
    # in_pdf_file = pdf_file
    # out_pdf_file = 'image_' + pdf_file
    # img_file = qrcode_img
 
    # packet = io.BytesIO()
    # can = canvas.Canvas(packet)
    # x_start = 0
    # y_start = 0
    # can.drawImage(img_file, x_start, y_start, width=120, preserveAspectRatio=True, mask='auto')
    # can.showPage()
    # can.showPage()
    # can.showPage()
    # can.save()
 
    # #move to the beginning of the StringIO buffer
    # packet.seek(0)
 
    # new_pdf = PdfFileReader(packet)
 
    # # read the existing PDF
    # existing_pdf = PdfFileReader(open(in_pdf_file, "rb"))
    # output = PdfFileWriter()
 
    # for i in range(len(existing_pdf.pages)):
    #     page = existing_pdf.getPage(i)
    #     page.mergePage(new_pdf.getPage(i))
    #     output.addPage(page)
 
    # outputStream = open(out_pdf_file, "wb")
    # output.write(outputStream)
    # outputStream.close()
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
    pdf.cell(200, 10, txt = "Box Number: " + str(box_number), ln = 2, align = 'L')
    pdf.cell(200, 10, txt = "Quantity: " + str(quantity), ln = 3, align = 'L')
    pdf.cell(200, 10, txt = "Description: " + str(description), ln = 4, align = 'L')
    pdf.cell(200, 10, txt = "Order: " + str(order), ln = 5, align = 'L')
    
    # add another cell
    pdf.image(qrcode_img, w = 120)
    
    # save the pdf
    pdf.output(pdf_file)


if __name__ == "__main__":
    print_box_label(box_number='HGHJH868YGH', quantity=12, description='Vente du 30 octobre', order='BUY7YHOJGFJH')
    print('Done')
