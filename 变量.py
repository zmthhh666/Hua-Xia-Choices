import pygame
import tkinter as tk

root = tk.Tk()

pygame.init()

screen = pygame.display.set_mode((1000,500))

#'紫'屏退出判定
exit_error = True

choice_class = 0

pass_student = []

pass_student_with3 = []

student_with3_time = 0

x_student_with3 = 130

font_little = pygame.font.Font ('字体/SourceHanSansSC-Light.otf',30)

font = pygame.font.Font ('字体/SourceHanSansSC-Light.otf',50)

font_big = pygame.font.Font ('字体/SourceHanSansSC-Light.otf',100)

music_file = '音乐/'

photo_p = pygame.image.load('图片/P图.jpg').convert()

#用P图1调整出P图2
photo_p_2 = pygame.transform.scale(photo_p,(1000, 40))

#白色按钮图片
photo_choice_class_white  = pygame.image.load('图片/白色按钮图片/选班级.jpg').convert()

photo_student_with3_white = pygame.image.load('图片/白色按钮图片/三连抽.jpg').convert()

photo_student_white = pygame.image.load('图片/白色按钮图片/幸运学生.jpg').convert()

photo_choice_music_white = pygame.image.load('图片/白色按钮图片/选音乐.jpg').convert()

#黑色按钮图片
photo_choice_class_black = pygame.image.load('图片/黑色按钮图片/选班级.jpg').convert()

photo_student_with3_black = pygame.image.load('图片/黑色按钮图片/三连抽.jpg').convert()

photo_student_black = pygame.image.load('图片/黑色按钮图片/幸运学生.jpg').convert()

photo_choice_music_black = pygame.image.load('图片/黑色按钮图片/选音乐.jpg').convert()

#黑色帮助
photo_help_black = pygame.image.load('图片/黑色帮助/帮助.jpg').convert()

#白色帮助
photo_help_white = pygame.image.load('图片/白色帮助/帮助.jpg').convert()

text_choice_class = font.render(('选班级'),True,(0,0,0))

text_student_with3 = font.render(('三连抽'),True,(0,0,0))

text_student = font.render(('幸运学生'),True,(0,0,0))

text_choice_music = font.render(('选音乐'),True,(0,0,0))

text_help = font_little.render(('帮助'),True,(255,255,255))

warn = font.render(('请选择班级成员名单'),True,(0,0,255))

text_face = font_big.render(('> <'),True,(255,255,255))

text_face_2 = font.render(('^'),True,(255,255,255))
	
warn_error = font_little.render(('我们遇到了一些问题'),True,(255,255,255))