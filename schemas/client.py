from pydantic import BaseModel

class ClientSchema(BaseModel):
    full_name: str
    address: str | None=None
    num_document: str | None=None
    email: str | None=None
    phone: str | None=None
