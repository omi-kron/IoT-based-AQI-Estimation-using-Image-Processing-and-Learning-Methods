
# IoT-based AQI Estimation using Image Processing and Learning Methods

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
## Implementation

The proposed methodology for the IoT-based AQI Estimation using Image Processing and Learning Methods was executed through the following steps:

#### Preparation of Hardware Setup

Before commencing data collection, a robust hardware setup was assembled. This setup consisted of A Raspberry Pi 3B+ (Rpi 3B+) microcontroller unit (MCU) and a PiCamera are connected to it to capture and process the vehicle images. The other sensors that were interfaced with the MCU include BME280 for temperature and humidity. A SDS011 Nova PM sensor was used for measuring the PM2.5 and PM10 concentrations.

![Hardware Setup]()

#### Data Collection Drive

With the help of above hardware setup, the data collection device is prepared. The data collection device is mounted on the top of the vehicle and roamed around the city of hyderabad.

![Data Collection Device]()

The above device is made of Raspberry Pi 3B+ and extensively runs on the Python3. One needs to run following command on the Rpi to start data collection.

```Python
python3 data_collection_rpi.py

```
To run this file on boot one needs to create a service file. To create a service file automation.md should be followed.

'''
automation.md
'''


## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
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
## 👨‍🏫Authors

- [@Nitin Nilesh](https://github.com/Pi-Rasp)
- [@Om Kathalkar](https://github.com/omi-kron)

## Contact

```
nitin.nilesh@research.iiit.ac.in

om.kathalkar@research.iiit.ac.in
```
