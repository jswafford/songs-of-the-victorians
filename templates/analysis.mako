<%inherit file="songbase.mako"/>

<%block name="title">${thetitle}</%block>

<%block name="content">
  <div class="article">
    <h2 class="title">${thetitle}</h2>

    ${analysis_html}

  </div>
</%block>