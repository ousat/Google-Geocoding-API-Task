import io
import datetime
import xlrd
import pandas as pd
from geo.geocoding_handler import get_client, get_lat_long_from_address
from geoUpdater.settings import OUTPUT_FILEPATH

def update_column(input_file):
    try:
        df = pd.read_excel(input_file)
        gmaps_client = get_client()
        # print(gmaps_client)
        # print(df.columns)
        df.columns = map(str.lower, df.columns)
        # print(df.columns)
        if "address" in df.columns:
            df["coordinates"] = df["address"].apply(get_lat_long_from_address, gmaps_client=gmaps_client)
            df = df.join(pd.DataFrame(df["coordinates"].values.tolist(), index=df.index, columns=["latitude", "longitude"]))
            # print(df.head())
            epoch_timestamp = int((datetime.datetime.now() - \
                datetime.datetime.utcfromtimestamp(0)).total_seconds()*1000)
            df.to_excel(OUTPUT_FILEPATH.format(timestamp=str(epoch_timestamp)), index=False)
            return {"status": 1, "timestamp": epoch_timestamp}
        else:
            return {"status": -1, "message": "Address Column Not Found"}
    except xlrd.biffh.XLRDError:
        # TODO: include csv support
        # if str(input_file.content_type) == "text/csv"
        #     try:
        #         df = pd.read_csv(input_file)
        #     except pd.errors.EmptyDataError:
        #         pass
        # else:
        #     return {}
        return {"status": -1, "message": "Wrong File Type"}
