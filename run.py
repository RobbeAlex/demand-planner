import sys
import os
from streamlit.web import cli as stcli

def main():
    # Define la ruta absoluta o relativa a tu dashboard
    script_path = "app_dashboard.py"
    
    # Construye los argumentos como si estuvieras en la terminal
    sys.argv = ["streamlit", "run", script_path]
    
    # Ejecuta streamlit internamente
    sys.exit(stcli.main())

if __name__ == "__main__":
    main()