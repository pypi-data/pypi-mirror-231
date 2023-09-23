from __future__ import annotations

#
# Copyright (c) 2023 unSkript.com
# All rights reserved.
#
from pydantic import BaseModel, Field
from typing import Optional, Tuple



class InputSchema(BaseModel):
    threshold: Optional[float] = Field(
        70.0,
        description='Threshold for CPU utilization in percentage.',
        title='Threshold (in %)',
    )


print(InputSchema.schema_json(indent=4))
