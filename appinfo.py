from appium import webdriver
import subprocess

def get_apk_activity(apkpath):
    cmd = "aapt dump badging " + apkpath + " | findstr launchable-activity:"
    result = ""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if output != "":
        result = output.split()[1].decode()[6:-1]
    return result

def get_apk_package(apkpath):
    cmd = "aapt dump badging " + apkpath + " | findstr package:"
    result = ""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if output != "":
        result = output.split()[1].decode()[6:-1]
    return result

def get_devciename():
    cmd = "adb devices"
    result = ""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if output != "":
        result = output.split()[4].decode()
    return result

def get_platformVersion():
    cmd = "adb shell getprop ro.build.version.release"
    result = ""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if output != "":
        result = output.split()[0].decode()
    return result

def login():
    desired_caps = {'platformName': 'Android',
                    'deviceName': '801KPZK1505397',
                    'platformVersion': '9',
                    'appPackage': 'com.ifenglian.superapptest3',
                    'appActivity': 'com.ifenglian.superapp.ui.splash.SAWelcomeActivity',
                    'unicodeKeyboard': True,
                    'resetKeyboard': True}
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    driver.find_element_by_id('com.ifenglian.superapptest3:id/tv_login_type').click()
    driver.find_element_by_id('com.ifenglian.superapptest3:id/sa_edt_phone_number').send_keys('18500507432')
    driver.find_element_by_id('com.ifenglian.superapptest3:id/sa_edt_pwd').send_keys('99999999')
    driver.find_element_by_id('com.ifenglian.superapptest3:id/sa_btn_login').click()


if __name__ == '__main__':
    apkpath = "C:\\Users\\gaowei5\\Desktop\\360firewall_beta_5.2.7_390.apk"

    get_apk_package(apkpath)