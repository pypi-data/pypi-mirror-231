from typing import TypedDict


class CalculationJob(TypedDict):
    imaginary_height: float
    min_imaginary: float
    min_real: float
    max_iterations: int
    pixel_height: int
    pixel_width: int
    real_width: float
    working_directory: str
    y: int
