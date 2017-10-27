"""
Module name: conditions.py

This module provides an interface to the Wunderground Weather API for
conditions only. Below is an example of using the module.
Example:
    if __name__ == '__main__':
        import conditions

        # test code...real script can pull args from cmd line if desired
        location_data = {'city': 'Philadelphia',
                         'state' : 'PA'
                        }
        local_conditions = conditions.conditions(**location_data)
        # for temperature in farenheit, per US convention
        temp_farenheit = local_conditions['current_observation']['temp_f']
        location_data['temp'] = temp_farenheit
        print "Current temperature in {city}, {state}  is: {temp}".format(**location_data)

Attributes:
    WU_KEY (str): Wunderground API key. This must contain a working API key.
    WU_CONDITIONS_URL (str): URL used for the conditions API
    conditions(state=state, city=city, format='json'): function designed to return conditions

"""
# Sending example key for testing
WU_KEY = 'c01627a696907f9d'
WU_CONDITIONS = "http://api.wunderground.com/api/{key}/conditions/q/{query}.{result_format}"

import urllib2
import json

def us_state_city(state, city):
    '''Compose query string for state and city'''
    state = state.upper()
    city = city.strip().title().replace(' ', '_')
    return state + '/' + city

def conditions(query_type='US_State_City', result_format='json', *args, **kwargs):
    '''Call conditions API with proper inputs'''
    args = {}
    args['key'] = WU_KEY
    args['result_format'] = result_format
    # This is expandable if we want to add new queries
    if query_type == 'US_State_City':
        args['query'] = us_state_city(kwargs['state'], kwargs['city'])

    wu_url = WU_CONDITIONS.format(**args)
    api = urllib2.urlopen(wu_url)

    json_string = api.read()
    parsed_json = json.loads(json_string)

    return parsed_json
