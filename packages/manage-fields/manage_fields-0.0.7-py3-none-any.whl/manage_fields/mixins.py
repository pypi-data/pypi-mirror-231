class MFViewMixin:
    def get_allow_fields(self):
        allow_fields = self.request.query_params.get('allow_fields')
        if allow_fields:
            return allow_fields.strip('{}').split(',')
        return []

    def get_disallow_fields(self):
        disallow_fields = self.request.query_params.get('disallow_fields')
        if disallow_fields:
            return disallow_fields.strip('{}').split(',')
        return []

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()

        kwargs['context'] = self.get_serializer_context()

        # Allowed fields
        allow_fields = self.get_allow_fields()
        if len(allow_fields) > 0:
            kwargs['allow_fields'] = allow_fields

        # Disallowed fields
        disallow_fields = self.get_disallow_fields()
        if len(disallow_fields) > 0:
            kwargs['disallow_fields'] = disallow_fields

        return serializer_class(*args, **kwargs)


class MFSerializerMixin:
    def __init__(self, instance=None, data=None, **kwargs):
        allow_fields = kwargs.pop('allow_fields', None)
        disallow_fields = kwargs.pop('disallow_fields', None)
        super().__init__(instance, data, **kwargs)

        if disallow_fields:
            disallow_fields = set(disallow_fields)
            for field_name in disallow_fields:
                self.fields.pop(field_name, None)

        if allow_fields:
            allow_fields = set(allow_fields)
            existing_fields = set(self.fields.keys())
            for field_name in existing_fields - allow_fields:
                self.fields.pop(field_name, None)
