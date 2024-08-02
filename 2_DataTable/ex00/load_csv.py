"""2_DataTable ex00"""

import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """Return writes the dimension & returns a dataset"""

    if not isinstance(path, str):
        raise Exception("wrong type")
    if not os.path.isfile(path):
        raise Exception(f"invalid parameter : {path}")
    if not path.endswith('.csv'):
        raise Exception("The file must have a .csv extension.")
    if not os.access(path, os.R_OK):
        raise Exception(f"The file is not readable: {path}")

    try:
        data = pd.read_csv(path)
    except pd.errors.EmptyDataError:
        raise Exception("The file is empty or only contains headers.")
    except pd.errors.ParserError:
        raise Exception("The file contains parsing errors.")
    except Exception as e:
        raise Exception(f"Error other: {str(e)}")

    if data.empty:
        raise Exception('DataFrame is empty')

    print(f'Loading dataset of dimensions {data.shape}')
    return data
