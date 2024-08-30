from pydantic import BaseModel, validator, Field

class Toy(BaseModel):
    x: int = Field(ge=0)
    y: int = Field(ge=0)
    face : str

    @validator('face')
    def validate_face(cls, value):
        # Allow case insensitive values
        choices = {'north', 'south', 'east', 'west'}
        normalized_value = value.lower()
        
        if normalized_value not in {v.lower() for v in choices}:
            raise ValueError(f'Invalid face value. The choices are: {", ".join(choices)}')
        
        return normalized_value