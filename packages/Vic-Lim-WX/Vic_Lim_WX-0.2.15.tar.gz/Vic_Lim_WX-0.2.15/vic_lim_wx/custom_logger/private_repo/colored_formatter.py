import logging
class ColoredFormatter(logging.Formatter):
    COLORS = {
        'info': '\033[92m',  # Green
        'warning': '\033[93m',  # Yellow
        'error': '\033[91m'  # Red
    }
    RESET_COLOR = '\033[0m'

    def format(self, record):
        log_message = super().format(record)
        log_level = record.levelname.lower()
        color = self.COLORS.get(log_level, '')
        return f"{color}{log_message}{self.RESET_COLOR}"