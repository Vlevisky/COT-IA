from reportlab.lib.pagesizes import A4
from reportlab.playtypus import SimpleDocTemplate, Paragraph, Spacer
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

