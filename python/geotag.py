# Change Image path and address accordingly
from PIL import Image, ImageDraw, ImageFont
import requests
import io
import os

base_image_path = "/Users/Asus/Desktop/console-applications/python/bd.jpeg"
img = Image.open(base_image_path).convert("RGBA")
draw = ImageDraw.Draw(img)

font_path = "/Users/Asus/Desktop/console-applications/python/fonts"
try:
    font_title = ImageFont.truetype(f"{font_path}/arialbd.ttf", 38)
    font_text = ImageFont.truetype(f"{font_path}/arial.ttf", 30)
    font_small = ImageFont.truetype(f"{font_path}/arial.ttf", 22)
except:
    print("⚠️ Arial fonts not found, fallback to default fonts")
    font_title = font_text = font_small = ImageFont.load_default()

lat, lon = 19.018165, 72.844016
location = "Dadar, Maharashtra, India"
address_line1 = "Swami Gyan Jivandas Marg, Dadar East,"
address_line2 = "Mumbai, Maharashtra, India"
date = "17/04/25 13:04 UTC+05:30"
watermark = "Captured by Tagofy Geotag Camera"

def get_map(lat, lon):
    url = f"https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v12/static/pin-s+ff0000({lon},{lat})/{lon},{lat},17,0/400x400?access_token=pk.eyJ1IjoiYWxpYXNnYXIxODAwIiwiYSI6ImNtOWs1ZzVpZTA5MTAyaXNiNzUzdzYzZm8ifQ.7m5jOaIe0tfODK8PIg5JZA"
    resp = requests.get(url)
    return Image.open(io.BytesIO(resp.content))

margin_bottom = 30
map_width = 230  
map_height = 260
gap_between_map_text = 40  
extra_watermark_gap = 20

y_start = img.height - map_height - margin_bottom - extra_watermark_gap

map_x = 30
map_y = y_start
map_img = get_map(lat, lon).resize((map_width, map_height))
img.paste(map_img, (map_x, map_y))

text_block_x = map_x + map_width + gap_between_map_text
text_block_y = map_y
text_block_width = img.width - text_block_x - 30  
text_block_height = map_height

overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
overlay_draw = ImageDraw.Draw(overlay)
overlay_draw.rounded_rectangle(
    [(text_block_x - 20, text_block_y), (img.width - 30, text_block_y + text_block_height)],
    radius=30,
    fill=(30, 30, 30, 180)
)
img = Image.alpha_composite(img, overlay)

draw = ImageDraw.Draw(img)
x_text = text_block_x
y_text = text_block_y + 20

draw.text((x_text, y_text), location, font=font_title, fill="white")
y_text += font_title.size + 10

draw.text((x_text, y_text), address_line1, font=font_text, fill="white")
y_text += font_text.size + 8

draw.text((x_text, y_text), address_line2, font=font_text, fill="white")
y_text += font_text.size + 10

draw.text((x_text, y_text), f"Lat: {lat}, Long: {lon}", font=font_text, fill="white")
y_text += font_text.size + 8

draw.text((x_text, y_text), date, font=font_text, fill="white")

watermark_text_width = draw.textlength(watermark, font=font_small)
x_watermark = img.width - watermark_text_width - 30
y_watermark = text_block_y + text_block_height + 10  # just below box

draw.text((x_watermark, y_watermark), watermark, font=font_small, fill=(255, 255, 255, 180))


output_path = "/Users/Asus/Desktop/console-applications/python/final_tagofy_stretchedperfect.png"
img.save(output_path, format="PNG")
print(f"✅ FINAL stretched aligned watermarked Tagofy-style saved at {output_path}")
