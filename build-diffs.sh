# May need to install diff2html first -- `npm install -g diff2html-cli`
mkdir .empty
diff -Nru --exclude ".pytest_cache" --exclude "__pycache__" --exclude ".DS_Store" .empty app-section-1 | diff2html -i stdin -s side -F diffs/1.html
diff -Nru --exclude ".pytest_cache" --exclude "__pycache__" --exclude ".DS_Store" app-section-1 app-section-2 | diff2html -i stdin -s side -F diffs/2.html
diff -Nru --exclude ".pytest_cache" --exclude "__pycache__" --exclude ".DS_Store" app-section-2 app-section-3 | diff2html -i stdin -s side -F diffs/3.html
diff -Nru --exclude ".pytest_cache" --exclude "__pycache__" --exclude ".DS_Store" app-section-3 app-section-4 | diff2html -i stdin -s side -F diffs/4.html

rmdir .empty
