from django.utils.translation import gettext_lazy as _

GENDER = (
    ('M', _('Male')),
    ('F', _('Female')),
    ('O', _('Others')),
)
RELIGIONS = (
    ('hindu', _('Hindu')),
    ('christian', _('Christian')),
    ('buddhist', _('Buddhist')),
    ('muslim', _('Muslim'))
)
ETHNICITY = (
    ('brahmin', _('Brahmin')),
    ('chhetri', _('Chhetri')),
    ('baishya', _('Baishya')),
    ('shudra', _('Shudra'))
)

EDUCATION_LEVELS = (
    ('primary', _('Primary')),
    ('upper primary', _('Upper Primary')),
    ('higher secondary', _('Higher Secondary')),
    ('bachelor', _('Bachelor')),
    ('vocational', _('Vocational')),
    ('master', _('Master')),
    ('doctorate', _('Doctorate'))
)

JOB_LEVELS = (
    ('grade 1', _('Grade 1')),
    ('grade 2', _('Grade 2')),
    ('grade 3', _('Grade 3')),
    ('grade 4', _('Grade 4')),
    ('grade 5', _('Grade 5')),
    ('grade 6', _('Grade 6')),
    ('grade 7', _('Grade 7')),
    ('grade 8', _('Grade 8')),
    ('grade 9', _('Grade 9')),
    ('grade 10', _('Grade 10'))
)

JOB_TYPES = (
    ('private', _('Private')),
    ('governmental', _('Governmental')),
    ('ngos/ingos', _('NGOs/INGOs')),
)
