from django.db import models


class Orders(models.Model):
    """Categories of available user's financial goal.
    Attributes:
        start_date(Date): Date when order was set.
        goods(str): User's goods.
    """
    start_date = models.DateField()
    goods = models.CharField(blank=True, max_length=30)

class UserProfile(models.Model):
    """A user's profile.
    Attributes:
        first_name (str): User's first name
        last_name (str): User's last name
        birthday (str): User's birthday
        registration_date (str): Date of order registration
    """

    first_name = models.CharField(blank=True, max_length=30)
    last_name = models.CharField(blank=True, max_length=20)
    birthday = models.DateField(null=True)
    registration_date = models.DateField()
    order = models.OneToOneField(
        Orders,
        on_delete=models.CASCADE,
        related_name='user',
        null=True
    )

    def __str__(self):
        """
        :return: All the information about user which is added.
        """
        return str(self.to_dict())[:]

    def __repr__(self):
        """
        :return: Basic information which includes user id fist and last name.
        """
        return f"id:{self.id} first_name:{self.first_name} last_name:{self.last_name}"

    def to_dict(self):
        """
        Convert information which added user to dictionary where
        key is description of added information and value is an information.
        """
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birthday': self.birthday,
            'registration_date': self.registration_date
        }