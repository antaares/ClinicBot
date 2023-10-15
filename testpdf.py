from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont



# create pdf file with function
def create_pdf(
        user_id,
        type: str = None,
        age: str = None,
        weight: str = None,
        height: str = None,
        start_illness: str = None,
        start_insulin: str = None,
        age_range: str = None
):
    from loader import db
    pdf_buffer = BytesIO()
    # Create a PDF document
    pdf = canvas.Canvas(pdf_buffer)
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))

        # Set the font to the registered Cyrillic font
    pdf.setFont('DejaVuSerif', 12)

    # user data
    user = db.select_user(user_id)
    name, language, phone = "Jahongir Ismoilov","Uzbek","998795542" #user[0], user[1], user[2]

    # Add some text to the PDF
    pdf.drawString(200, 750, "Ma'lumotlar")

    pdf.drawString(100, 700, f"Ism: {name}")
    pdf.drawString(100, 670, f"Telegram_id: {user_id}")
    pdf.drawString(100, 640, f"Tanlangan til: {language}")
    pdf.drawString(100, 610, f"Telefon raqam: {phone}")

    pdf.drawString(200, 550, "Ma'lumotlar")

    pdf.drawString(100, 520, "Kasallik:  Qandli diabet")
    pdf.drawString(100, 490, f"Tip: {type}")
    pdf.drawString(100, 460, f"Yoshi: {age}")
    pdf.drawString(100, 430, f"Vazni: {weight}")
    pdf.drawString(100, 400, f"Boyi: {height}")
    pdf.drawString(100, 370, f"Kasallik boshlangan: {start_illness}")
    pdf.drawString(100, 340, f"Insulin olish boshlangan: {start_insulin}")
    pdf.drawString(100, 310, f"Yosh oraligi: {age_range}")



    # Save the PDF to the buffer
    pdf.save()

    # Reset the buffer's position to the beginning
    pdf_buffer.seek(0)

    # Now, you can save the BytesIO object to a file
    with open(f"./files/{user_id}.pdf", "wb") as f:
        f.write(pdf_buffer.read())



def create_pdf_obesity(
        user_id,
        age: str = None,
        weight: str = None,
        height: str = None,
        location: str = None,
):
    from loader import db
    pdf_buffer = BytesIO()
    # Create a PDF document
    pdf = canvas.Canvas(pdf_buffer)
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))

# Set the font to the registered Cyrillic font
    pdf.setFont('DejaVuSerif', 12)

    # user data
    user = db.select_user(user_id)
    name, language, phone = user[0], user[1], user[2]

    # Add some text to the PDF
    pdf.drawString(200, 750, "Ma'lumotlar")

    pdf.drawString(100, 700, f"Ism: {name}")
    pdf.drawString(100, 670, f"Telegram_id: {user_id}")
    pdf.drawString(100, 640, f"Tanlangan til: {language}")
    pdf.drawString(100, 610, f"Telefon raqam: {phone}")

    pdf.drawString(200, 550, "Ma'lumotlar")

    pdf.drawString(100, 520, "Kasallik:  Semizlik(Ortiqcha vazn)")
    pdf.drawString(100, 490, f"Yoshi: {age}")
    pdf.drawString(100, 460, f"Vazni: {weight}")
    pdf.drawString(100, 430, f"Boyi: {height}")
    pdf.drawString(100, 400, f"Manzil: {location}")





    # Save the PDF to the buffer
    pdf.save()

    # Reset the buffer's position to the beginning
    pdf_buffer.seek(0)

    # Now, you can save the BytesIO object to a file
    with open(f"./files/{user_id}.pdf", "wb") as f:
        f.write(pdf_buffer.read())


create_pdf_obesity(5950193177, 20, 70, 170, "Ташкент")