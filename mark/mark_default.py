def main(test_number, resources, notify):
    print(f"Function mark test #{test_number}")
    for resource in resources:
        notify.main(test_number, resource["name"])