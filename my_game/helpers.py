from datetime import datetime


def log_message(message, log_level='INFO'):

    with open('logs.txt', 'a') as file:
        now = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        file.write(f'{now} - {log_level} - {message}\n')
