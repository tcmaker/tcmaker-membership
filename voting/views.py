from django.shortcuts import render
from django.http import HttpResponse
from membership.models import Household, Person
from django.contrib.auth.decorators import login_required

import csv
import random
import string
from datetime import datetime

def _compute_voting_list():
    voters = []
    # cutoff = datetime(2021, 9, 20)
    cutoff = datetime.now()
    for household in Household.objects.filter(valid_through__gte=cutoff):
        for person in household.person_set.all():
            voters.append(person)
    voters.sort(key=lambda x: x.family_name + ' ' + x.given_name)
    return voters

@login_required
def voting_list_2021(request):
    voters = _compute_voting_list()
    return render(request, 'voting/index.html', {
        'voters': voters,
    })

@login_required
def voting_list_2021_csv(request):
    voters = _compute_voting_list()

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="voters.csv"'},
    )

    writer = csv.writer(response)

    writer.writerow(['name', 'voter_identifier', 'voter_key', 'email', 'vote_weight'])

    voter_id = 1000
    for voter in voters:
        name = ' '.join([voter.given_name, voter.family_name])
        # voter_identifier = voter_id
        voter_identifier = voter.id
        email = voter.email
        vote_weight = 1
        voter_key = ''
        writer.writerow([name, voter_identifier, voter_key, email, vote_weight])
        # ensure unique voter identifiers
        voter_id += 1

    return response
