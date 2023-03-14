from django.core.management.base import BaseCommand

from apps.NepalAdministrativeDivision.models import WardDetail, MunicipalityDetail


class Command(BaseCommand):
    help = "command"

    def handle(self, **options):
        # WardDetail.objects.all().delete()
        # quit()
        municipalities = MunicipalityDetail.objects.all()
        for mun in municipalities:
            print('Creating ward of ', mun)
            print(mun.wards, '-----')
            if mun.wards:
                self.create_wards(mun.id, mun.wards)

    def create_wards(self, municipality_id, total_numbers=0):
        for number in range(total_numbers):
            ward_name = number + 1
            ward = WardDetail(municipality_id=municipality_id, name='वार्ड %s' % ward_name,
                              name_eng='ward %s' % ward_name)
            ward.save()
