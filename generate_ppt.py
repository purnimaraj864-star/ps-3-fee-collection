import os
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt

# Paths
base_path = Path('/Users/purnimaraj/Downloads/PS3-FeeCollection')
output_path = base_path / 'PS3_FeeCollection_Overview.pptx'

prs = Presentation()

# Define corporate style (dark background, white text)
# We'll use a simple title layout and add shapes manually.

def add_title_slide(title, subtitle):
    slide_layout = prs.slide_layouts[0]  # Title Slide
    slide = prs.slides.add_slide(slide_layout)
    slide.shapes.title.text = title
    slide.placeholders[1].text = subtitle
    # Apply corporate formatting
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        tf = shape.text_frame
        for p in tf.paragraphs:
            for run in p.runs:
                run.font.name = 'Calibri'
                run.font.size = Pt(32) if shape == slide.shapes.title else Pt(24)
                run.font.bold = True
        

def add_content_slide(title, bullet_points=None, image_path=None):
    slide_layout = prs.slide_layouts[5]  # Title Only
    slide = prs.slides.add_slide(slide_layout)
    title_shape = slide.shapes.title
    title_shape.text = title
    tf = title_shape.text_frame
    tf.paragraphs[0].font.name = 'Calibri'
    tf.paragraphs[0].font.size = Pt(28)
    tf.paragraphs[0].font.bold = True

    left = Inches(0.5)
    top = Inches(1.5)
    width = Inches(9)
    height = Inches(5)
    if bullet_points:
        txBox = slide.shapes.add_textbox(left, top, width, height)
        tf = txBox.text_frame
        tf.word_wrap = True
        for point in bullet_points:
            p = tf.add_paragraph()
            p.text = point
            p.font.name = 'Calibri'
            p.font.size = Pt(18)
            p.level = 0
    if image_path:
        img = Path(image_path)
        if img.is_file():
            slide.shapes.add_picture(str(img), Inches(5), Inches(1.5), width=Inches(4))

# Slide 1: Title
add_title_slide('PS3 Fee Collection', 'Automated Fee Management System')

# Slide 2: Project Overview
overview_text = [
    'A web‑based solution for managing student fee payments.',
    'Provides secure login, fee tracking, receipt generation, and admin dashboards.',
    'Designed for schools/colleges to streamline financial operations.'
]
add_content_slide('Project Overview', overview_text)

# Slide 3: Architecture
arch_text = [
    'Frontend: React (SPA) communicating with REST APIs.',
    'Backend: Node.js + Express with MongoDB for data persistence.',
    'Authentication via JWT, logging with Winston, environment config via dotenv.'
]
add_content_slide('Architecture Overview', arch_text)

# Slide 4: Key Features
features = [
    '🔐 Secure user authentication and role‑based access.',
    '📊 Real‑time dashboard for fee statistics.',
    '🧾 Automated receipt generation (PDF).',
    '💳 Online payment integration.',
    '🛠️ Admin panel for managing students, fees, and payments.'
]
add_content_slide('Key Features', features)

# Slide 5: UI Screenshots (show login and dashboard)
# We'll place two images side by side.
slide_layout = prs.slide_layouts[5]
slide = prs.slides.add_slide(slide_layout)
slide.shapes.title.text = 'Application UI Snapshots'
# Add login screenshot
login_path = base_path / 'screenshot-login.png'
if login_path.is_file():
    slide.shapes.add_picture(str(login_path), Inches(0.5), Inches(1.5), width=Inches(4))
# Add dashboard screenshot
dash_path = base_path / 'screenshot-dashboard.png'
if dash_path.is_file():
    slide.shapes.add_picture(str(dash_path), Inches(5), Inches(1.5), width=Inches(4))

# Slide 6: Technologies Used
tech = [
    'Frontend: React, JavaScript, HTML5, CSS3',
    'Backend: Node.js, Express.js',
    'Database: MongoDB',
    'Auth: JWT, bcrypt',
    'Styling: Bootstrap (custom corporate theme)',
    'Tools: Git, Docker (optional), npm'
]
add_content_slide('Technologies Used', tech)

# Save presentation
prs.save(str(output_path))
print(f'Presentation saved to {output_path}')
