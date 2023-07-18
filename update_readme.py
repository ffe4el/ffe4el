import feedparser

sola_blog_rss_url = "https://ffe4el.tistory.com/rss"
rss_feed = feedparser.parse(sola_blog_rss_url)

MAX_POST_NUM = 10

latest_blog_post_list = ""

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"


markdown_text = """[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fffe4el&count_bg=%23FF7676&title_bg=%23000000&icon=openai.svg&icon_color=%23E5A0A0&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
.
<!-- 인사말 -->
![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=300&section=header&text=SOLA%20GITHUB🎀&fontSize=90&animation=fadeIn&fontAlignY=38&desc=studying%20GenerativeAI%20and%20FullStack&descAlignY=51&descAlign=62)
<!-- <h1 align="center">HI 👋, I'M SOLA</h1> -->


<!-- 백준레벨 -->
[![Solved.ac프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=codkan)](https://solved.ac/백준아이디)
</h4></div>


<!-- 사용하는 언어와 도구들 -->
  <h4 align=center> languages and tools: </h4>
<p align=center>
<!--   python -->
  <code><img height="30" src="https://cdn-icons-png.flaticon.com/512/5968/5968350.png"></code> 
<!--   html -->
  <code><img height="30" src="https://cdn-icons-png.flaticon.com/512/5968/5968267.png"></code>
<!--   css -->
  <code><img height="30" src="https://cdn-icons-png.flaticon.com/512/5968/5968242.png"></code>
<!--   javascript -->
  <code><img height="30" src="https://cdn-icons-png.flaticon.com/512/1199/1199124.png"></code>
<!--   C -->
  <code><img height="30" src="https://user-images.githubusercontent.com/93892724/210708533-60adaa42-cf77-4ffb-8576-246512979764.png"></code>
<!--   C++ -->
  <code><img height="30" src="https://cdn-icons-png.flaticon.com/512/6132/6132222.png"></code>
<!--   vs code -->
  <code><img height="30" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/2048px-Visual_Studio_Code_1.35_icon.svg.png"></code>
<!--   pycharm -->
  <code><img height="30" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1024px-PyCharm_Icon.svg.png"></code>
<!--   Clion -->
<code><img height="30" src="https://user-images.githubusercontent.com/93892724/211053466-f8474354-71fd-486e-bacf-4b597d98dc8e.png"></code>
<!--   jupyter -->
  <code><img height="30" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1200px-Jupyter_logo.svg.png"></code>
<br><br></p>
  
  
<!-- 깃허브레벨, 자주쓰는 언어 -->
<p align="center"><img src="https://github-readme-stats.vercel.app/api?username=ffe4el&bg_color=30,e96443,904e95&title_color=fff&text_color=fff">
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=ffe4el&bg_color=30,e96443,904e95&title_color=fff&text_color=fff"></p>




  

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
