"""
Module name: main.py

This module provides the run script for the Wunderground Weather
API quiz question.

Attributes:
    QUERY_TYPE:        The type of query for the conditions engine. Note that
                       conditions handles one query type right now, but can
                       expand to handle other query types

    CITY_AND_STATE:    The input parameters needed or the US_State_City
                       query type.

    CONDITIONS_TYPES:  The types of conditions handled at this period of time.
                       Currently, only US_State_City is handled, but this
                       can be expanded to handle the wider range of
                       conditions arguments.

"""
# Add QUERY_TYPE in case we want to generalize this routine later
QUERY_TYPE = 'US_State_City'

# City and state input for the conditions engine. Note that capitalization
# doesn't matter here...the code cleans it up later
CITY_AND_STATE = {'city': 'philadelphia', 'state_abbrev': 'pa'}

# Make sure other conditions types can be added later
CONDITIONS_TYPES = {'US_State_City': CITY_AND_STATE}

def state_city_location_data():
    '''Compose state and city location data'''
    location = {'city': CONDITIONS_TYPES[QUERY_TYPE]['city'],
                'state' : CONDITIONS_TYPES[QUERY_TYPE]['state_abbrev'],
                'query_type': QUERY_TYPE
               }
    return location

def state_city_result(current):
    '''Return state and city result data from API'''
    result_data = {}
    # temp is in farenheit, per US convention
    result_data['temp'] = current['temp_f']
    result_data['city'] = current['display_location']['city']
    result_data['state'] = current['display_location']['state']

    return "Current temperature in {city}, {state} is: "\
           "{temp}".format(**result_data)

if __name__ == '__main__':
    import conditions

    # Gather location data by query type
    if QUERY_TYPE == 'US_State_City':
        location_data = state_city_location_data()

    local_conditions = conditions.conditions(**location_data)
    try:
        current_observation = local_conditions['current_observation']
    except KeyError, e:
        print "Looks like an error with URL. Please check key.\n"
        raise
    # Print results by query type
    if QUERY_TYPE == 'US_State_City':
        print state_city_result(current_observation)

