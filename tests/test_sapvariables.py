import calendar
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import SAPvariables


def test_sttDate_format():
    expected = f"{SAPvariables.thisYear}.{SAPvariables.thisMonth}.01"
    assert SAPvariables.sttDate == expected


def test_endDate_last_day():
    last_day = calendar.monthrange(SAPvariables.thisYear, SAPvariables.thisMonth)[1]
    expected = f"{SAPvariables.thisYear}.{SAPvariables.thisMonth}.{last_day}"
    assert SAPvariables.endDate == expected
