from fpdf import FPDF

def main():
    inp = input("Name: ").strip()
    shirtificate(inp)

def shirtificate(name):
    pdf = FPDF(orientation= "portrait", format ="A4")
    pdf.add_page()
    pdf.set_font('helvetica', size=48)
    cell_width = pdf.w - 2 * pdf.l_margin
    pdf.cell(cell_width, 50, "CS50 Shirtificate", align="C")
    pdf.set_xy(10, 70)
    pdf.image("shirtificate.png", w=cell_width, h=190)
    pdf.set_xy(10, 120)
    pdf.set_font('helvetica', size=25)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(cell_width, 20, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
