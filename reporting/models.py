from django.db import models

class DailySummary(models.Model):
    date = models.DateField('Date of Summary', blank=False)
    
    active_members_total = models.PositiveIntegerField('Members', blank=False, default=0, help_text='Total members, of all types')

    active_households_singleperson = models.PositiveIntegerField('Single-Person Households', blank=False, default=0, help_text='Households with multiple members')
    active_households_multiperson = models.PositiveIntegerField('Multiperson Households', blank=False, default=0, help_text='Households with multiple members')

    active_student_teams = models.PositiveIntegerField('Student Teams', blank=False, default=0)
    active_student_team_members = models.PositiveIntegerField('Student Team Members', blank=False, default=0)

    @property
    def active_households(self):
        return self.active_households_singleperson + self.active_households_multiperson
