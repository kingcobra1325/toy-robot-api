from pydantic import BaseModel, field_validator, Field
from conf import MAX_TABLE_X, MAX_TABLE_Y


class Toy(BaseModel):
    x: int = Field(ge=0, le=MAX_TABLE_X)
    y: int = Field(ge=0, le=MAX_TABLE_Y)
    face: str

    @field_validator("face")
    def validate_face(cls, value):
        # Allow case insensitive values
        choices = {"north", "south", "east", "west"}
        normalized_value = value.lower()

        if normalized_value not in {v.lower() for v in choices}:
            raise ValueError(
                f'Invalid face value. The choices are: {", ".join(choices)}'
            )

        return normalized_value
