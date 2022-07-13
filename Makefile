.PHONY = all upload

all: upload

upload: settings.txt .ampy
	ampy put settings.txt
	ampy put main.py
	ampy put environment_sensor/