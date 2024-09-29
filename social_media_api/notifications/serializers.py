from notifications.models import Notification
from rest_framework import serializersgit

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.ReadOnlyField(source='actor.username')
    target_type = serializers.SerializerMethodField()
    target_id = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'actor_username', 'verb', 'target_type', 'target_id', 'unread', 'timestamp']
        read_only_fields = ['recipient', 'actor', 'verb', 'target_type', 'target_id', 'unread', 'timestamp']

    def get_target_type(self, obj):
        return obj.target_content_type.model if obj.target_content_type else None

    def get_target_id(self, obj):
        return obj.target_object_id
