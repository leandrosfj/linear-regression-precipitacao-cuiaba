import sys
import os

# Garante que a pasta src está no sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from analise_precipitacao import * 