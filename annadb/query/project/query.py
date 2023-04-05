import typing

from annadb.query.base import BaseQuery
from annadb.query.query_set import QuerySet
from annadb.query.types import Project

if typing.TYPE_CHECKING:
    from annadb.collection import Collection


class ProjectQuery(BaseQuery):
    def __init__(
            self,
            project_map: typing.Optional[dict],
            query_set: QuerySet,
            collection: "Collection"
    ):
        self.collection = collection
        self.query_set = query_set
        self.query_set.push(Project(data=project_map))
