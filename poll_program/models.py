from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    """
    Model representing a poll.

    Attributes:
        poll_question (str): The question for the poll.
        creating_time (datetime): The time when the poll was created, automatically set to the current date and time.
    """

    poll_question = models.CharField(max_length=255)
    creating_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the Poll object.

        Returns:
            str: The poll question.
        """
        return self.poll_question


class Option(models.Model):
    """
    Model representing an option in a poll.

    Attributes:
        poll (ForeignKey): A reference to the Poll that this option belongs to.
        option_name (str): The name of the option.
    """

    poll = models.ForeignKey(Poll, related_name='option', on_delete=models.CASCADE)
    option_name = models.CharField(max_length=255)

    def __str__(self):
        """
        String representation of the Option object.

        Returns:
            str: The option name.
        """
        return self.option_name


class Select(models.Model):
    """
    Model representing a user's selection of an option in a poll.

    Attributes:
        user (ForeignKey): A reference to the User who made the selection.
        option (ForeignKey): A reference to the Option that was selected.
        selecting_time (datetime): The time when the selection was made, automatically set to the current date and time.
    """

    user = models.ForeignKey(User, related_name='select', on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    selecting_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta options for the Select model.

        Attributes:
            unique_together (tuple): Ensures that a user can select a particular option only once.
        """
        unique_together = ('user', 'option')
