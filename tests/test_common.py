import pytest
import allure
from assertpy import assert_that
from apps.common import get_env_vars


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
