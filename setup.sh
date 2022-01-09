mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

#mkdir -p ~/.streamlit/\necho "\n[general]\nemail = "woeichyi_wan@outlook.com"\n" > ~/.streamlit/credentials.toml\necho "\n[server]\nheadless = true\nenableCORS=false\nport = $PORT\n" > ~/.streamlit/config.toml
#mkdir -p ~/.streamlit/
#echo "
#[general]n
#email = "woeichyi_wan@outlook.com"n
#" > ~/.streamlit/credentials.toml
#echo "
#[server]n
#headless = truen
#enableCORS=falsen
#port = $PORTn
#" > ~/.streamlit/config.toml
