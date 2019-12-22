import pytest

import read_csv


@pytest.fixture()
def some_parameters():
    test_input = './testfiles/example.csv'

    expected_output = {'10/20/2019': [('100.0', 'N4000051-N4000058')],
                       '10/21/2019': [('100.0', 'N4000052-N4000058'), ('100.0', 'N4000053-N4000058')],
                       '10/24/2019': [('100.0', 'N4000054-N4000058'), ('1.0', 'N4000055-N4000058')]}

    return test_input, expected_output


def test_read_csv(some_parameters):
    test_input = some_parameters[0]
    expected_output = some_parameters[1]
    print(test_input)
    assert read_csv.read_csv(test_input) == expected_output

#

#
#
# def test_initial_transform(generate_initial_transform_parameters):
#    test_input = generate_initial_transform_parameters[0]
#    expected_output = generate_initial_transform_parameters[1]
#    assert test_app.initial_transform(test_input) == expected_output
#
#
# def test_final_transform(generate_initial_final_transform_parameters):
#    test_input = generate_initial_final_transform_parameters[0]
#    expected_output = generate_initial_final_transform_parameters[1]
#    assert test_app.final_transform(test_input) == expected_output
#
