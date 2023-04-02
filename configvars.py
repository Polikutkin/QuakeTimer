from random import randrange
from configparser import ConfigParser


def normalize(input_str):
    return input_str.strip('"') if '#' in input_str else input_str


config = ConfigParser()
config.read('config.ini')

# common section values
exit_key = config.get('common', 'exit_key')
window_x_y_position_pixels = config.get('common', 'window_x_y_position_pixels')
text_size = config.getint('common', 'text_size')
bold_text = config.getboolean('common', 'bold_text')
font = config.get('common', 'font')
visibility = config.getfloat('common', 'visibility')
transparent_bg = config.getboolean('common', 'transparent_bg')
enable_sound_alarm = config.getboolean('common', 'enable_sound_alarm')
sound_alarm_timeout_seconds = config.getint('common', 'sound_alarm_timeout_seconds')

# mega section values
mega_timeout_seconds = config.getint('mega', 'timeout_seconds')
mega_text_color = normalize(config.get('mega', 'text_color'))
mega_bg_color = normalize(config.get('mega', 'bg_color'))
mega_attention_timeout_seconds = config.getint('mega', 'attention_timeout_seconds')
mega_attention_text_color = normalize(config.get('mega', 'attention_text_color'))
mega_attention_bg_color = normalize(config.get('mega', 'attention_bg_color'))
mega_warning_timeout_seconds = config.getint('mega', 'warning_timeout_seconds')
mega_warning_text_color = normalize(config.get('mega', 'warning_text_color'))
mega_warning_bg_color = normalize(config.get('mega', 'warning_bg_color'))
mega_start_key = config.get('mega', 'start_key')

# heavy section values
heavy_timeout_seconds = config.getint('heavy', 'timeout_seconds')
heavy_text_color = normalize(config.get('heavy', 'text_color'))
heavy_bg_color = normalize(config.get('heavy', 'bg_color'))
heavy_attention_timeout_seconds = config.getint('heavy', 'attention_timeout_seconds')
heavy_attention_text_color = normalize(config.get('heavy', 'attention_text_color'))
heavy_attention_bg_color = normalize(config.get('heavy', 'attention_bg_color'))
heavy_warning_timeout_seconds = config.getint('heavy', 'warning_timeout_seconds')
heavy_warning_text_color = normalize(config.get('heavy', 'warning_text_color'))
heavy_warning_bg_color = normalize(config.get('heavy', 'warning_bg_color'))
heavy_start_key = config.get('heavy', 'start_key')

transparent_color = 'black'
if transparent_bg:
    text_colors = {
        mega_text_color,
        mega_attention_text_color,
        mega_warning_text_color,
        heavy_text_color,
        heavy_attention_text_color,
        heavy_warning_text_color
    }

    while transparent_color in text_colors:
        transparent_color = '#' + ''.join([str(randrange(10)) for i in range(6)])

    mega_bg_color = mega_attention_bg_color = mega_warning_bg_color = heavy_bg_color = heavy_attention_bg_color = heavy_warning_bg_color = transparent_color
