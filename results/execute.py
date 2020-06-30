import os, sys


def main():
    
    detector_types = ["HARRIS", "FAST", "BRISK", "ORB", "AKAZE", "SIFT"]
    descriptor_types = ["BRIEF", "ORB", "FREAK", "AKAZE", "SIFT"]
    matcher_types = "MAT_BF" # "MAT_FLANN"
    matcher_descriptor_type = "DES_BINARY" # "DES_HOG"
    matcher_selectorType = "SEL_KNN" # SEL_NN
    
    if len(sys.argv) == 2:
        result_file = sys.argv[1]
    else: 
        result_file = "{}/results.csv".format(os.getcwd())
        
    for detector in detector_types:
        for descriptor in descriptor_types:
            cmd = "../build/2D_feature_tracking {} {} {} {} {} {}".format(detector, descriptor, 
                                                                          matcher_types, matcher_descriptor_type, 
                                                                          matcher_selectorType, result_file)
            os.system(cmd)
            # print(cmd)

if __name__ == "__main__":
    main()