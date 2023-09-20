import toml
from snowflake.snowpark.session import Session


def connect(header,file_name="creds.conf"):
    """
    Allows users to put configurations in a file with toml header
    and pull to generate a session variable in snowpark.

    Para:
        header - Header of the toml file section to read from.
        
        file_name - File name to get credentials from. Default - "creds.conf"


    Example:
        >>> import snowauth
        >>> session = snowauth.connect('example_connection')
        ...
        ... PUT EXAMPLE OUT HERE.
        ...
    """
    with open(file_name, 'r') as f:
        creds = toml.load(f)

    if not creds:
        raise Exception('Connection Name not Found!')
    
    return Session.builder.configs(creds[header]).create()