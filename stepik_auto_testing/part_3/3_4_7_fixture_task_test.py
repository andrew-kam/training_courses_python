import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("\n", 111)
    print("^_^", "\n")
    yield
    print("\n", 222)
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print("\n", 333)
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print("\n", 444)
    print(":-B", "\n")


class TestPrintSmilingFaces:
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass

    def test_second_smiling_faces(self, prepare_faces):
        pass


if __name__ == "__main__":
    pytest.main()

# https://stepik.org/lesson/237257/step/7?auth=login&unit=209645
