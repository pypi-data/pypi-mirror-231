# from . import available_functions
# from . import blueprint_code
# from . import blueprint_text
# from . import documents_management
# from . import file_management
# from . import function_calling_spec_maker
# from . import function_management
# from . import helpers
# from . import llm_functions
# from . import menu
# from . import project_management
# from . import project_management_data
# from . import prompts
# from . import requirements_with_chat
# from . import session_state_management
# from . import simple_auth

# import sys
# import os
# from pathlib import Path

# # Get the directory containing your main.py
# main_dir = Path(__file__).parent.absolute()

# # Add the 'plugins' directory to the Python path
# sys.path.append(os.path.join(main_dir, 'plugins'))

# from .main import main

# if __name__ == "__main__":
#     main()

from testranunculus.main import main

if __name__ == "__main__":
    main()