# May need to install diff2html first -- `npm install -g diff2html-cli`
diff -Nru --exclude ".pytest_cache" --exclude "__pycache__" --exclude ".DS_Store" "$1" "$2" | diff2html -i stdin -s side
