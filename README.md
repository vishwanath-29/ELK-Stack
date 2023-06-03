
# IoT Crop Yield Preiction

A full fledged IoT based application to monitor vitals of plants and predict the overall yield of the crop. It uses a linear regression based model to predict the yield based of various factors such as soil moisture,temperature etc.
The application has three parts to it, they are
- Sensor End
- Prediction model
- Full Stack application to integrate all

To emulate the hardware, there is a python script to randomly generate the values and send it to cloud. Instead of which we can use real sensors and computing device to process the same. The Prediction model uses a linear regression based model to predict the yield. For the final application, python based Django was used. It integrates everything into a single application, it is responsible for fetching data from cloud, processing it with the model and showing the result in a web page. 
For bringing everything together various services of Azure was used 
- Azure IoT Hub
- Azure Database
- Azure Stream
The IoT device sends data to IoT Hub, the stream fetches the data from there and posts it in a common database hosted to which the Djano application can communicates with and do all the post processing
## Tech Stack

**Client:**  HTML,CSS,Tailwind CSS,Javascript

**Server:** Python, Django

**Cloud:** Azure - IoT Hub, Stream Analytics, Azure SQL Database

## Run Locally

Before doing these, you need to configure IoT Stream and IoT Hub. The stream must take data from IoT Hub and saves it in the database. Azure Relational Database is required for the same\
Clone the project

```bash
  git clone https://github.com/vishwanath-29/Iot_Crop_yield_Prediction.git
```

Go to the directory

```bash
  cd Iot_Crop_yield_Prediction
```

Install dependencies and necessary files

```bash
  pip install -r requirements.txt
```

For the IoT End, the following command will start the script and send data to the Azure IoT Hub, do note that you require IoT Hub credentials set for sending the data 
```bash
  cd IoT_Wheat_Yield_Prediction/IoT_End
  python azure_iot_emulate.py
```

For starting the Django Applcation
```bash
  python manage.py runserver
```



## Authors

- [@Vishwanath N](https://www.github.com/vishwanath-29)
- [@Vishal GK](https://www.github.com/gkvishal7)
- [@Varun ](https://www.github.com/varunbalaji1303)

