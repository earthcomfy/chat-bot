from django.views.generic import TemplateView


class ChatView(TemplateView):
    template_name: str = "chat/chat.html"
