from fpdf import FPDF

def main():

    name = str(input("name: "))

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    pdf.set_font("helvetica",style="",size=40)
    pdf.set_stretching(106)
    pdf.cell(w=0, h=50, text="CS50 Shirtificate", align="C")
    pdf.set_stretching(100)
    pdf.image("shirtificate.png", x=20,y=60,w=170)
    pdf.set_text_color(255,255,255)
    pdf.set_font("helvetica",style="",size=18)
    pdf.set_xy(x=10,y=100)
    pdf.cell(w=0, h=40, text=f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
