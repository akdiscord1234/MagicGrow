#Flask Webserver
from flask import Flask
import webserver
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to the MagicGrow Webserver Api!'

#Getting current values

@app.route('/get_value_temperature')
def temperature_modify():
    return webserver.get_current_value("temperature")

@app.route('/get_value_pH')
def pH_modify():
    return webserver.get_current_value("pH")

@app.route('/get_value_temperature')
def temperature_modify():
    return webserver.get_current_value("temperature")

@app.route('/get_value_EC')
def EC_modify():
    return webserver.get_current_value("EC")

#Changing Plug On/Off

#Water Pump

#Water Pump Down
@app.route('/water_pump_down_on')
def EC_modify_down_pump_on():
    webserver.WaterPumpControls("down_on")
    return "done"

@app.route('/water_pump_down_off')
def EC_modify_down_pump_off():
    webserver.WaterPumpControls("down_off")
    return "done"

@app.route('/water_pump_down_toggle')
def EC_modify_down_pump_toggle():
    webserver.WaterPumpControls("down_toggle")
    return "done"

#Water Pump Up

@app.route('/water_pump_up_on')
def EC_modify_up_pump_on():
    webserver.WaterPumpControls("up_on")
    return "done"

@app.route('/water_pump_up_off')
def EC_modify_up_pump_off():
    webserver.WaterPumpControls("up_off")
    return "done"

@app.route('/water_pump_up_toggle')
def EC_modify_up_pump_toggle():
    webserver.WaterPumpControls("up_toggle")
    return "done"

#pH Pump

#pH pump down

@app.route('/pH_pump_down_on')
def EC_modify_down_pump_on():
    webserver.pHPumpControls("down_on")
    return "done"

@app.route('/pH_pump_down_off')
def EC_modify_down_pump_off():
    webserver.pHPumpControls("down_off")
    return "done"

@app.route('/pH_pump_down_toggle')
def EC_modify_down_pump_toggle():
    webserver.pHPumpControls("down_toggle")
    return "done"

#pH pump up

@app.route('/pH_pump_up_on')
def EC_modify_up_pump_on():
    webserver.pHPumpControls("up_on")
    return "done"

@app.route('/pH_pump_up_off')
def EC_modify_up_pump_off():
    webserver.pHPumpControls("up_off")
    return "done"

@app.route('/pH_pump_up_toggle')
def EC_modify_up_pump_toggle():
    webserver.pHPumpControls("up_toggle")
    return "done"

#EC pump

@app.route('/EC_pump_on')
def EC_modify_pump_on():
    webserver.ECPumpControls("on")
    return "done"

@app.route('/EC_pump_off')
def EC_modify_pump_off():
    webserver.ECPumpControls("off")
    return "done"

@app.route('/EC_pump_toggle')
def EC_modify_pump_toggle():
    webserver.ECPumpControls("toggle")
    return "done"

#Light plug

@app.route('/light_on')
def EC_modify_light_on():
    webserver.LightPlugControls("on")
    return "done"

@app.route('/light_off')
def EC_modify_light_off():
    webserver.LightPlugControls("off")
    return "done"

@app.route('/light_toggle')
def EC_modify_light_toggle():
    webserver.LightPlugControls("toggle")
    return "done"

app.run(host='0.0.0.0')