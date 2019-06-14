from typing import Any, Callable, List, Tuple, Union

_INPUTS_DIR = 'inputs'


def _read_lines(file: str) -> List[str]:
    with open(file) as f:
        return f.read().splitlines()


def read_input(day: int) -> List[str]:
    return _read_lines(f'{_INPUTS_DIR}/day{day}/input.txt')


def test_case(text: str) -> List[str]:
    return text[1:-1].splitlines()


def empty_list(
        shape: Union[int, Tuple[int, ...]],
        default_factory: Callable[..., Any] = lambda: None) -> List[Any]:
    if isinstance(shape, int):
        return [default_factory() for _ in range(shape)]
    
    if len(shape) == 1:
        return [default_factory() for _ in range(shape[0])]
    
    return [empty_list(shape[1:], default_factory) for _ in range(shape[0])]
