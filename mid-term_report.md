# Mid-Term Report

MP.0 Mid-Term Report 
    - Provide a Writeup / README that includes all the rubric points and how you addressed each one. You can submit your writeup as markdown or pdf.

### Data Buffer

MP.1 Data Buffer Optimization
    - Dequeue has been implemented to push new frame at the end and remove old frames at the front


### Keypoints

MP.2 Keypoint Detection
    - Detectors HARRIS, FAST, BRISK, ORB, AKAZE, and SIFT has same interface and hence its easier to select according to the detectorType.

MP.3 Keypoint Removal
    - Keypoints were checked if it lies within the bounding rectangle, keypoints outside this rectange were discarded for further processing.

### Descriptors

MP.4 Keypoint Descriptors
    - Descriptors BRIEF, ORB, FREAK, AKAZE and SIFT has same interface and hence its easier to implement and select according to the descriptorType.
    - There is an intercompatability within some detectors output, but ORB and AKAZE descriptor works only with their respective output.

MP.5 Descriptor Matching
    - Descriptor Matching BF and FLANN has same interface and hence its easier to implement and select according to the matcherType.

MP.6 Descriptor Distance Ratio
    - In K-Nearest-Neighbor matching, keypoints were filtered to have nearestNeighborDistanceRatio < 0.8 to decide whether to keep best vs. second-best associated pair of keypoints.

<!-- instructions for the task, following needs to replaced by how solutions are arrived -->
### Performance

MP.7 Performance Evaluation 1
    - Count the number of keypoints on the preceding vehicle for all 10 images and take note of the distribution of their neighborhood size. Do this for all the detectors you have implemented.

MP.8 Performance Evaluation 2
    - Count the number of matched keypoints for all 10 images using all possible combinations of detectors and descriptors. In the matching step, the BF approach is used with the descriptor distance ratio set to 0.8.

MP.9 Performance Evaluation 3
    - Log the time it takes for keypoint detection and descriptor extraction. The results must be entered into a spreadsheet and based on this data, the TOP3 detector / descriptor combinations must be recommended as the best choice for our purpose of detecting keypoints on vehicles.