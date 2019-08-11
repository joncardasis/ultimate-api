# TabDown
Markdown for guitar tabs.

### Why TabDown?
TabDown serves as an intermediate tab representation of guitar tabs. They can be shared between multiple platforms and the parser can be reimplemented for the platforms if needed.


### Spec
The TabDown spec consists of a number of sections each deliniated by three dashes (`---`).

##### Metadata Section
Metadata occurs at the top of a TabDown file and use the `@` identifier, following the format: `@key: value`

|key|type|valid values|optional|example|
|--- |---|---|---|---|
|song|string| any |NO|Slow Dancing in a Burning Room|
|artist|string| any |NO|John Mayer|
|tuning|string| any |YES|E A D G B E|
|difficulty|string| novice, intermediate, advanced |YES|novice|
|capo|string| 0...12 |YES|3|
|key|string| any |YES|C#m|

Example:
```
@song: When We Were Young chords
@artist: Adele
@difficulty: novice
@tuning: E A D G B E
@capo: 3
@key: Cm
---
```


##### Strumming Section (Optional)
Tabs containing strumming section(s) are represented like so:

```
@section: Whole Song
@bpm: 155bpm
...
---
```

```
@section: Verse
@bpm: 155bpm
...

@section: Chorus
@bpm: 155bpm
---
...
```


##### Tab/Chord Section
Chords in the tab are escaped via `\`.

Example:
```
    \Am              \C             \F            \C   \G/B      
If heaven and hell decide that they both are satisfied,
---
```

Chord Variations:


---

### Chord Variations

### Examples:
### Examples
https://tabs.ultimate-guitar.com/tab/adele/when_we_were_young_chords_1782038:
```
/* Metadata section */
@song: When We Were Young chords
@artist: Adele
@difficulty: novice
@tuning: E A D G B E
@capo: 3
@key: Cm

% variations:
[1]: 
[2]:

/* Tab / Chords */

```

```

[Dm][1]  [A#]           [F][2]
Do you wanna do nothing with me,

Just to watch the world...
```
```
% variations:
[1]: 
[2]:
```