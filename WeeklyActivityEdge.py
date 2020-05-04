import pandas as pd
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import Select
import math
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def isnan(value):
    try:
        return math.isnan(float(value))
    except:
        return False


source_file_path = "E:\\Python\\BSH Online academic activity_Student Copy.csv"
source_df = pd.read_csv(source_file_path)
source_df = source_df.loc[0:433,
            'Faculty Name':'Mention Google Class Code/Link/Meeting ID                          (If applicable)']

cse_df = source_df[source_df["Stream-Sec"].str.find("CSE") >= 0]
# print(cse_df.shape)
# print(cse_df)
cse_df.to_csv("Filtered CSE Classes.csv")
browser = webdriver.Edge(executable_path=r'E:\\Python\\msedgedriver.exe')
browser.set_page_load_timeout(240)
browser.get('https://makaut1.ucanapply.com/smartexam/public/student/week-report-activity/create')
# student=browser.find_element_by_name('STUDENT')
# student.click()
print("Click on Student  :)")
print("After logging in press Enter in console")
wait = input()
browser.get("https://makaut1.ucanapply.com/smartexam/public/student/week-report-activity/create")
# weeklyactivity = browser.find_element_by_id('week-report-activity/create')
# weeklyactivity.click()
week = datetime.now()
topic = ""
duration = ""
takenby = ""
platform = ""
date = ""
link = ""
i = int(input("Previous Entries : "))
for index, row in cse_df.iterrows():
    if not i == 0:
        i -= 1
        continue
    browser.get("https://makaut1.ucanapply.com/smartexam/public/student/week-report-activity/create")
    sleep(3)
    weekobj = browser.find_element_by_id("week")
    topicfld = browser.find_element_by_id("topic_covered")
    platusd = browser.find_element_by_id("platform_used")
    dateobj = browser.find_element_by_id("date_tme")
    leclink = browser.find_element_by_id("record_lecture_upload_link")
    durationform = browser.find_element_by_id("duration_in_min")
    interraction = browser.find_element_by_id("post_class_interraction_note")
    assignmentrec = browser.find_element_by_id("assignment_received")
    assignmentsub = browser.find_element_by_id("assignment_submitted")
    test = browser.find_element_by_id("test_attended_if_any")
    self = browser.find_element_by_id("daily_self_acitvity")
    remark = browser.find_element_by_id("remark")
    sem = Select(browser.find_element_by_id("SEMCODE"))
    sem.select_by_value("SM02")
    sleep(3)
    course = Select(browser.find_element_by_id("COURSECD"))
    course.select_by_value('C000024')
    sleep(3)
    prof = Select(browser.find_element_by_id("class_taken_by"))
    sleep(3)
    # week = datetime.strptime(row[2] , '%mm %dd %yyyy')

    date = str(row[2]) + "-" + str(row[3])
    topic = row[7]
    duration = row[3]
    takenby = row[0]
    platform = row[9]
    link = row[10]
    code = row[6]
    # pcin = row[12]
    # assignmentR = row[13]
    # assignmentS = row[14]
    # testatt = row[15]
    print("Date/Time = " + str(date))
    print("Topic Covered= " + str(topic))
    print("Course Code = " + str(code))
    print("Time= " + str(duration))
    print("Taken by " + str(takenby))
    print("Platform Used = " + str(platform))
    print("Recorded Lecture Link = ", end="")
    if not link == "":
        print(link)
    else:
        print("Not Available")
    if not isnan(duration):
        durationform.send_keys(duration)
    else:
        durationform.send_keys("NA")
    interraction.send_keys('NA')
    assignmentrec.send_keys('NA')
    assignmentsub.send_keys("NA")
    test.send_keys("NA")
    self.send_keys("NA")
    remark.send_keys("NA")
    if not isnan(topic):
        topicfld.send_keys(topic)
    else:
        topicfld.send_keys("NA")
    if not isnan(link):
        # WebDriverWait(browser, 20).until(
        # EC.element_to_be_clickable((By.CLASS_NAME, "record_lecture_upload_link"))).click()
        leclink.send_keys(link)

    else:
        leclink.send_keys("NA")
    if not isnan(platform):
        platusd.send_keys(platform)
    else:
        platusd.send_keys("NA")
    print("Press Enter for next entry")
    wait0 = input()  # waiting for interrupt
    submit = browser.find_element_by_id('btnSubmit')
    submit.click()
