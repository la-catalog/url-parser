from pydantic import AnyHttpUrl, BaseModel, constr


class SkuUrl(BaseModel):
    url: AnyHttpUrl
    code: constr(min_length=1, strip_whitespace=True)
