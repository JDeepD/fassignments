from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("./img/logo.png", 10, 10, 200)
        self.set_font("helvetica", "B", 15)
        self.cell(80)
        self.ln(20)

    def chapter_body(self, txt):
        self.ln(90)
        self.add_font(family="jbmono", style="B", fname="./fonts/JetBrainsMono-Bold.ttf", uni=True)
        self.add_font(family="jbmono", style="I", fname="./fonts/JetBrainsMono-Italic.ttf", uni=True)
        self.set_font("jbmono", "B", 18)
        self.multi_cell(0, 7, txt, align="C")
        self.ln()

    def info(self, data: tuple[tuple[str, str],...]):
        self.ln(50)
        line_height = self.font_size * 2
        col_width = self.epw / 4  # distribute content evenly
        for row in data:
            for datum in row:
                self.cell(25)
                self.cell(col_width, line_height, datum, border=0, ln=3)
            self.ln(line_height)

if __name__ == "__main__":
    txt = str("""Aim: blah fjaslkdfjkldsfjd  fdsf""")
    
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.chapter_body(txt)
    data = (
        ("Name", "Jaydeep P Das"),
        ("Scholar ID", "2112095"),
        ("Course", "CS-101"),
        ("Department", "CSE"),
        ("Submitted to", "teacher"),
        ("Date", "25 August 2022"),
    )
    pdf.info(data)
    pdf.output("tuto1.pdf")
