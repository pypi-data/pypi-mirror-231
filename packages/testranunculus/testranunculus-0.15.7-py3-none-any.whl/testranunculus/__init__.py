import available_functions
import blueprint_code
import blueprint_text
import documents_management
import file_management
import function_calling_spec_maker
import function_management
import helpers
import llm_functions
import menu
import project_management
import project_management_data
import prompts
import requirements_with_chat
import session_state_management
import simple_auth
import main
import sys
import os
from pathlib import Path

# Get the directory containing your main.py
main_dir = Path(__file__).parent.absolute()

# Add the 'plugins' directory to the Python path
sys.path.append(os.path.join(main_dir, 'plugins'))

if __name__ == "__main__":
    main.main()