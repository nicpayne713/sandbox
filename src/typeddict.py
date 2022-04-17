from mypy_extensions import TypedDict
from typing import Dict, List, Union

my_dict: Dict[str, Union[List[str], str]] = {
    "key_1": "val_1",
    "key_2": ["ls_1", "ls_2"],
}

my_dict["key_2"].pop()


MyDict = TypedDict("MyDict", {"key_1": str, "key_2": List[str]})

my_typed_dict: MyDict = {
    "key_1": "val_1",
    "key_2": ["ls_1", "ls_2"],
}


my_typed_dict["key_2"].pop()
