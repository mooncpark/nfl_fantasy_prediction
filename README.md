# Using ML to Predict NFL Fantasy Football Performance
*cyeskoo, mcpark, zeisner*

![alt text](https://github.com/mooncpark/nfl_fantasy_prediction/blob/main/poster.png)

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

## How to use notebooks

