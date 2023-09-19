import uuid

from .types.app_type_interface import AppTypeInterface
from .types.chat import ChatApp
from .types.discord import DiscordApp
from .types.slack import SlackApp
from .types.web import WebApp
from apps.models import App
from apps.models import AppType
# Import all app types here


class AppTypeFactory:
    """
    Factory class for App types
    """
    @staticmethod
    def get_app_type_handler(app_type: AppType, platform: str = None) -> AppTypeInterface:
        subclasses = AppTypeInterface.__subclasses__()
        # Match with platform
        if platform:
            for subclass in subclasses:
                # Convert to lowercase to avoid case sensitivity
                if subclass.slug().lower() == platform.lower():
                    return subclass

        # Match with slug
        for subclass in subclasses:
            if subclass.slug() == app_type.slug.lower():
                return subclass

        return None

    @staticmethod
    def get_app_type_signature_verifier(app_id: str, platform: str = 'web'):
        app = App.objects.get(uuid=uuid.UUID(app_id))
        app_type_handler = AppTypeFactory.get_app_type_handler(
            app.type, platform,
        )

        return app, app_type_handler.verify_request_signature
