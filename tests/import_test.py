from google.cloud import storage


def test_import():
    # dummy test that will fail if google.cloud.storage isn't found
    assert storage
