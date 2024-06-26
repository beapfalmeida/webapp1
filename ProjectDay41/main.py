from fpdf import FPDF
import pandas

df = pandas.read_csv("articles.csv", dtype={"id": str})
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()


class Article:
    def __init__(self, article_id):
        self.id = article_id
        self.name = df.loc[df["id"] == self.id, "name"].squeeze().title()
        self.price = df.loc[df["id"] == self.id, "price"].squeeze()

    def available(self):
        stock = df.loc[df["id"] == self.id, "in stock"].squeeze()
        return stock


class Receipt:
    def __init__(self, article):
        self.article = article

    def generate(self):
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article.id}", ln=1)
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}")
        pdf.output("receipt.pdf")


print(df)
article_ID = input("Enter the article ID: ")
article = Article(article_ID)

if article.available():
    receipt = Receipt(article)
    receipt.generate()
print(df)
    
