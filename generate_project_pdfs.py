"""
generate_project_pdfs.py
─────────────────────────
Generates one-page, non-confidential project summary PDFs for the portfolio
site: assets/central-migration-assistant.pdf and assets/cnx-ticket-analyzer.pdf

Run:
    /Users/vishallokhande/Aruba-Central-mcp:/.venv/bin/python3 generate_project_pdfs.py
"""

import os

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, HRFlowable,
)

ACCENT = colors.HexColor("#0f9e8e")
ACCENT_2 = colors.HexColor("#5b7fd6")
DARK = colors.HexColor("#12161d")
DIM = colors.HexColor("#5a6472")

OUT_DIR = os.path.join(os.path.dirname(__file__), "assets")

styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    "TitleStyle", parent=styles["Title"], textColor=DARK, fontSize=22,
    spaceAfter=4, alignment=TA_LEFT,
)
tag_style = ParagraphStyle(
    "TagStyle", parent=styles["Normal"], textColor=ACCENT, fontSize=11,
    spaceAfter=14, alignment=TA_LEFT,
)
body_style = ParagraphStyle(
    "BodyStyle", parent=styles["Normal"], textColor=DARK, fontSize=10.5,
    leading=16, spaceAfter=12, alignment=TA_LEFT,
)
h2_style = ParagraphStyle(
    "H2Style", parent=styles["Heading2"], textColor=ACCENT_2, fontSize=13,
    spaceBefore=6, spaceAfter=8,
)
bullet_style = ParagraphStyle(
    "BulletStyle", parent=styles["Normal"], textColor=DARK, fontSize=10,
    leading=15,
)
footer_style = ParagraphStyle(
    "FooterStyle", parent=styles["Normal"], textColor=DIM, fontSize=8.5,
)


def build_pdf(filename, title, tag, summary, highlights, stack):
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, filename)
    doc = SimpleDocTemplate(
        path, pagesize=letter,
        topMargin=0.9 * inch, bottomMargin=0.8 * inch,
        leftMargin=0.9 * inch, rightMargin=0.9 * inch,
    )
    story = [
        Paragraph(title, title_style),
        Paragraph(tag, tag_style),
        HRFlowable(width="100%", color=colors.HexColor("#dfe4ea"), thickness=1),
        Spacer(1, 14),
        Paragraph("Overview", h2_style),
        Paragraph(summary, body_style),
        Paragraph("Highlights", h2_style),
        ListFlowable(
            [ListItem(Paragraph(h, bullet_style), bulletColor=ACCENT) for h in highlights],
            bulletType="bullet", start="•", leftIndent=14,
        ),
        Spacer(1, 14),
        Paragraph("Tech Stack", h2_style),
        Paragraph(stack, body_style),
        Spacer(1, 24),
        HRFlowable(width="100%", color=colors.HexColor("#dfe4ea"), thickness=1),
        Spacer(1, 8),
        Paragraph(
            "Vishal Lokhande &middot; vishallokhande.com &middot; No customer, "
            "tenant, or proprietary data is included in this summary.",
            footer_style,
        ),
    ]
    doc.build(story)
    print(f"Wrote {path}")


build_pdf(
    filename="central-migration-assistant.pdf",
    title="Aruba Central Migration Assistant",
    tag="CLI / Classic Central → New Central · Migration Readiness Tool",
    summary=(
        "A migration readiness tool that connects to an Aruba Central tenant, discovers the "
        "full deployment, and produces a comprehensive migration plan without pushing any "
        "changes. It bridges legacy CLI-based configuration templates and the newer Element "
        "Profiles model, using a deterministic multi-phase pipeline to map every CLI "
        "configuration block to its equivalent profile and classify scope across a five-level "
        "hierarchy (Global &rarr; Site Collection &rarr; Site &rarr; Device Group &rarr; Device)."
    ),
    highlights=[
        "Validated against large-scale production-style deployments (100K+ devices, 700+ groups)",
        "Full tenant discovery completes in roughly 12 minutes using an optimized API call pipeline",
        "Deduplicates near-identical templates down to a smaller set of unique profiles",
        "Generates a multi-tab migration intelligence report: inventory, mapping, compatibility, risk, and strategy",
        "Read-only by design &mdash; write/push operations are disabled by default",
    ],
    stack="Python, FastAPI, TextFSM (CLI parsing), regex + deterministic rule mapping, React frontend, Aruba Central REST API.",
)

build_pdf(
    filename="cnx-ticket-analyzer.pdf",
    title="CNX Ticket Analyzer",
    tag="Support Operations · Ticket &amp; Issue Cross-Referencing Tool",
    summary=(
        "A local-first analytics tool that cross-references customer support tickets with "
        "engineering issue-tracker entries, surfacing patterns across product component, "
        "technology area, and regression trends. It supports both a point-in-time workbook "
        "view and a live-query mode against a self-hosted issue tracker, so findings can be "
        "either a snapshot or always current &mdash; all processing happens on the user's own "
        "machine, and no data is uploaded to any third party."
    ),
    highlights=[
        "Cross-references two independent ticket data sources entirely on-device",
        "KPI dashboard summarizing ticket volume by customer, component, and technology area",
        "Optional live-query mode against a self-hosted issue tracker via a personal access token",
        "Multi-select filtering (component, label, status, priority, severity) compiled into a query client-side",
        "Paginated browsing with a safety-capped export so large result sets stay manageable",
    ],
    stack="Python, FastAPI, pandas (workbook analysis), REST API integration, vanilla JS frontend.",
)
