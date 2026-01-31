import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

# Step 1: Read data from file
data = pd.read_csv("data.csv")

# Step 2: Analyze data
average_marks = data["Marks"].mean()
highest_marks = data["Marks"].max()
lowest_marks = data["Marks"].min()

# Step 3: Create PDF
pdf = SimpleDocTemplate("Student_Report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("Student Performance Report", styles["Title"]))
elements.append(Spacer(1, 12))

# Summary
elements.append(Paragraph(f"Average Marks: {average_marks:.2f}", styles["Normal"]))
elements.append(Paragraph(f"Highest Marks: {highest_marks}", styles["Normal"]))
elements.append(Paragraph(f"Lowest Marks: {lowest_marks}", styles["Normal"]))
elements.append(Spacer(1, 12))

# Table data
table_data = [list(data.columns)] + data.values.tolist()
table = Table(table_data)

elements.append(table)

# Build PDF
pdf.build(elements)

print("PDF Report Generated Successfully")
