import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kimbo_django.settings' )

import django
django.setup()

# FAKE POP SCRPT
import random

from help_app.models import Topic, AccessRecord, Webpage

from faker import Faker

fakegen =Faker() # NEED TO CREATE A INSTANCE IN FAKER

topics =['Search', 'Social', 'Marketplace', 'News', 'Games']  # on cree une lisrte de topic

def add_topic():  # la fonction qui va add le topic comme dans shell
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):

        # GET THE TOPIC FOR THE ENTRY
        top = add_topic()

        # create the fake data for that entry on peut utiliser plusieur model avec fake avec l instace cree fakegen
        fake_url=fakegen.url()
        fake_date= fakegen.date()
        fake_name = fakegen.company()



        #create the  new webpage entry

        webpg= Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #Create a fake access record fo that page
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__=='__main__':
    print("populatin script!")
    populate(15)
    print("populating complete")


