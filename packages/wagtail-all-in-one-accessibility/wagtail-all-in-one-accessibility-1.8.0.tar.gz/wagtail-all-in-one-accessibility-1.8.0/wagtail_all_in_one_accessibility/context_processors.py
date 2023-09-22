import random
from .models import wagtail_all_in_one_accessibility
from django.utils.safestring import mark_safe
from django.utils.safestring import SafeString
from urllib.parse import urlparse
from django.utils.html import format_html



def admin_AIOA(request):
    aioa_BaseScript = ''
    domain = urlparse(request.build_absolute_uri())
    wagtail_all_in_one_accessibility._meta.get_field('aioa_license_Key').help_text = mark_safe("<span class='validate_pro'></br>Please <a href=""https://ada.skynettechnologies.us/trial-subscription?utm_source="+domain.netloc+"&utm_medium=wagtail-package&utm_campaign=trial-subscription"" target=""_blank"">subscribe</a> for a 10 days free trial and receive a license key to enable 52+ features of All in One Accessibility Pro.<br>No payment charged upfront, Cancel anytime.</span>")

    for a in wagtail_all_in_one_accessibility.objects.all():        
        a_LK =a.aioa_license_Key.replace(']','').replace('[','').replace("'","")
        a_CC =a.aioa_color_code.replace(']','').replace('[','').replace("'","")
        a_AP =str(a.aioa_place).replace(']','').replace('[','').replace("'","")
        MOBILE_SIZE =str(a.aioa_mobile).replace(']','').replace('[','').replace("'","")
        ICON = str(a.aioa_icon_type).replace(']','').replace('[','').replace("'","")
        SIZE = str(a.aioa_icon_size).replace(']','').replace('[','').replace("'","")
        
        if a_LK != '':
            wagtail_all_in_one_accessibility._meta.get_field('aioa_icon_size').default = ('aioa-default-icon', format_html('<img src="https://skynettechnologies.com/sites/default/files/python/{}" width="65" height="65" />'.format(ICON+'.svg')))
            wagtail_all_in_one_accessibility._meta.get_field('aioa_mobile').blank = False
            wagtail_all_in_one_accessibility._meta.get_field('aioa_icon_type').blank = False
            wagtail_all_in_one_accessibility._meta.get_field('aioa_icon_size').blank = False
            
            value_i = ICON+".svg"
            wagtail_all_in_one_accessibility._meta.get_field('aioa_icon_size').choices = [('aioa-big-icon', format_html('<img class="csticontype" src="https://skynettechnologies.com/sites/default/files/python/{}" width="75" height="75" />',value_i)), ('aioa-medium-icon', format_html('<img class="csticontype" src="https://skynettechnologies.com/sites/default/files/python/{}" width="65" height="65" />',value_i)), ('aioa-default-icon', format_html('<img class="csticontype" src="https://skynettechnologies.com/sites/default/files/python/{}" width="55" height="55" />',value_i)), ('aioa-small-icon', format_html('<img class="csticontype" src="https://skynettechnologies.com/sites/default/files/python/{}" width="45" height="45" />',value_i)), ('aioa-extra-small-icon',format_html('<img class="csticontype" src="https://skynettechnologies.com/sites/default/files/python/{}" width="35" height="35"/>',value_i))]
            
            aioa_BaseScript = 'https://www.skynettechnologies.com/accessibility/js/all-in-one-accessibility-js-widget-minify.js?colorcode='+ a_CC + '&token=' +a_LK+'&t='+str(random.randint(0,999999))+'&position=' + a_AP+'.'+ICON+'.'+SIZE

        else:
            wagtail_all_in_one_accessibility._meta.get_field('aioa_icon_size').default = ('aioa-default-icon', format_html('<img src="https://skynettechnologies.com/sites/default/files/python/{}" width="65" height="65" />'.format(ICON+'.svg')))
            
            # wagtail_all_in_one_accessibility._meta.get_field('aioa_icon_type').default = ('aioa-icon-type-1', format_html('<img src="https://skynettechnologies.com/sites/default/files/python/{}" width="65" height="65" />'))
            
            aioa_BaseScript = ""

    return {'AIOA_URL': aioa_BaseScript}

