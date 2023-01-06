from user_interface import temp_view
from user_interface import pressure_view
from user_interface import wind_speed_view


def create(device=1):
    style = 'style="font-size:20px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '     <p {}>Temperature:{} C</p>\n ' \
        .format(style, temp_view(device))
    html += '     <p {}>Pressure:{} pascal</p>\n ' \
        .format(style, pressure_view(device))
    html += '     <p {}>Wind_speed:{} m/s</p>\n ' \
        .format(style, wind_speed_view(device))
    html += '  </body>\n<html>'

    with open('index.html', 'w') as page:
        page.write(html)
    return html
