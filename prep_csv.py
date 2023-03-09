import data
"""
This module is used to process the filtered data input and refine it based on the
 requirements specified
"""


def the_median(numbers):
    """
    This function takes a list of numbers as input and returns the median value.

    The median is the middle value in a sorted list of numbers. If the list has an
    even number of elements, the median is the average of the two middle values.
    """

    n = len(numbers)
    numbers_sorted = sorted(numbers)

    if n % 2 == 0:  # True once there is no remainder
        # If the list has an even number of elements, take the average of the middle two values
        middle_index = n // 2
        median = (numbers_sorted[middle_index - 1] + numbers_sorted[middle_index]) / 2
    else:
        # If the list has an odd number of elements, take the middle value
        middle_index = n // 2
        median = numbers_sorted[middle_index]

    return median


def csv_gen(refine):
    """
    This function uses the data in the argument passed to be processed based on the requirements set.

    The data is split into different dicts as the first dict holds the extracted values whilst the other
    is used for formatting required for csv parser.
    """

    segmented = {}
    for states in refine:
        state = states["addresses"][0]["state"]
        if state not in segmented:
            segmented[state] = {}
            segmented[state]['Num_Leads'] = 1
            segmented[state]["Leads_Revenue"] = [states["custom"]["Company Revenue"]]
            segmented[state]["Total_Revenue"] = states["custom"]["Company Revenue"]
            segmented[state]["Check_Revenue"] = states["custom"]["Company Revenue"]
            segmented[state]["Max_Revenue"] = states["name"]
        else:
            segmented[state]['Num_Leads'] += 1
            segmented[state]["Leads_Revenue"].append(states["custom"]["Company Revenue"])
            segmented[state]["Total_Revenue"] += states["custom"]["Company Revenue"]
        if segmented[state]["Check_Revenue"] < states["custom"]["Company Revenue"]:
            segmented[state]["Max_Revenue"] = states["name"]

        segmented[state]["Avg_Revenue"] = the_median(segmented[state]["Leads_Revenue"])

    csv_data = {
        "States": [],
        "Total Number of Leads": [],
        "The lead with most revenue": [],
        "Total Revenue": [],
        "Median Revenue": [],
    }

    for lines in segmented:
        csv_data["Total Number of Leads"].append(segmented[lines]["Num_Leads"])
        csv_data["Total Revenue"].append(segmented[lines]["Total_Revenue"])
        csv_data["Median Revenue"].append(segmented[lines]["Avg_Revenue"])
        csv_data["The lead with most revenue"].append(segmented[lines]["Max_Revenue"])
        for fullname in data.us_state_to_abbrev:
            if data.us_state_to_abbrev[fullname] == lines:
                csv_data["States"].append(fullname)

    return csv_data


# print(the_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
