import pygame
import random
import os
pygame.init() 
WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CASH = 1
LAB = 0


FONT = pygame.font.SysFont('monospace', 15)
FONT2 = pygame.font.SysFont('monospace', 32)

BACKGROUND_COLOR = (0, 0, 0)
BUTTON_COLOR = (0, 255, 0)
#Main Screen for drawing buttons
DRAW_SCREEN = pygame.Surface((WIDTH,HEIGHT))
DRAW_SCREEN.fill(BACKGROUND_COLOR)
#text
TITLE = FONT2.render('Tea-Tropolis', 1, (255, 255, 0))
BYVS = FONT.render('Made by ValiantShape', 1, (255, 255, 0))
#Buttons
GEN1 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 100, 200, 30), 1)
GEN2 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 135, 200, 30), 1)
GEN3 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 170, 200, 30), 1)
BUILDLAB = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 205, 200, 30), 1)
SCIENCE = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 240, 200, 30), 1)
#Button Text
GEN1_LABEL = FONT.render('More Tea Plants', 1, (255, 255, 0))
GEN2_LABEL = FONT.render('More farmers', 1, (255, 255, 0))
GEN3_LABEL = FONT.render('Quality Fertilizer', 1, (255, 255, 0))
BUILDLAB_LABEL = FONT.render('Build Labs', 1, (255, 255, 0))
SCIENCE_LABEL = FONT.render('Scientists', 1, (255, 255, 0))
#Profit Timers
GEN1_TIMER = 1000
GEN2_TIMER = 5000
GEN3_TIMER = 7500
BUILDLAB_TIMER = 10000
SCIENTIST_TIMER = 1000
#Generator Profits
GEN1_PROFIT = 10
GEN2_PROFIT = 100
GEN3_PROFIT = 1000
BUILDLAB_PROFIT = 0 
SCIENCE_PROFIT = 1000
#Generator Levels
GEN1_LEVEL = 1
GEN2_LEVEL = 1
GEN3_LEVEL = 1
BUILDLAB_LEVEL = 0
SCIENCE_LEVEL = 0
#Generator Level Labels
GEN1_LEVEL_LABEL = 'Level: '
GEN2_LEVEL_LABEL = 'Level: '
GEN3_LEVEL_LABEL = 'Level: '
BUILDLAB_LEVEL_LABEL = 'You have:'
SCIENCE_LEVEL_LABEL = 'You have'
#Events
GEN1_EVENT = pygame.USEREVENT + 0
GEN2_EVENT = pygame.USEREVENT + 1
GEN3_EVENT = pygame.USEREVENT + 0
BUILDLAB_EVENT = pygame.USEREVENT + 0
SCIENCE_EVENT = pygame.USEREVENT + 0
def add_gen1_profit():
	global CASH
	CASH += GEN1_PROFIT
	
def add_gen2_profit():
	global CASH
	CASH += GEN2_PROFIT

def add_gen3_profit():
	global CASH
	CASH += GEN3_PROFIT

def handle_events():
	event_dict = {
		pygame.QUIT: exit,
		GEN1_EVENT: add_gen1_profit,
		GEN2_EVENT: add_gen2_profit,
		   
	}
	for event in pygame.event.get():
		if event.type in event_dict:
			event_dict[event.type]()

def handle_mouse_clicks():
	global CASH, LAB, PROFITS, GEN1_TIMER, GEN2_TIMER,GEN3_TIMER,BUILDLAB_TIMER, GEN1_LEVEL, GEN2_LEVEL, GEN3_LEVEL, BUILDLAB_LEVEL
	if pygame.mouse.get_focused():
		left_button = pygame.mouse.get_pressed()
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if GEN1.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 100 and GEN1_TIMER > 100:
			CASH -= 100
			GEN1_TIMER -= 100
			pygame.time.set_timer(GEN1_EVENT, GEN1_TIMER)
			GEN1_LEVEL += 1
		if GEN2.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 1000 and GEN2_TIMER > 100:
			CASH -= 1000
			GEN2_TIMER -= 100
			pygame.time.set_timer(GEN2_EVENT, GEN2_TIMER)
			GEN2_LEVEL += 1
		if GEN3.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 1000 and GEN3_TIMER > 100:
			CASH -= 10000
			GEN3_TIMER -= 100
			pygame.time.set_timer(GEN3_EVENT, GEN3_TIMER)
			GEN3_LEVEL += 1
		if BUILDLAB.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 1000 and BUILDLAB_TIMER > 100:
			CASH -= 1000000
			BUILDLAB_TIMER -= 100
			LAB += 10
			pygame.time.set_timer(BUILDLAB_EVENT, BUILDLAB_TIMER)
			BUILDLAB_LEVEL += 1
		if SCIENCE.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 1000 and SCIENTIST_TIMER > 100:
			CASH -= 100000
			LAB -= 10
			SCIENTIST_TIMER -= 100
			pygame.time.set_timer(SCIENCE_EVENT, SCIENTIST_TIMER)
			SCIENCE_LEVEL += 1
def update_text():
	global CASH_LABEL, GEN1_LEVEL_LABEL, GEN2_LEVEL_LABEL, LAB_LABEL, SCIENCE_LABEL
	WINDOW.blit(DRAW_SCREEN, (0, 0))
	WINDOW.blit(GEN1_LABEL, (10, 108))
	WINDOW.blit(GEN2_LABEL, (10, 143))
	WINDOW.blit(GEN3_LABEL, (10, 178))
	WINDOW.blit(TITLE, (5, 35))
	WINDOW.blit(BYVS, (10, 70))
	WINDOW.blit(BUILDLAB_LABEL, (10, 213))
	WINDOW.blit(SCIENCE_LABEL, (10, 248))
	CASH_LABEL = FONT.render('Total Tea leaves (TL): {}'.format(CASH), 1, (255,255,0))
	LAB_LABEL = FONT.render('Labs: {}'.format(LAB), 1, (255,255,0))
	WINDOW.blit(CASH_LABEL, (0, 0))
	WINDOW.blit(LAB_LABEL, (0, 15))
	GEN1_LEVEL_LABEL = FONT.render('Level: {}/{} --- +10 TL every {} milliseconds costs: 100TL'.format(GEN1_LEVEL, 10, GEN1_TIMER), 1, (255,255,0))
	WINDOW.blit(GEN1_LEVEL_LABEL, (220, 108))
	GEN2_LEVEL_LABEL = FONT.render('Level: {}/{} --- +100 TL every {} milliseconds costs: 1000TL'.format(GEN2_LEVEL, 50, GEN2_TIMER), 1, (255,255,0))
	WINDOW.blit(GEN2_LEVEL_LABEL, (220, 143))
	GEN3_LEVEL_LABEL = FONT.render('Level: {}/{} --- +1000 TL every {} milliseconds costs: 10000TL'.format(GEN3_LEVEL, 75, GEN3_TIMER), 1, (255,255,0))
	WINDOW.blit(GEN3_LEVEL_LABEL, (220, 178))
	BUILDLAB_LEVEL_LABEL = FONT.render('You have: {} --- +10 Labs 1M TL'.format(LAB, 100, BUILDLAB_TIMER), 1, (255,255,0))
	WINDOW.blit(BUILDLAB_LEVEL_LABEL, (220, 213))
	SCIENCE_LEVEL_LABEL = FONT.render('Level: {}/{} --- +1000 TL every {} ms costs: 10000TL and 10 labs'.format(SCIENCE_LEVEL, 75, SCIENTIST_TIMER), 1, (255,255,0))
	WINDOW.blit(SCIENCE_LEVEL_LABEL, (220, 248))
	pygame.display.flip()

def game_loop():
	while True:
		handle_events()
		handle_mouse_clicks()
		update_text()

def main():
	pygame.display.set_caption('Tea-Tropolis')
	pygame.time.set_timer(GEN1_EVENT, GEN1_TIMER)
	icon = pygame.image.load('tea leaf icon.png')
	pygame.display.set_icon(icon)
	game_loop()

main()