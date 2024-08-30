def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifier labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a percentage or a count) where the key is the statistic's 
                   name (starting with 'pct' for percentage or 'n' for count)
                   and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    

    # Print model architecture used
    print(f"\n\n*** Results Summary for CNN Model Architecture {model.upper()} ***")

    # Print total number of images, dog images, and non-dog images
    print(f"N Images: {results_stats_dic['n_images']}")
    print(f"N Dog Images: {results_stats_dic['n_dogs_img']}")
    print(f"N Not-a-Dog Images: {results_stats_dic['n_notdogs_img']}")

    # Print summary statistics (percentages)
    print("\nSummary Statistics:")
    for key in results_stats_dic:
        # Print only percentages
        if key.startswith('pct'):
            print(f"{key}: {results_stats_dic[key]:.1f}%")

    # If print_incorrect_dogs is True and there were misclassified dogs
    if print_incorrect_dogs and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
        print("\nINCORRECT Dog/NOT Dog Assignments:")

        # Process through the results dictionary
        for key in results_dic:
            # Pet Image Label is a Dog - Classified as NOT-A-DOG or 
            # Pet Image Label is NOT-a-Dog - Classified as a-DOG
            if sum(results_dic[key][3:]) == 1:
                print(f"Real: {results_dic[key][0]}   Classifier: {results_dic[key][1]}")

    # If print_incorrect_breed is True and there were misclassified dog breeds
    if print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        print("\nINCORRECT Dog Breed Assignment:")

        # Process through the results dictionary
        for key in results_dic:
            # Pet Image Label is-a-Dog, but breed is misclassified
            if (results_dic[key][3] == 1 and results_dic[key][2] == 0):
                print(f"Real: {results_dic[key][0]}   Classifier: {results_dic[key][1]}")

    # End of function
    return None
