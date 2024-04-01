from scripts.seed_database_with_yugioh_card.db_layer import iter_chunk_list


def test_list_that_is_smaller_then_chunk_size__returns_list_as_only_chunk():
    input_list = [1, 2, 3]

    chunks = list(iter_chunk_list(input_list, 4))

    assert len(chunks) == 1
    assert chunks[0] == input_list


def test_list_that_is_larger_then_chunk_size__returns_list_split_into_two_chunks():
    input_list = [1, 2, 3]

    chunks = list(iter_chunk_list(input_list, 2))

    assert len(chunks) == 2
    assert chunks[0] == input_list[0:2]
    assert chunks[1] == input_list[2:]


def test_list_that_is_huge_when_chunked__returns_list_split_into_equal_part_chunks():
    input_list = [1] * 24

    chunks = list(iter_chunk_list(input_list, 2))

    assert len(chunks) == 12


def test_when_chunked__list_contains_no_more_then_chunk_size_elements():
    input_list = [1] * 24

    chunks = list(iter_chunk_list(input_list, 2))

    assert len(chunks[0]) <= 2
