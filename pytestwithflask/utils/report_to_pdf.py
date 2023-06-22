
import pdfkit

pdfkit.from_file('reports/report.html', 'reports/report.pdf',
                 css='reports/assets/style.css', verbose=False)
