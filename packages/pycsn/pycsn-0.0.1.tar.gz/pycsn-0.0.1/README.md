# pycsn

Python package supporting cds for table definitions in the first place. The data type is a ```dict``` and therefore using csn/json as the primary formatn from which a cds-document can be created. 

Use cases:
- Create csn/cds file from pandas DataFrame
- Use a csn-file to update the datatypes of a DataFrame (keys, data types and consistency check)

To Do:
- Support pyspark DataFrame and Delta Lake

Commandline
```shell
usage: pycsn [-h] [filename] [csn]

Creates csn-file from pandas DataFrame.

positional arguments:
  filename    Data Filename (csv) or folder (delta)
  csn         csn-file (optional)

options:
  -h, --help  show this help message and exit
```



[![PyPI - Version](https://img.shields.io/pypi/v/pycsn.svg)](https://pypi.org/project/pycsn)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pycsn.svg)](https://pypi.org/project/pycsn)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)



## Installation

```console
pip install pycsn
```

### For testing

#### Install cds
Install the cds cli tool "cds-dk"

```shell
npm add -g @sap/cds-dk
```

#### Local Database

Because the final destination of a table is HANA, you should test if the resulting sql-statement (CREATE TABLE) works. sqlite is recommended by SAP CAP. 

For MacOs:
```shell
brew install sqlite
```

## Testing

**pyscn** is using a ```dict``` a its primary data format. 



## Example Data

table : store
columns : 
    transaction_id: 
    store_id: 
    

## License

`pycsn` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
