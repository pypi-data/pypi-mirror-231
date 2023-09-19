from typing import List

import checkmarkandcross


def row_count(count: int) -> str:
    return f'{count} row{"" if count == 1 else "s"}'


def rows_table(rows: List[List]) -> str:
    return ''.join(map(
        lambda row: '<tr>' + ''.join(map(lambda e: f'<td>{e}</td>', row)) + '</tr>',
        rows
    ))


def wrap_image(val: bool, msg: str = '') -> str:
    image = checkmarkandcross.image_html(val, size=24, title=msg)
    return f'''
        <div style="display: flex; align-items: center; margin-top: 0.5rem">
            {image}
            <span style="margin-left: 0.5rem">
                {msg}
            </span>
        </div>
    '''
