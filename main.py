#!/usr/bin/env python
from flask import Flask, render_template, flash, request, jsonify, Markup

# model constants
# set up constants from linear regressor model 
INTERCEPT = -119.061877
COEF_HOLIDAY = -29.096613   # if day is holiday or not
COEF_HOUR = 8.626766        # hour (0 to 23)
COEF_SEASON_1 = 3.523756    # 1:spring 
COEF_SEASON_2 = -3.808865   # 2:summer
COEF_SEASON_3 = -42.697445  # 3:fall
COEF_SEASON_4 = 42.982554   # 4:winter
COEF_TEMP = 425.523181      # normalized temp in Celsius -8 to +39

# data mean values
MEAN_HOLIDAY = 0        # if day is holiday or not (mean is closer to 0 so 0)
MEAN_HOUR = 11.6        # hour (0 to 23)
MEAN_SEASON_1 = 0       # 1:spring -- these are binary so don't use mean, instead pick one season
MEAN_SEASON_2 = 0       # 2:summer
MEAN_SEASON_3 = 1       # 3:fall
MEAN_SEASON_4 = 0       # 4:winter
MEAN_TEMP = 0.4967      # normalized temp in Celsius -8 to +39
 
app = Flask(__name__)
 
@app.route("/", methods=['POST', 'GET'])
def index():
    # on load set form with defaults
    return render_template('index.html',
            mean_holiday = MEAN_HOLIDAY,
            mean_hour = MEAN_HOUR,
            mean_sesaon1 = MEAN_SEASON_1,
            mean_sesaon2 = MEAN_SEASON_2,
            mean_sesaon3 = MEAN_SEASON_3,
            mean_sesaon4 = MEAN_SEASON_4,
            mean_temp = MEAN_TEMP,
            model_intercept = INTERCEPT,
            model_holiday = COEF_HOLIDAY,
            model_hour = COEF_HOUR,
            model_season1 = COEF_SEASON_1,
            model_season2 = COEF_SEASON_2,
            model_season3 = COEF_SEASON_3,
            model_season4 = COEF_SEASON_4,
            model_temp = COEF_TEMP)


# when running app locally
if __name__=='__main__':
      app.run(debug=False)
