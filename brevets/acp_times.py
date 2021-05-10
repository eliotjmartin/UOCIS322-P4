"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    times = {'200': 34, '300': 32, '400': 30, '600': 28, '1000': 26}
    maxSpeed = times['200']
    if control_dist_km < 200:
       maxSpeed = times['200']
    if control_dist_km >= 200:
       maxSpeed = times['300']
    if control_dist_km >= 300:
       maxSpeed = times['400']
    if control_dist_km >= 400:
       maxSpeed = times['600']
    if control_dist_km >= 600:
       maxSpeed = times['1000']
    hours = control_dist_km / maxSpeed
    return brevet_start_time.shift(hours=hours)


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    times = {'200': 15, '300': 15, '400': 15, '600': 11.428, '1000': 13.333}
    minSpeed = times[str(brevet_dist_km)]
    if control_dist_km < 200:
       minSpeed = times['200']
    if control_dist_km >= 200:
       minSpeed = times['300']
    if control_dist_km >= 300:
       minSpeed = times['400']
    if control_dist_km >= 400:
       minSpeed = times['600']
    if control_dist_km >= 600:
       minSpeed = times['1000']
    hours = control_dist_km / minSpeed
    if control_dist_km < 60:
       hours = hours + (60 - control_dist_km)/60
    return brevet_start_time.shift(hours=hours)



#t = arrow.get('2020-01-01T12:00:00')
#a = close_time(15, 200, t).isoformat().format('YYYY-MM-DDTHH:mm')
#print(a)