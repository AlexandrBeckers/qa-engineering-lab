from framework.config.settings import DB_NAME


def test_settings():
    assert DB_NAME == "qa_lab"
