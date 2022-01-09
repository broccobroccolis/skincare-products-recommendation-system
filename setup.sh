mkdir -p ~/.streamlit/
echo "
[general]n
email = "woeichyi_wan@outlook.com"n
" > ~/.streamlit/credentials.toml
echo "
[server]n
headless = truen
enableCORS=falsen
port = $PORTn
" > ~/.streamlit/config.toml