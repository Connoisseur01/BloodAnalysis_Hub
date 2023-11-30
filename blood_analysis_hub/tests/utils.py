
def compare_test_results(values, referance_values):
    interpretation = {}
    for attribute in values:
        reference = referance_values[attribute]
        if reference["min"] <= values[attribute][0] <= reference["max"]:
            interpretation[attribute] = "Within Reference Range"
        elif values[attribute][0] > reference["max"]:
            interpretation[attribute] = "High"
        else:
            interpretation[attribute] = "Low"
    return interpretation
