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

    def find_column_lengths(rows: List[List[Any]], n_cols: int, n_rows: int) -> List[int]:
        col_lens = [0] * n_cols
        for j in range(n_cols):
            for i in range(n_rows):
                if len(str(rows[i][j])) > col_lens[j]:
                    col_lens[j] = len(str(rows[i][j]))
        return col_lens

    def build_top_line(col_lens: List[int]) -> str:
        line = '┌'
        for i, col_len in enumerate(col_lens):
            if i == len(col_lens) - 1:
                # last index
                line += ('─' * col_len) + '┐'
            else:
                line += ('─' * col_len) + '┬'
        return line + '\n'

    def build_header(values: List[Any], col_lens: List[int]) -> str:
        line = build_row(values, col_lens)
        line += '├'
        for i, c_len in enumerate(col_lens):
            if i == len(col_lens) - 1:
                # last index
                line += ('─' * c_len) + '┤'
            else:
                line += ('─' * c_len) + '┼'
        return line + '\n'


    def build_row(values: List[Any], col_lens: List[int]) -> str:
        line = '│'
        for i, value in enumerate(values):
            col_len = col_lens[i]
            if centered:
                line += f'{str(value):^{col_len}}|'
            else:
                line += f'{str(value):<{col_len}}|'

        return line + '\n'

    def build_last_line(col_lens: List[int]) -> str:
        # ┴ ┘ 
        line = '└'
        for i, c_len in enumerate(col_lens):
            if i == len(col_lens) - 1:
                line += ('─' * c_len) + '┘'
            else:
                line += ('─' * c_len) + '┴'
        
        return line

    table = ''
    try:
        n_rows = len(rows)
        n_cols = len(rows[0])
    except (TypeError, IndexError):
        # not sure how we want to handle errors like this yet? is this even possible with the type checking??
        return None

    if labels:
        col_lens = find_column_lengths(rows + [labels], n_cols, n_rows + 1)
    else:
        col_lens = find_column_lengths(rows, n_cols, n_rows)

    table += build_top_line(col_lens)

    if labels:
        # build header
        table += build_header(labels, col_lens)

    for row in rows:
        table += build_row(row, col_lens)

    table += build_last_line(col_lens) 

    return table


if __name__ == '__main__':
    print('test 1')
    table = make_table(
        [['hello', 'there',], ['obi', 'wan'], ['ooga', 'boogachooga'],],
        labels=['boss', 'baby']
    )
    print(table)

    print('example 1')
    table = make_table(
        rows=[
            ["Lemon"],
            ["Sebastiaan"],
            ["KutieKatj9"],
            ["Jake"],
            ["Not Joe"]
        ]
    )
    print(table)

    print('example 2')
    table = make_table(
        rows=[
            ["Lemon", 18_3285, "Owner"],
            ["Sebastiaan", 18_3285.1, "Owner"],
            ["KutieKatj", 15_000, "Admin"],
            ["Jake", "MoreThanU", "Helper"],
            ["Joe", -12, "Idk Tbh"]
        ],
        labels=["User", "Messages", "Role"]
    )
    print(table)

    print('example 3')
    table = make_table(
       rows=[
           ["Ducky Yellow", 3],
           ["Ducky Dave", 12],
           ["Ducky Tube", 7],
           ["Ducky Lemon", 1]
       ],
       labels=["Name", "Duckiness"],
       centered=True
    )
    print(table)

