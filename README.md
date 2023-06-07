# RED-ScheduleManager

Welcome to the repository of the **Schedule Manager** project. 
This project has been created by **team number 9** of the [R&D course of Radboud University](https://www.ru.nl/courseguides/science/vm/osirislinks/ipc/nwi-ipc030/).
Our application is a website build in [Django](https://www.djangoproject.com/) that allow its user to manage its schedule in an efficient way.

## 💡 Table of content

  1. [🏁 Features](#🏁-features)
  2. [🔍 Overview](#🔍-overview)
  3. [🚀 Setup](#🚀-setup)
  4. [💾 Database](#💾-database)
  5. [💛 Contributors](#💛-contributors)

## 🏁 Features

List of features implemented and in development:
- [x] View of the schedule
- [x] View of the schedule editor
- [x] Editing the schedule
- [x] Algorithm that schedule your working time
- [x] Adding preferences for the algorithm
- [ ] Connect the University schedule to the app
- [ ] Connect the University assignment to the app
- [ ] Ask for help to a TA

## 🔍 Overview

The website is composed of `two main parts`.
The first one is the page that you get when you open the website.

*HERE INSERT SCREENSHOT*

This part allow the user to **edit the events** of its schedule. 
The user can add **Appointments** *(Doctor, lecture...)* and **Tasks** *(assignments, objective with deadline...)*  to it's table. \
You can also add your **preferences** for the scheduler, for example your sleeping time. \
When the user clicks on the `Home` button at the bottom right, it will be able to visualize its schedule.

*HERE INSERT SCREENSOT*

User can go through all the weeks by click on the `Arrow` buttons on top right corner of the screen. 

## 🚀 Setup

To lauch the website on your device, you can copy this repository and use the following commands:

```bash
cd scheduler
python manage.py runserver
```

## 💾 Database

The database used to store the data of the schedule is [sqlite3](https://www.sqlite.org/index.html).  
In a django project sqlite3 is the default database. The models included in the database are designed in the `playground/model.py` file. Please see the [Django model documentation](https://docs.djangoproject.com/en/4.2/topics/db/models/) for more information. 

## 💛 Contributors

[<img src="screenshots/Kiril.png" alt="Kiril" width="50" height="50">](https://gitlab.science.ru.nl/kvoigtlaender)
[<img src="screenshots/Theoo.png" alt="Théo" width="50" height="50">](https://gitlab.science.ru.nl/tlavandier)
[<img src="screenshots/ping.png" alt="Ping" width="50" height="50">](https://gitlab.science.ru.nl/pvogels)
[<img src="screenshots/kareem.png" alt="Kareem" width="50" height="50">](https://gitlab.science.ru.nl/kquillettes)



