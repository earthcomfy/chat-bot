from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ListTrainer


class Command(BaseCommand):
    help = "Training the chatbot"

    def handle(self, *args, **options):
        chatterbot = ChatBot(**settings.CHATTERBOT)
        trainer = ListTrainer(chatterbot)
        trainer.train(
            [
                "Hello",
                "Hi there!",
                "How are you doing?",
                "I'm doing great.",
                "That is good to hear",
                "Thank you.",
                "You're welcome.",
            ]
        )
        self.stdout.write(self.style.SUCCESS("Successfull!"))
