# Payments Script
This project is created by [Juan Graciano](https://github.com/JuanGraciano).

#### -- Project Status: completed

## Project Intro/Objective
As part of the recruitment process we would like you to solve a programming exercise to evaluate your skills in Python and later we will schedule a meeting to discuss your solution. It’s important to notice that you can not use any external library to solve the exercise, however you can add any dependency for testing purposes like JUnit, Mockito, etc.

## Project Description

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:
- Monday - Friday
    - 00:01 - 09:00 25 USD
    - 09:01 - 18:00 15 USD
    - 18:01 - 00:00 20 USD
- Saturday and Sunday
    - 00:01 - 09:00 30 USD
    - 09:01 - 18:00 20 USD
    - 18:01 - 00:00 25 USD

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:
- MO: Monday
- TU: Tuesday
- WE: Wednesday
- TH: Thursday
- FR: Friday
- SA: Saturday
- SU: Sunday

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.
Output: indicate how much the employee has to be paid
For example:
- Case 1:
    - INPUT
        RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
    - OUTPUT:
        The amount to pay RENE is: 215 USD

- Case 2:
    - INPUT
        ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
    - OUTPUT:
        The amount to pay ASTRID is: 85 USD

### Technologies
* Python 3

## Needs of this project

- Install python 3
- Install pip 3

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. install requirements. The requirements are in requirements.txt like:
```
    pip install -r requirements.txt
```
3. Run the project
```
    python app.py
```

## Configurations

- ###### config.py file
    - properties:

        * CALENDAR_1: Represents hourly payments by range of days.
        * CALENDAR_2: Represents hourly payments for each day.
        * DAY_ABBR: Represents the abbreviations of the days of the week.

## Project architecture

* [Use case diagram](https://drive.google.com/file/d/1tVuUBnerbislf-Y7GlZhcZBOgGRZ9wL-/view?usp=sharing)
* [flow chart](https://drive.google.com/file/d/1F7Ir9vPo56CaaXLeZ07jPEMH7WCBboI3/view?usp=sharing)
* [Component diagram](https://drive.google.com/file/d/1hJXEp91M0uv45PwL5ZDu4J7D-xylAYyu/view?usp=sharing)

## Project folder structure

```
├──  doc ->  Contains the documents describing the architecture and the script.
├──  src
    ├──  services -> Contains the required script services.
    ├──  test -> Contains the tests for each of the services and validate their execution.
    ├──  utils -> Contains the basic functions of the script.
    ├──  config.py -> Payments configuration file.
├──  app.py -> Main script file. Contains the execution pipeline
├──  READMED.md
├──  requirements.txt
├──  test_cases.txt -> File with use cases for testing the script. 
```

## Contributing Members
Developer (Contacts) : [Juan Graciano](https://github.com/JuanGraciano)