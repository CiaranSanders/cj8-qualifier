from typing import Any, List, Optional


# │ ─ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    def find_column_lengths(rows: List[List[Any]]) -> List[int]:
        """
        Find the length of the largest element in each column of the parameter rows.
        :return: A list of the longest lengths for each row (indexes matching).
        """
        col_lengths = [0] * len(rows[0])
        for j in range(len(rows[0])):
            for i in range(len(rows)):
                if len(rows[i][j]) > col_lengths[j]:
                    col_lengths[j] = len(rows[i][j])
        return col_lengths

    def build_top_line(col_lengths: List[int]) -> str:
        """
        Build the very first line of the table.
        :param col_lengths: A list of the longest lengths for each row (indexes matching).
        :return: One line str of the top of the table.
        """
        line = '┌'
        for i, col_len in enumerate(col_lengths):
            if i == len(col_lengths) - 1:
                # last index
                line += ('─' * col_len) + '┐'
            else:
                line += ('─' * col_len) + '┬'
        return line

    table = ''
    try:
        num_cols = len(rows[0])
    except (TypeError, IndexError):
        # not sure how we want to handle errors like this yet? is this even possible with the type checking??
        return None

    col_lengths = find_column_lengths(rows)

    table += build_top_line(col_lengths)
    if labels:
        # build headers
        pass

    return table


if __name__ == '__main__':
    table = make_table([
        ['hello', 'there',],
        ['obi', 'wan'],
        ['ooga', 'boogachooga'],
    ])
    print(table)
