#!/bin/bash -x

key=quickstart-QUdJIGlzIGNvbWluZy4uLi4K
# key=eff7f9f8-6b01-42ba-af24-32ea16ce522d

echo Requesting: $@...

json=$(curl -# -F "$(echo text=$@)" -H "api-key:$key" https://api.deepai.org/api/text2img)
imgUrl=$(echo $json | jq .output_url)

echo Saving image $imgUrl...

curl -# "$imgUrl" > aimage.png

xdg-open aimage.png
