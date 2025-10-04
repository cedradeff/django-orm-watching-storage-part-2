from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    not_leaved_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in not_leaved_visits:
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': timezone.localtime(visit.entered_at),
            'duration': visit.format_duration(),
            'is_strange': visit.is_visit_long(),
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
