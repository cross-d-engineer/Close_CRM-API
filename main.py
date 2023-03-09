"""This is the main module script"""

from closeio_api import Client, ValidationError
import data
import prep_csv
import pandas as pd

"""Global Variables"""
# Equips Private API Key to Client that is used for authentication
your_api_key = input("Please enter your API key here: ")
API = Client(your_api_key)

# # Stores the leads that were already created
passed_leads = {}
#
# Custom data fields for Founder & Revenue
cf_founder = ""
cf_revenue = ""

ERROR_COUNTER = 0
num_of_created_leads = 0

# the response gathering existing Custom Field IDs for reuse
resp = API.get('custom_field/lead')

field_type = {}

# extracted the  required id for custom fields whilst changing the data type for filter process
for i in range(len(resp['data'])):
    if resp['data'][i]['name'] == "Company Founded":
        cf_founder = resp['data'][i]['id']
        create_custom = {
            "type": "date"
        }
        new_field = API.put(f'custom_field/lead/{cf_founder}', data=create_custom)

    if resp['data'][i]['name'] == "Company Revenue":
        cf_revenue = resp['data'][i]['id']
        create_custom = {
            "type": "number"
        }
        new_field = API.put(f'custom_field/lead/{cf_revenue}', data=create_custom)
#

# using the pandas Data Frame package to read from csv and later write to csv
input_file = input("Please enter filename: ") # should be within the same directory as script
df = pd.read_csv(input_file, sep=",", header=0)

# data assigned to variables from data frames
for index in range(len(df)):
    companies = df.loc[index]["Company"]
    contacts = df.loc[index]["Contact Name"]
    contact_email = df.loc[index]["Contact Emails"]
    contact_number = df.loc[index]["Contact Phones"]
    date_founded = df.loc[index]["custom.Company Founded"]
    comp_revenue = df.loc[index]["custom.Company Revenue"]
    comp_location = df.loc[index]["Company US State"]

    # the conditional logic used is to have leads if not found within the list be added by name in the list
    # and created on it's first iteration. on following iterations that matches leads within the list
    # only require the contact information be created

    if companies not in passed_leads:
        lead_data = data.create_leads(companies, contacts, contact_email, contact_number, cf_founder, date_founded,
                 cf_revenue, comp_revenue, comp_location)
        # Try & Except used to bypass the errors received whilst trying to post data
        try:
            lead = API.post('lead', data=lead_data)
            passed_leads[companies] = lead['id']  # dictionary used to evaluate if leads already exist
            num_of_created_leads = len(lead)
        except ValidationError as e:
            ERROR_COUNTER += 1
            print(f"Number of invalid data detected: {ERROR_COUNTER}")
            print(f"Validation: {e}")
            continue
        except Exception as e:
            print(f"API Error: {e}")
            continue
    else:
        contact_data = data.create_contact(passed_leads, companies, contacts, contact_number, contact_email)
        try:
            API.post('contact', data=contact_data)
        except ValidationError as e:
            ERROR_COUNTER += 1
            print(f"Number of invalid data detected: {ERROR_COUNTER}")
            print(f"Validation: {e}")
            continue
        except Exception as e:
            print(f"API Error: {e}")
            continue

print(f"Number of Leads created successfully via API: {num_of_created_leads}")
# finds all leads that were founded within a date range specified when running the script


# stores filter dates range to be sorted by
after_date = input("Please enter the date for start of filter in (YYYY/MM/DD): ")
before_date = input("Please enter the date for end of filter in (YYYY/MM/DD): ")


# arguments mapped to avoid conflicts
query_resp = API.post("data/search/", data=data.date_range(after=after_date, before=before_date))

print(f"Number of records found{len(query_resp)}")


final_df = pd.DataFrame(prep_csv.csv_gen(query_resp["data"]))


final_df.to_csv("Project_Output.csv", sep=",", index=False, header=True)

print(final_df)
