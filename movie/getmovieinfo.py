from selenium import webdriver

def getMovieInfos(movieId):
    infosDict={}
    movieURL = "https://movie.douban.com/subject/" + str(movieId)
    browser = webdriver.Chrome("D:\\test\\chromedriver.exe")
    browser.get(movieURL)
    #定位到页面关于影片基本信息的元素节点
    infoElement = browser.find_element_by_id("info")
    #获取导演信息
    director = infoElement.find_element_by_xpath("//span//a[@rel='v:directedBy']").text
    infosDict["导演"] = director


    return infosDict

if __name__ == "main":
    movieId = "26266893"
    infosDict = getMovieInfos(movieId)



