# pyidoit
A Simple and Easy-to-use python client for  [i-doit](https://www.i-doit.com/)'s JSON-RPC API

## Installation

```console
$ pip install pyidoit
```

## Example

* Create a file python file(`main.py`) with:

```Python
from pyidoit import IDoitClient

PYIDOIT_HOST = "http://localhost/idoit-22/src/jsonrpc.php"
PYIDOIT_API_KEY = "XXXXX-XXXXX-XXX"

def main():
    client = IDoitClient(
        host=PYIDOIT_HOST,
        apikey=PYIDOIT_API_KEY,
        username="",
        password="",
    )

    data = client.cmdb_objects_read()
    print(data)

if __name__ == "__main__":
    main()
```

Then run the file

```console
$ python main.py
```


## CONTRIBUTION GUIDE LINES