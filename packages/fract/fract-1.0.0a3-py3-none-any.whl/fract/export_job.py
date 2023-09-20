from typing import TypedDict


class ExportJob(TypedDict):
    height: int
    max_iterations: int
    path: str
    width: int
