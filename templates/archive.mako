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
  var score_div = $(".score-div");
  var audio_elt = $("audio#aplayer");
  window.augnotes_ui = new AugmentedNotesUI(augnotes, score_div, audio_elt);
});
  </script>
</%block>

<%block name="title">${thetitle} - Archive</%block>

<%block name="content">
  <div class="article">
    <div class="audtools">
      <audio style="width:100%" controls="controls" id='aplayer' preload='auto'>
        <source id="mp3" src="/data/${dset}/music.mp3" type="audio/mp3"/>
        <source id="ogg" src="/data/${dset}/music.ogg" type="audio/ogg"/>
        Your browser does not support the audio tag!
      </audio>
    </div>
    <div>
      <div class="score-div">
        % for i in range(npages):
          <div class="score-page" ${'style="display:none"' if i !=0 else ''}>
            <img class="score" src="/data/${dset}/pages/${i+1}.jpg" width="542px" alt="Page ${i+1}"/>
          </div>
        % endfor
      </div>
      % if credits:
        <h3>Credits and Publication Information</h3>
        ${credits}
      %endif
    </div>
  </div>
</%block>