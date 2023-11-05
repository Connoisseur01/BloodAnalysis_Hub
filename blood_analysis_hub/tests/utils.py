
def compare_test_results(test, referance_values):
    interpretation = {}
    for attribute, value in vars(test).items():
        if attribute in ('title', 'date_posted', 'user_id', 'id', '_sa_instance_state', 'author'):
            continue
        reference = referance_values[attribute]
        if reference["min"] <= value <= reference["max"]:
            interpretation[attribute] = "Within Reference Range"
        elif value > reference["max"]:
            interpretation[attribute] = "High"
        else:
            interpretation[attribute] = "Low"
    return interpretation
