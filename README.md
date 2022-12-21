# kaixei

## LCD

Description and brightness control: https://www.waveshare.com/wiki/7inch_HDMI_LCD_(C)

## Armbian

https://mirror.yandex.ru/mirrors/armbian/archive/orangepizeroplus2-h3/archive/Armbian_22.08.7_Orangepizeroplus2-h3_jammy_current_5.15.74.img.xz


## App autostart

Install slim

    apt get install slim

Edit /ect/slim.conf

    default_user user
    auto_login yes

Create  ~/.config/openbox/autostart:

    export DISPLAY=:0
    python3 $HOME/kaixei/kaixei.py &
