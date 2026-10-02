from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors

pdf = SimpleDocTemplate("relatorio.pdf", pagesize=A4)

dados = [
    ["Produto", "Quantidade", "Nível"],
    ["Café em Grãos", "12 kg", "Bom"],
    ["Leite", "8 litros", "Atenção"],
    ["Açúcar", "3 kg", "Baixo"],
    ["Copos", "150 unidades", "Bom"],
    ["Guardanapos", "200 unidades", "Bom"]
]

tabela.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.brown),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 1, colors.black)
    ])
)
pdf.build([tabela])

print("PDF gerado")