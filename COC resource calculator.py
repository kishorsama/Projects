
from datetime import datetime, timedelta
#current time
cr=datetime.now()


#gold production from user
gold_coin=int(input('Enter current gold coin production per hour: '))
#required gold from user
req_gc=int(input('Enter required gold coins: '))

#required time in hr
cal_req_gc=req_gc/gold_coin

#round off time till 4 decimal
rounded_gc=round(cal_req_gc,4)

#convert round off time near to 0.8of that number
conv_r_gc=rounded_gc+(0.8-(rounded_gc%1))



#converting to dd:hh:mm:ss format
#days
dd=round(conv_r_gc/24,4)
da=int(dd)
#hours
hh=(dd%1)*24
ho=int(hh)
#minutes
mm=(hh%1)*60
mi=int(mm)
#seconds
ss=(mm%1)*60
s=int(ss)

#adding days, hours, minutes in current datetime
ad_cr_gc_d=cr+timedelta(days=da)
ad_cr_gc_hr=cr+timedelta(hours=ho)
ad_cr_gc_min=cr+timedelta(minutes=mi)

#extracting days, hours and min, month from modified datetime

#modifired day
mod_gc_d=ad_cr_gc_d.strftime('%d')
#modified hour
mod_gc_hr=ad_cr_gc_hr.strftime('%I')
#modified minutes
mod_gc_min=ad_cr_gc_min.strftime('%M')
#modified month
mod_gc_month=ad_cr_gc_d.strftime('%h')

#condition for today
if mod_gc_d==cr.strftime('%d'):
    mod_gc_d='Today'
    mod_gc_month='at'
else:
    mod_gc_month=ad_cr_gc_d.strftime('%h')

#12 hour format
mod_gc_12hr=ad_cr_gc_hr.strftime('%p')

#string for estimated time
est_gc='Estimated time is for Gold coin is'

#final gold coin extimated output
print(est_gc,mod_gc_d,mod_gc_month,mod_gc_hr+':'+mod_gc_min,mod_gc_12hr)
print()


#-================================================================================-#



#for elixer

elixer=int(input('Enter current elixer production per hour: '))

req_elixer=int(input('Enter required elixers: '))
#calculating elixer
cal_req_elixer=(req_elixer/elixer)
#rounding off
rounded_elixer=round(cal_req_elixer,4)
#converting near 0.8
conv_r_elixer=rounded_elixer+(0.8-(rounded_elixer%1))


#converting to dd:hh:mm
#days
de=round(conv_r_elixer/24,4)
dee=int(de)
#hours
he=(de%1)*24
hee=int(he)
#minutes
me=(he%1)*60
mee=int(me)

#adding days, hours, mminutes to current time
#adding days
ad_cr_elixer_d=cr+timedelta(days=dee)
#adding hours
ad_cr_elixer_hr=cr+timedelta(hours=hee)
#adding minutes
ad_cr_elixer_min=cr+timedelta(minutes=mee)

#extracting day, hours, minutes and month
#day
mod_elixer_d=ad_cr_elixer_d.strftime('%d')
#hours
mod_elixer_hr=ad_cr_elixer_hr.strftime('%I')
#minutes
mod_elixer_min=ad_cr_elixer_min.strftime('%M')
#month
mod_elixer_month=ad_cr_elixer_d.strftime('%h')

#condition for today
if mod_elixer_d==cr.strftime('%d'):
    mod_elixer_d='Today'
    mod_elixer_month='at'
else:
    mod_elixer_d=ad_cr_elixer_d.strftime('%d')
    mod_elixer_month=ad_cr_gc_d.strftime('%h')

#AM,PM
mod_elixer_ampm=ad_cr_elixer_hr.strftime('%p')

#estimated time string
est_elixer='Estimated time for elixer is'

print(est_elixer,mod_elixer_d,mod_elixer_month,mod_elixer_hr+':'+mod_elixer_min,mod_elixer_ampm)
print()
#-================================================================================-#


#for dark elixer

dark_elixer=int(input('Enter current dark elixer production rate per hours: '))

req_dark_elixer=int(input('Enter required dark elixer: '))

cal_req_dark_elixer=(req_dark_elixer/dark_elixer)

#rounding off
rounded_dark_elixer=round(cal_req_dark_elixer,4)
#converting near 0.8
conv_r_dark_elixer=rounded_dark_elixer+(0.8-(rounded_dark_elixer%1))


#converting to dd:hh:mm
#days
dde=round(conv_r_dark_elixer/24,4)
ddee=int(dde)
#hours
hhe=(de%1)*24
hhee=int(hhe)
#minutes
mme=(he%1)*60
mmee=int(mme)

#adding days, hours, mminutes to current time
#adding days
ad_cr_dark_elixer_d=cr+timedelta(days=ddee)
#adding hours
ad_cr_dark_elixer_hr=cr+timedelta(hours=hhee)
#adding minutes
ad_cr_dark_elixer_min=cr+timedelta(minutes=mmee)

#extracting day, hours, minutes and month
#day
mod_dark_elixer_d=ad_cr_dark_elixer_d.strftime('%d')
#hours
mod_dark_elixer_hr=ad_cr_dark_elixer_hr.strftime('%I')
#minutes
mod_dark_elixer_min=ad_cr_dark_elixer_min.strftime('%M')
#month
mod_dark_elixer_month=ad_cr_dark_elixer_d.strftime('%h')

#condition for today
if mod_dark_elixer_d==cr.strftime('%d'):
    mod_dark_elixer_d='Today'
    mod_dark_elixer_month='at'
else:
    mod_dark_elixer_d=ad_cr_dark_elixer_d.strftime('%d')
    mod_dark_elixer_month=ad_cr_dark_elixer_d.strftime('%h')

#AM,PM
mod_dark_elixer_ampm=ad_cr_dark_elixer_hr.strftime('%p')

#estimated time string
est_dark_elixer='Estimated time for elixer is'

print(est_dark_elixer,mod_dark_elixer_d,mod_dark_elixer_month,mod_dark_elixer_hr+':'+mod_dark_elixer_min,mod_dark_elixer_ampm)

