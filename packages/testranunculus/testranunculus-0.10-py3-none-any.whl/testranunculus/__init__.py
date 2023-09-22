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
from . import prompts
from . import requirements_with_chat
from . import session_state_management
from . import simple_auth

import os
def run():
    # Get the path to the directory that contains your package
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Construct the path to main.py
    main_path = os.path.join(dir_path,'testranunculus', 'main.py')
    print(main_path)
    # Run the Streamlit app
    os.system(f'streamlit run {main_path}')

if __name__ == '__main__':
    run()