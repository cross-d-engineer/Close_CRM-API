
def create_leads(companies, contacts, contact_email, contact_number, cf_founder, date_founded,
                 cf_revenue, comp_revenue, comp_location):
    """
    This function receives the input arguments to be  mapped to fields in the json data before post
    """

    data = {
        "name": companies,
        "contacts": [
            {
                "name": contacts,
                "emails": [
                    {
                        "type": "office",
                        "email": contact_email
                    }
                ],
                "phones": [
                    {
                        "type": "office",
                        "phone": contact_number,
                    }
                ]
            }
        ],
        f"custom.{cf_founder}": date_founded,
        "custom." + cf_revenue: comp_revenue,
        "addresses": [
            {"state": comp_location}]

    }
    return data


def create_contact(passed_leads, companies, contacts, contact_number, contact_email):
    """
    This function receives the input arguments to be  mapped to fields in the json data before post
    """
    contact_data = {
        "lead_id": passed_leads[companies],
        "name": contacts,
        "phones": [
            {"phone": contact_number, "type": "other"}
        ],
        "emails": [
            {"email": contact_email, "type": "office"}
        ],
    }
    return contact_data


# filter extracted using visual builder. pagination "_limit" field edited for require performance.

def date_range(after, before):
    """
    Captures the after date as the filter start to a before date as the filter's end.
    Also includes the number of records to be returned for the call
    """
    custom_range = {
        "limit": None,
        "query": {
            "negate": False,
            "queries": [
                {
                    "negate": False,
                    "object_type": "lead",
                    "type": "object_type"
                },
                {
                    "negate": False,
                    "queries": [
                        {
                            "negate": False,
                            "queries": [
                                {
                                    "condition": {
                                        "before": None,
                                        "on_or_after": {
                                            "type": "fixed_local_date",
                                            "value": after,
                                            "which": "start"
                                        },
                                        "type": "moment_range"
                                    },
                                    "field": {
                                        "custom_field_id": "cf_5UxWpPzUh2XtrBDRd8E0ckYVHB4C9TFPZU8CaPKVZfp",
                                        "type": "custom_field"
                                    },
                                    "negate": False,
                                    "type": "field_condition"
                                }
                            ],
                            "type": "and"
                        },
                        {
                            "negate": False,
                            "queries": [
                                {
                                    "condition": {
                                        "before": {
                                            "type": "fixed_local_date",
                                            "value": before,
                                            "which": "end"
                                        },
                                        "on_or_after": None,
                                        "type": "moment_range"
                                    },
                                    "field": {
                                        "custom_field_id": "cf_5UxWpPzUh2XtrBDRd8E0ckYVHB4C9TFPZU8CaPKVZfp",
                                        "type": "custom_field"
                                    },
                                    "negate": False,
                                    "type": "field_condition"
                                }
                            ],
                            "type": "and"
                        }
                    ],
                    "type": "and"
                }
            ],
            "type": "and"
        },
        "results_limit": None,
        "_limit": 200,
        "_fields": {
            "lead": ["name", "addresses", "custom"]
            },
        "sort": []
            }
    return custom_range

# required dict to transpose from two letter US State codes to their full-names.
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}