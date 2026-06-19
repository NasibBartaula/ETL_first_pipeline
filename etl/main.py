from extract import extract
from flattern_json import flatten_json
from transform import transform
from load import load_csv
import logging
import pandas as pd

logging.basicConfig(
    filename="etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

data, output_file = extract()

if data is None:
    print("Extraction failed")
    exit()

fdata = flatten_json(data)

df = transform(fdata) 

load_csv(df, output_file)


df = pd.read_csv("data/Data.csv")
print(df.shape)