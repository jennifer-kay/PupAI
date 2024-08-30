from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames 
    of the image files. These pet image labels are used to check 
    the accuracy of the labels returned by the classifier function, 
    since the filenames of the images contain the true identity of
    the pet in the image.
    
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains the following item:
         index 0 = pet image label (string)
    """
    
    filename_list = listdir(image_dir)

    results_dic = {}
    
    for filename in filename_list:
        # Skip files that start with a dot (hidden files)
        if filename.startswith('.'):
            continue
        
        lower_filename = filename.lower()
        word_list = lower_filename.split('_')
        
        pet_name = ''
        for word in word_list:
            if word.isalpha():  # Only include alphabetic words in the pet name
                pet_name += word + ' '
        
        pet_name = pet_name.strip()  # Remove any trailing whitespace
        
        # Check if the filename already exists in the dictionary
        if filename not in results_dic:
            results_dic[filename] = [pet_name]
        else:
            print(f"Warning: {filename} already exists in the dictionary.")
    
    return results_dic
