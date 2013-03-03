<%inherit file="base.html"/>

<%block name="extra_head">
  <script src="/static/js/jquery.js"></script>
  <script src="/static/js/augnotes.js"></script>
  <script src="/static/js/augnotesui.js"></script>
</%block>

<%block name="header">
  <div id="header-left">
    <img src="/static/img/logo.jpg" class="header-logo">
  </div>
  <div id="header-right">
    <div class="content">
      <b>
        An archive and analysis of parlor and art song settings of
        Victorian poems
      </b>
    </div>
  </div>
  <div style="clear:both"></div>
  <%block name="navbar">
  <ul class="navbar">
    <li class="navitem active"><a href="/index.html">Home</a></li>
    <li class="navitem"><a href="/index.html#about">About</a></li>
    <li class="navitem"><a href="/index.html#songs">Songs</a></li>
  </ul>
  </%block>
</%block>
