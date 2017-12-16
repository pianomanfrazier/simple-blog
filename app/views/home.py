from flask import render_template, redirect, url_for

from app import app

body = """
# Quam pigetque

## Argentea obnoxia mutataeque simul

Lorem markdownum coepere Thebis vixque ego prius cave algae, vires puero, ab.
Meae illo hominem auras Parthaone Nereis resonant plano nec eum, multa felices
viriles afueram: nec edam. Pectusque aliquis conlectus **effugit** cultique
Rhadamanthon multa acutae deseruit mitto. Haec cum qua funesta tremit speculabar
ignota segetem! Vos latus obstitit, felix, fata nunc visum formosus: quod!

- En suspirat urget ut cadunt arbore promittit
- Nil texit potest
- Tunc iamque duobus ternis nimis neque quae
- Peragit hanc
- Tuta pronepos terras currus Aeacide lamentabile exigere

First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell

## Tum manu

Inque misit! Tamen zephyri, lumina crescitque Perseus invideatis pinguia semina,
dolore, liquitur litora repetita.

- Extulit gravitate accessisse conpellat addidici toto parte
- Nocens ipse
- Longum bracchia Astraei messis palus
- Finiat ab ait tamen icta
- Opposuitque multo contraria iura est aestuat inque
- Bistoniis fiat ac omnemque ultima

Sui inquit ait cecidere iam, **verbis**, quam. Repellit et fata clamore credat
discedere, tibi nova viae, dare. Est eiectat potero hunc, letiferos componar, an
effluat. Natam et mercede longoque si tantus Persea. Latices iacent.

<script> alert('hacked'); </script>

```javascript
<script> alert('hacked'); </script>
```

## In sed Volturnus in occasus capellae contingere

*Nec nitidae premit*, armenti odiis, qui lumine debere gemitu Myrrha venerande
oblectamina, nosterque. Anno habebat silentia quoque Iovis nostra harenae luna
conubia quaesita iam caput qua fallaces, mixtos, et. Nostro gentis colla, sic
subito necis admoto creverat? Eque dum fides thalamos.

Pectora in cinerem umor certo forma, fontesque te ibat. Euboea deducens nec sum
ac elementaque tellus facies properatus ad nostris contigit eligit conpendia.
**Et ut** labore dixit tenens quem cepit Aeoliique. In Iphis tua et retro,
[omnes coercet](http://narisaris.com/tacitorum) comas.
"""

#database add create date, update date
posts = [
  { 'title' : 'How to tame a cat',
    'date'  : 'December 16, 2017',
    'slug'  : 'tame-a-cat',
    'tags'  : ['food', 'stuff', 'cat'],
    'body'  : body,
    'draft' : False
  },
  { 'title' : 'How to tame a wildabeast',
    'date'  : 'December 18, 2017',
    'slug'  : 'tame-your-wildabeast',
    'tags'  : ['food', 'stuff', 'cat'],
    'body'  : body,
    'draft' : False
  },
  { 'title' : 'How to tame a bear',
    'date'  : 'December 17, 2017',
    'slug'  : 'tame-your-bear',
    'tags'  : ['food', 'stuff', 'cat'],
    'body'  : body,
    'draft' : False
  },
]

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html', posts=posts)

@app.route('/post')
@app.route('/post/<slug>')
def post(slug=None):
  if slug == None:
    return redirect(url_for('index'))
  else:
    post = {}
    for p in posts:
      if p['slug'] == slug:
        post = p
    return render_template('post.html', post=post)

#@app.route('/tags')
#@app.route('/tags/<tag>')
#def tags(tag=None):
#  if tag == None:
#    #show all tags
#  else:
#    #filter by tag

