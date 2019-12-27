class DownloadLookupTableApp(object):
    def __init__(self):
        self.name = "DownloadLookupTableApp"

    @staticmethod
    def run():
        from ..common.helpers import get_file_at_url, parse_csv_to_data_frame
        url = "https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/wykaz_stacji.csv"
        file = get_file_at_url(url).content
        df = parse_csv_to_data_frame(file,
                                     columns=["kod_stacji", "nazwa_stacji", "5_znakowy_kod_stacji"],
                                     index="5_znakowy_kod_stacji")
        print(df)
        return df
