PythonのwebフレームワークDjangoを使ってHello Worldを実行。

### 環境構築~Djangoプロジェクトの作成
python3のインストール -> Djangoのインストール -> プロジェクトの作成まではDjango公式を参考。
https://docs.djangoproject.com/ja/3.0/intro/tutorial01/

### Hello Worldアプリの作成
Hello Worldアプリの作成は下記を参考。  
https://qiita.com/frosty/items/e545c6258672d88b7707

### 処理の流れ
1. mysite/mysite/settings.pyの56行目 `'DIRS': [BASE_DIR, 'templates']`
mysite/templatesをテンプレートのベースディレクトリに設定
2. mysite/mysite/urls.pyの21行目 `path('', include('helloworld.urls'))`  
ルートURLにアクセスすると、mysite/helloworld/urls.pyへ
3. mysite/helloworld/urls.pyの5行目 `path('', views.helloworldfunction)`  
views.pyのhelloworldfunctionへ 
4. mysite/helloworld/views.pyの6,7行目 `def helloworldfunction(request): return render(request, 'index.html')`  
mysite/templates/index.htmlを返す
