# Using ML to Predict NFL Fantasy Football Performance
*cyeskoo, mcpark, zeisner*

![alt text](https://github.com/mooncpark/nfl_fantasy_prediction/blob/main/poster.png)

Click [here](https://docs.google.com/document/d/1NXc-nB46SxTuLS9GU_CiDFvoz0szuS7YYCcqL0AKtWE) for more information in our blog.

## Background & Motivation

NFL Fantasy Football is a game where fans simulate being NFL general managers and create teams of real NFL players to compete against other teams by scoring fantasy points. Points are awarded based on real-time game player performance, including things like yards gained and touchdowns scored. Each week, league managers will go head to head with an opponent to see which team yields the highest total fantasy score, based on the player line ups set for the given week.

The goal of our project is to provide NFL fantasy football team managers with informative and comprehensive fantasy performance prediction data. Our MVP is a dashboard that will go beyond what other platforms offer, incorporating machine learning methods to provide weekly points projections, player categorizations, injury status, and sentiment analysis. By providing prediction data and visualizations not included in other public tools and algorithms, we believe our projections can be more accurate and give users the edge they need to win their fantasy leagues.

## Purpose

This GitHub repository provides the source code to how our workflow: 
1. Extracts and processes features for model training from NFL & Twitter APIs
2. Models and predicts player fantasy performance using supervised learning techniques
3. Exports and visualizes data for users to draw performance insights and set their lineup optimally with the latest information

## Getting Started

Our models are trained primarily on NFL data sourced from the [nfl_data_py library](https://github.com/cooperdff/nfl_data_py) & Twitter data sourced from the [snscrape scraper](https://github.com/JustAnotherArchivist/snscrape).

**Installation**

~~~
pip install nfl_data_py
~~~

~~~
pip install snscrape
~~~

## Generating performance predictions

Our workflow can be executed simply by running all cells in <file_name>. We have also added the specific python functions below for step-by-step instruction.

### Data Extraction & Preparation

![alt text](https://github.com/mooncpark/nfl_fantasy_prediction/blob/main/processing.png)

1. <reference file for given step>
2. <reference file for given step>

### Modeling

1. <reference file for given step>
2. <reference file for given step>

### Visualizing Final Results

1. <reference file for exporting data to overwrite existin sheet>
2. Outputted data is stored and visualized in our [Final Dashboard MVP](https://lookerstudio.google.com/u/1/reporting/b9277c40-6df9-48d2-9cbf-346c0c52b8f3/page/iUELD)

