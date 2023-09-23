from . import available_functions
from . import blueprint_code
from . import blueprint_text
from . import documents_management
from . import file_management
from . import function_calling_spec_maker
from . import function_management
from . import helpers
from . import llm_functions
from . import menu
from . import project_management
from . import project_management_data
from . import requirements_with_chat
from . import session_state_management
from . import simple_auth

from .main import main as run
import os
os.system("streamlit run main.py")