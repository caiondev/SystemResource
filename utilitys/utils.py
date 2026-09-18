import sys
import ctypes
import os
import logging

def admin_verify():
    if os.name == 'nt':
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            return is_admin
        except Exception as e:
            logging.error(f"Erro ao verificar privilégios de administrador: {e}")
            return False
    else:
        return os.geteuid() == 0


