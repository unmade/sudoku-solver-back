from typing import Tuple

from social_core.backends import google


class GoogleOAuth2(google.GoogleOAuth2):
    EXTRA_DATA: Tuple[str, str, bool] = [
        ("picture", "picture", False),
    ] + google.GoogleOAuth2.EXTRA_DATA
