from rest_framework import generics


# list
class BaseListAPIView(generics.ListAPIView):

    def __init__(self, model, serializer_class, permission_classes, **kwargs):
        super().__init__(**kwargs)
        self.queryset = model
        self.serializer_class = serializer_class
        self.permission_classes = permission_classes


# create
class BaseCreateAPIView(generics.CreateAPIView):
    def __init__(self, queryset, serializer_class, permission_classes, **kwargs):
        super().__init__(**kwargs)
        self.queryset = queryset
        self.serializer_class = serializer_class
        self.permission_classes = permission_classes


# retrieve
class BaseRetrieveAPIView(generics.RetrieveAPIView):
    def __init__(self, queryset, serializer_class, permission_classes, **kwargs):
        super().__init__(**kwargs)
        self.queryset = queryset
        self.serializer_class = serializer_class
        self.permission_classes = permission_classes


# update
class BaseUpdateAPIView(generics.RetrieveUpdateAPIView):
    def __init__(self, queryset, serializer_class, permission_classes, **kwargs):
        super().__init__(**kwargs)
        self.queryset = queryset
        self.serializer_class = serializer_class
        self.permission_classes = permission_classes


# destroy
class BaseDestroyAPIView(generics.DestroyAPIView):
    def __init__(self, queryset, serializer_class, permission_classes, **kwargs):
        super().__init__(**kwargs)
        self.queryset = queryset
        self.serializer_class = serializer_class
        self.permission_classes = permission_classes
