import os

# Required environs
BASE_DIR = os.path.dirname(__file__)
SECRET_KEY = os.getenv('SECRET_KEY')
POSTGRES_DSN = os.getenv('POSTGRES_DSN')

# Environs with default values
DEBUG = os.getenv('DEBUG', '').lower() == 'true'
ALLOW_ORIGINS = os.getenv('ALLOW_ORIGINS', '').split()
STAGE = os.getenv('APP_STAGE', 'development').lower()
