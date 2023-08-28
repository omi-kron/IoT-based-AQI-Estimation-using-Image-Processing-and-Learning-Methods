
# IoT-based AQI Estimation using Image Processing and Learning Methods

![Algorithmic Pipeline](/algorithm_pipeline.png)

Air pollution is a concern to the health of all
living beings. It is essential to check on the quality of air in
the surroundings. This article presents an IoT-based real-time
air quality index (AQI) estimation technique using images and
weather sensors on Indian rods. A mixture of image features,
i.e., traffic density, visibility, and sensor features, i.e., temperature
and humidity, were used to predict the AQI. Object detection and
localization-based Deep Learning (DL) method along with image
processing techniques were used to extract image features while
an Machine Learning (ML) model was trained on those features
to estimate the AQI. In order to conduct this experiment, a
dataset containing 5048 images along with co-located AQI values
across different seasons was collected by driving on the roads
of Hyderabad city in India. The experimental results report an
overall accuracy of 82% for AQI prediction.


## Novel Contributions of this work

- An IoT based novel methodology is proposed to estimate the real-time AQI into five levels using traffic images and weather parameters. 
- To the best of authors’ knowledge, this work is the first of its kind to achieve this on Indian roads.
- An entirely new traffic dataset is collected on Indian roads containing 5048 images and related weather data with co-located ground truth PM values. The dataset contains samples across the Indian city of Hyderabad in different seasons.
- The proposed method achieved overall 82% accuracy considering PM variation due to season.


## 🌱Contents

1. [Implementation](#Implementation)
2. [Installation](#Installation)
3. [Citation](#Citation)
4. [Paper](#Paper)
5. [Authors](#Authors)
## Installation

To clone this repository, 

```bash
git clone omi-kron/IoT-based-AQI-Estimation-using-Image-Processing-and-Learning-Methods
```
After that run if you are using pip,

```bash
pip install -r requirements.txt
```

and in case of conda,

```bash
conda env create -f environment.yml

```
After creating the environment, you can activate it with:

```bash
conda activate my_project_env
```
## Implementation

The proposed methodology for the IoT-based AQI Estimation using Image Processing and Learning Methods was executed through the following steps:

#### Preparation of Hardware Setup

Before commencing data collection, a robust hardware setup was assembled. This setup consisted of A Raspberry Pi 3B+ (Rpi 3B+) microcontroller unit (MCU) and a PiCamera are connected to it to capture and process the vehicle images. The other sensors that were interfaced with the MCU include BME280 for temperature and humidity. A SDS011 Nova PM sensor was used for measuring the PM2.5 and PM10 concentrations.

![Hardware Setup](/hardware.png)

#### Data Collection Drive

With the help of above hardware setup, the data collection device is prepared. The data collection device is mounted on the top of the vehicle and roamed around the city of hyderabad.

![Data Collection Device](/AQI_node.png)

The above device is made of Raspberry Pi 3B+ and extensively runs on the Python3. One needs to run following command on the Rpi to start data collection.

```Python
python3 data_collection_rpi.py

```
To run this file on boot one needs to create a service file. To create a service file, ***automation.md*** can be followed.

```
automation.md
```

The GPS coordinates are collected using the android phone with the application named GPS Logger installed in it: [GPS Logger](https://play.google.com/store/apps/details?id=eu.basicairdata.graziano.gpslogger&hl=en&gl=US).

### Sensor Data Calibration and Preprocessing

The sensor data which is collected using the data collection device is need to be calibrated and pre-processed. The pre-processing involves estimating the AQI from the PM2.5 and PM10 values which are collected using the sensor. The preprocessing is done in the ipython notebook file called,

```
sensor_data_preprocessing.ipynb
```

### Image Features Extraction

To detect the vehicles from a given image,
You-Only-Look-Once version 5 (YOLOv5) was trained
on Indian Driving Dataset (IDD). 

### Final Dataset Preparation

The final dataset was prepared using concatenation of sensor features and image features. This was acheived using python and dataset is also cleaned as there are few outliers in it, that might affect the accuracy of the overall accuracy of the classification model. 
 



## Experiments and Results

For a comprehensive understanding of the conducted experiments and the outcomes achieved, I encourage you to refer to the accompanying paper. In particular, you can gain detailed insights into all the experiments and their corresponding results by reviewing the content presented in the IPython notebook titled "main_script.ipynb". This notebook serves as a comprehensive resource, providing thorough explanations and analyses of each experiment, making it an invaluable reference to delve into the research's intricacies and findings.

```
main_script.ipynb
```
## Citation

```
  @INPROCEEDINGS{10152272,
  author={Nitin Nilesh, Ishan Patwardhan, Jayati Narang and Sachin Chaudhari},
  booktitle={2022 IEEE 8th World Forum on Internet of Things (WF-IoT)}, 
  title={IoT-based AQI Estimation using Image Processing and Learning Methods}, 
  year={2022},
  volume={},
  number={},
  pages={1-5},
  doi={10.1109/WF-IoT54382.2022.10152272}}
```
## License

The code, platform, and dataset are made available for academic research purpose only.

## Paper

[Official Version of paper presented at 2022 IEEE 8th World Forum on Internet of Things (WF-IoT), Yokohama, Japan.](https://ieeexplore.ieee.org/document/10152272)
## Tools 

- [Angry IP Scanner]() 
- [VNC Viewer]()
- [Raspberry Pi]()
- [GPS Logger]()
- [YoloV5]()
- [Google Draw]()
## 👨‍🏫Authors

- [@Nitin Nilesh](https://github.com/Pi-Rasp)
- [@Om Kathalkar](https://github.com/omi-kron)
- [@Shreyash Gujar](https://github.com/ShreyashGujar)
## Contact

```
nitin.nilesh@research.iiit.ac.in
om.kathalkar@research.iiit.ac.in
```
