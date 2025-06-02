import subprocess, os

def export_html_to_pdf(html_path: str, output_path: str):
    """Convert HTML report to PDF using wkhtmltopdf if available."""
    try:
        subprocess.run(["wkhtmltopdf", html_path, output_path], check=True, capture_output=True)
        print(f"PDF saved: {output_path}")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("wkhtmltopdf not available — install it or use a headless browser alternative.")
