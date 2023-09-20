from __future__ import annotations

from datetime import datetime
from math import ceil
from multiprocessing import Lock, Manager, Pool, Queue, current_process
from os.path import join
from pathlib import Path
from shutil import rmtree
from tempfile import mkdtemp
from types import TracebackType
from typing import Iterator, Type

import png

from fract.calculation_job import CalculationJob
from fract.export_job import ExportJob
from fract.logging import logger


class MandelbrotCalculator:
    def __init__(
        self,
        calculators: int,
        exporters: int,
        pool_working_directory: Path,
    ) -> None:
        self._started = datetime.now()

        self._calculators = calculators
        self._exporters = exporters
        self._pool_working_directory = pool_working_directory

        self._exports = Manager().dict()
        self._exports_lock = Lock()

        self._remaining = Manager().dict()
        self._remaining_lock = Lock()

        self._calculation_queue: "Queue[CalculationJob | None]" = Queue()
        self._export_queue: "Queue[str | None]" = Queue()

        logger.debug("Starting %i calculators", calculators)
        self._calculation_pool = Pool(
            calculators,
            self._start_calculation_worker,
            (self._calculation_queue, self._export_queue),
        )
        # Don't allow any more processes.
        self._calculation_pool.close()

        logger.debug("Starting %i exporters", exporters)
        self._export_pool = Pool(
            exporters,
            self._start_export_worker,
            (self._export_queue,),
        )
        # Don't allow any more processes.
        self._export_pool.close()

    def __enter__(self) -> MandelbrotCalculator:
        return self

    def __exit__(
        self,
        exc_type: Type[BaseException] | None,
        exc_inst: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool:
        for _ in range(self._calculators):
            self._calculation_queue.put(None)

        self._calculation_pool.join()

        for _ in range(self._exporters):
            self._export_queue.put(None)

        self._export_pool.join()

        logger.info(
            "%s closed after %0.1f seconds",
            self.__class__.__name__,
            (datetime.now() - self._started).total_seconds(),
        )

        return exc_type is not None

    def _start_calculation_worker(
        self,
        calculation_queue: "Queue[CalculationJob | None]",
        export_queue: "Queue[str | None]",
    ) -> None:
        name = current_process().name
        logger.debug("Calculation worker %s started", name)

        while True:
            job = calculation_queue.get()

            if job is None:
                logger.debug("Calculation worker %s stopping", name)
                return

            y = job["y"]

            logger.debug("Calculation worker %s now working on line %i", name, y)

            pixel_height = job["pixel_height"]
            real_width = job["real_width"]
            main_real = job["min_real"]
            imaginary_height = job["imaginary_height"]
            min_imaginary = job["min_imaginary"]
            max_iterations = job["max_iterations"]
            working_directory = job["working_directory"]

            imaginary = min_imaginary + (y / pixel_height) * imaginary_height

            pixel_width = job["pixel_width"]

            path = join(working_directory, str(y))
            result_byte_length = ceil(max_iterations.bit_length() / 8.0)

            with open(path, "wb") as f:
                for x in range(pixel_width):
                    count = MandelbrotCalculator.count_iterations(
                        main_real + (x / pixel_width) * real_width,
                        imaginary,
                        max_iterations,
                    )

                    f.write(count.to_bytes(result_byte_length))

            with self._remaining_lock:
                remaining_count = self._remaining[working_directory] - 1
                if self._remaining[working_directory] == 0:
                    del self._remaining[working_directory]
                else:
                    self._remaining[working_directory] = remaining_count

            if remaining_count == 0:
                export_queue.put(working_directory)

    def _start_export_worker(self, queue: "Queue[str | None]") -> None:
        name = current_process().name
        logger.debug("Export worker %s started", name)

        while True:
            working_directory = queue.get()

            if working_directory is None:
                logger.debug("Export worker %s stopping", name)
                return

            logger.debug(
                "Export worker %s received %s",
                name,
                working_directory,
            )

            with self._exports_lock:
                job = self._exports[working_directory]
                del self._exports[working_directory]

            path = job["path"]
            width = job["width"]
            height = job["height"]
            max_iterations = job["max_iterations"]

            with open(path, "wb") as f:
                writer = png.Writer(
                    width,
                    height,
                    greyscale=False,
                )

                rows = MandelbrotCalculator.iterations_to_color_rows(
                    height,
                    max_iterations,
                    working_directory,
                )

                writer.write(f, rows)

            rmtree(working_directory)

    @staticmethod
    def count_iterations(
        real: float,
        imaginary: float,
        maximum: int,
    ) -> int:
        """
        Counts the number of iterations required for the point (`real`,
        `imaginary`) to escape the Mandelbrot set, to a `maximum` iteration.
        """

        if MandelbrotCalculator.estimate_in_mandelbrot_set(real, imaginary):
            return maximum

        count = 0

        x = 0.0
        y = 0.0

        x_squared = 0.0
        y_squared = 0.0

        x_cycle = 0.0
        y_cycle = 0.0

        period = 0

        while x_squared + y_squared <= 4.0 and count < maximum:
            y = ((2 * x) * y) + imaginary
            x = (x_squared - y_squared) + real

            x_squared = x * x
            y_squared = y * y

            if x == x_cycle and y == y_cycle:
                return maximum

            period += 1

            if period > 20:
                period = 0
                x_cycle = x
                y_cycle = y

            count += 1

        return count

    def enqueue(
        self,
        width: int,
        height: int,
        path: Path | str,
        real: float = -0.65,
        imaginary: float = 0.0,
        real_width: float = 3.0,
        max_iterations: int = 1_000,
    ) -> None:
        working_directory = mkdtemp(dir=self._pool_working_directory)

        self._exports[working_directory] = ExportJob(
            height=height,
            max_iterations=max_iterations,
            path=path.as_posix() if isinstance(path, Path) else path,
            width=width,
        )

        self._remaining[working_directory] = height
        imaginary_height = real_width * (height / width)

        for y in range(height):
            job = CalculationJob(
                imaginary_height=imaginary_height,
                min_imaginary=imaginary - (imaginary_height / 2),
                min_real=real - (real_width / 2),
                max_iterations=max_iterations,
                pixel_height=height,
                pixel_width=width,
                real_width=real_width,
                working_directory=working_directory,
                y=y,
            )

            self._calculation_queue.put(job)

    @staticmethod
    def estimate_in_mandelbrot_set(
        real: float,
        imaginary: float,
    ) -> bool:
        """
        Estimates whether or not the point of (`real`, `imaginary`) is inside the
        Mandelbrot set's cardioid or a second-order bulb.

        `True` indicates certainty that the point is within the cardioid or a
        second-order bulb. `False` indicates uncertainty whether the point is inside
        or outside.
        """

        # Check cardioid:

        imaginary_squared = imaginary * imaginary

        real_minus_quarter = real - 0.25

        q = (real_minus_quarter * real_minus_quarter) + imaginary_squared

        if q * (q + real_minus_quarter) <= (0.25 * imaginary_squared):
            return True

        # Check bulbs:

        real_plus_one = real + 1

        return (real_plus_one * real_plus_one) + imaginary_squared <= 0.0625

    @staticmethod
    def iterations_to_color_rows(
        height: int,
        max_iterations: int,
        working_directory: str,
    ) -> Iterator[list[int]]:
        colors: list[int] = []
        result_byte_length = ceil(max_iterations.bit_length() / 8.0)

        for y in range(height):
            if y > 0:
                yield colors
                colors = []

            path = join(working_directory, str(y))

            with open(path, "rb") as f:
                while read_bytes := f.read(result_byte_length):
                    iteration_count = int.from_bytes(read_bytes)

                    if iteration_count < max_iterations:
                        colors.extend([255, 255, 255])
                    else:
                        colors.extend([0, 0, 0])

        yield colors
