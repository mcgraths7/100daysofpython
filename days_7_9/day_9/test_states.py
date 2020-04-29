import pytest
from states import get_every_nth_state, get_state_abbrev, \
    assign_longest_state, get_longest_state, combine_state_names_and_abbreviations


us_state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ',
                   'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
                   'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL',
                   'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
                   'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
                   'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
                   'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
                   'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                   'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE',
                   'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                   'New Mexico': 'NM', 'New York': 'NY',
                   'North Carolina': 'NC', 'North Dakota': 'ND',
                   'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
                   'Pennsylvania': 'PA', 'Rhode Island': 'RI',
                   'South Carolina': 'SC', 'South Dakota': 'SD',
                   'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
                   'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                   'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

states = ['Oklahoma', 'Kansas', 'North Carolina', 'Georgia', 'Oregon',
          'Mississippi', 'Minnesota', 'Colorado', 'Alabama',
          'Massachusetts', 'Arizona', 'Connecticut', 'Montana',
          'West Virginia', 'Nebraska', 'New York', 'Nevada', 'Idaho',
          'New Jersey', 'Missouri', 'South Carolina', 'Pennsylvania',
          'Rhode Island', 'New Mexico', 'Alaska', 'New Hampshire',
          'Tennessee', 'Washington', 'Indiana', 'Hawaii', 'Kentucky',
          'Virginia', 'Ohio', 'Wisconsin', 'Maryland', 'Florida',
          'Utah', 'Maine', 'California', 'Vermont', 'Arkansas', 'Wyoming',
          'Louisiana', 'North Dakota', 'South Dakota', 'Texas',
          'Illinois', 'Iowa', 'Michigan', 'Delaware']

NOT_FOUND = 'N/A'


def test_get_every_nth_state():
    assert get_every_nth_state() == ["Massachusetts", "Missouri",
                                           "Hawaii", "Vermont", "Delaware"]
    assert get_every_nth_state(n=15) == ["Nebraska", "Hawaii", "South Dakota"]
    assert get_every_nth_state(n=3) == ['North Carolina', 'Mississippi', 'Alabama',
                                        'Connecticut', 'Nebraska', 'Idaho',
                                        'South Carolina', 'New Mexico', 'Tennessee',
                                        'Hawaii', 'Ohio', 'Florida', 'California',
                                        'Wyoming', 'South Dakota', 'Iowa']


@pytest.mark.parametrize("arg, ret", [
    ('Alabama', 'AL'),
    ('Georgia', 'GA'),
    ('New Mexico', 'NM'),
    ('Wisconsin', 'WI')
])
def test_get_state_abbrev(arg, ret):
    assert get_state_abbrev(arg) == ret


def test_assign_longest_state():
    assert assign_longest_state(states) == "North Carolina"


def test_get_longest_state():
    assert get_longest_state(states) == "North Carolina"
    assert get_longest_state(us_state_abbrev) == "North Carolina"


def test_combine_state_names_and_abbreviations():
    assert combine_state_names_and_abbreviations() == ['AK', 'AL', 'AR', 'AZ',
                                                       'CA', 'CO', 'CT', 'DE',
                                                       'FL', 'GA', 'South Dakota',
                                                       'Tennessee', 'Texas', 'Utah',
                                                       'Vermont', 'Virginia', 'Washington',
                                                       'West Virginia', 'Wisconsin',
                                                       'Wyoming']

