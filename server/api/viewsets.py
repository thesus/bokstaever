from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated


class MultiSerializerViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(MultiSerializerViewSet, self).get_serializer_class()


class ConditionalAuthenticationMixin:
    def get_permissions(self):
        if self.action in self.unauthenticated_actions:
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
