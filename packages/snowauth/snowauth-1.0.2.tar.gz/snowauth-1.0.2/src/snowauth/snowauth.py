import toml
import os
from snowflake.snowpark.session import Session

HOME = os.path.expanduser('~')
CREDS_PATH = os.path.join(HOME, '.snowauth', 'snowflake.conf')


def connect(header, file_path=CREDS_PATH):
    """
    Allows users to put configurations in a file with toml header
    and pull to generate a session variable in snowpark.

    Para:
        header - Header of the toml file section to read from.
        
        file_path - File path to get credentials from. Default - "snowflake.conf"

    Example:
        >>> import snowauth
        >>> session = snowauth.connect('example_connection')
        >>> print(session)
        ...
        ... <snowflake.snowpark.session.Session: account=...>
    """


    with open(file_path, 'r') as f:
        creds = toml.load(f)

    if not creds:
        raise Exception('Connection Name not Found!')
    
    return Session.builder.configs(creds[header]).create()