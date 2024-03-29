from pyowm import OWM
import logging
from utils import OWM_TOKEN

owm = OWM(OWM_TOKEN)


def get_forecast(place):
    logging.debug("Get forecast function")
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    # temperature
    t = w.temperature('celsius')
    print(t)
    t1 = t['temp']
    t2 = t['feels_like']
    t3 = t['temp_max']
    t4 = t['temp_min']
    hu = w.humidity
    wi = w.wind()['speed']
    # clouds
    cl = w.clouds
    # status
    st = w.status
    # details
    det = w.detailed_status
    # time
    ti = w.reference_time('iso')
    # pressure
    pr = w.pressure['press']

    forecast = f"""У населеному пункті {place} температура {t1}°C, щоправда відчуваєтся як {t2}°C. 
               \nПротягом доби, максимальна температура {t3}°C,
               \nШвидкість вітру протягом дня: {wi} м/с.
               \nАтмосферний тиск: {pr} Па
               \nВологість: {hu}%"""

    return forecast

