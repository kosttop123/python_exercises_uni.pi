"""
11. Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα λεξικό από αρχείο. 
Το λεξικό μπορεί να περιέχει και άλλα λεξικά, λίστες, κτλ. 
Εμφανίστε στο χρήστη τα κλειδιά που εμφανίζονται τις περισσότερες φορές, 
ελέγχοντας και τα εμφωλευμένα λεξικά.

"""
import json

class DictKeyCounter(object):
    def __init__(self, dictionary):
        self.key_list = []
        self.iterate_through_dict(dictionary)

    # Iterate through dict using recursion
    def iterate_through_dict(self, dictionary):
        for key, value in dictionary.items():
            # Append key to the list
            self.key_list.append(key)
            # If value also is a dict, call the function again
            # with value as the parameter
            if isinstance(value, dict):
                self.iterate_through_dict(value)
            # If value is a list, call iterate_through_list()
            # with value as a parameter
            elif isinstance(value, list):
                self.iterate_through_list(value)

    # Iterate through list using recursion
    def iterate_through_list(self, lst):
        # Iterate through each element of the list
        for element in lst:
            # If element is a dict, call iterate_through_dict(),
            # with element as a parameter
            if isinstance(element, dict):
                self.iterate_through_dict(element)
            # If element also is a list, call the function again
            # with element as a parameter
            elif isinstance(element, list):
                self.iterate_through_list(element)

    def get_key_list(self):
        # Returns the list of keys
        return self.key_list


# Read the file
with open('exercise_11.txt', 'r') as txt_file:
    file_input = txt_file.read()
    
# Convert it to a dictionary
dictionary = json.loads(file_input)

# Pass it to the DickKeyCounter class
key_counter = DictKeyCounter(dictionary)

# Get the list of keys
key_list = key_counter.get_key_list()

# Remove duplicates to get each individual key
individual_keys = list(set(key_list))

key_count = []

# Get the count of each key
for key in individual_keys:
    key_count.append({"key": key, "count": key_list.count(key)})

# Sort the list by count in descending order
key_count = sorted(key_count, key=lambda key: key['count'], reverse=True)

# Print the results
for key in key_count:
    print(f"{key['key']}\t shows up {key['count']} times")