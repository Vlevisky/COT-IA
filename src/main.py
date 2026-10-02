from reportlab.lib.pagesizes import A4
from reportlab.playtypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib import colors

pdf = SimpleDocTemplate("relatorio.pdf", pagesize=A4)
