# Snowauth.
A package for the simple local management of snowpark for python connections.

## Documentation 
Documentation can be found here: [Wiki](https://sfc-gh-dwilczak.github.io/snowauth/)

## Example

```python
import snowauth

session = snowauth.connect('example_connection')
```


## Setup

```
pip install snowauth
```

After installing `snowauth`, set up your snowflake credentials:

1. Create the `.snowauth` folder and the `snowflake.conf` file that will store different snowflake credentials.
    ```
    mkdir ~/.snowauth

    mkfile ~/.snowauth/snowflake.conf
    ```
2. Add your snowflake credentials.

    Example:
    ```toml
    [example_connection]
    account = "ACCOUNT_NAME"
    user = "USER"
    password = "PASSWORD"
    role = "ACCOUNTADMIN"
    warehouse = "EXAMPLE_WH"
    ```



Then, to create a snowpark session in 1 line.

```python
import snowauth

session = snowauth.connect('example_connection')
```



### Output:
```
<snowflake.snowpark.session.Session: account=...>
```
