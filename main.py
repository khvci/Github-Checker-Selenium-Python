from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

userToCheck = "khvci"
profileUrl = "https://www.github.com/" + userToCheck

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(profileUrl)

numberOfFollowers = (int)(driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[4]/main[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/a[1]/span[1]").text)
numberOfFollowing = (int)(driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[4]/main[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/a[2]/span[1]").text)

print(f"Followers: {numberOfFollowers}")
print(f"Following: {numberOfFollowing}")

#go to followers page
numberOfPagesFollowers = (int)(numberOfFollowers / 50)
followers = []

for i in range(1, (numberOfPagesFollowers + 1)):
    driver.get(profileUrl + "?page=" + (str)(i) + "&tab=followers")
    driver.implicitly_wait(3)

    for j in range(1,51):
        xpath = "//*[@id=\"user-profile-frame\"]/div/div[" + (str)(j) + "]/div[2]/a/span[2]"
        username = driver.find_element(By.XPATH,xpath).text
        followers.append(username)

        if len(followers) == numberOfFollowers:
            break
    

print(followers)
print(f"number of fetched followers: {len(followers)}")
