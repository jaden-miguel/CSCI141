# Name: Jaden Miguel
# Date: May 30, 2019
# Purpose: Cancer classifier code, as discussed in handout A5

###############################################################################
# GLOBAL CONSTANT
# For use as dictionary keys
# You can use this list throughout the program without passing it to a function
# DO NOT MODIFY
ATTRS = [
    "ID", "radius", "texture", "perimeter", "area", "smoothness",
    "compactness", "concavity", "concave", "symmetry", "fractal", "class"
]
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
    Return a list with the same form as the training set, except that each dictionary has an additional
    key "prediction" initialized to "none" that will be used to store the label predicted by the classifier.
    """
    test_records = make_training_set(filename)
    for record in test_records:
        record["prediction"] = "none"
    return test_records

def train_classifier(training_records):
    """Return a dict containing the midpoint between averages among each class (malignant and benign) of each attribute.
    (See the A5 writeup for a more complete description)
    Precondition: training_records is a list of patient record dictionaries, each of which has the keys
    in the global variable ATTRS.
    Postcondition: the returned dict has midpoint values calculated from the training set for all 10 attributes except
    "ID" and "class".
    """
    malignant_records = {key: [] for key in ATTRS[1:11]}
    benign_records = {key: [] for key in ATTRS[1:11]}
    for record in training_records:
        if record['class'] == 'M':
            for key in ATTRS[1:11]:
                malignant_records[key].append(record[key])
        elif record['class'] == 'B':
            for key in ATTRS[1:11]:
                benign_records[key].append(record[key])
    
    malignant_avgs = {key: sum(vals) / len(vals) for key, vals in malignant_records.items()}
    benign_avgs = {key: sum(vals) / len(vals) for key, vals in benign_records.items()}
    midpoint_records = {key: (malignant_avgs[key] + benign_avgs[key]) / 2 for key in ATTRS[1:11]}
    
    return midpoint_records

def classify(test_records, classifier):
    """Use the given classifier to make a prediction for each record in test_records, a list of dictionary patient records
    with the keys in the global variable ATTRS. A record is classified as malignant if at least 5 of the attribute values are
    above the classifier's threshold.
    Precondition: classifier is a dict with midpoint values for all keys in ATTRS except "ID" and "class".
    Postcondition: each record in test_records has the "prediction" key filled in with the predicted class, either "M" or "B".
    """
    for record in test_records:
        threshold = sum(record[key] > classifier[key] for key in ATTRS[1:11])
        record['prediction'] = 'M' if threshold >= 5 else 'B'

def report_accuracy(test_records):
    """Print the accuracy of the predictions made by the classifier on the test set as a percentage of correct predictions.
    Precondition: each record in the test set has a "prediction" key that maps to the predicted class label ("M" or "B"), as well
    as a "class" key that maps to the true class label.
    """
    correct_predictions = sum(1 for record in test_records if record['prediction'] == record['class'])
    accuracy = (correct_predictions / len(test_records)) * 100
    print(f"Classifier accuracy: {accuracy}%")

def get_patient_rec(test_records, user_id):
    """Find the respective patient record from the ID number.
    Precondition: patient ID is an integer.
    """
    for record in test_records:
        if record['ID'] == user_id:
            return record
    print("Your ID is not in the data set.")

def get_vote(classifier, record):
    """Create a new dict to store votes, and then to proceed to assign string equivalents to each related value.
    Necessary for the correct output of the table.
    """
    votes = {}
    for key in ATTRS[1:11]:
        votes[key] = 'Malignant' if float(record[key]) > float(classifier[key]) else 'Benign'
    return votes

def change_diag(record):
    """Check the prediction of the record and then returning the correct string equivalent."""
    return 'Malignant' if record['prediction'] == 'M' else 'Benign'

def print_table(classifier, record):
    """Create a table for each attribute and follow the handout of A5. Each value is structured in its best way to be lined up,
    right justified, and the correct value as stated.
    """
    votes = get_vote(classifier, record)
    print("Attribute".rjust(15), "Patient".rjust(12), "Classifier".rjust(15), "Vote".rjust(12))
    for key in ATTRS[1:11]:
        print(key.rjust(15), 
              str("{:12.4f}".format(record[key])).rjust(12),
              str("{:12.4f}".format(classifier[key])).rjust(15), 
              votes[key].rjust(12))
    print("\n", "Classifier's diagnosis:", change_diag(record))

def check_patients(test_records, classifier):
    """Prompt the user for a Patient ID until the user enters "quit". For each patient ID entered, search the test set for the
    record with that ID, print a message and prompt the user again. If the patient is in the test set, print a table: for each
    attribute, list the name, the patient's value, the classifier's midpoint value, and the vote cast by the classifier. After the
    table, output the final prediction made by the classifier. If the patient ID is not in the test set, print a message and repeat
    the prompt. Assume the user enters an integer or "quit" when prompted for the patient ID.
    """
    identifier = ''
    while identifier != "quit":
        identifier = input("Enter a patient ID to see classification details: ")
        if identifier == "quit":
            break
        try:
            user_id = int(identifier)
            record = get_patient_rec(test_records, user_id)
            if record:
                print_table(classifier, record)
            else:
                print("No record found for ID:", user_id)
        except ValueError:
            print("Invalid input. Please enter a valid patient ID or 'quit' to exit.")

if __name__ == "__main__":
    # Main program execution
    print("Reading in training data...")
    training_data_file = "cancerTrainingData.txt"
    training_set = make_training_set(training_data_file)
    print("Done reading training data.")

    print("Reading in test data...")
    test_data_file = "cancerTestingData.txt"
    test_set = make_test_set(test_data_file)
    print("Done reading test data.\n")

    print("Training classifier...")
    classifier = train_classifier(training_set)
    print("Classifier cutoffs:")
    for key in ATTRS[1:11]:
        print(f" {key}: {classifier[key]}")
    print("Done training classifier.\n")

    print("Making predictions and reporting accuracy")
    classify(test_set, classifier)
    report_accuracy(test_set)
    print("Done classifying.\n")

    check_patients(test_set, classifier)
