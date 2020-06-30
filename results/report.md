# Mid-Term Report

### Data Buffer

MP.1 Data Buffer Optimization
    - Dequeue has been implemented to push new frame at the end and remove old frames at the front

### Keypoints

MP.2 Keypoint Detection
    - Comparing string value of detectorType corresponding detectors were called
    - Detectors HARRIS, FAST, BRISK, ORB, AKAZE, and SIFT has same interface and hence its easier to select according to the detectorType.

MP.3 Keypoint Removal
    - Keypoints were checked if it lies within the bounding rectangle, keypoints outside this rectange were discarded for further processing.

### Descriptors

MP.4 Keypoint Descriptors
    - Descriptors BRIEF, ORB, FREAK, AKAZE and SIFT has same interfaceinterfaceinterface and hence its easier to implement and select according to the descriptorType.
    - There is an intercompatability between the following detectors/descriptor:
        - HARRIS / AKAZE
        - FAST / AKAZE
        - BRISK / AKAZE
        - ORB / AKAZE
        - SIFT / ORB
        - SIFT / AKAZE

MP.5 Descriptor Matching
    - Descriptor Matching BF and FLANN has same interface and hence its easier to implement and select according to the matcherType.

MP.6 Descriptor Distance Ratio
    - In K-Nearest-Neighbor matching, keypoints were filtered to have nearestNeighborDistanceRatio < 0.8 to decide whether to keep best vs. second-best associated pair of keypoints.

### Performance

MP.7 Performance Evaluation 1
    The size of the resulting keypoints of task 3 gives the number of detected keypoints on the vehicle. The same has been logged to results.csv

MP.8 Performance Evaluation 2
    - In the matching step, the BF approach is used with the descriptor distance ratio set to 0.8.
    - For all possible combinations of detectors and descriptors, the size of the resulting matched keypoints of task 6 has been logged to results.csv


MP.9 Performance Evaluation 3
    For all possible combinations of detectors and descriptors, keypoints were detected and descriptor were extracted. These results has been logged to results.csv
    TOP3 detector / descriptor combination based on the time it takes for keypoint detection and descriptor extraction:
    - FAST/BRIEF
    - FAST/FREAK
    - FAST/ORB