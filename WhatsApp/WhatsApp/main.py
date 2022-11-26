import kivy
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, DictProperty, OptionProperty, BooleanProperty
from kivy.lang.builder import Builder
from demo.demo import profiles

codeMain = """
<MessageScreen>
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: app.theme_cls.bg_normal
        MDToolbar:
            id: logoToolbar
            height: dp(50)
            title: "WhatsApp"
            margin: 0
            MDIconButton:
                icon: 'dots-vertical'
                on_press:
                    root.manager.transition.direction = "right"
            
        ScrollView:
            do_scroll_y: True
            effect_cls: "ScrollEffect"
            bar_width: 0
            MDBoxLayout:
                adaptive_height: True
                orientation: "vertical"
                md_bg_color: app.theme_cls.primary_color
                spacing: dp(20)
                MDBoxLayout:
                    height: dp(60)
                    size_hint_y: None
                    ScrollView:
                        do_scroll_y: False
                        bar_width: 0
                        MDBoxLayout:
                            id: story_layout
                            adaptive_width: True
                            spacing: dp(10)
                            padding: [10,0,0,0]
                            StoryWithIcon:
                            StoryWithImage:
                                text: "l_amr2_l"
                                source: "pic.jpg"

                MDBoxLayout:
                    orientation: "vertical"
                    md_bg_color: app.theme_cls.bg_normal
                    size_hint_y: None
                    adaptive_height: True
                    radius: [20,20,0,0]
                    padding: [0,0,0,40]
                    MDList:
                        id: chatTimeLine
                        spacing: dp(10)
<StoryWithImage>:
    orientation: "vertical"
    size: (dp(60),dp(60))
    size_hint: None,None
    spacing: dp(5)
    width: avatar.width
    Avatar:
        id: avatar
        source: root.source
        pos_hint: {"center_x":.5}
    MDLabel:
        text: root.text
        size: self.texture_size
        theme_text_color: "Custom"
        size_hint_y: None
        halign: "center"
        font_size: sp(9)
        color: [1,1,1,1]
        bold: True

<StoryWithIcon@MDBoxLayout>:
    orientation: "vertical"
    size: (dp(60),dp(60))
    size_hint: None,None
    spacing: dp(5)
    MDIconButton:
        icon: "camera-outline"
        pos_hint: {"center_x":.5}
        theme_text_color: "Custom"
        md_bg_color: app.theme_cls.accent_color
        text_color: [1,1,1,1]
        size: (dp(40),dp(40))
        size_hint: None,None
        user_font_size: sp(18)
    MDLabel:
        text: "Add Story"
        size: self.texture_size
        theme_text_color: "Custom"
        size_hint_y: None
        halign: "center"
        font_size: sp(9)
        color: [1,1,1,1]
        bold: True

<Avatar@RelativeLayout>:
    size: (dp(45),dp(45))
    size_hint: None,None
    source: root.source
    MDCard:
        size: root.size
        size_hint: (None,None)
        radius: [30,30,30,30]
        md_bg_color: app.theme_cls.accent_color
        elevation: 0
        pos_hint: {"center_x":.5,"center_y":.5}

    FitImage:
        size: root.size[0] - dp(3), root.size[1] - dp(3)
        radius: [30,]
        size_hint: None,None
        source: root.source
        pos_hint: {"center_x":.5,"center_y":.5}
<ChatListItem>:
    ripple_behavior: True
    md_bg_color: 0,0,0,0
    elevation: 0
    size_hint_y: None
    padding: [10,0,10,0]
    spacing: dp(10)
    height: chatAvatar.height + dp(10)
    on_press: app.create_chat(root.profile)
    Avatar:
        id: chatAvatar
        source: root.friend_avatar
        pos_hint: {"center_x":.5}
        radius: [30,]
    MDBoxLayout:
        orientation: "vertical"
        padding: [0,0,0,10]
        spacing: 2
        Label:
            id: chatUsername
            text: root.friend_name
            theme_text_color: "Custom"
            size: self.texture_size
            size_hint: None,None
            font_size: 15
            color: app.theme_cls.opposite_bg_normal
            bold: True
        MDLabel:
            id: lastMessage
            text: root.mssg
            height: self.texture_size[1]
            theme_text_color: "Custom"
            size_hint_y: None
            bold: True
            font_size: 13
            color: [.5,.5,.5,1] if root.isRead != 'new' else app.theme_cls.primary_color
            shorten: True
            shorten_from: "right"
    MDBoxLayout:
        orientation: "vertical"
        width: time.width
        size_hint_x: None
        pos_hint: {"center_x":.5}
        spacing: dp(2)
        padding: [0,15,0,5]
        Label:
            id: time
            text: root.timestamp
            size: self.texture_size
            size_hint: None,None
            font_size: sp(9)
            color: app.theme_cls.opposite_bg_normal

        MDIcon:
            #: set icons {'read':'checkbox-multiple-marked-circle','delivered':'checkbox-multiple-marked-circle-outline','new': 'circle'}
            id: chatIcon
            theme_text_color: "Custom"
            icon: icons[root.isRead] if root.isRead in icons.keys() else ''
            size_hint: None,None
            font_size: dp(12)
            size: dp(20),dp(20)
            pos_hint: {"center_x":.5,"center_y":.5}
            text_color: app.theme_cls.primary_color
<ChatScreen>:
    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: app.theme_cls.bg_normal
        MDBoxLayout:
            size_hint_y: None
            height: dp(50)
            spacing: dp(5)
            md_bg_color: app.theme_cls.bg_normal
            padding: [0,0,10,0]
            MDIconButton:
                icon: 'arrow-left'
                theme_text_color: "Custom"
                text_color: app.theme_cls.opposite_bg_normal
                user_font_size: sp(18)
                size_hint: None,None
                pos_hint: {"center_y": .5}
                size: dp(30),dp(30)
                padding: 0
                on_press: app.change_screen("message")
            MDBoxLayout:
                size_hint: None,None
                size: dp(30),dp(30)
                orientation: "vertical"
                pos_hint: {"center_y":.5}
                Avatar:
                    source: root.image
                    size: dp(30),dp(30)
                    size_hint: None,None
            MDBoxLayout:
                orientation: "vertical"
                padding: [0,10,0,10]
                Label:
                    text: root.text
                    size: self.texture_size
                    size_hint: None,None
                    font_size: sp(17)
                    color: app.theme_cls.opposite_bg_normal
                    bold: True

                MDBoxLayout:
                    size_hint_x: None
                    spacing: dp(5)
                    MDIcon:
                        icon: 'circle'
                        theme_text_color: 'Custom'
                        color: [0,1,0,1] if root.active == True else [.5,.5,.5,1]
                        font_size: sp(10)
                        size: dp(10),dp(10)
                        size_hint: None,None
                    Label:
                        text: "Online" if root.active == True else "Offline"
                        size: self.texture_size
                        size_hint: None,None
                        font_size: sp(10)
                        color: app.theme_cls.opposite_bg_normal

            MDBoxLayout:
                size_hint_x: 1.3
                spacing: dp(5)
                MDIconButton:
                    icon: 'video-outline'
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    user_font_size: sp(16)
                    size_hint: None,None
                    pos_hint: {"center_y":.5}
                    size: dp(30),dp(30)
                    padding: dp(0)
                    md_bg_color: app.theme_cls.bg_darkest if app.theme_cls.theme_style == "Light" else app.theme_cls.bg_dark
                
                MDIconButton:
                    icon: 'phone-outline'
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    user_font_size: sp(16)
                    size_hint: None,None
                    pos_hint: {"center_y":.5}
                    size: dp(30),dp(30)
                    padding: dp(0)
                    md_bg_color: app.theme_cls.bg_darkest if app.theme_cls.theme_style == "Light" else app.theme_cls.bg_dark
                
                MDIconButton:
                    icon: 'dots-vertical'
                    theme_text_color: "Custom"
                    text_color: app.theme_cls.primary_color
                    user_font_size: sp(16)
                    size_hint: None,None
                    pos_hint: {"center_y":.5}
                    size: dp(30),dp(30)
                    padding: dp(0)
                    md_bg_color: app.theme_cls.bg_darkest if app.theme_cls.theme_style == "Light" else app.theme_cls.bg_dark
        

        
        ScrollView:
            MDList:
                id: msgHistory
                spacing: dp(5)
                padding: [0,10,0,10]

        MDBoxLayout:
            padding: [10, ]
            spacing: dp(5)
            size_hint_y: None
            height: dp(40)
            md_bg_color: app.theme_cls.bg_normal
            TextField:
            MDIconButton:
                size_hint: None,None
                icon:  "send"
                elevation: 0
                user_font_size: sp(16)
                theme_text_color: "Custom"
                text_color: [1,1,1,1]
                md_bg_color: app.theme_cls.accent_color
<TextField@MDCard>:
    md_bg_color: [.9,.9,.9,.9]
    elevation: 0
    height: dp(40)
    size_hint_y: None
    radius: [15, ]
    padding: [5,5,5,5]
    MDIconButton:
        icon: 'emoticon-happy-outline'
        text_color: "#767B7C"
        size_hint_x: None
        user_font_size: sp(20)
        size_hint: None,None
        pos_hint: {'center_y': .5}
        theme_text_color: "Custom"
        size: dp(30),dp(30)
        padding: 0
    TextInput:
        id: txtinpt
        font_size: sp(14)
        cursor_color: .5,.5,.5,1
        color_mode: "Custom"
        background_color: 0,0,0,0
        current_hint_text_color: .5,.5,.5,1
        pos_hint: {'center_x': .5,'center_y': .5}
        height: 30
        hint_text: "Type a Message"
        padding: [5, ]
    MDIconButton:
        icon: 'microphone-outline'
        text_color: "#767B7C"
        size_hint_x: None
        user_font_size: sp(20)
        size_hint: None,None
        pos_hint: {'center_y': .5}
        theme_text_color: "Custom"
        size: dp(30),dp(30)
        padding: 0
    MDIconButton:
        icon: 'paperclip'
        text_color: "#767B7C"
        size_hint_x: None
        user_font_size: sp(20)
        size_hint: None,None
        pos_hint: {'center_y': .5}
        theme_text_color: "Custom"
        size: dp(30),dp(30)
        padding: 0
<ChatBubble>:
    id: chtbld
    md_bg_color: [0,0,0,0]
    size_hint_y: None
    adaptive_height: True
    halign: dp(60)
    width: root.width
    padding: [10,0,10,0]
    orientation: 'vertical'

    MDBoxLayout:
        height: msg_content.height + time.height + 10
        width: msg_content.width + wid1.width + wid3.width
        size_hint: None,None
        pos_hint: {'right': 1} if chtbld.sender == 'you' else {'left':1}
        radius: [10,10,(1,-5),10] if self.pos_hint == {'right': 1} else [10,10,10,(1,-5)]
        md_bg_color: app.theme_cls.bg_darkest if app.theme_cls == "Light" else app.theme_cls.bg_dark

        Spacer:
            id: wid1
        
        MDBoxLayout:
            orientation: 'vertical'
            height:msg_content.height + timeAndIcon.height + wid2.height
            height: msg_content.width
        
            MDLabel:
                id: msg_content
                text: root.msg
                width: timeAndIcon.width if self.texture_size[0] < timeAndIcon.width else self.texture_size[0]
                height: self.texture_size[1]
                size_hint_y: None
                text_size: chtbld.width - 30 if self.width >= chtbld.width - 30 else None,None
                halign: 'left'
                color: app.theme_cls.opposite_bg_normal
            MDBoxLayout:
                id: timeAndIcon
                size_hint_y: None
                height: time.height
                width: time.width + recieptIcon.width + 3
                spacing: 3
                MDLabel:
                    id: time
                    text: root.time
                    size: self.texture_size
                    size_hint_y: None
                    font_size: 9
                    bold: True
                    halign: 'right'
                    text_size: None,None
                    color: [.8,.8,.8,1]
                MDIcon: 
                    id: recieptIcon
                    #: set iconDict {'read':'check-all','waiting':'clock-time-three-outline','delivered':'check'}
                    theme_text_color: 'Custom'
                    icon: iconDict[chtbld.isRead] if chtbld.isRead in iconDict.keys() else ""
                    size_hint: None,None
                    font_size: 12
                    size: 12,12
                    color: time.color
            Spacer:
                id: wid2
                height: 5
        Spacer:
            id: wid3
            

<Spacer@Widget>:
    id: wid
    width: 5
    size_hint: None,None
"""
Builder.load_string(codeMain)
Window.size = (320, 600)


class WindowManager(ScreenManager):
    pass


class MessageScreen(Screen):
    pass


class StoryWithImage(MDBoxLayout):
    text = StringProperty()
    source = StringProperty()


class ChatBubble(MDBoxLayout):
    msg = StringProperty()
    time = StringProperty()
    sender = StringProperty()
    isRead = OptionProperty('read', option=['read', 'deliverd', 'waiting'])


class WelcomeScreen(Screen):
    pass


class Message(MDLabel):
    pass


class ChatListItem(MDCard):
    mssg = StringProperty()
    friend_avatar = StringProperty()
    timestamp = StringProperty()
    profile = DictProperty()
    isRead = OptionProperty(None,
                            options=['delivered', 'read', 'new', 'waiting'])
    friend_name = StringProperty()


class ChatScreen(Screen):
    text = StringProperty()
    image = StringProperty()
    active = BooleanProperty()


class MainApp(MDApp):
    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Teal"
        self.theme_cls.accent_hue = "400"
        self.title = "WhatsApp"

        screens = [
            MessageScreen(name="message"),
            ChatScreen(name="chat-screen")
        ]

        self.wm = WindowManager(transition=FadeTransition())
        for screen in screens:
            self.wm.add_widget(screen)

        self.story_builder()
        self.chat_list_builder()

        return self.wm

    def story_builder(self):

        for profile in profiles:
            self.story = StoryWithImage()
            self.story.text = profile["name"]
            self.story.source = profile["image"]
            self.wm.screens[0].ids["story_layout"].add_widget(self.story)

    def chat_list_builder(self):

        for profile in profiles:
            for message in profile['msg']:
                self.chatitem = ChatListItem()
                self.chatitem.profile = profile
                self.chatitem.friend_name = profile['name']
                self.chatitem.friend_avatar = profile['image']

                lastMessage, time, isRead, sender = message.split(";")
                self.chatitem.mssg = lastMessage
                self.chatitem.timestamp = time
                self.chatitem.isRead = isRead
            self.wm.screens[0].ids["chatTimeLine"].add_widget(self.chatitem)

    def change_screen(self, screen):
        self.wm.current = screen

    def create_chat(self, profile):

        self.chat_screen = ChatScreen()
        self.chat_screen.text = profile['name']
        self.chat_screen.image = profile['image']
        self.chat_screen.active = profile['active']

        self.msg_builder(profile, self.chat_screen)

        self.wm.switch_to(self.chat_screen)

    def msg_builder(self, profiles, screen):

        for messages in profiles['msg']:
            if messages != '':
                message, time, isRead, sender = messages.split(";")
                self.chatmsg = ChatBubble()
                self.chatmsg.msg = message
                self.chatmsg.time = time
                # self.chatmsg.isRead = isRead
                self.chatmsg.sender = sender
                screen.ids['msgHistory'].add_widget(self.chatmsg)


if __name__ == "__main__":
    MainApp().run()