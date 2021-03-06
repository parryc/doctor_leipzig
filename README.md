# Leipzig, MD

## What is this?

An extension for [Python Markdown](https://pythonhosted.org/Markdown/)

## How do I use it?

You can look at _leipzig.md_ for a full example of how to do anything that the _[The Leipzig Glossing Rules](http://www.eva.mpg.de/lingua/resources/glossing-rules.php)_ allow for. 

Surround the text you want to gloss with `--GLOSS--` and `--ENDGLOSS--`. Anchors are created in order for each gloss as `leipzig-line-1`. The number has the class _leipzig-num_. The first 4 lines in a gloss are marked with the classes _source_, _morphemes_, _translation_, _translation_. The whole gloss has the class _leipzig-table_.

### Small Caps `{ABC}`

Use `{ABC}` to render `ABC` in small caps.  If this matters to you, I suggest using Computer Modern for your gloss font (it's free and has a wide range of glyphs).

### Full lines `{!}`

Use `{!}` at the front. For example:

```
--GLOSS--
{!} Latin
insul-arum
island-{GEN.PL}
{!} of the islands
--ENDGLOSS--
```

### Spaces in gloss items `' '`

Surround the item with single quotes, ex.

```
--GLOSS--
Бейнең жеке менің түн-ием,
image-{2SG.POSS} personal {1SG.GEN} 'night spirit-{1SG.POSS}'
{!} Your image is my personal night spirit
--ENDGLOSS--
```

### Merging Lines `{m}`

If you need to have one gloss encompass multiple source words (say for an idiom), place as many `{m}` in front of the word you'd like to merge

```
--GLOSS--
Тез қол ұшын бер маған, тез!
quickly {m} {m} 'to give a hand' {1SG.DAT}, quickly!
{!} Hold out your hand, quickly!
{!} Quickly give me a hand, quickly!
--ENDGLOSS--
```

`to give a hand` will be paired with `қол ұшын бер`.

### Blank gloss `{b}`

If you need a blank to appear in any of the lines, use `{b}`.

```
--GLOSS--
{!} Latin
puer or: puer-Ø
boy[{NOM.SG}] {b} boy-{NOM.SG}
'boy' {b} 'boy’
--ENDGLOSS--
```