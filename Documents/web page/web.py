from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_items():
    html_content = """
    <html>
  <head>
    <title>repl.it</title>
    <style>
   body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.topnav {
  overflow: hidden;
  background-color:brown;
}

.topnav a {
  float: left;
  color:black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color:green;
  color: black;
}

.topnav a.active {
  background-color:black;
  color:brown;
}
    </style>
  </head>
  <body bgcolor=black>
    <div class="topnav">
  <a class="active" href="index.html">fortnite guide</a>
  <a href="page_two.html">monster hunter world guide</a>
</div>
  <script src="index.js"></script>
  <H1 align="center"><font color=blue>HOW TO BE A BOSS AT FORTNITE</H1>
  <hr>
  <P><h1 style="float:right"><font color="purple"> Are you bord of being killed again and again even when you have the high ground and a legandery scar? well then you are in luck for i am da best well no not realy but still i think i am good enough to teach you some tips</h1></P>
  <img alt="fn image" src="https://images.techhive.com/images/article/2014/07/screenshot_buildingediting-100355190-orig.png">  
    <h1 align="center"><font color=blue>TIP NUMBER 1:Build,Build,build!!!!</h1>
    <p><h1 algn="center">My first tip is simple and its to build. not many peole utalize the extreamly usful building in a game like this for example if your in a gun fight you can easly build a stair case to give your self a hight advantage or a wall to hide from incoming bullets so if you dont build allready then do and i bet it will help you so much.</h1></p>
    <img src="https://i.kinja-img.com/gawker-media/image/upload/t_original/y5bw2ggmeexz7xg23lg0.gif" alt="fortnite gif">
    """
    return HTMLResponse(content=html_content, status_code=200)
@app.get("/pagetwo.html", response_class=HTMLResponse)
async def read_items():
    html_content = """ 
    
    """
    return HTMLResponse(content=html_content, status_code=200)