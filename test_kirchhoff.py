import sys
import os

sys.path.append(
    os.path.join(os.path.dirname(__file__), "..", "src")
)

from kirchhoff import check_kcl, check_kvl


def test_kcl():
    entering = [5, 3]
    leaving = [6, 2]

    total_in, total_out, valid = check_kcl(
        entering, leaving
    )

    assert total_in == total_out
    assert valid is True


def test_kvl():
    sources = [12]
    drops = [5, 7]

    total_source, total_drop, valid = check_kvl(
        sources, drops
    )

    assert total_source == total_drop
    assert valid is True


def test_kcl_failure():
    entering = [5, 3]
    leaving = [6, 1]

    _, _, valid = check_kcl(
        entering, leaving
    )

    assert valid is False


print("All Kirchhoff's Law test cases passed!")