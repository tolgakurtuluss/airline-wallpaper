## 🖼️ Set Airline Wallpaper Using Selenium and Python
This is a Python script that uses Selenium to set an airplane photo as your desktop wallpaper.

## 📋 Requirements
To use this script, you will need to have the following software installed on your machine:

* Python 3
* Selenium
* Pillow
* ChromeDriver
* Google Chrome

## 🚀 Installation

1. Clone the repository to your local machine:
```
git clone https://github.com/tolgakurtuluss/airline-wallpaper.git
```

2. Install the required Python libraries:
```
pip install selenium pillow
```
3. Download the ChromeDriver executable from the [official website](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in the project folder.
4. Run the script:
```
python airline_wallpaper.py
```


## ⚙️ How it works

1. The script uses Selenium to open a random airplane photo from [JetPhotos](https://www.jetphotos.com/).
2. It then downloads the photo and saves it to a local file.
3. Finally, it sets the downloaded photo as your desktop wallpaper.

## 🔧 Customization

You can customize the script by changing the following variables:

- `WALLPAPER_PATH`: the path to the local file where the downloaded photo will be saved.
- `PHOTO_ID_RANGE`: the range of photo IDs to choose from on JetPhotos. By default, the script selects a random ID between 10844358 and 10864383.

## 🚫 Limitations

- This script only works on Windows.
- The script may not work if your computer is locked or if you have multiple virtual desktops.
- JetPhotos may block your IP address if you download too many photos in a short period of time.

## ⚖️ License
All rights are reserved by JetPhotos.com.
