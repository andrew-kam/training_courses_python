import pytest


@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False


if __name__ == "__main__":
    pytest.main()

    # pytest -v -rsxX stepik_auto_testing/part_3/3_5_6_task_mark_xfail_test.py

# https://stepik.org/lesson/236918/step/6?auth=login&next=&unit=209305
