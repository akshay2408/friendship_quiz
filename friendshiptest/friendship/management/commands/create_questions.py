from django.core.management.base import BaseCommand, CommandError
from friendship.models import Ques,QuizUser

class Command(BaseCommand):
    help = "Command to create quiz questions"

    def handle(self, *args, **options):
        questions = [
            {
                'question':'Favorite book',
                'op1':'Pride and Prejudice',
                'op2':'To Kill a Mockingbird ',
                'op3':'Jane Eyre by Charlotte Bronte',
                'op4':'Gone With the Wind by Margaret Mitchell',
            },
            {
                'question':'Favorite food',
                'op1':'Chili con carne',
                'op2':'Chimichanga',
                'op3':'Chinese chicken salad',
                'op4':'Chop suey',
            },
            {
                'question':'Favorite place',
                'op1':'South Island',
                'op2':'Paris',
                'op3':'Bora Bora',
                'op4':'Maui',
            },
            {
                'question':'Favorite serial',
                'op1':'Criminal Minds',
                'op2':'The Brady Bunch',
                'op3':'Columbo',
                'op4':'All in the Family',
            },
            {
                'question':'dream job',
                'op1':'Politician',
                'op2':'Athlete',
                'op3':'Doctor',
                'op4':'Teacher',
            },
            {
                'question':'Weather do you prefer most',
                'op1':'Hot',
                'op2':'Rainy',
                'op3':'Moderate',
                'op4':'Snowy',
            },
            {
                'question':'Favorite emoji',
                'op1':'Tear of joy',
                'op2':'Heart',
                'op3':'Smile',
                'op4':'Heart-Eyes',
            },
            {
                'question':'Favorite place in nature',
                'op1':'Mountain',
                'op2':'Lake',
                'op3':'River',
                'op4':'Forest',
            },
            {
                'question':'What are you good at',
                'op1':'Singing',
                'op2':'Dancing',
                'op3':'Cooking',
                'op4':'Swimming',
            },
            {
                'question':'Favorite game',
                'op1':'Chess',
                'op2':'Darts',
                'op3':'Poker',
                'op4':'Cricket',
            },
            {
                'question':'Favorite popcorn flavor',
                'op1':'Salted',
                'op2':'Caramel',
                'op3':'Chocolate',
                'op4':'Tutt-frutti',
            },
            {
                'question':'Favorite vacation destination',
                'op1':'Beach',
                'op2':'Mountains',
                'op3':'Big City',
                'op4':'Forest',
            },
            {
                'question':'Favorite part of the day',
                'op1':'Morning',
                'op2':'Evening',
                'op3':'Night',
                'op4':'Afternoon',
            },
            {
                'question':'Favorite app',
                'op1':'Facebook',
                'op2':'Instagram',
                'op3':'Youtube',
                'op4':'Tinder',
            },
            {
                'question':'What matters most in your life',
                'op1':'Friend',
                'op2':'Money',
                'op3':'Health',
                'op4':'Family',
            },

        ]
        try:
            for ques in questions:
                Ques.objects.get_or_create(question=ques['question'],op1=ques['op1'],op2=ques['op2'],op3=ques['op3'],op4=ques['op4'])
        except Exception as e:
            raise CommandError(e)