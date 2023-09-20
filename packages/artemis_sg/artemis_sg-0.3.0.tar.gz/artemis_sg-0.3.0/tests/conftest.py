import json
import os
import tempfile

import pytest

from artemis_sg.config import CFG


@pytest.fixture(autouse=True)
def vendor_db(request):
    fh, file_name = tempfile.mkstemp()
    os.close(fh)
    CFG["asg"]["data"]["file"]["vendor"] = file_name
    data = {
        "sample": {
            "name": "Super Sample Test Vendor",
            "isbn_key": "ISBN-13",
        }
    }
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f)
    yield
    os.unlink(file_name)
