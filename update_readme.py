import feedparser

sola_blog_rss_url = "https://ffe4el.tistory.com/rss"
rss_feed = feedparser.parse(sola_blog_rss_url)

MAX_POST_NUM = 7

latest_blog_post_list = ""

for idx, feed in enumerate(rss_feed['entries']):
    if idx >= MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - <a href='{feed['link']}'>{feed['title']}</a><br>\n"

# 기본 README.md 내용 정의
markdown_text = """
📬  Contact Email : codkan20@gmail.com

👨🏻‍💻  Tech & Daily Blog : https://ffe4el.tistory.com

<!-- 사용하는 언어와 도구들 -->
📚  Lang & Stack :<br><br>
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/c++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white">
<img src="https://img.shields.io/badge/java-007396?style=for-the-badge&logo=java&logoColor=white">
<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"><br>
<img src="https://img.shields.io/badge/spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white">
<img src="https://img.shields.io/badge/springboot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white">
<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white">
<br><br>
🧩  PS Lang :<br><br>
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/c++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white">

<br> 

🏫 Currently in **KAIST** Visual Media Lab, <br>
adviser prof. Junyong Noh 

<h3>🤩 Latest Blog Post</h3>
"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

# README.md 파일 업데이트
with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
