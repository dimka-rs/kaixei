# kaixei

## LCD

Description and brightness control: https://www.waveshare.com/wiki/7inch_HDMI_LCD_(C)
Enclosure
* https://www.chipdip.ru/product/bicolor-case-for-7inch-lcd
* https://www.waveshare.com/bicolor-case-for-7inch-lcd.htm

## Armbian

### Orange Pi Zero Plus 2 (WiFi only, Full size HDMI)

* http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-Zero-Plus-2.html
* https://mirror.yandex.ru/mirrors/armbian/archive/orangepizeroplus2-h3/archive/Armbian_22.08.7_Orangepizeroplus2-h3_jammy_current_5.15.74.img.xz

### Orange Pi Zero 2 (WiFi + Ethernet, micro HDMI)

* http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-Zero-2.html
    * Download latest XFCE: https://drive.google.com/file/d/1qTtGsdRtx4EtQQIXGP-6RgXL6NTIjvmw/view?usp=share_link
    * Login/pass: orangepi/orangepi, root/orangepi
* http://www.orangepi.org/orangepiwiki/index.php/Orange_Pi_Zero_2
* https://linux-sunxi.org/File:Orange_Pi_Zero2_H616_Schematic_v1.3.pdf
* Download Jammy: https://www.armbian.com/orange-pi-zero-2/
* https://mirrors.dotsrc.org/armbian-dl/orangepizero2/archive/Armbian_22.11.1_Orangepizero2_jammy_edge_6.0.10.img.xz

Enable USB OTG:

* https://lore.kernel.org/linux-arm-kernel/20220211122643.1343315-18-andre.przywara@arm.com/
* https://forum.armbian.com/topic/16170-orangepi-zero2-allwinner-h616/


## App autostart

Install xserver, openbox and slim

    sudo apt update
    sudo apt get install xserver-xorg openbox slim

Edit /ect/slim.conf

    default_user user
    auto_login yes

Create  ~/.config/openbox/autostart:

    export DISPLAY=:0
    python3 $HOME/kaixei/kaixei.py &
