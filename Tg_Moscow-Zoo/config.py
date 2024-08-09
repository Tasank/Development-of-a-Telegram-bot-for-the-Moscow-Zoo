from pathlib import Path
import os
from dotenv import load_dotenv

# Загрузка переменных из .енв
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv('TOKEN')