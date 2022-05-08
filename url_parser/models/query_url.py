from pydantic import AnyHttpUrl, BaseModel, constr


class QueryUrl(BaseModel):
    url: AnyHttpUrl
    query: constr(min_length=1, strip_whitespace=True)
