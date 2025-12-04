# ruff check --select I --fix: import 알파벳 순 정렬
import os
import sys

import temp2 # noqa (특정 라인에 대해서 lint를 하고 싶지 않을 때, 특수한 경우에만 사용)


# O = "abc"

a = 123
# reveal_type(a) # mypy용 type print

my_int: int = 1
my_list: list[str] = ["abc", "def"]
my_tuple: tuple[str, str] = ("abc", "def")
my_tuple2: tuple[str, ...] = ("abc", "def") # 길이를 모르는 경우
my_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3, "d": 4}
or_type_list: list[str | int] = ["a", 1]