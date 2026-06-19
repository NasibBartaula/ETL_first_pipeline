import pandas as pd
import json
import logging
try:
   def flatten_json(data):
    
      fdata=pd.DataFrame(data)
      logging.info("Json flatterned successfully")
      return fdata

except Exception as e:
   logging.error(f"Failed to flattern_json{e} ")
