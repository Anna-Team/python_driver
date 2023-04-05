from annadb.constants import KEEP_OPERATOR
from annadb.data_types.primitive import PrimitiveBase


class Keep(PrimitiveBase):
    prefix = KEEP_OPERATOR
    instance_type = "keep"

    def __init__(self, _=None):
        super(Keep, self).__init__(None)
