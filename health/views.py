from django.shortcuts import render, redirect
from .forms import SelectTeamForm, HealthCheckEntryForm
from .models import Team, HealthCheckEntry

# 1. Select team view
def select_team(request):
    if request.method == 'POST':
        form = SelectTeamForm(request.POST)
        if form.is_valid():
            team = form.cleaned_data['team']
            request.session['team_id'] = team.id
            return redirect('intro_page')  # Redirect to intro after selecting team
    else:
        form = SelectTeamForm()
    return render(request, 'details.html', {'form': form})

# 2. Intro page view
def intro_page(request):
    team_id = request.session.get('team_id')
    if not team_id:
        return redirect('select_team')
    return render(request, 'Intro.html')

# 3. Done page view
def done(request):
    return render(request, 'done.html')

# 4. DELIVERING VALUE page - updated to SAVE into database
def deliver(request):
    team_id = request.session.get('team_id')
    if not team_id:
        return redirect('select_team')

    team = Team.objects.get(id=team_id)

    if request.method == 'POST':
        form = HealthCheckEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.team = team
            entry.card_title = 'Delivering Value'  # This specific card
            entry.save()
            return redirect('ease_of_release')  # Go to next card
    else:
        form = HealthCheckEntryForm()

    return render(request, 'Deliver.html', {'form': form})


def ease_of_release(request):
    team_id = request.session.get('team_id')
    if not team_id:
        return redirect('select_team')

    team = Team.objects.get(id=team_id)

    if request.method == 'POST':
        form = HealthCheckEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.team = team
            entry.card_title = 'Ease of Release'
            entry.save()
            return redirect('healthbasecoder')
    else:
        form = HealthCheckEntryForm()

    return render(request, 'Easeofrelease.html', {'form': form})


def healthbasecoder(request):
    team_id = request.session.get('team_id')
    if not team_id:
        return redirect('select_team')

    team = Team.objects.get(id=team_id)

    if request.method == 'POST':
        form = HealthCheckEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.team = team
            entry.card_title = 'Health of Codebase'
            entry.save()
            return redirect('learning')
    else:
        form = HealthCheckEntryForm()

    return render(request, 'Healthbasecoder.html', {'form': form})



def learning(request):
    team_id = request.session.get('team_id')
    if not team_id:
        return redirect('select_team')

    team = Team.objects.get(id=team_id)

    if request.method == 'POST':
        form = HealthCheckEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.team = team
            entry.card_title = 'Learning'
            entry.save()
            return redirect('fun')
    else:
        form = HealthCheckEntryForm()

    return render(request, 'Learning.html', {'form': form})


def fun(request):
    team_id = request.session.get('team_id')
    if not team_id:
        return redirect('select_team')

    team = Team.objects.get(id=team_id)

    if request.method == 'POST':
        form = HealthCheckEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.team = team
            entry.card_title = 'Fun'
            entry.save()
            return redirect('suitable_process')
    else:
        form = HealthCheckEntryForm()

    return render(request, 'Fun.html', {'form': form})



def suitable_process(request):
    team_id = request.session.get('team_id')
    if not team_id:
        return redirect('select_team')

    team = Team.objects.get(id=team_id)

    if request.method == 'POST':
        form = HealthCheckEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.team = team
            entry.card_title = 'Suitable Process'
            entry.save()
            return redirect('speed')
    else:
        form = HealthCheckEntryForm()

    return render(request, 'Suitable process.html', {'form': form})


def speed(request):
    team_id = request.session.get('team_id')
    if not team_id:
        return redirect('select_team')

    team = Team.objects.get(id=team_id)

    if request.method == 'POST':
        form = HealthCheckEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.team = team
            entry.card_title = 'Speed'
            entry.save()
            return redirect('mission')  # Move to next step
    else:
        form = HealthCheckEntryForm()

    return render(request, 'Speed.html', {'form': form})






def mission(request):
    team_id = request.session.get('team_id')
    if not team_id:
        return redirect('select_team')

    team = Team.objects.get(id=team_id)

    if request.method == 'POST':
        form = HealthCheckEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.team = team
            entry.card_title = 'Mission'
            entry.save()
            return redirect('support')
    else:
        form = HealthCheckEntryForm()

    return render(request, 'Mission.html', {'form': form})




def support(request):
    team_id = request.session.get('team_id')
    if not team_id:
        return redirect('select_team')

    team = Team.objects.get(id=team_id)

    if request.method == 'POST':
        form = HealthCheckEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.team = team
            entry.card_title = 'Support'
            entry.save()
            return redirect('pawnsonplayers')
    else:
        form = HealthCheckEntryForm()

    return render(request, 'Support.html', {'form': form})






def pawnsonplayers(request):
    team_id = request.session.get('team_id')
    if not team_id:
        return redirect('select_team')

    team = Team.objects.get(id=team_id)

    if request.method == 'POST':
        form = HealthCheckEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.team = team
            entry.card_title = 'Pawns or Players'
            entry.save()
            return redirect('done')
    else:
        form = HealthCheckEntryForm()

    return render(request, 'pawnsonplayers.html', {'form': form})




def feedback(request): return render(request, 'feedback.html')
def trends(request): return render(request, 'trends.html')
def login(request): return render(request, 'Login.html')
def logout(request): return render(request, 'logout.html')
def factors(request): return render(request, 'factors.html')


