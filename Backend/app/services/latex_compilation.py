import subprocess
import tempfile
import os
import platform
import shutil
from pathlib import Path
from typing import Tuple
from app.core.logging_config import get_logger

logger = get_logger(__name__)


def find_pdflatex() -> str:
    """
    Find pdflatex executable, checking PATH and common installation locations.
    
    Returns:
        Path to pdflatex executable, or empty string if not found
    """
    # First check PATH
    pdflatex_path = shutil.which("pdflatex")
    if pdflatex_path:
        return pdflatex_path
    
    # On Windows, check common MiKTeX installation paths
    if platform.system() == "Windows":
        username = os.getenv("USERNAME", "")
        userprofile = os.getenv("USERPROFILE", "")
        programfiles = os.getenv("ProgramFiles", r"C:\Program Files")
        programfiles_x86 = os.getenv("ProgramFiles(x86)", r"C:\Program Files (x86)")
        localappdata = os.getenv("LOCALAPPDATA", os.path.join(userprofile, "AppData", "Local"))
        
        common_paths = [
            # Standard installation paths
            os.path.join(programfiles, "MiKTeX", "miktex", "bin", "x64", "pdflatex.exe"),
            os.path.join(programfiles, "MiKTeX", "miktex", "bin", "pdflatex.exe"),
            os.path.join(programfiles_x86, "MiKTeX", "miktex", "bin", "pdflatex.exe"),
            # User installation paths
            os.path.join(localappdata, "Programs", "MiKTeX", "miktex", "bin", "x64", "pdflatex.exe"),
            os.path.join(localappdata, "Programs", "MiKTeX", "miktex", "bin", "pdflatex.exe"),
            os.path.join(userprofile, "AppData", "Local", "Programs", "MiKTeX", "miktex", "bin", "x64", "pdflatex.exe"),
            os.path.join(userprofile, "AppData", "Local", "Programs", "MiKTeX", "miktex", "bin", "pdflatex.exe"),
            # Portable installation
            os.path.join(programfiles, "MiKTeX Portable", "miktex", "bin", "x64", "pdflatex.exe"),
            os.path.join(programfiles, "MiKTeX Portable", "miktex", "bin", "pdflatex.exe"),
        ]
        
        for path in common_paths:
            if os.path.exists(path):
                logger.info(f"Found pdflatex at: {path}")
                return path
        
        # Also check if there's a MiKTeX installation directory and search for pdflatex
        miktex_dirs = [
            os.path.join(programfiles, "MiKTeX"),
            os.path.join(programfiles_x86, "MiKTeX"),
            os.path.join(localappdata, "Programs", "MiKTeX"),
        ]
        
        for miktex_dir in miktex_dirs:
            if os.path.exists(miktex_dir):
                # Search for pdflatex.exe in subdirectories
                for root, dirs, files in os.walk(miktex_dir):
                    if "pdflatex.exe" in files:
                        found_path = os.path.join(root, "pdflatex.exe")
                        logger.info(f"Found pdflatex at: {found_path}")
                        return found_path
    
    return ""


def check_pdflatex_available() -> Tuple[bool, str]:
    """
    Check if pdflatex is available in the system PATH or common installation locations.
    
    Returns:
        Tuple of (is_available, error_message)
    """
    pdflatex_path = find_pdflatex()
    if pdflatex_path:
        return True, ""
    
    system = platform.system()
    if system == "Windows":
        error_msg = (
            "LaTeX compiler (pdflatex) not found on Windows.\n\n"
            "MiKTeX appears to be installed but pdflatex is not accessible.\n\n"
            "Solutions:\n"
            "1. Add MiKTeX to PATH:\n"
            "   - Open System Properties > Environment Variables\n"
            "   - Add MiKTeX bin directory to PATH (usually: C:\\Program Files\\MiKTeX\\miktex\\bin\\x64)\n"
            "   - Restart your terminal/command prompt and FastAPI server\n\n"
            "2. Reinstall MiKTeX with PATH option:\n"
            "   - Download from: https://miktex.org/download\n"
            "   - During installation, check 'Add MiKTeX to PATH'\n"
            "   - Restart your terminal and server after installation\n\n"
            "3. Verify installation:\n"
            "   - Check if pdflatex.exe exists in: C:\\Program Files\\MiKTeX\\miktex\\bin\\x64\\\n"
            "   - If it exists, manually add that directory to your PATH"
        )
    elif system == "Linux":
        error_msg = (
            "LaTeX compiler (pdflatex) not found on Linux.\n\n"
            "Install with: sudo apt-get install texlive-latex-base texlive-latex-extra texlive-fonts-recommended\n"
            "Or on other distributions, use your package manager to install texlive packages."
        )
    elif system == "Darwin":  # macOS
        error_msg = (
            "LaTeX compiler (pdflatex) not found on macOS.\n\n"
            "Install with: brew install --cask mactex\n"
            "Or download MacTeX from: https://www.tug.org/mactex/"
        )
    else:
        error_msg = (
            "LaTeX compiler (pdflatex) not found.\n\n"
            "Please install a LaTeX distribution:\n"
            "- Windows: MiKTeX (https://miktex.org/download) or TeX Live\n"
            "- Linux: texlive-latex-base texlive-latex-extra\n"
            "- macOS: MacTeX or brew install --cask mactex"
        )
    
    return False, error_msg


def compile_latex_to_pdf(latex_content: str) -> bytes:
    """
    Compile LaTeX content to PDF using pdflatex.
    
    Args:
        latex_content: The LaTeX source code as a string
        
    Returns:
        PDF content as bytes
        
    Raises:
        RuntimeError: If LaTeX compilation fails
    """
    # Create a temporary directory for compilation
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        tex_file = temp_path / "cv.tex"
        pdf_file = temp_path / "cv.pdf"
        
        # Write LaTeX content to file
        tex_file.write_text(latex_content, encoding='utf-8')
        
        # Find pdflatex executable
        pdflatex_exe = find_pdflatex()
        if not pdflatex_exe:
            is_available, error_msg = check_pdflatex_available()
            system = platform.system()
            logger.error(f"pdflatex not found on {system}. {error_msg}")
            raise RuntimeError(error_msg)
        
        # Compile LaTeX to PDF using pdflatex
        # Run with -interaction=nonstopmode to avoid prompts
        # -output-directory to specify where to put the output
        # -halt-on-error to stop on errors
        # LaTeX often needs two passes for references, so we run it twice
        try:
            compile_args = [
                pdflatex_exe,
                "-interaction=nonstopmode",
                "-output-directory", str(temp_path),
                "-halt-on-error",
                str(tex_file)
            ]
            
            # First pass
            result1 = subprocess.run(
                compile_args,
                capture_output=True,
                text=True,
                timeout=30,
                check=False
            )
            
            # Second pass (for references, table of contents, etc.)
            result2 = subprocess.run(
                compile_args,
                capture_output=True,
                text=True,
                timeout=30,
                check=False
            )
            
            # Check if PDF was created
            if not pdf_file.exists():
                error_output = result2.stderr or result2.stdout or result1.stderr or result1.stdout
                logger.error(f"LaTeX compilation failed. Output: {error_output}")
                raise RuntimeError(f"LaTeX compilation failed: {error_output[:500]}")
            
            # Read the PDF file
            pdf_bytes = pdf_file.read_bytes()
            
            # Log success
            logger.info(f"Successfully compiled LaTeX to PDF ({len(pdf_bytes)} bytes)")
            
            return pdf_bytes
            
        except subprocess.TimeoutExpired:
            logger.error("LaTeX compilation timed out")
            raise RuntimeError("LaTeX compilation timed out after 30 seconds")
        except FileNotFoundError:
            is_available, error_msg = check_pdflatex_available()
            system = platform.system()
            logger.error(f"pdflatex not found on {system}. {error_msg}")
            raise RuntimeError(error_msg)
        except Exception as e:
            logger.error(f"Error compiling LaTeX: {e}", exc_info=True)
            raise RuntimeError(f"Error compiling LaTeX: {str(e)}")

