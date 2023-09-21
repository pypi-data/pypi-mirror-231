from abc import ABC, abstractmethod
from collections.abc import Mapping
from typing import Any, Protocol, TypeVar

_T_co = TypeVar("_T_co", covariant=True)


class SupportsRead(Protocol[_T_co]):
    def read(self, n: int = ..., /) -> _T_co:
        ...


DecoderError = ValueError


class Decoder(ABC):
    name: str
    extensions: tuple[str]

    @classmethod
    @abstractmethod
    def load(cls, fp: SupportsRead[bytes], /) -> Mapping[str, Any]:
        """Deserialize `fp` (binary file-like object) with this decoder"""

    @classmethod
    def get_default_extension(cls) -> str:
        return cls.extensions[0]


class TOMLDecoder(Decoder):
    name = "toml"
    extensions = (".toml",)

    @classmethod
    def load(cls, fp: SupportsRead[bytes]) -> Mapping[str, Any]:
        import tomllib

        return tomllib.load(fp)


class JSONDecoder(Decoder):
    name = "json"
    extensions = (".json",)

    @classmethod
    def load(cls, fp: SupportsRead[bytes]) -> Mapping[str, Any]:
        import json

        data: dict[str, Any] | Any = json.load(fp)
        if not isinstance(data, dict):
            raise json.JSONDecodeError("Expecting object", "", 0)
        return data
