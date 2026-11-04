import os

files = [
    r'C:\Users\Z09057\poker-behavioral-economics\analysis\build_paper_docx.py',
    r'C:\Users\Z09057\poker-behavioral-economics\analysis\build_paper_pdf.py'
]

ref_add_docx = '        "Maurer, M. (1995-2001). The IRC Poker Database. Logged via the Observer program. Hosted and maintained by the Computer Poker Research Group, University of Alberta. URL: https://poker.cs.ualberta.ca/irc_poker_database.html.",\n'
ref_add_pdf = '  <p>Maurer, M. (1995-2001). The IRC Poker Database. Logged via the Observer program. Hosted and maintained by the Computer Poker Research Group, University of Alberta. URL: https://poker.cs.ualberta.ca/irc_poker_database.html.</p>\n'

# Update docx script
with open(files[0], 'r', encoding='utf-8') as f:
    text = f.read()
target_docx = '"Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. Econometrica, 47(2), 263-291.",\n'
if target_docx in text:
    text = text.replace(target_docx, target_docx + ref_add_docx)
    with open(files[0], 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated build_paper_docx.py")

# Update pdf script
with open(files[1], 'r', encoding='utf-8') as f:
    text = f.read()
target_pdf = '<p>Kahneman, D., &amp; Tversky, A. (1979). Prospect theory: An analysis of decision under risk. <em>Econometrica</em>, 47(2), 263-291.</p>\n'
if target_pdf in text:
    text = text.replace(target_pdf, target_pdf + ref_add_pdf)
    with open(files[1], 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated build_paper_pdf.py")
