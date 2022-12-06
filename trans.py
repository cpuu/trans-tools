# pip install googletrans
# pip install selenium
from googletrans import Translator
from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep


def googlet(eng):
    translator = Translator()
    return (translator.translate(eng, src='en', dest='ko').text)

def daumapi(text):
    # python 3에서는 print() 으로 사용합니다.
    myoptions = webdriver.ChromeOptions()
    myoptions.add_argument('headless')
    myoptions.add_argument('window-size=1920x1080')
    myoptions.add_argument("disable-gpu")
    
    # https://chromedriver.storage.googleapis.com/index.html 에서 알맞은 드라이버 다운로드 필요
    # 
    # 드라이버 로드
    driver = webdriver.Chrome(executable_path="C:/Users/cpuu/Downloads/chromedriver_win32/chromedriver.exe")
    
    # 맞춤법 검사기 url
    url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=맞춤법+검사기"
    # url에서 정보 로드하기
    driver.get(url)
    # 검사할 내용 입력
    driver.find_element(By.ID, "tfGrammar").send_keys(text)
    # 검사하기 버튼 클릭
    driver.find_element(By.ID, "btnGrammarCheck").click()
    sleep(1)
    # 검사된 맞춤법 출력
    result = driver.find_element(By.ID, "contResult").text
    # 드라이버 닫기
    driver.close()
    return result

def main():
    # 대상 문장
    eng = "Symbex executes an application with symbolic values instead of the concrete values used when you normally run a program."

    kor = googlet(eng)

    print(kor)
    
    # text = "기호 실행은 대상 애플리케이션을 실행(또는 에뮬레이션)할 때 일반적인 동작에서 사용하듯 구체적인 값(concrete value)을 특정하는 것이 아니라, 대신 기호로 표현된 값(symbolic value)을 사용한다."
    print(daumapi(kor))
    
if __name__ == "__main__":
	main()
