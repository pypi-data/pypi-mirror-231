# Manage fields

## Usage

**views.py**

```pycon
from manage_fields.mixins import MFViewMixin

class MyView(MFViewMixin, ...):
    serializer_class = MySerializer
    ....
```

**serializers.py**

```pycon
from manage_fields.mixins import MFSerializerMixin

class MySerializer(MFSerializerMixin, ...):
    ...
```

**Request**

```text
https://abcd.com/?allow_fields={id,name}
```

### Params

`allow_fields` - Fields returned in response

`disallow_fields` - Fields that are not returned in the response

### Example

**models.py**

```pycon
class Example(models.Model):
    field1 = models.CharField(max_length=50)
    field2 = models.TextField()
    field3 = models.IntegerField()
```

**Request**

```text
https://example.com/?allow_fields={id,field1}
```

**Response**

```json
[
  {
    "id": 1,
    "field1": "Field1 value 1"
  },
  {
    "id": 2,
    "field1": "Field1 value 2"
  }
]
```

**Request**

```text
https://example.com/?disallow_fields={id,field1}
```

**Response**

```json
[
  {
    "field2": "Field2 value 1",
    "field3": "Field3 value 1"
  },
  {
    "field2": "Field2 value 2",
    "field3": "Field3 value 2"
  }
]
```

Also you can use this package for `CreateAPIView`, `UpdateAPIView`, `RetrieveAPIView`
