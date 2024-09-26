# Named params ######################################

from activity.named_params import sartorial_splendor

print(f"1) {sartorial_splendor('cat', 'hat')}")
print(f"2) {sartorial_splendor('hat', 'cat')}")
print(f"3) {sartorial_splendor(creature='cat', clothing='hat')}")
print(f"4) {sartorial_splendor(clothing='hat', creature='cat')}")
print(f"5) {sartorial_splendor('cat', clothing='hat')}")
# print(f"error) {sartorial_splendor(creature='cat', 'hat')}")

from activity.named_params import sartorial_splendor_only_positional

print(f"1) {sartorial_splendor_only_positional('cat', 'hat')}")
# print(f"error) {sartorial_splendor_only_positional(creature='cat', clothing='hat')}")

from activity.named_params import sartorial_splendor_only_named

print(f"1) {sartorial_splendor_only_named(creature='cat', clothing='hat')}")
# print(f"error) {sartorial_splendor_only_named('cat', 'hat')}")

# Default params ####################################

from activity.default_params import sartorial_splendor_default

print(f"1) {sartorial_splendor_default('animal', 'flannel')}")
print(f"2) {sartorial_splendor_default('animal')}")
print(f"3) {sartorial_splendor_default()}")
print(f"4) {sartorial_splendor_default(clothing='flannel')}")

from activity.default_params import add_to_list_surprise

first_list = []
first_list = add_to_list_surprise("one", first_list)
print(f"{first_list=}")
first_list = add_to_list_surprise("two", first_list)
print(f"{first_list=}")

default_list = add_to_list_surprise("default")
print(f"{default_list=}")
maybe_another_default_list = add_to_list_surprise("another default")
print(f"{maybe_another_default_list=}")
print(f"{default_list is maybe_another_default_list=}")

from activity.default_params import add_to_list_ok

first_list = []
first_list = add_to_list_ok("one", first_list)
print(f"{first_list=}")
first_list = add_to_list_ok("two", first_list)
print(f"{first_list=}")

default_list = add_to_list_ok("default")
print(f"{default_list=}")
maybe_another_default_list = add_to_list_ok("another default")
print(f"{maybe_another_default_list=}")
print(f"{default_list is maybe_another_default_list=}")

# Dunder methods ####################################

from activity.dunder_methods import DunderExamples

de1 = DunderExamples(0, 10)
de2 = DunderExamples()
de3 = DunderExamples(10, 100)

# calls __str__
print(f"de1: {de1}")
print(f"de2: {de2}")
print(f"de3: {de3}")

# calls __repr__
print(f"{de1=}")
print(f"{de2=}")
print(f"{de3=}")

# calls __contains__
print(f"{5 in de1=}")
print(f"{5 in de2=}")
print(f"{5 in de3=}")

# reference comparison (is CANNOT be overridden)
print(f"{de1 is de2=}")
print(f"{de1 is de3=}")
print(f"{de2 is de3=}")

# value comparison (calls __eq__)
print(f"{de1 == de2=}")
print(f"{de1 == de3=}")
print(f"{de2 == de3=}")
