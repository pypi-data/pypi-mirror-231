from time import sleep
from datetime import date, datetime
from unittest import TestCase

from datatool.time import (
    parse_date, parse_datetime, stringify_date, stringify_datetime,
    Meter, Estimator
)


class TimeTest(TestCase):
    def test_parse_date(self):
        self.assertEqual(parse_date("2021-09-03"), date(2021, 9, 3))

    def test_parse_datetime(self):
        self.assertEqual(
            parse_datetime("2021-09-03 21:05:38"),
            datetime(2021, 9, 3, 21, 5, 38)
        )

    def test_stringify_date(self):
        self.assertEqual(
            stringify_date(date(2021, 9, 3)),
            "2021-09-03"
        )

    def test_stringify_datetime(self):
        self.assertEqual(
            stringify_datetime(datetime(2021, 9, 3, 21, 5, 38)),
            "2021-09-03 21:05:38"
        )

    def test_meter(self):
        with Meter() as tm:
            sleep(0.1)
        self.assertLess(abs(tm.duration() - 0.1), 0.001)

    # def test_estimator(self):
    #     with Estimator(total=10) as te:
    #         for i in range(10):
    #             sleep(0.5)
    #             te.send()
