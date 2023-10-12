from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route('/')
def index():
    # 使用Selenium打开index.html并隐藏地址栏
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 隐藏浏览器窗口
    chrome_options.add_argument("--disable-infobars")  # 隐藏地址栏
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('index.html')  # 替换为您的index.html文件路径

    # 获取index.html的内容
    content = driver.page_source

    # 关闭浏览器
    driver.quit()

    return render_template('index.html', content=content)

if __name__ == '__main__':
   # app.run()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
