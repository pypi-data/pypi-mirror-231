# Snowauth.
A package for the simple local management of snowpark for python connections.

# Example:

### Setup:
Create a file name ``creds.conf``.
```
[connection]
account   = "ACCOUNT"
user      = "USER"
password  = "PASSWORD"
role      = "ROLE"
warehouse = "WAREHOUSE"
```

### Usage

```py
import snowauth

# creds.conf is the default. It can be change to whatever name you want.
session = snowauth.connect('creds.conf','connection')
```

### Output:
PUT OUTPUT HERE.