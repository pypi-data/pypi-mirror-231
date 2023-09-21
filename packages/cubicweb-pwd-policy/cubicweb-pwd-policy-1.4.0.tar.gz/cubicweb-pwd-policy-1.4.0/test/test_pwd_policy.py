import unittest

from cubicweb.devtools.testlib import CubicWebTC
from cubicweb_pwd_policy import accept_password

from utils import PSWCubicConfigMixIn


class BasicPasswordPolicyTests(PSWCubicConfigMixIn, CubicWebTC):
    def test_password_strength(self):
        for psw, expected in (
            ("iuzYEr7£zerI1PE", True),
            ("+uzYEr7£zérIE", True),
            ("o2ieuUYEtrz4ud", False),
            ("o2ieuUY trz4ud", True),  # space is acceptable
            ("o2ieuUYétrz4ud", False),
            ("o2ieuUY$trz4ud", True),
            ("o2uUY$rzud", False),
            ("o2uaa$rzudpo*d2", False),
            ("O2UAA$REZ3ED*D", False),
            ("IuzYEr7azérIE", False),
            ("Iuz1YEr7azérIE", False),
            ('Iuz1YEr7azér"E', True),
            ("Iùz1YEr7az$rIE", True),
        ):
            self.assertEqual(accept_password(psw, "utf-8"), expected)
            self.assertTrue(
                accept_password(
                    psw,
                    "utf-8",
                    maxlen=10,
                    upper=False,
                    lower=False,
                    digit=False,
                    other=False,
                )
            )
        self.assertTrue(
            accept_password(
                "IuzYEr7azérIE",
                "utf-8",
                maxlen=10,
                upper=True,
                lower=True,
                digit=False,
                other=False,
            )
        )
        self.assertTrue(
            accept_password(
                "IuzYEr7azérIE",
                "utf-8",
                maxlen=10,
                upper=True,
                lower=True,
                digit=False,
                other=False,
            )
        )
        self.assertTrue(
            accept_password(
                "IuzYEr7£azérIE",
                "utf-8",
                maxlen=10,
                upper=True,
                lower=True,
                digit=False,
                other=True,
            )
        )


if __name__ == "__main__":
    unittest.main()
