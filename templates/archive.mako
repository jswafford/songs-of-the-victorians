<%inherit file="songbase.mako"/>

<%block name="extra_head">
${parent.extra_head()}
<%
import json
%>
  <script type="text/javascript" charset="utf-8">
$(function() {
  window.augmented_notes_data = ${json.dumps(data)};
  window.augnotes = new AugmentedNotes(augmented_notes_data);
  var img_elt = $("img.score");
  var audio_elt = $("audio#aplayer");
  window.augnotes_ui = new AugmentedNotesUI(augnotes, img_elt, audio_elt);
});
  </script>
</%block>

<%block name="title">${thetitle} - Archive</%block>

<%block name="content">
  <div class="article">
    <div class="audtools">
      <audio style="width:100%" controls="controls" id='aplayer' preload='auto'>
        <source id="ogg" src="/data/${dset}/music.ogg" type="audio/ogg"/>
        <source id="mp3" src="/data/${dset}/music.mp3" type="audio/mp3"/>
        Your browser does not support the audio tag!
      </audio>
    </div>
    <div>
      <img class="score" src="/data/${dset}/pages/1.jpg" width="100%" alt="Scan">
      <h3>Credits and Publication Information</h3>
      <p>Norton, Caroline. "Juanita." London: Chappell, 1853.</p>
        <p>"Juanita" by Caroline Norton performed by Anthony Rolfe Johnson (tenor) and Graham Johnson (piano). Courtesy of Hyperion Records Ltd, London. <a href="http://www.hyperion-records.co.uk/al.asp?al=CDH55159">http://www.hyperion-records.co.uk/al.asp?al=CDH55159</a></p>
    </div>
  </div>
</%block>