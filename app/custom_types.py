from typing import Annotated
from sqlalchemy.orm import mapped_column

intpk = Annotated[int, mapped_column(primary_key=True)]
phone_number = Annotated[str, 10]
adress = Annotated[str, 100]
title = Annotated[str, 100]
name = Annotated[str, 100]