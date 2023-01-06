import data_provider
import logger


def temp_view(sensor):
    data = data_provider.get_temperatur(sensor)
    logger.temp_logger(data)
    return data


def pressure_view(sensor):
    data = data_provider.get_pressure(sensor)
    logger.pressure_logger(data)
    return data


def wind_speed_view(sensor):
    data = data_provider.get_wind_speed(sensor)
    logger.wind_speed_logger(data)
    return data
