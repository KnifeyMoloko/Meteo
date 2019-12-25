import pytest
import allure
from assertpy import assert_that
from apps.common import get_env_vars, get_file_at_url, parse_csv_to_data_frame


class TestEnvironmentVariableParsing(object):
    params = ["FLASK_APP", "FLASK_DEBUG", "FLASK_ENV"]

    @pytest.fixture()
    def set_up(self, monkeypatch):
        monkeypatch.setenv(self.params[0], "download_lookup_table")
        monkeypatch.setenv(self.params[1], "1")
        monkeypatch.setenv(self.params[2], "testing")

    def test_get_env_vars_returns_dict(self, set_up):
        assert_that(get_env_vars("download_lookup_table")).is_type_of(dict)

    def test_get_env_vars_returns_dict_with_keys_and_values(self, set_up):
        assert_that(list(get_env_vars().values())).is_not_empty()

    def test_get_env_vars_returns_dict_with_relevant_vars(self, set_up):
        assert_that(list(get_env_vars().keys())).is_in(self.params)


class TestFileDownload(object):
    station_url = "https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/wykaz_stacji.csv"

    def test_download_of_lookup_table_csv_response_status_is_200(self):
        assert_that(get_file_at_url(self.station_url).status_code).is_equal_to(200)

    def test_download_of_lookup_table_csv_response_content_contains_valid_station_names(self):
        stations = ["WEJHEROWO"]
        assert_that(get_file_at_url(self.station_url).content.decode("ISO-8859-2")).contains(stations[0])


class TestDataParsers(object):
    import pandas as pd
    station_url = "https://dane.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/wykaz_stacji.csv"

    @pytest.fixture()
    def fetch_data(self):
        return get_file_at_url(self.station_url).content

    def test_parse_lookup_table_to_pandas_data_frame_returns_data_frame(self, fetch_data):
        assert_that(parse_csv_to_data_frame(fetch_data)).is_type_of(self.pd.DataFrame)
