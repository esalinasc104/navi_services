from bson import ObjectId
from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.utils.functional import curry
from json import dumps, loads, JSONEncoder

from api.models import Zones


class DjangoJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Zones):
            return dumps(Zones)

        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, QuerySet):
            # `default` must return a python serializable
            # structure, the easiest way is to load the JSON
            # string produced by `serialize` and return it
            return loads(serialize('json', obj))
        return JSONEncoder.default(self, obj)


# partial function, we can now use dumps(my_dict) instead
# of dumps(my_dict, cls=DjangoJSONEncoder)

dumps = curry(dumps, cls=DjangoJSONEncoder)
