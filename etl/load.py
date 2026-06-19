import logging

try:
   def load_csv(df, output_file):
       if df is None:
           print("No data to save")
           return


       df.to_csv(output_file, index=False)
       logging.info("CSV saved successfully")

except Exception as e:
    logging.error(f"Loading data failed due to {e}")