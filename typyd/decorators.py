from typing import Callable

from typyd.use_cases.validate_annotations_use_case import ValidateAnnotationsUseCase


def typed_function(func, ignore_float_and_integer_difference: bool = True) -> Callable:
    def return_func(*args, **kwargs):
        core = ValidateAnnotationsUseCase(func, ignore_float_and_integer_difference=ignore_float_and_integer_difference)
        core.execute(*args, **kwargs)
        return func(*args, **kwargs)

    return return_func
