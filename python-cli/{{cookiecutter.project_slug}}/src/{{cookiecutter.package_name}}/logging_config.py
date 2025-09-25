import logging
import sys
from pathlib import Path


# Color codes for terminal output
class LogColors:
    DEBUG = "\033[36m"  # Cyan
    INFO = "\033[32m"  # Green
    WARNING = "\033[33m"  # Yellow
    ERROR = "\033[31m"  # Red
    CRITICAL = "\033[41m"  # Red background
    RESET = "\033[0m"  # Reset to default

class ColoredFormatter(logging.Formatter):
    """Custom formatter adding colors and file/line info for errors"""
    
    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        
        if record.levelno >= logging.ERROR:
            # Add file and line number for errors
            filename = Path(record.pathname).name
            message = f"{message} ({filename}:{record.lineno})"
            return f"{LogColors.ERROR}{message}{LogColors.RESET}"
        elif record.levelno >= logging.WARNING:
            return f"{LogColors.WARNING}{message}{LogColors.RESET}"
        elif record.levelno >= logging.INFO:
            return f"{LogColors.INFO}{message}{LogColors.RESET}"
        elif record.levelno >= logging.DEBUG:
            return f"{LogColors.DEBUG}{message}{LogColors.RESET}"
        
        return message

def configure_logging(level: int = logging.INFO) -> None:
    """Set up colored logging for the application"""
    
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(ColoredFormatter(
        fmt="%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))
    
    # Configure root logger
    logging.basicConfig(
        level=level,
        handlers=[handler],
        force=True  # Override any existing handlers
    )
    
    # Special formatting for third-party libraries if needed
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("atlassian").setLevel(logging.INFO)