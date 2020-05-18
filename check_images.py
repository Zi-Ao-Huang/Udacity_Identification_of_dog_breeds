#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# PROGRAMMER: ZiAoHuang
# DATE CREATED: 05172020
# REVISED DATE: 05182020
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task.
#          Note that the true identity of the pet (or object) in the image is
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep
# Imports print functions that check the lab
from print_functions_for_lab_checks import *
# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    start_time = time() # Collecting start time

    in_arg = get_input_args() # This function returns command line arguments
    check_command_line_arguments(in_arg) # Checks command line argument

    results = get_pet_labels(in_arg.dir) # Creates the results dictionary
    check_creating_pet_image_labels(results) # Checks pet images in the results Dictionary

    # Creates Classifier Labels with classifier function, Compares Labels,
    # and adds these results to the results dictionary - results
    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results) # Checks Results Dictionary using results

    adjust_results4_isadog(results, in_arg.dogfile) # Adjusts the results dictionary
    check_classifying_labels_as_dogs(results) # Checks Results Dictionary for is-a-dog adjustment

    results_stats = calculates_results_stats(results) # Calculates results of run
    check_calculating_results(results, results_stats) # Checks Results Statistics Dictionary

    print_results(results, results_stats, in_arg.arch, True, True) #Prints summary results

    end_time = time() # Collecting end time

    # Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )


# Call to main function to run the program
if __name__ == "__main__":
    main()
