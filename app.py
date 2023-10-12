from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # 设置私有目录路径
    private_dir = os.path.join(app.root_path, 'private')
    # 设置静态文件夹路径
    app.static_folder = private_dir
    # 设置静态路由
    app.add_url_rule('/private/<path:filename>', endpoint='private', view_func=app.send_static_file)
    # 启动应用程序
    app.run()
