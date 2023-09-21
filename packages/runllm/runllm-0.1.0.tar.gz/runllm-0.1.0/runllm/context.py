from pydantic import BaseModel


class ContextKey(BaseModel):
    key: str


class Context:
    def __getitem__(self, key):
        return ContextKey(key=key)
