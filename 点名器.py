import os,re,sys,time
import pygame
import pyttsx3
from 变量 import*
from random import choice
from tkinter import filedialog
from chardet.universaldetector import UniversalDetector
try:
	#隐藏主窗口
	root.withdraw()
	#设置屏幕标题
	pygame.display.set_caption('点名器')
	#填充屏幕
	screen.fill((239,136,190))
	#打印按钮图片
	screen.blit(photo_choice_class_black,(0,400))
	screen.blit(photo_student_with3_black,(250,400))
	screen.blit(photo_student_black,(500,400))
	screen.blit(photo_choice_music_black,(750,400))
	#打印班级名称字体
	screen.blit(text_choice_class,(55,410))
	screen.blit(text_student_with3,(300,410))						
	screen.blit(text_student,(530,410))										
	screen.blit(text_choice_music,(790,410))
	pygame.display.update()
	#检测音乐文件名称
	music_list=os.listdir(music_file)
	for music in music_list:
		if(music.endswith('.mp3')):
			music_play = music_file + music
	music_name = os.path.basename(music_play)
	text_music_name = font_little.render(('当前的音乐是:' + music_name),True,(0,0,0))
	#战术P图2
	screen.blit(photo_p_2,(0,320))
	#打印音乐文件名
	screen.blit(text_music_name,(0,315))
	pygame.display.update()
	while True:
		for user_input in pygame.event.get():	
			mouse = pygame.mouse.get_pos()
			#退出
			if user_input.type == pygame.QUIT:	
				pygame.quit()
			if user_input.type == pygame.MOUSEBUTTONDOWN:
				#选班级
				if (0 <= mouse[0] <= 250 and 400 <= mouse[1] <= 500):
					#战术P图
					screen.blit(photo_p,(0,135))
					#选班级按动反馈
					screen.blit(photo_choice_class_white,(0,400))
					screen.blit(text_choice_class,(55,410))
					pygame.display.update()
					screen.blit(photo_choice_class_black,(0,400))
					screen.blit(text_choice_class,(55,410))
					time.sleep(0.1)
					pygame.display.update()
					pygame.mixer.music.stop()
					#归零
					choice_class = 0
					#选班级窗口
					students_names = filedialog.askopenfilename()
					if students_names != '':
						#带后缀的班级文件名
						class_name = os.path.basename(students_names)
						text_class_name = font_little.render(('当前的班级成员名单是:' + class_name),True,(0,0,0))
						#战术P图2
						screen.blit(photo_p_2,(0,360))
						#打印班级文件名
						screen.blit(text_class_name,(0,355))
						pygame.display.update()
						#检测班级文件字体类型
						try_text = UniversalDetector()
						try_text.reset()
						for test_txt in open(students_names,'rb'):
							try_text.feed(test_txt)
							if try_text.done:
								break
						try_text.close()
						#判断班级文件是否需要更改为utf-8
						if try_text.result['encoding'] != 'utf-8':
							#创建一个临时文件
							students_names_utf_8 = open('临时班级成员名单.txt', 'w')
							open_student_names = open(students_names,'r',errors = 'replace')
							text_read = open_student_names.read()
							open_student_names.close()
							students_names_utf_8 = '临时班级成员名单.txt'
							write_student_names_utf_8 = open(students_names_utf_8,'w',encoding = 'utf-8',errors = 'replace')
							write_student_names_utf_8.write(text_read)
							write_student_names_utf_8.close()
						else:
							students_names_utf_8 = students_names
						#允许抽选学生
						choice_class += 1
					else:
						#战术P图
						screen.blit(photo_p,(0,135))
						#战术P图2
						screen.blit(photo_p_2,(0,360))
						#警告
						screen.blit(warn,(275,150))	
						pygame.display.update()
				#选音乐
				if (750 <= mouse[0] <= 1000 and 400 <= mouse[1] <= 500):
					#战术P图
					screen.blit(photo_p,(0,135))
					#暂停音乐按动反馈
					screen.blit(photo_choice_music_white,(750,400))
					screen.blit(text_choice_music,(790,410))
					pygame.display.update()
					time.sleep(0.1)
					screen.blit(photo_choice_music_black,(750,400))
					screen.blit(text_choice_music,(790,410))
					pygame.display.update()
					#选音乐窗口
					music_play = filedialog.askopenfilename()
					if music_play != '':
						music_name = os.path.basename(music_play)
						text_music_name = font_little.render(('当前的音乐是:' + music_name),True,(0,0,0))
						#战术P图2
						screen.blit(photo_p_2,(0,320))
						#打印音乐文件名
						screen.blit(text_music_name,(0,315))
						pygame.display.update()
					else:
						#检测音乐文件名称
						music_list=os.listdir(music_file)
						for music in music_list:
							if(music.endswith('.mp3')):
								music_play = music_file + music
						#战术P图2
						screen.blit(photo_p_2,(0,320))
						#打印音乐文件名
						screen.blit(text_music_name,(0,315))
						pygame.display.update()
				#幸运学生
				if (500 <= mouse[0] <= 750 and 400 <= mouse[1] <= 500):
					if choice_class == 1:
						#幸运学生按动反馈
						screen.blit(photo_student_white,(500,400))
						screen.blit(text_student,(530,410))					
						#继续播放
						pygame.mixer.music.unpause() 
						play = pygame.mixer_music.get_busy()
						#播放
						if play == False:    
							#播放音乐
							pygame.mixer.music.load(music_play)
							pygame.mixer.music.set_volume(0.5)
							pygame.mixer.music.play() 
						#归零
						student_running = True
						#快速抽选幸运学生
						while student_running:														
							with open(students_names_utf_8,encoding = 'utf-8',errors = 'replace') as stu_names:
								stu_lines= stu_names.readlines()
								student = choice(stu_lines)																				
								#去除'\n'
								student = re.sub(r'\n','',student)
								text_name = font.render((student),True,(0,0,255))
								#战术P图
								screen.blit(photo_p,(0,135))								
								#打印学生姓名					
								screen.blit(text_name,(430,135))
								pygame.display.update()
								#快速抽选幸运学生延迟
								time.sleep(0.05)
							#真正的幸运学生
							for user_input in pygame.event.get():	
								if user_input.type == pygame.MOUSEBUTTONDOWN:
									if (500 <= mouse[0] <= 750 and 400 <= mouse[1] <= 500):
										#暂停音乐
										pygame.mixer.music.pause()
										#幸运学生按动反馈
										screen.blit(photo_student_black,(500,400))
										screen.blit(text_student,(530,410))
										pygame.display.update()		
										#防重复列表
										student_lines_max = len(stu_lines)
										if student in pass_student:
											continue
										pass_student.append(student)
										pass_student_max = len(pass_student)
										if pass_student_max == student_lines_max:
											pass_student.clear()
										#战术P图
										screen.blit(photo_p,(0,135))								
										#打印学生姓名					
										screen.blit(text_name,(430,135))		
										pygame.display.update()					
										#朗读学生姓名						
										pyttsx3.speak(student)
										#结束快速抽选幸运学生
										student_running = False
										break														
					else:
						#战术P图
						screen.blit(photo_p,(0,135))
						#警告
						screen.blit(warn,(275,150))	
						pygame.display.update()		
				#三连抽
				if (250 <= mouse[0] <= 500 and 400 <= mouse[1] <= 500):													
					if choice_class == 1:
						#三连抽按动反馈
						screen.blit(photo_student_with3_white,(250,400))
						screen.blit(text_student_with3,(300,410))
						pygame.display.update()
						#归零
						student_with3_running = True
						x_student_with3_fast = 130
						#继续播放
						pygame.mixer.music.unpause() 
						play = pygame.mixer_music.get_busy()
						#播放
						if play == False:    
							#播放音乐
							pygame.mixer.music.load(music_play)
							pygame.mixer.music.set_volume(0.5)
							pygame.mixer.music.play()							
						#战术P图
						screen.blit(photo_p,(0,135))
						#快速三连抽
						while student_with3_running:														
							student_with3_time += 1
							with open(students_names_utf_8,encoding = 'utf-8',errors = 'replace') as stu_names:
								stu_lines= stu_names.readlines()
								student_with3 = choice(stu_lines)																				
								#去除'\n'
								student_with3 = re.sub(r'\n','',student_with3)
								text_name_with3 = font.render((student_with3),True,(0,0,255))							
								#打印学生姓名					
								screen.blit(text_name_with3,(x_student_with3,150))
								pygame.display.update()
								#学生姓名X轴坐标增加值
								x_student_with3 += 300
								if student_with3_time == 3:
									#快速三连抽延迟
									time.sleep(0.05)
									#归零
									x_student_with3 = 130
									student_with3_time = 0
									#战术P图
									screen.blit(photo_p,(0,135))
							#真正的三连抽
							for user_input in pygame.event.get():	
								if user_input.type == pygame.MOUSEBUTTONDOWN:
									if (250 <= mouse[0] <= 500 and 400 <= mouse[1] <= 500):	
										#暂停音乐
										pygame.mixer.music.pause()
										#三连抽按动反馈
										screen.blit(photo_student_with3_black,(250,400))
										screen.blit(text_student_with3,(300,410))
										pygame.display.update()
										#战术P图
										screen.blit(photo_p,(0,135))
										#归零
										x_student_with3 = 130
										student_with3_time = 0
										while True:
											with open(students_names_utf_8,encoding = 'utf-8',errors = 'replace') as stu_names:
												stu_lines= stu_names.readlines()
												student_with3 = choice(stu_lines)
												#去除'\n'
												student_with3 = re.sub(r'\n','',student_with3)
												text_name_with3 = font.render((student_with3),True,(0,0,255))
												#防重复列表
												student_lines_max = len(stu_lines)
												#检测班级人员名单是否是3的倍数
												while True:
													if (student_lines_max % 3) == 0:	
														student_lines_max_3 = student_lines_max
														break
													else:
														student_lines_max -= 1 
														continue
												if student_with3 in pass_student_with3:	
													continue
												pass_student_with3.append(student_with3)
												pass_student_max = len(pass_student_with3)
												if pass_student_max == student_lines_max_3:
													pass_student_with3.clear()
												#打印第1位学生姓名				
												screen.blit(text_name_with3,(x_student_with3,150))	
												pygame.display.update()																				
												#朗读第1位学生姓名
												pyttsx3.speak(student_with3)											
												#学生姓名X轴坐标增加值
												x_student_with3 += 300
												#打印学生姓名次数
												student_with3_time += 1									
												#三连抽结束判定
												if student_with3_time == 3:
													#结束快速三连抽
													student_with3_running = False
													#归零
													x_student_with3 = 130
													student_with3_time = 0			
													break					
					else:
						#战术P图
						screen.blit(photo_p,(0,135))
						#警告
						screen.blit(warn,(275,150))	
						pygame.display.update()			
except:	
	#暂停音乐
	pygame.mixer.music.stop()
	#'紫'屏
	screen.fill((115,43,245))
	screen.blit(text_face,(100,40))
	screen.blit(text_face_2,(152,103))
	screen.blit(warn_error,(100,145))
	screen.blit(photo_help_black,(100,190))
	screen.blit(text_help,(120,190))
	pygame.display.update()
	while exit_error:	
		for user_input in pygame.event.get():
			mouse = pygame.mouse.get_pos()
			#退出
			if user_input.type == pygame.QUIT:				
				pygame.quit()
			if user_input.type == pygame.MOUSEBUTTONDOWN:
				if (100 <= mouse[0] <= 200 and 190 <= mouse[1] <= 240):
					screen.blit(photo_help_white,(100,190))
					screen.blit(text_help,(120,190))
					pygame.display.update()
					time.sleep(0.1)
					screen.blit(photo_help_black,(100,190))
					screen.blit(text_help,(120,190))
					pygame.display.update()
					os.system(r'notepad 关于/帮助.txt')
					pygame.quit()
					break
finally:
	try:
		os.remove(r'临时班级成员名单.txt')
	finally:
		sys.exit()