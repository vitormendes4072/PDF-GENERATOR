from reportlab.pdfgen import canvas


def generate_pdf(list):
    try:
        pdf_name = input("PDF name: ")
        pdf = canvas.Canvas(f"{pdf_name}.pdf")
        x = 720
        for name, age in list.items():
            x -= 20
            pdf.drawString(247, x, f"{name} : {age}")
        pdf.setTitle(pdf_name)
        pdf.setFont("Helvetica-Oblique", 24)
        pdf.drawString(240, 750, "People list")
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(247, 724, "Name and age")
        pdf.save()
        print(f"{pdf_name}.pdf successfuly create!")
    except:
        print(f"Generation error {pdf_name}.pdf")


list = {'Vitor': '19', 'Márcio': '55', 'Elania': '53'}

generate_pdf(list)
