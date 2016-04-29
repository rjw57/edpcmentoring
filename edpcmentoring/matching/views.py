from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.base import TemplateView

class MatchmakeView(PermissionRequiredMixin, TemplateView):
    http_method_names = ['get', 'head', 'options']
    permission_required = 'matching.matchmake'
    raise_exception = True
    template_name = 'matching/matchmake.html'

    def get_context_data(self, **kwargs):
        # Get a list of users who are active CUED members seeking mentors
        seekers = get_user_model().objects.\
            filter(cued_member__is_active=True,
                   mentorship_preferences__is_seeking_mentor=True).\
            select_related('cued_member',
                           'cued_member__research_group',
                           'cued_member__research_group__division')
        return {
            'seekers': seekers,
        }
