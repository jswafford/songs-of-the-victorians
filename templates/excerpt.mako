<%!
import json
%>

<!DOCTYPE html>
<html>
<head>
    <link type="text/css" rel="stylesheet" href="/static/css/style.css"/>

  <style>
  div.box {
    border: 4px solid rgb(128,81,44);
    background-color: rgba(0,0,0,0);
    position:absolute;
  }
  </style>
  <script src="/static/js/jquery.js"></script>
  <script src="/static/js/augnotes.js"></script>
  <script src="/static/js/augnotesui.js"></script>
  <script type="text/javascript" charset="utf-8">
  $(function() {
    window.augmented_notes_data = ${json.dumps(data)};
    window.augnotes = new AugmentedNotes(augmented_notes_data);
    var img_elt = $("img.score");
    var audio_elt = $("audio#aplayer");
    window.augnotes_ui = new AugmentedNotesUI(augnotes, img_elt, audio_elt);
  });
  </script>
</head>
<body>
  <div class="center-content">
    <div class="audtools">
      <audio style="width:612px" controls="controls" id='aplayer' preload='auto' autoplay>
        <source id="mp3" src="/data/${dset}/music.mp3" type="audio/mp3"/>
        <source id="ogg" src="/data/${dset}/music.ogg" type="audio/ogg"/>
        Your browser does not support the audio tag!
      </audio>
    </div>
    <div>
      <img class="score" src="/data/${dset}/pages/1.jpg" width="612px" alt="Score Image"/>
    </div>
  </div>
</div>
</body>
</html>
