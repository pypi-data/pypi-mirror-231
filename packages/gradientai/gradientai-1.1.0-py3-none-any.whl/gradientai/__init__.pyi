from importlib import metadata as _metadata

__version__ = _metadata.version("gradientai")

from gradientai._gradient import Gradient
from gradientai.pydantic_models.types import FineTuneResponse, CompleteResponse

from typing import List, Optional
from typing_extensions import NotRequired, Protocol, TypedDict

class Model(Protocol):
    @property
    def id(self) -> str: ...
    @property
    def workspace_id(self) -> str: ...
    def complete(
        self,
        *,
        query: str,
        max_generated_token_count: Optional[int] = ...,
        temperature: Optional[float] = ...,
        top_k: Optional[int] = ...,
        top_p: Optional[float] = ...
    ) -> CompleteResponse: ...

class Sample(TypedDict):
    inputs: str
    multiplier: NotRequired[float]

class ModelAdapter(Model, Protocol):
    @property
    def base_model_id(self) -> str: ...
    @property
    def name(self) -> str: ...
    def delete(self) -> None: ...
    def fine_tune(self, *, samples: List[Sample]) -> FineTuneResponse: ...

class BaseModel(Model, Protocol):
    @property
    def slug(self) -> str: ...
    def create_model_adapter(
        self,
        *,
        name: str,
        rank: Optional[int] = ...,
        learning_rate: Optional[float] = ...
    ) -> ModelAdapter: ...

__all__ = [
    "BaseModel",
    "Gradient",
    "Model",
    "ModelAdapter",
    "Sample",
]
