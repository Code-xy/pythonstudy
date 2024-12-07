from twikit import Client

async def main():
    # 创建客户端实例
    client = Client(language='en-US')
    
    # 登录
    await client.login(
        auth_info_1='@bccfxs',  # 用户名
        auth_info_2='2780396291@qq.com',     # 邮箱(可选)
        password='cnm123456'       # 密码
    )
    
    # 发推文
    tweet = await client.create_tweet(
        text="Hello World!"
    )
    
    # 发带图片的推文
    media_id = await client.upload_media('image.jpg')
    tweet = await client.create_tweet(
        text="Tweet with image",
        media_ids=[media_id]
    )

    # 搜索推文
    tweets = await client.search_tweet("python", "Latest")
    for tweet in tweets:
        print(tweet.text)

    # 获取用户信息
    user = await client.get_user_by_screen_name("twitter")
    print(user.name)

    # 登出
    await client.logout()

# 运行异步函数
import asyncio
asyncio.run(main())
