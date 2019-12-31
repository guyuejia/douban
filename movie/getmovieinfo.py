from selenium import webdriver
from selenium.common.exceptions import TimeoutException

def getMovieInfos(movieId):
    infosDict={}
    movieURL = "https://movie.douban.com/subject/" + str(movieId)
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome("D:\\test\\chromedriver.exe",options=option)
    # 设置页面加载和脚本执行超时时间
    browser.set_page_load_timeout(20)
    browser.set_script_timeout(20)
    try:
        browser.get(movieURL)
    except TimeoutException:
        print("加载过慢")
        browser.execute_script('window.stop()')
    #定位到页面关于影片基本信息的元素节点
    infoElement = browser.find_element_by_id("info")
    #获取导演信息
    director = infoElement.find_element_by_xpath("//span//a[@rel='v:directedBy']").text
    infosDict["导演"] = [director]

    #获取演员信息，结果类似：'屈楚萧 / 吴京 / 李光洁 / 吴孟达 / 赵今麦 / 更多...'
    actorStr = infoElement.find_element_by_xpath("//span[@class='actor']/span[@class='attrs']").text
    #格式化演员信息
    actorList = []
    for actor in actorStr.split("/"):
        actorList.append(actor.strip())
    #利用切片，去除最后的"更多"
    actorList = actorList[0:-1]
    infosDict["演员"] = actorList

    # 获取影片类型：战争、爱情、剧情、戏剧等
    typeElement = infoElement.find_elements_by_xpath("//span[@property='v:genre']")
    types = []
    for type in typeElement:
        types.append(type.text)
    infosDict["类型"] = types

    browser.quit()
    return infosDict





if __name__ == "__main__":
    movieId = "26363254"
    infosDict = getMovieInfos(movieId)

    for key in infosDict.keys():
        print(key + ":" + ",".join(infosDict[key]))



