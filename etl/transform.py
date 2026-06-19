def transform(data):
    import pandas as pd
    import logging

    df = pd.DataFrame(data)
    
    try:

      if "name" in df.columns:
          df["name"]=df["name"].str.strip()
          df["name"]=df["name"].str.title()

    
      if "email" in df.columns:
          df=df[df["email"].str.contains("@",na=False)]
        

      df = df.drop_duplicates(subset=["id"])
      logging.info("Trasformation done")
      return df
     
    except Exception as e:
        logging.error(f"Transformation failed . {e}")