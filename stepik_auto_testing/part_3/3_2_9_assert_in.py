def test_substring(full_string, substring):
    assert substring in full_string, \
        f'expected {substring!r} to be substring of {full_string!r}'


if __name__ == '__main__':
    test_substring('fulltext', 'some_value')
