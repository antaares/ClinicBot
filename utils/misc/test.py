# from fpdf import FPDF

# from loader import db





# async def create_diabet_pdf(
#         user_id,
#         diabet_type: str = None,
#         age: str = None,
#         weight: str = None,
#         height: str = None,
#         start_illness: str = None,
#         start_insulin: str = None,
#         age_range: str = None
# ):
#     # ####
#     user = db.select_user(user_id)
#     name, language, phone = user[0], user[1], user[2]
#     # ####
#     pdf = FPDF()
#     pdf.add_page()

#     # Set font
#     pdf.set_font("Arial", size = 12)

#     def add_content(title, content_dict):
#         pdf.cell(200, 10, txt = title, ln=True, align='C')
#         for key, value in content_dict.items():
#             pdf.cell(200, 10, txt = f"{key}: {value}", ln=True)

#     personal_info = {
#         'Ism': name,
#         'telegram_id': user_id,
#         'Tanlangan til': language,
#         'Telefon raqam': phone
#     }

#     illness_info = {
#         'Kasallik': 'Qandli diabet',
#         'Tip': diabet_type,
#         'Yoshi': age,
#         'Vazni': weight,
#         'Boyi': height,
#         'Kasallik boshlangan': start_illness,
#         'Insulin olish boshlangan': start_insulin,
#         'Yosh oraligi': age_range,
#     }
#     # set encoding to utf-8
#     pdf.add_font

#     # Add content 
#     add_content("Ma'lumotlar", personal_info)
#     add_content("Kasalliklar ma'lumotlari", illness_info)

#     filename = f"./Files/{user_id}.pdf"


#     pdf.output(filename)

    


# import requests, json

# def main():
#     api_key = "7832MjA6MTE6UjlkM3h4emxpTExzeFR0aQ="
#     data = {
#       'invoice_number': 'INV38379',
#       'date': '2021-09-30',
#       'currency': 'USD',
#       'total_amount': 82542.56
#     }

#     json_payload = {
#       "data": json.dumps(data) ,
#       "output_file": "output.pdf",
#       "export_type": "json",
#       "expiration": 10,
#       "template_id": "05f77b2b18ad809a"
#     }

#     response = requests.post(
#         F"https://api.craftmypdf.com/v1/create",
#         headers = {"X-API-KEY": F"{api_key}"},
#         json = json_payload
#     )

#     print(response.content)

# if __name__ == "__main__":
#     main()




