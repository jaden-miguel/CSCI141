# Name: Jaden Miguel
# Date: May 30, 2019
# Purpose: Cancer classifier code, as discussed in handout A5

###############################################################################
# GLOBAL CONSTANT
# For use as dictionary keys
# You can use this list throughout the program without passing it to a function
# DO NOT MODIFY
ATTRS = ["ID", "radius", "texture", "perimeter", "area", "smoothness", "compactness", "concavity", "concave", "symmetry", "fractal", "class"]

###############################################################################
def make_training_set(filename):
    """Read training data from the file whose path is filename.
    Return a list of records, where each record is a dictionary
    containing a value for each of the 12 keys in ATTRS.
    """
    training_records = []
    for line in open(filename, 'r'):
        if '#' in line:
            continue
        line = line.strip('\n')
        line_list = line.split(',')
        record = {}
        record[ATTRS[0]] = int(line_list[0].strip())
        for i in range(1, 11):
            record[ATTRS[i]] = float(line_list[i])
        record[ATTRS[11]] = line_list[31].strip()
        training_records.append(record)
    return training_records

def make_test_set(filename):
    """Read test data from the file whose path is filename.
    Return a list with the same form as the training
    set, except that each dictionary has an additional
    key "prediction" initialized to "none" that will be
    used to store the label predicted by the classifier.
    """
    test_records = make_training_set(filename)
    for record in test_records:
        record["prediction"] = "none"
    return test_records

def train_classifier(training_records):
    """Return a dict containing the midpoint between averages
    among each class (malignant and benign) of each attribute.
    """
    malignant_records = {key: [] for key in ATTRS[1:11]}
    benign_records = {key: [] for key in ATTRS[1:11]}
    malignant_avgs = {}
    benign_avgs = {}
    midpoint_records = {}
    for record in training_records:
        if record['class'] == 'M':
            for key in malignant_records.keys():
                malignant_records[key].append(record[key])
        elif record['class'] == 'B':
            for key in benign_records.keys():
                benign_records[key].append(record[key])
    for key in malignant_records:
        malignant_avgs[key] = sum(malignant_records[key]) / len(malignant_records[key])
    for key in benign_records:
        benign_avgs[key] = sum(benign_records[key]) / len(benign_records[key])
    for key in malignant_avgs:
        midpoint_records[key] = (malignant_avgs[key] + benign_avgs[key]) / 2
    return midpoint_records

def classify(test_records, classifier):
    """Classify each record in test_records as 'M' or 'B' based on the classifier's threshold."""
    for record in test_records:
        threshold = 0
        for key in ATTRS[1:11]:
            if record[key] > classifier[key]:
                threshold += 1
        record['prediction'] = 'M' if threshold >= 5 else 'B'

def report_accuracy(test_records):
    """Print the accuracy of the predictions."""
    correct_predictions = sum(1 for record in test_records if record['prediction'] == record['class'])
    accuracy = (correct_predictions / len(test_records)) * 100
    print(f"Classifier accuracy: {accuracy}%")

def get_patient_rec(test_records, user_id):
    """Find and return the patient record by ID, or print a message if not found."""
    for record in test_records:
        if record['ID'] == user_id:
            return record
    print("Your ID is not in the data set.")
    return None

def get_vote(classifier, record):
    """Return a dictionary indicating votes for each attribute as 'Malignant' or 'Benign'."""
    votes = {}
    for key in ATTRS[1:11]:
        votes[key] = 'Malignant' if record[key] > classifier[key] else 'Benign'
    return votes

def print_table(classifier, record):
    """Print a detailed table comparing patient values, classifier midpoints, and votes."""
    votes = get_vote(classifier, record)
    print("Attribute".rjust(15), "Patient".rjust(12), "Classifier".rjust(15), "Vote".rjust(12))
    for key in ATTRS[1:11]:
        patient_value = f"{record[key]:12.4f}"
        classifier_value = f"{classifier[key]:12.4f}"
        print(key.rjust(15), patient_value.rjust(12), classifier_value.rjust(15), votes[key].rjust(12))
    diagnosis = 'Malignant' if record['prediction'] == 'M' else 'Benign'
    print("\nClassifier's diagnosis:", diagnosis)

def check_patients(test_records, classifier):
    """Interactive function to get patient details based on user input."""
    while True:
        identifier = input("Enter a patient ID to see classification details or 'quit' to exit: ")
        if identifier.lower() == "quit":
            break
        try:
            user_id = int(identifier)
            record = get_patient_rec(test_records, user_id)
            if record:
                print_table(classifier, record)
            else:
                print("Patient ID not found.")
        except ValueError:
            print("Please enter a valid integer ID or 'quit' to exit.")

# Example usage
if __name__ == "__main__":
    # Follow the steps as outlined in the main program block
    pass# Name: Jaden Miguel
# Date: May 30, 2019
# Purpose: Cancer classifier code, as discussed in handout A5

###############################################################################
# GLOBAL CONSTANT
# For use as dictionary keys
# You can use this list throughout the program without passing it to a function
# DO NOT MODIFY
ATTRS = ["ID", "radius", "texture", "perimeter", "area", "smoothness", "compactness", "concavity", "concave", "symmetry", "fractal", "class"]

###############################################################################
def make_training_set(filename):
    """Read training data from the file whose path is filename.
    Return a list of records, where each record is a dictionary
    containing a value for each of the 12 keys in ATTRS.
    """
    training_records = []
    for line in open(filename, 'r'):
        if '#' in line:
            continue
        line = line.strip('\n')
        line_list = line.split(',')
        record = {}
        record[ATTRS[0]] = int(line_list[0].strip())
        for i in range(1, 11):
            record[ATTRS[i]] = float(line_list[i])
        record[ATTRS[11]] = line_list[31].strip()
        training_records.append(record)
    return training_records

def make_test_set(filename):
    """Read test data from the file whose path is filename.
    Return a list with the same form as the training
    set, except that each dictionary has an additional
    key "prediction" initialized to "none" that will be
    used to store the label predicted by the classifier.
    """
    test_records = make_training_set(filename)
    for record in test_records:
        record["prediction"] = "none"
    return test_records

def train_classifier(training_records):
    """Return a dict containing the midpoint between averages
    among each class (malignant and benign) of each attribute.
    """
    malignant_records = {key: [] for key in ATTRS[1:11]}
    benign_records = {key: [] for key in ATTRS[1:11]}
    malignant_avgs = {}
    benign_avgs = {}
    midpoint_records = {}
    for record in training_records:
        if record['class'] == 'M':
            for key in malignant_records.keys():
                malignant_records[key].append(record[key])
        elif record['class'] == 'B':
            for key in benign_records.keys():
                benign_records[key].append(record[key])
    for key in malignant_records:
        malignant_avgs[key] = sum(malignant_records[key]) / len(malignant_records[key])
    for key in benign_records:
        benign_avgs[key] = sum(benign_records[key]) / len(benign_records[key])
    for key in malignant_avgs:
        midpoint_records[key] = (malignant_avgs[key] + benign_avgs[key]) / 2
    return midpoint_records

def classify(test_records, classifier):
    """Classify each record in test_records as 'M' or 'B' based on the classifier's threshold."""
    for record in test_records:
        threshold = 0
        for key in ATTRS[1:11]:
            if record[key] > classifier[key]:
                threshold += 1
        record['prediction'] = 'M' if threshold >= 5 else 'B'

def report_accuracy(test_records):
    """Print the accuracy of the predictions."""
    correct_predictions = sum(1 for record in test_records if record['prediction'] == record['class'])
    accuracy = (correct_predictions / len(test_records)) * 100
    print(f"Classifier accuracy: {accuracy}%")

def get_patient_rec(test_records, user_id):
    """Find and return the patient record by ID, or print a message if not found."""
    for record in test_records:
        if record['ID'] == user_id:
            return record
    print("Your ID is not in the data set.")
    return None

def get_vote(classifier, record):
    """Return a dictionary indicating votes for each attribute as 'Malignant' or 'Benign'."""
    votes = {}
    for key in ATTRS[1:11]:
        votes[key] = 'Malignant' if record[key] > classifier[key] else 'Benign'
    return votes

def print_table(classifier, record):
    """Print a detailed table comparing patient values, classifier midpoints, and votes."""
    votes = get_vote(classifier, record)
    print("Attribute".rjust(15), "Patient".rjust(12), "Classifier".rjust(15), "Vote".rjust(12))
    for key in ATTRS[1:11]:
        patient_value = f"{record[key]:12.4f}"
        classifier_value = f"{classifier[key]:12.4f}"
        print(key.rjust(15), patient_value.rjust(12), classifier_value.rjust(15), votes[key].rjust(12))
    diagnosis = 'Malignant' if record['prediction'] == 'M' else 'Benign'
    print("\nClassifier's diagnosis:", diagnosis)

def check_patients(test_records, classifier):
    """Interactive function to get patient details based on user input."""
    while True:
        identifier = input("Enter a patient ID to see classification details or 'quit' to exit: ")
        if identifier.lower() == "quit":
            break
        try:
            user_id = int(identifier)
            record = get_patient_rec(test_records, user_id)
            if record:
                print_table(classifier, record)
            else:
                print("Patient ID not found.")
        except ValueError:
            print("Please enter a valid integer ID or 'quit' to exit.")

# Example usage
if __name__ == "__main__":
    # Follow the steps as outlined in the main program block
    pass
