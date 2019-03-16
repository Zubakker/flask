from flask import Flask
from flask import url_for, request
from random import choice
from index import gen_audio
 
app = Flask(__name__)

 
@app.route('/')
@app.route('/form_sample', methods=['POST', 'GET'])
def low_button():
    letters = [".-", "-...", "-.-.", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    if request.method == 'GET':
        n = 0
    elif request.method == "POST":
        n = int(request.form['class'])
    lessons = open("lessons.txt", "r").read().split("\n")
    inp = str()
    for i in range(1, 41):
        inp += choice(lessons[int(n)])
        if i % 4 == 0:
            inp += " "
    gen_audio(inp)
    gen_audio(lessons[int(n)][-1], name="letter.wav")
    return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport"
                        content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                        crossorigin="anonymous">
                        <title>Пример формы</title>
                        <script>
                          function check() {}
                            var a = document.getElementById("about");
                            var b = "{}";
                            var k = Math.abs(b.length - a.value.length);
                            for(var i = 0; i < Math.min(a.length, b.length); ++i){}
                              if (a.value.toLowerCase().charAt(i) != b.charAt(i)) k ++;
                            {}
                            a.value = "Получено:\\n" + a.value.toLowerCase() + "\\nОтправлено:\\n" + b + "\\nОшибок:" + k.toString();
                            {}
                        </script>
                      </head>
                      <body>
                        <form method="post">
                            <div class="form-group">
                               
                                <label id="br" style="position: absolute; top:0px; left:90px; width:210px; height:25px"><b>Изучение морзы</b></label>

                                <label style="position: absolute; top:0px; left:10px; width:70px; height:25px" for="classSelect">урок</label>
                                <audio controls style="position: absolute; top:185px; left:0px;">
                                  <source src="static/audio/lesson.wav" type="audio/wav">
                                  Your browser does not support the audio element.
                                </audio>
                                
                                <audio controls style="position: absolute; top:105px; left:0px;">
                                  <source src="static/audio/letter.wav" type="audio/wav">
                                  Your browser does not support the audio element.
                                </audio>
                                
                                <label style="position: absolute; top:80px; left:10px; width:290px; height:10px" for="about">знакомьтесь, буква {}</label>
                                <label style="position: absolute; top:160px; left:10px; width:295px; height:10px" for="about">запишите то что услышите</label>
                                <textarea class="form-control" id="about" rows="3" name="about" style="position: absolute; font-size:125%; top:250px; left:0px; width:300px; height:100px"></textarea>
                                <button type="submit" class="btn btn-primary" style="position: absolute; top:30px; left:80px; width:220px; height:50px;" action="num.py">выбрать</button>                     
                                <select class="form-control" id="classSelect" name="class" style="position: absolute; top:30px; left:0px; width: 70px; height: 50px;">
                                  <option selected>{}</option>
                                  <option>0</option>
                                  <option>1</option>
                                  <option>2</option>
                                  <option>3</option>
                                  <option>4</option>
                                  <option>5</option>
                                  <option>6</option>
                                  <option>7</option>
                                  <option>8</option>
                                  <option>9</option>
                                  <option>10</option>
                                  <option>11</option>
                                  <option>12</option>
                                  <option>13</option>
                                  <option>14</option>
                                  <option>15</option>
                                  <option>16</option>
                                  <option>17</option>
                                  <option>18</option>
                                  <option>19</option>
                                  <option>20</option>
                                  <option>21</option>
                                  <option>22</option>
                                  <option>23</option>
                                  <option>24</option>
                                  <option>25</option>
                                  
                                </select>
                            </div>
                            <button type="button" class="btn btn-primary" style="position: absolute; top:355px; left:0px; width:300px; height:50px" value="himyfriend" onclick="check()">отправить на проверку</button>
                        </form>
                      </body>
                    </html>'''.format("{", inp, "{", "}", "}", str(lessons[int(n)][-1]), str(n))
 
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

