## 前端测试坑点

### CORS 

本地测试时，对于前端，可以使用`npm run serve`，从而浏览器可以访问本地`8080`端口获取页面。对于后端，可以`./manage.py runserver`启动服务，前端可访问本地`8000`端口获取数据。

然而在使用axios获取数据时，会因为浏览器的[CORS policy](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Access_control_CORS)而被拒绝访问。一般情况下会出现两种拒绝访问的情况：

```
1. Cross origin requests are only supported for protocol schemes: http, data, chrome, chrome-extension, https.
2. No 'Access-Control-Allow-Origin' header is present on the requested resource.
```

~~解决方法如下~~

- ~~使用`127.0.0.1:8000`而不是`localhost:8000`获取数据，解决第一个问题~~
- ~~安装[此插件](https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf)，启用后解决第二个问题。该插件会修改获得数据的头部，为其加上`Access-Control-Allow-Origin: *`字段以使得跨域获取的数据的使用能被浏览器允许~~

~~还有一种更好的解决方法：~~

~~可以在命令行中启动chrome，启动一个新的浏览器环境，并关闭安全选项~~

    google-chrome --disable-web-security --user-data-dir="your/base/dir"

现在后端已经支持CORS，不需要再作处理了。可以在后端配置CORS支持的跨域访问白名单，目前白名单只有`localhost:8080`和`127.0.0.1:8080`。

### Axios 中处理数据

我们喜欢这样使用axios

```javascript
    axios
    .get(url)
    .then(function (response) {
        this.data = response.data;
    });
```

然而会报错，显示this没有data这个对象。这是因为`this.data = response.data;`中的`this`不是我们所需要的vue component。一种解决方法为

```javascript
    let vm = this;
    axios
    .get(url)
    .then(function (response) {
        vm.data = response.data;
    });
```

另一种解决方法为

```javascript
    axios
    .get(url)
    .then((response) => {
        this.data = response.data;
    });
```
