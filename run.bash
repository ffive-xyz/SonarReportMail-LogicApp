# use this script to trigger logicapp

pip3 install -r requirements.txt
html=$(python3 program.py)
echo "'$html'"
echo "'$LOGICAPP_URL'"

wget --no-check-certificate --quiet \
  --method POST \
  --timeout=0 \
  --header 'Content-Type: text/plain' \
  --body-data "'$html'" \
  "'$LOGICAPP_URL'"