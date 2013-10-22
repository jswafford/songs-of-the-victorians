<%inherit file="base.html"/>

<%block name="extra_head">
  <script type="text/javascript">
  $(function() {
    $(".tabs").tabs();
    $(".tabs").bind("tabsactivate", function(event, ui) {
      history.pushState(null, null, "#"+ui.newPanel.attr("id"));
    });
    $(".button").click(function() {
      $('a', this).click();
    })
  })
  </script>
</%block>

<%block name="header">
    <img src="/static/img/splash-top.jpg" alt="Songs of the Victorians: An Archive Designed and developed by Joanna Swafford, Containing parlor and art song settings of Victorian poems, using Augmented Notes. Coming soon!" />
    <div style="height:10px; width:10px"></div>
</%block>

<%block name="content">
  <div class="tabs">
    <ul class="navbar">
      <li class="navitem"><a href="#home">Home</a></li>
      <li class="navitem"><a href="#about">About</a></li>
      <li class="navitem"><a href="#songs">Songs</a></li>
      <li class="navitem"><a href="#thanks">Special Thanks</a></li>
    </ul>
    <div style="clear:both"></div>
    <div id="home">
      <div style="height:20px; width:10px"></div>
      <img src="/static/img/splash-bottom.jpg" alt="Songs of the Victorians: An Archive Designed and developed by Joanna Swafford, Containing parlor and art song settings of Victorian poems, using Augmented Notes. Coming soon!" />
    </div>
    <div id="about">
      <div class="article">
        <h2> About Songs of the Victorians </h2>
        <p>
          Welcome to Songs of the Victorians, an archive of parlor and art song settings of Victorian poems, and also a scholarly tool to facilitate interdisciplinary music and poetry scholarship.  It is designed and developed by Joanna Swafford with the generous support of a Scholars' Lab Fellowship from the University of Virginia.  It contains four songs:  Michael William Balfe's "Come into the Garden, Maud" and Sir Arthur Somervell's "Come into the Garden, Maud" (both based on Alfred Lord Tennyson's monodrama, <i>Maud</i>), Sir Arthur Sullivan's version of Adelaide Procter's "A Lost Chord," and Caroline Norton's "Juanita," although for the March 11th "sneak-peek release" it only includes "Juanita."
        </p>
        <p>
          Parlor and art song settings of Victorian poems are not mere examples of Victorian kitsch: rather, these settings function as readings of the poems they use as lyrics. Songs of the Victorians includes parlor songs alongside art songs to challenge the conventional musicological assumption that popular, domestic music na&iuml;vely misrepresents its poetic source material.  Many parlor songs actually perform nuanced understandings of the texts they set and address subjects such as the silencing of women, the difficulty of resolving gender inequalities, religious questionings, and "cross-singing," or women singing text written for a male character.  These socially acceptable, sentimental songs often enabled women to address transgressive topics that otherwise would have been forbidden.
        </p>
        <p>
          Since many of these songs are available only in a handful of special collections libraries, this archive enables a wider range of scholars to view digital versions.  Its digital form can in fact enhance the original, since with songs, merely digitizing scores helps only the most adept scholars; many cannot read music, and those who can are often unable to hear in their minds the music printed on the page. The Songs of the Victorians framework helps solve that problem.
        </p>
        <p>
        The archival portion of this site includes high-resolution images of the first edition printings of each song integrated with an audio file so that each measure is highlighted in time with the music.  The scholarly component for each work includes an article-length analysis of the song's interpretation of the poem. Whenever this analysis references a specific section of the piece, the reader can click the speaker symbol (<img src="/static/img/tinyspeaker.png"/>) to view the score and hear the audio for this excerpt, again with the measures highlighted in time with the music. In this way all scholars, regardless of their ability to read music, can follow both the score and the thread of the argument.
        </p>
        <p>
        Songs of the Victorians will continue adding new songs for the foreseeable future, and it may in a few years be open to accepting submissions from other scholars interested in archivally preserving and analyzing parlor and art song settings of Victorian poems digitally.
        </p>
        <p>
        To learn more about the creation of this site or to receive updates on its development schedule, please visit and subscribe to the development blog, <a href="http://anglophileinacademia.blogspot.com/">"Anglophile in Academia"</a>.  Please email using the link at the bottom of the page to provide comments and feedback!
        </p>
        <p>Please note: the audio clips may not work on older browsers. If you experience this problem, please upgrade your browser or try a different one.</p>
        <h2> About the Author</h2>
        <p>
        Joanna Swafford is a PhD candidate in the English Department at the University of Virginia, specializing in Victorian poetry, sound studies, and digital humanities.  She has forthcoming articles in <i>Victorian Poetry</i>, <i>Victorian Review</i>, and the <i>Victorian Institute Journal's</i> Digital Annex, and she has held multiple digital humanities fellowships:  the Scholars' Lab Fellowship (2012-2013), the Praxis Program Fellowship (2011-2012), and the NINES fellowship (2010-2012).  Her dissertation, "Transgressive Tunes and the Music of Victorian Poetry," traces the gendered intermediations of poetry and music, and the final chapter on musical settings of Victorian poems will have an exclusively digital form drawn from this website.  She was also lead developer on the Praxis Program's project, <a href="http://prism.scholarslab.org/">Prism</a>, a tool for collective interpretation.  In addition to designing and developing Songs of the Victorians, she is also creating Augmented Notes, a website where users will upload scores, audio files, and measure information to produce websites like Songs of the Victorians, thus enabling scholars to pursue their own interdisciplinary projects.
        </p>
      </div>
    </div>
    <div id="thanks">
      <div class="article">
        <h1>Special Thanks</h1>
        <h3>This project was made possible by the kind support of the following people and groups:</h3>
        <p>The Scholars' Lab: <a href="http://www.scholarslab.org/">http://www.scholarslab.org/</a></p>
        <p>The University of Virginia's English Department: <a href="http://www.engl.virginia.edu/">http://www.engl.virginia.edu/</a></p>
        <p>NINES (Networked Infrastructure for Nineteenth-Century Electronic Scholarship): <a href="http://www.scholarslab.org/">http://www.scholarslab.org/</a></p>
        <p>The Buckner W. Clay Endowment Committee: <a href="http://www.virginia.edu/humanities/awards/clay-fellowships/">http://www.virginia.edu/humanities/awards/clay-fellowships/</a></p>
        <p>Hyperion Records: <a href="http://www.hyperion-records.co.uk/">http://www.hyperion-records.co.uk/</a></p>
        <p>The British Library: <a href="http://www.bl.uk/">http://www.bl.uk/</a></p>
        <p>The National Library of Australia: <a href="http://www.nla.gov.au/">http://www.nla.gov.au/</a></p>
        <p>San Francisco Public Library: <a href="http://sfpl.org/">http://sfpl.org/</a></p>
        <p>The Royal Academy of Music Library: <a href="http://www.ram.ac.uk/library">http://www.ram.ac.uk/library</a></p>
        <p>The Royal College of Music Library: <a href="http://www.rcm.ac.uk/library/">http://www.rcm.ac.uk/library/</a></p>
        <p>Herbert Tucker: <a href="http://www.engl.virginia.edu/people/ht2t">http://www.engl.virginia.edu/people/ht2t</a></p>
        <p>Andrew Stauffer: <a href="http://www.engl.virginia.edu/people/ams4k">http://www.engl.virginia.edu/people/ams4k</a></p>
        <p>Bruce Holsinger: <a href="http://www.engl.virginia.edu/people/bh9n">http://www.engl.virginia.edu/people/bh9n</a></p>
        <p> Derek Scott: <a href="http://music.leeds.ac.uk/people/derek-scott/">http://music.leeds.ac.uk/people/derek-scott/</a></p>
        <p>Perry Roland and the MEI Developers: <a href="http://www2.lib.virginia.edu/innovation/mei/">http://www2.lib.virginia.edu/innovation/mei/</a></p>
        <p>Daniel Lepage: <a href="http://www.dplepage.com">http://www.dplepage.com</a></p>
        <p>Inferlogic: <a href="http://inferlogic.deviantart.com/art/Black-White-Floral-Background-119926091">http://inferlogic.deviantart.com/art/Black-White-Floral-Background-119926091</a></p>
      </div>
    </div>
    <div id="songs">
      <div class="songs" style="position:relative">
        <img style="float:left" class="thumb" src="/static/img/Nortoncover1.jpg" alt="Caroline Norton&#39;s &#39;Juanita&#39;">
        <div class="links">
            <a class="button" href="/norton/analysis.html">
              Music Analysis
            </a>
            <a class="button" href="/norton/archive.html">
              Archive
            </a>
        </div>
        <span class="title">"Juanita" (1853)</span><br/>
        <span class="author">By Caroline Norton</span><br/><br/>
      </div>
      <div class="hr"></div>
      <div class="songs">
        <img style="float:left" class="thumb" src="/static/img/balfe_cover.jpg" alt="Michael William Balfe&#39;s &#39;Come into the Garden Maud">
        <div class="links has3">
            <a class="button" href="/tennyson/analysis.html">
              Poem Analysis
          </a>
          <a class="button" href="/balfe/analysis.html">
            Music Analysis
          </a>
          <a class ="button" href="/balfe/archive.html">
            Archive
          </a>
        </div>
        <span class="title">"Come into the Garden Maud" (1857)</span><br/>
        <span class="author">By Michael William Balfe</span><br/><br/>
        A setting from <i>Maud</i> &nbsp;(1855)<br/>
        By Alfred Lord Tennyson <br/>
      </div>
      <div class="hr"></div>
      <div class="songs">
        <img style="float:left" class="thumb" src="/static/img/somervell_cover.jpg" alt="Sir Arthur Somervell&#39;s &#39;Come into the Garden Maud&#39;">
        <div class="links has3">
            <a class="button" href="/tennyson/analysis.html">
              Poem Analysis
          </a>
          <a class="button" href="/somervell/analysis.html">
            Music Analysis
          </a>
          <a class ="button" href="/somervell/archive.html">
            Archive
          </a>
        </div>
        <span class="title">"Come into the Garden Maud" (1898)</span><br/>
        <span class="author">By Sir Arthur Somervell</span><br/><br/>
        A setting from <i>Maud</i> &nbsp;(1855)<br/>
        By Alfred Lord Tennyson <br/>
      </div>
      <div class="hr"></div>
      <div class="songs">
        <img style="float:left" class="thumb" src="/static/img/sullivan_cover.jpg" alt="Sir Arthur Sullivan&#39;s &#39;The Lost Chord&#39;">
        <div class="links">
            <a class="button" href="/sullivan/analysis.html">
              Music Analysis
            </a>
            <a class="button" href="/sullivan/archive.html">
              Archive
            </a>
        </div>
        <span class="title">"The Lost Chord" (1877)</span><br/>
        <span class="author">By Sir Arthur Sullivan</span><br/><br/>
        A setting of "A Lost Chord" &nbsp;(1858)<br/>
        By Adelaide Ann Procter<br/>
      </div>
      <div style="clear:both"></div>
    </div>
  </div>
</%block>
