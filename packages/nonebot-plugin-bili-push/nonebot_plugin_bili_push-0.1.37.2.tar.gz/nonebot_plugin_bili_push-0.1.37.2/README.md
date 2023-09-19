# nonebot-plugin-bili-push

B 订阅推送插件

## 示例

![输入图片描述](README_md_files/9cf89890-0952-11ee-8733-25d9c7397331.jpeg?v=1&type=image)
![输入图片描述](README_md_files/7fd7ee50-0952-11ee-8733-25d9c7397331.jpeg?v=1&type=image)

## 安装

（以下方法三选一）

一.命令行安装：

```python
nb plugin install nonebot-plugin-bili-push
```

二.pip 安装：

1.执行此命令

    pip install nonebot-plugin-bili-push

2.修改 pyproject.toml 使其可以加载插件

    plugins = [”nonebot-plugin-bili-push“]

三.使用插件文件安装：（不推荐）

1.下载插件文件，放到 plugins 文件夹。

2.修改 pyproject.toml 使其可以加载插件

## 配置

在 nonebot2 项目的`.env`文件中选填配置

1.配置管理员账户，只有管理员才能添加订阅

    SUPERUSERS=["12345678"] # 配置 NoneBot 超级用户

2.插件数据存放位置，默认为 “./”。

    bilipush_basepath="./"

3.推送样式

> 动态的推送样式
> 可配置选项：\[绘图]\[标题]\[链接]\[内容]\[图片]

    bilipush_push_style="[绘图][标题][链接]"

4.刷新间隔：

> 每次刷新间隔多少分钟，默认为 12 分钟。

    bilipush_waittime=12

5.发送间隔：

> 每次发送完成后等待的时间，单位秒，默认 10-30 秒。
> 时间为设置的时间再加上随机延迟 1-20 秒

    bilipush_sleeptime=10

6.最大发送数量

> 限制单次发送数量，防止一次性发送太多图导致风控。
> 默认 5 条

```
bilipush_maximum_send=5

```

其他配置项

> 只响应一个 bot
> 一个群内有多个 bot，可以只让 1 个 bot 推送消息。
> 默认为关闭该功能，既所有 bot 都会响应
> （正在考虑是否改为默认开启，如不需要请关闭该功能）

    bilipush_botswift=False

> 是否使用花音的 api 来支持更丰富的内容
>
> 默认开启。如出现连接不上或其他故障，请尝试关闭。

    bilipush_emojiapi=True

> 配置 api 地址，如未填写则使用默认地址。

    bilipush_apiurl="http://cdn.kanon.ink"

## To-Do

🔵 接下来：

- [ ] 完善动态类型（目前仅支持文字、图文、视频、转发、文章）

- [ ] 字体排版优化（字符位置以及）

- [ ] 自动修改“只响应一个 bot”数据，以及不推送时加提醒

- [ ] 添加话题标签

- [ ] 添加动态底部相关的内容绘制（游戏、动漫、视频）

- [ ] 升级数据库"

- [ ] 版面优化

- [ ] 优化 print（）

- [ ] 代码整理

- [ ] 增加多种适配器连接

- [ ] 推送黑名单（识别到文字或类型的时候不进行推送）

- [ ] ~~对话式配置（暂不考虑~~

- [ ] ~~将请求 api 改为异步（无限期延迟~~

🟢 已完成：

- [x] 对海外服务器支持

- [x] 头像过大

- [x] 动态卡片非粉丝的位置

- [x] 直播无 url

- [x] 动态卡片数字样式

- [x] 动态获取不到名字，导致关注报错

- [x] 配置推送样式

- [x] 添加各种装饰（头像框、装扮等）

- [x] 修复文件下载出错导致文件加载报错

- [x] 无动态时自动跳过

- [x] 关注时获取信息检查，防止输错 uid

- [x] 设置默认字体。在禁用 api 时候使用默认字体

- [x] 单 nb 对接多 q 的兼容

- [x] 增加上下播推送

- [x] 添加本地计算 emoji 模式

## 参考内容

Mirai 动态绘制插件 [BilibiliDynamic MiraiPlugin](https://github.com/Colter23/bilibili-dynamic-mirai-plugin)

## 交流

- 交流群[鸽子窝里有鸽子（291788927）](https://qm.qq.com/cgi-bin/qm/qr?k=QhOk7Z2jaXBOnAFfRafEy9g5WoiETQhy&jump_from=webapi&authKey=fCvx/auG+QynlI8bcFNs4Csr2soR8UjzuwLqrDN9F8LDwJrwePKoe89psqpozg/m)

- 有疑问或者建议都可以进群唠嗑唠嗑。
