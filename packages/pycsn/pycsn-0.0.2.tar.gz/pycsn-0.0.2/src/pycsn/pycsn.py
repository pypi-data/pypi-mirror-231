import argparse
import json
from pathlib import Path
from dataclasses import dataclass
import re
from datetime import date
import logging

import pandas as pd
from icecream import ic

logging.basicConfig(level=logging.INFO)

@dataclass
class C:
	n: str = "\033[0m"
	red: str = "\033[31m"
	green: str = "\033[32m"
	yellow: str = "\033[33m"
	blue: str = "\033[34m"
	magenta: str = "\033[35m"
	cyan: str = "\033[36m"

DEFAULT_STRING_LENGTH = 100

class PyCSN():
    def __init__(self, obj, table_name=None) -> None: 

        match obj:
            case pd.DataFrame():
                self.init_csn_dict()
                if not table_name:
                    raise Exception("Table name required!")
                self.add(obj, table_name)
            case dict():
                if isinstance(obj[list(obj)[0]], pd.DataFrame):
                    self.init_csn_dict()
                    for table_name, elem in obj.items():
                        self.add(elem,table_name)
                elif 'definitions' in obj:
                    self.csn = obj
                    logging.info("pycsn initialized with csn-formatted dict.")
                else: 
                    raise ValueError(f"Unknown format of dict for init pycsn!")
            case str():
                file = Path(obj)
                self.name = file.stem
                with open(obj) as fp:
                    self.csn = json.load(fp)
            case Path() | str():
                self.name = file.stem
                with open(obj) as fp:
                    self.csn = json.load(fp)
            case _:
                raise ValueError(f"{C.red}Unsupported obj:{type(obj)}{C.n}")

    # Class methods
    pd2cds_map = {
        "object": "cds.String",
        "int64": "cds.Int64",
        "float64": "cds.Double",
        "bool": "cds.Boolean",
        "datetime64": "cds.DateTime"
    }
    cds2pd = {
        "cds.String": "object",
        "cds.Int64": "int64",
        "cds.Double": "float64",
        "cds.Boolean": "bool",
        "cds.DateTime": "datetime64[ns]"
    }

    sql2pd = {
        "string": "object",
        "bigint": "int64",
        "double": "float64",
        "boolean": "bool",
        "datetime": "datetime64[ns]"
    }

    cds_numeric_types = ["cds.Int64", "cds.Double"]

    def init_csn_dict(self):
        self.csn = { "definitions": {},
                "version": {
                    "creator": "pycsn",
                    "csn": "0.1.99"
                }
            }

    def dt_records2pd(records: list) -> pd.DataFrame:
        cols = { rec['col_name']: pd.Series(dtype=PyCSN.sql2pd[rec['data_type'].lower()]) 
                for rec in records}
        return pd.DataFrame(cols)
    
    def cdstype(data_type) ->str:
        dt = str(data_type)
        if 'datetime64' in dt:
            dt = 'datetime64'
        return PyCSN.pd2cds_map[dt]
    
    def pd2cds(df: pd.DataFrame, name: str) -> str:
        csn = PyCSN.pd2csn(df, name)
        cds=""
        for dk, d in csn['definitions'].items():
            if d['kind'] == 'entity':
                cds=f"entity {dk} : {{\n"
                if 'elements' in d:
                    for ek, elem in d['elements'].items():
                        cds += f"  {ek:<8} : {elem['type'].split('.')[1]}\n"    
            cds += "}\n"
        return cds
    
    
    def search_elem(node: dict, key: str) -> dict:
        if key in node: 
            return node[key]
        for k, v in node.items():
            if isinstance(v,dict):
                elem = PyCSN.search_elem(v, key)
                if elem is not None:
                    return elem

    def is_numeric(dtype: str) -> bool:
        return True if dtype in PyCSN.cds_numeric_types else False
    
    # Instance methods
    def __str__(self) -> str:
        return json.dumps(self.csn, indent=4)
    
    def add(self, df: pd.DataFrame, table_name: str) -> dict:
        if table_name not in self.csn["definitions"]:
            self.csn["definitions"][table_name] = {"elements": dict()}
        csncols = self.csn["definitions"][table_name]["elements"]
        for c in df.index.names:
            if c:
                dt = PyCSN.cdstype(df.index.get_level_values(c).dtype)
                csncols[c] = {"type": dt, "key": True}
                if dt == 'cds.String':
                    max_length = df.index.get_level_values(c).str.len().max()
                    csncols[c]["length"] = int(max_length)
        for c in df.columns:
            dt = PyCSN.cdstype(df[c].dtype)
            csncols[c] = {"type": dt}
            if dt == 'cds.String':
                if not df.empty:
                    max_length = df[c].str.len().max()
                else:
                    max_length = DEFAULT_STRING_LENGTH
                csncols[c]["length"] = int(max_length)
    
    def write(self, filename=None, format='csn') -> str:        
        match format:
            case 'cds':
                cds = self.cds()
                with open(filename, 'w') as fp:
                    fp.write(cds)
                print(f"CDS-file written: {C.green}{filename}{C.n}")
            case 'csn':
                with open(filename, 'w') as js:
                    json.dump(self.csn, js, indent=4)
                print(f"CSN-file written: {C.green}{filename}{C.n}")
            case _:
                raise ValueError(f"{C.red}Unknown format: {C.green}{format}{C.n}")
  
    def update_df(self, df: pd.DataFrame, name: str) -> pd.DataFrame:

        # Check if csn and df have equal columns
        df_cols = set(df.columns)
        if df.index.names[0]: # in case there is not index set
            df_cols.update(df.index.names)
        table = self.csn['definitions'][name]['elements']
        csn_cols = set(table.keys())
        if csn_cols != df_cols:
            raise ValueError(f"Columns of csn and DataFrame({name}) are not equal: {csn_cols} <-> {df_cols}")
        
        # update keys
        csn_keys = set([ c for c,elem in table.items() if 'key' in elem and elem['key'] == True])
        df_keys = set(df.index.names)
        if csn_keys and csn_keys != df_keys:
            print(f"{C.red}Keys are not equal: csn({csn_keys}) <-> df({df_keys}){C.n}")
            if df.index.names[0]:
                df.reset_index(inplace=True)
            csn_keys = list(map(lambda x: x, csn_keys))
            df.set_index(csn_keys,inplace=True)

        # Check on data types
        for c in df.columns:
            pd_dtype = PyCSN.cds2pd[table[c]['type']]
            if pd_dtype != str(df[c].dtype):
                print(f"{C.green}Column dtypes are not equal:{C.n} cds:{pd_dtype} <-> df:{str(df[c].dtype)}")
                df[c] = df[c].astype(pd_dtype)

    def cds(self):
        cds=""
        for dk, d in self.csn['definitions'].items():
            if d['kind'] == 'entity':
                cds=f"entity {dk}  {{\n"
                if 'elements' in d:
                    for ek, elem in d['elements'].items():
                        key_elem = ek
                        if 'key' in elem and elem['key'] == True:
                            key_elem = 'key '+ ek
                        elem_type = elem['type'].split('.')[1]
                        if 'length' in elem:
                            elem_type += f"({elem['length']})"
                        cds += f"  {key_elem:<12} : {elem_type};\n"    
            cds += "}\n"
        return cds
    
    def set_primary_keys(self, pks) -> None:
        if isinstance(pks, str):
            pks = [pks]
        for pk in pks:
            for t in self.csn['definitions']:
                table = self.csn['definitions'][t]
                if 'elements' not in table:
                    continue
                if pk in table['elements']:
                    table['elements'][pk]['key'] = True


    def add_annotation(self, key_name: str, annotations: dict) -> None:
        elem = PyCSN.search_elem(self.csn, key_name)
        if elem :
            for a, v in annotations.items():
                if a[0] != '@':
                    a = '@' + a
                elem[a] = v
        else:
            raise ValueError(f"Entity \"{key_name}\" not found in csn.")

    def add_version_format(self, version: str) -> None:
        if re.match("\d+\.\d+\.\d+", version):
            self.csn['version']['@format'] = version
            self.csn['version']['@creation_date'] = str(date.today())
        else:
            raise ValueError(f"Version format not matched %d.%d.%d!")
        
    def set_col_length(self, table: str, column: str, length: int) -> None:
        elem = PyCSN.search_elem(self.csn, table)       
        if 'elements' not in elem:
            raise ValueError(f"Table \"{table}\"has no columns (elements)!")
        elem['elements'][column]['length'] = length

    def set_col_type(self, table: str, column: str, dtype: str, length=None) -> None:
        elem = PyCSN.search_elem(self.csn, table)       
        if 'elements' not in elem:
            raise ValueError(f"Table \"{table}\"has no columns (elements)!")
        elem['elements'][column]['type'] = dtype
        if PyCSN.is_numeric(dtype) and 'length' in elem['elements'][column]: 
            elem['elements'][column].pop('length')
        elif dtype == 'cds.String':
            elem['elements'][column]['length'] = length if length else DEFAULT_STRING_LENGTH


def main():

    parser = argparse.ArgumentParser(prog='pycsn',
                                     description='Creates csn-file from pandas DataFrame.')
    parser.add_argument('filenames', nargs='+', help='Data Filenames (csv)')
    parser.add_argument('-o', '--output', help='Overwrite default filename')
    parser.add_argument('-p', '--primary_keys', nargs='+', help='Add primary keys.')
    parser.add_argument('-t', '--test', help=argparse.SUPPRESS, action='store_true')
    args = parser.parse_args()

    dfs = dict()
    for i, f in enumerate(args.filenames):
        print(f"Read data-file:{C.green} {f}{C.n}")
        fp = Path(f)
        df = pd.read_csv(fp)
        dfs[str(fp.stem)] = df
        print(f"Table name:{C.green} {fp.stem}{C.n}")
    csn=PyCSN(dfs)

    if args.primary_keys:
        csn.set_primary_keys(args.primary_keys)


    if args.test:
        dt_dict = [{'col_name': 'country', 'data_type': 'string', 'comment': None}, 
                {'col_name': 'article_id', 'data_type': 'bigint', 'comment': None}, 
                {'col_name': 'category', 'data_type': 'string', 'comment': None}, 
                {'col_name': 'name', 'data_type': 'string', 'comment': None}, 
                {'col_name': 'size', 'data_type': 'string', 'comment': None}, 
                {'col_name': 'store_id', 'data_type': 'string', 'comment': None},
                {'col_name': 'transaction_id', 'data_type': 'bigint', 'comment': None}]
        csn = PyCSN(dt_dict, name='storex')
        csn.set_col_length('storex','category', 25)
        csn.set_col_type('storex','store_id', 'cds.Int64')
        csn.set_col_type('storex','transaction_id', 'cds.String', 25)
        print(csn)

    if args.output:
        csn.write(args.output)
    else: 
        if len(args.filenames) > 1:
            csn.write("tables.csn")
        else:
            csn.write(Path(args.filenames[0]).with_suffix('.csn'))


if __name__ == '__main__':
    main()