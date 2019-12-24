from .. import download_lookup_table


def test_what():
    assert download_lookup_table.DownloadLookupTableApp.run() == 0
