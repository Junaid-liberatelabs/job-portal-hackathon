from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import Response, HTMLResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Annotated
import base64
import platform
import html

from app.auth.dependencies import get_current_user
from app.db.session import get_db
from app.db.model.user import User
from app.core.logging_config import get_logger
from app.api.schemas.user import UserResponse
from app.api.schemas.job import JobResponse
from app.db.crud.application import get_applications_by_user
from app.db.crud.job import get_job_by_id
from app.llm.workflow.cv_generation.graph import cv_generation_graph
from app.services.latex_compilation import compile_latex_to_pdf

router = APIRouter()
logger = get_logger(__name__)


@router.get("/cv-export")
async def export_cv(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db),
    format: str = Query("pdf", description="Output format: 'pdf' for download, 'html' for web preview, 'latex' for LaTeX source, or 'latex-view' for LaTeX viewer")
) -> Response:
    """
    Export the authenticated user's profile and job applications as a CV document.
    
    Args:
        current_user: The authenticated user (injected by dependency)
        db: Database session (injected by dependency)
        format: Output format:
            - 'pdf' (default): PDF download (falls back to LaTeX if compilation fails)
            - 'html': HTML page with embedded PDF viewer (falls back to LaTeX if compilation fails)
            - 'latex': LaTeX source code directly (download)
            - 'latex-view': HTML page with LaTeX source viewer (syntax highlighting, copy, compile options)
        
    Returns:
        Response containing:
        - PDF document (application/pdf) when format='pdf' and compilation succeeds
        - HTML page with embedded PDF viewer when format='html' and compilation succeeds
        - LaTeX source (application/x-latex) when format='latex' or when compilation fails
        
    Raises:
        HTTPException: 401 if user is not authenticated (handled by dependency)
        HTTPException: 500 if there's an error generating the CV
    """
    try:
        # Compile the graph
        graph = cv_generation_graph.compile()
        
        # Convert user model to dict with all available data
        user_profile_data = UserResponse.model_validate(current_user).model_dump()
        
        # Get all applications for the user
        applications = get_applications_by_user(db, current_user.id)
        
        # Extract job IDs and get job details
        job_ids = [application.job_id for application in applications]
        jobs = [get_job_by_id(db, job_id) for job_id in job_ids]
        
        # Filter out None jobs (in case a job was deleted) and convert to dicts
        user_applied_job_data = [
            JobResponse.model_validate(job).model_dump() 
            for job in jobs 
            if job is not None
        ]
        
        # Prepare input data for the graph
        input_data = {
            "user_profile_data": user_profile_data,
            "user_applied_job_data": user_applied_job_data,
        }
        
        # Invoke the graph to generate LaTeX CV
        result = graph.invoke(input_data)
        latex_cv = result["latex_cv"]
        
        # If format is latex, return LaTeX source directly
        if format.lower() == "latex":
            return Response(
                content=latex_cv,
                media_type="application/x-latex",
                headers={"Content-Disposition": "attachment; filename=cv.tex"}
            )
        
        # If format is latex-view, return HTML page with LaTeX viewer
        if format.lower() == "latex-view":
            # Escape LaTeX content for HTML
            escaped_latex = html.escape(latex_cv)
            
            html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CV LaTeX Source</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: #1e1e1e;
            color: #d4d4d4;
            padding: 20px;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: #252526;
            border-radius: 8px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }}
        .header {{
            background: #2d2d30;
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
            border-bottom: 1px solid #3e3e42;
        }}
        .header h1 {{
            font-size: 24px;
            font-weight: 600;
            color: #ffffff;
        }}
        .button-group {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .btn {{
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.3s;
            color: white;
        }}
        .btn-primary {{
            background: #007acc;
        }}
        .btn-primary:hover {{
            background: #005a9e;
        }}
        .btn-success {{
            background: #28a745;
        }}
        .btn-success:hover {{
            background: #218838;
        }}
        .btn-secondary {{
            background: #6c757d;
        }}
        .btn-secondary:hover {{
            background: #5a6268;
        }}
        .code-container {{
            position: relative;
            background: #1e1e1e;
            overflow: auto;
            max-height: calc(100vh - 120px);
        }}
        pre {{
            margin: 0;
            padding: 20px;
            overflow-x: auto;
        }}
        code {{
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            font-size: 14px;
            line-height: 1.6;
        }}
        .info-banner {{
            background: #264f78;
            color: #ffffff;
            padding: 15px 20px;
            border-left: 4px solid #007acc;
            margin: 0;
        }}
        .info-banner p {{
            margin: 5px 0;
            font-size: 14px;
        }}
        .info-banner a {{
            color: #4fc3f7;
            text-decoration: underline;
        }}
        @media (max-width: 768px) {{
            body {{
                padding: 10px;
            }}
            .header {{
                flex-direction: column;
                text-align: center;
            }}
            .button-group {{
                width: 100%;
                justify-content: center;
            }}
            .btn {{
                flex: 1;
                min-width: 120px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📄 CV LaTeX Source</h1>
            <div class="button-group">
                <button class="btn btn-primary" onclick="copyToClipboard()">📋 Copy LaTeX</button>
                <button class="btn btn-secondary" onclick="downloadLatex()">💾 Download .tex</button>
                <button class="btn btn-success" onclick="openInOverleaf()">🚀 Open in Overleaf</button>
            </div>
        </div>
        <div class="info-banner">
            <p><strong>💡 Tip:</strong> You can copy this LaTeX code and compile it using:</p>
            <p>• <a href="https://www.overleaf.com" target="_blank">Overleaf</a> (online LaTeX editor) • MiKTeX/TeX Live (local compilation) • Any LaTeX editor</p>
        </div>
        <div class="code-container">
            <pre><code class="language-latex">{escaped_latex}</code></pre>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
    <script>
        // Initialize Prism for syntax highlighting
        Prism.plugins.autoloader.languages_path = 'https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/';
        
        function copyToClipboard() {{
            const latexCode = document.querySelector('code.language-latex').textContent;
            navigator.clipboard.writeText(latexCode).then(function() {{
                const btn = event.target;
                const originalText = btn.textContent;
                btn.textContent = '✅ Copied!';
                btn.style.background = '#28a745';
                setTimeout(function() {{
                    btn.textContent = originalText;
                    btn.style.background = '#007acc';
                }}, 2000);
            }}, function(err) {{
                alert('Failed to copy: ' + err);
            }});
        }}
        
        function downloadLatex() {{
            const latexCode = document.querySelector('code.language-latex').textContent;
            const blob = new Blob([latexCode], {{ type: 'application/x-latex' }});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'cv.tex';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }}
        
        function openInOverleaf() {{
            // Copy to clipboard first, then open Overleaf
            const latexCode = document.querySelector('code.language-latex').textContent;
            navigator.clipboard.writeText(latexCode).then(function() {{
                window.open('https://www.overleaf.com/project', '_blank');
                alert('LaTeX code copied to clipboard! Paste it into the new Overleaf project.');
            }}, function(err) {{
                window.open('https://www.overleaf.com/project', '_blank');
                alert('Please copy the LaTeX code manually and paste it into Overleaf.');
            }});
        }}
    </script>
</body>
</html>
            """
            return HTMLResponse(content=html_content)
        
        # Compile LaTeX to PDF
        pdf_bytes = None
        compilation_error = None
        try:
            pdf_bytes = compile_latex_to_pdf(latex_cv)
        except RuntimeError as e:
            compilation_error = str(e)
            logger.warning(f"LaTeX compilation failed, will return LaTeX source as fallback: {e}")
            # If compilation fails and format is pdf/html, we'll fall back to LaTeX source
        
        # If compilation failed and format requires PDF, return LaTeX source with error message
        if pdf_bytes is None:
            if format.lower() in ["pdf", "html"]:
                system = platform.system()
                if system == "Windows":
                    error_message = (
                        "PDF compilation failed: LaTeX compiler (pdflatex) not found on Windows.\n\n"
                        "To install LaTeX on Windows:\n"
                        "1. Download MiKTeX from: https://miktex.org/download\n"
                        "   - Choose the 'Basic MiKTeX Installer' (smaller, ~150MB) or 'Complete MiKTeX Installer' (~4GB)\n"
                        "   - Run the installer and follow the setup wizard\n"
                        "   - IMPORTANT: Check 'Add MiKTeX to PATH' during installation\n"
                        "   - After installation, restart your terminal/command prompt and the FastAPI server\n\n"
                        "2. Alternative: Install TeX Live from: https://www.tug.org/texlive/windows.html\n\n"
                        "After installation, verify by running: pdflatex --version\n\n"
                        "Returning LaTeX source instead. You can compile it manually using an online LaTeX editor "
                        "(like Overleaf) or use format=latex to get the source directly."
                    )
                elif system == "Linux":
                    error_message = (
                        "PDF compilation failed: LaTeX compiler (pdflatex) not found on Linux.\n\n"
                        "Install with: sudo apt-get install texlive-latex-base texlive-latex-extra texlive-fonts-recommended\n\n"
                        "Returning LaTeX source instead. You can compile it manually or use format=latex to get the source directly."
                    )
                elif system == "Darwin":  # macOS
                    error_message = (
                        "PDF compilation failed: LaTeX compiler (pdflatex) not found on macOS.\n\n"
                        "Install with: brew install --cask mactex\n"
                        "Or download MacTeX from: https://www.tug.org/mactex/\n\n"
                        "Returning LaTeX source instead. You can compile it manually or use format=latex to get the source directly."
                    )
                else:
                    error_message = (
                        "PDF compilation failed: LaTeX compiler (pdflatex) not found.\n\n"
                        "Please install a LaTeX distribution:\n"
                        "- Windows: MiKTeX (https://miktex.org/download) or TeX Live\n"
                        "- Linux: sudo apt-get install texlive-latex-base texlive-latex-extra\n"
                        "- macOS: brew install --cask mactex\n\n"
                        "Returning LaTeX source instead. You can compile it manually or use format=latex to get the source directly."
                    )
                logger.error(f"LaTeX compilation error: {compilation_error}")
                # Return LaTeX source with error info in comments
                latex_with_error = f"% ERROR: {compilation_error}\n% {error_message}\n\n{latex_cv}"
                return Response(
                    content=latex_with_error,
                    media_type="application/x-latex",
                    headers={
                        "Content-Disposition": "attachment; filename=cv.tex",
                        "X-Compilation-Error": "true"
                    }
                )
        
        # Return based on format parameter
        if format.lower() == "html":
            # Encode PDF as base64 for embedding in HTML
            pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
            
            # Create HTML page with embedded PDF viewer
            html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CV Preview</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: #f5f5f5;
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }}
        .header {{
            background: #2c3e50;
            color: white;
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .header h1 {{
            font-size: 24px;
            font-weight: 600;
        }}
        .download-btn {{
            background: #3498db;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            font-size: 14px;
            transition: background 0.3s;
        }}
        .download-btn:hover {{
            background: #2980b9;
        }}
        .pdf-viewer {{
            width: 100%;
            height: calc(100vh - 120px);
            min-height: 800px;
            border: none;
        }}
        @media (max-width: 768px) {{
            body {{
                padding: 10px;
            }}
            .header {{
                flex-direction: column;
                gap: 15px;
                text-align: center;
            }}
            .pdf-viewer {{
                height: calc(100vh - 180px);
                min-height: 600px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>CV Preview</h1>
            <a href="data:application/pdf;base64,{pdf_base64}" download="cv.pdf" class="download-btn">
                Download PDF
            </a>
        </div>
        <iframe 
            class="pdf-viewer" 
            src="data:application/pdf;base64,{pdf_base64}"
            type="application/pdf"
        >
            <p>Your browser does not support PDFs. 
            <a href="data:application/pdf;base64,{pdf_base64}" download="cv.pdf">Download the PDF</a> instead.</p>
        </iframe>
    </div>
</body>
</html>
            """
            return HTMLResponse(content=html_content)
        else:
            # Return PDF response with appropriate content type
            return Response(
                content=pdf_bytes,
                media_type="application/pdf",
                headers={"Content-Disposition": "attachment; filename=cv.pdf"}
            )
        
    except SQLAlchemyError as e:
        logger.error(f"Database error in CV export: {e}", exc_info=True)
        raise HTTPException(
            status_code=500, 
            detail="Database error occurred while generating CV"
        )
    except ValueError as e:
        logger.error(f"Data validation error in CV export: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Incomplete user profile data: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Unexpected error in CV export: {e}", exc_info=True)
        raise HTTPException(
            status_code=500, 
            detail=f"Error generating CV: {str(e)}"
        )
