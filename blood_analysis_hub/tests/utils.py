
def compare_test_results(values, referance_values):
    interpretation = {}
    for attribute in values:
        reference = referance_values[attribute]
        if reference["min"] <= values[attribute] <= reference["max"]:
            interpretation[attribute] = "Within Reference Range"
        elif values[attribute] > reference["max"]:
            interpretation[attribute] = "High"
        else:
            interpretation[attribute] = "Low"
    return interpretation
