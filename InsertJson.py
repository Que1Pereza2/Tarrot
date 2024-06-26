import pygame
from Button import Button
from TextBox import TextBox

# this class creates the insert JSON menu 

class InsertJSON():
    
    def __init__(self,screen,conn):
        self.screen=screen
        self.textColor=(124,73,166)
        self.textBackground=(2,47,64)
        font=pygame.font.Font('tarrot cards/Ldfcomicsans-jj7l.ttf', 32)
        self.text1=font.render("Please provide the path of the json you wish ",True,self.textColor,self.textBackground)
        self.text2=font.render("to upload to the database using the textbox below!",True,self.textColor,self.textBackground)
        self.textBox=TextBox(self.screen.get_width()//2 - 70,434,screen,"json")
        self.textRect1=self.text1.get_rect()
        self.textRect1.center=(screen.get_width()//2,18)
        self.textRect2=self.text2.get_rect()
        self.textRect2.center=(screen.get_width()//2,57)
        self.conn=conn
        self.back=Button(1000,150,94,39,"back",self.screen)
        self.send=Button(self.screen.get_width()//2,500,94,39,"insert",self.screen)
        self.inserted=False
    
    def drawMenu(self):
        miau=(3, 6, 55)
        self.screen.fill(miau)
        self.screen.blit(self.text1,self.textRect1)
        self.screen.blit(self.text2,self.textRect2)
        self.textBox.rect.center=(self.screen.get_width()//2,450)

        self.textBox.draw()
        self.back.draw()
        self.send.draw()
    
    # this checks if the button used for insertion has been pressed and if the text box has something in it
    def eventHandler(self,menu:str)->str:
        
        if menu=="insert json":
            if self.send.textRect.collidepoint(pygame.mouse.get_pos()) and self.textBox.userText:
                self.insert("insert/"+self.textBox.userText+".json")
                self.inserted=True
                menu="initial"
                
            else:
                menu = "insert json"
        return menu
   
    # this method does the insertion
    def insert(self,loc):
        try:
            self.conn.insertJSON(loc)
        except(FileNotFoundError):
            print("the JSON was not found")
        