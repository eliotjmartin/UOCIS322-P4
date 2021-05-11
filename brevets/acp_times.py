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
    if control_dist_km < 200:
       hours = control_dist_km / times['200']
    elif control_dist_km >= 200 and control_dist_km < 300:
       hours = 200 / times['200'] 
       hours = hours + (control_dist_km - 200) / times['300']
    elif control_dist_km >= 300 and control_dist_km < 400:
       hours = 200 / times['200']
       hours = hours + 100 / times['300'] 
       hours = hours + (control_dist_km - 300) / times['400']       
    elif control_dist_km >= 400 and control_dist_km < 600:
       hours = 200 / times['200']
       hours = hours + 100 / times['300'] 
       hours = hours + 100 / times['400']
       hours = hours + (control_dist_km - 400) / times['600'] 
    else:
       hours = 200 / times['200']
       hours = hours + 100 / times['300'] 
       hours = hours + 100 / times['400']
       hours = hours + 200 / times['600']
       hours = hours + (control_dist_km - 600) / times['1000']
    minutes = round(hours * 60)
    return brevet_start_time.shift(minutes=minutes)


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
    if control_dist_km < 200:
       hours = control_dist_km / times['200']
    elif control_dist_km >= 200 and control_dist_km < 300:
       hours = 200 / times['200'] 
       hours = hours + (control_dist_km - 200) / times['300']
    elif control_dist_km >= 300 and control_dist_km < 400:
       hours = 200 / times['200']
       hours = hours + 100 / times['300'] 
       hours = hours + (control_dist_km - 300) / times['400']       
    elif control_dist_km >= 400 and control_dist_km < 600:
       hours = 200 / times['200']
       hours = hours + 100 / times['300'] 
       hours = hours + 100 / times['400']
       hours = hours + (control_dist_km - 400) / times['600'] 
    else:
       hours = 200 / times['200']
       hours = hours + 100 / times['300'] 
       hours = hours + 100 / times['400']
       hours = hours + 200 / times['600']
       hours = hours + (control_dist_km - 600) / times['1000'] 
    if control_dist_km < 60:
       hours = hours + (60 - control_dist_km)/60
    minutes = round(hours*60)
    return brevet_start_time.shift(minutes = minutes)



t = arrow.get('2020-01-01T00:00:00')
a = close_time(200, 400, t).isoformat().format('YYYY-MM-DDTHH:mm')
print(a)