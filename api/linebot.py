from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, CarouselColumn,
                            CarouselTemplate, MessageAction, URIAction, ImageCarouselColumn, ImageCarouselTemplate,
                            ImageSendMessage,ConfirmTemplate,ButtonsTemplate,URTAction,CarouselTemplate,URIAction)
import os
line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
line_handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/webhook", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    if event.messege.text == "確認樣板":
        confirm_template = TemplateSendMessage(
            alt_text = 'confirm template',
            template = ConfirmTemplate(
                text = 'drink coffee?',
                actions = [
                    
                    MessageAction(
                        lable= 'yes',
                        text='yes'
                        ),
                    
                    MessageAction(
                        lable= 'no',
                        text='no'
                        ),
                    
                    ]

                )
            
            
            )
        
        line_bot_api.reply_message(event.replay_token,confirm_template)
    if event.message.text == "按鈕樣板":
        buttons_template = TemplateSendMessage(
            alt_text = 'button template',
            template = ButtonsTemplate(
                
                thumbnail_image_url = 'https://images.pexels.com/photos/302899/pexels-photo-302899.jpeg',
                
                title = "Brown Care",
                
                text = 'Enjoy',
                
                actions =[
                    
                    MessageAction(
                        
                        lable = '咖啡好處?',
                        text = '讓人有精神',
                        
                        ),
                    URTAction(
                        lable = '伯朗咖啡',
                        url='https://www.mrbrown.com.tw/'
                        
                        
                        
                        )
                    
                    ]
                
                
                )
            
            
            )
        line_bot_api.reply_message(event.replay_token,buttons_template)
    if event.message.text == "橫向卷軸樣板":
        carousel_template = TemplateSendMessage(
            alt_text = "carousel template",
            template = CarouselTemplate(
                
                columns =[
                    
                    CarouselColumn(
                        
                        thumbnail_image_url = 'https://images.pexels.com/photos/302899/pexels-photo-302899.jpeg',
                        title = "this is menu1",
                        text = 'menu 1',
                        action =[
                            MessageAction(
                                lable = '咖啡好處',
                                text = '有精神',
                                
                                ),
                            
                            URTAction(
                                lable = '伯朗咖啡',
                                url='https://www.mrbrown.com.tw/'
                                )
                            ]
                        ),
                    CarouselColumn(
                        
                        thumbnail_image_url = 'https://images.pexels.com/photos/302899/pexels-photo-302899.jpeg',
                        title = "this is menu2",
                        text = 'menu 2',
                        action =[
                            MessageAction(
                                lable = '咖啡好處',
                                text = '有精神',
                                
                                ),
                            
                            URTAction(
                                lable = '伯朗咖啡',
                                url='https://www.mrbrown.com.tw/'
                 
                                )         
                            ]
   
                        ),
    
                    ]
                )
            )
        line_bot_api.reply_message(event.replay_token,carousel_template)
    if event.message.text == "圖片卷軸樣板":
        image_template = TemplateSendMessage(
            alt_text = "image template",
            template = ImageCarouselTemplate(
                columns =[
                    ImageCarouselColumn(
                        
                        image_url="https://images.pexels.com/photos/302899/pexels-photo-302899.jpeg"
                        actions = URIAction(
                            
                            
                            
                            label = "伯朗咖啡",
                            url="https://www.mrbrown.com.tw/",
                            )
                        )
                    ImageCarouselColumn(
                        image_url="https://images.pexels.com/photos/302899/pexels-photo-302899.jpeg"
                        actions = URIAction(
                            
                            label = "伯朗咖啡",
                            url="https://www.mrbrown.com.tw/",
                            )
                        )
                    ]
                )
            )
        line_bot_api.reply_message(event.replay_token,image template)
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text="hi"))

if __name__ == "__main__":
    app.run()
