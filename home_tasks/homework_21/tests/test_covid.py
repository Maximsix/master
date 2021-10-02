
def test_check_main_id(covid_service):
    summary = covid_service.get_summary_info()
    assert summary.json()['ID'] == 'b8fb6369-3a85-4c14-b1c0-c1495ff8f96e'


def test_check_country_status(covid_service):
    country_status_response = covid_service.get_country_status('ukraine')
    key_list = ['Country', 'CountryCode']
    assert (country_status_response.json()[0][key_list[0]] == 'Ukraine'
            and
            country_status_response.json()[0][key_list[1]] == 'UA')


def test_check_city_status(covid_service):
    city_status_response = covid_service.get_city_status('ukraine')
    right_info = {}
    for key, value in city_status_response.json()[10].items():
        if key == 'Province' and value == "Kiev":
            right_info[key] = value
    assert right_info['Province'] == 'Kiev'


