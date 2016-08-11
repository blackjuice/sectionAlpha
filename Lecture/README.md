# Introdução à Web
*workshop by: IME Workshop*

This lecture consists on 4 parts:

| date   | topic |
|:-------|:------|
| 160804 | [HTML + CSS](#lecture1) |
| 160811 | [Javascript + jQuery](#lecture2) |
| 1608XX | [Forms + AJAX + JSON](#lecture3) |
| 1608XX | [Bootstrap](#lecture4) |

Description:
> Na primeira oficina do ciclo de Introdução a Web, vamos ver os conceitos de HTML5 e CSS3 que nos permitem estruturar o layout da nossa aplicação Web e estilizá-la como quisermos.

Main source: http://slides.com/imeworkshop/

## Quick notes

1st lecture:

* MariaDB, PostgreSQL are MySQL open-source alternatives;
* *tool: https://jsfiddle.net/*;
* It was recommended to learn AngularJS;
* **LAMP** is a stack type;

2nd lecture:

* jQuery, Node (server), Angular (popular between startups) are libraries for Javascript;
* As mobiles dows not support Javascript, we have an alternative such as *Apache Cordova*;
* insert jQuery before your Javascript;

## Lecture1
# First course: HTML + CSS
*lecture given by Gustavo Silva*

The folder on this repository named [`160804_html_css`](https://github.com/blackjuice/sectionAlpha/tree/master/Lecture/160804_html_css) contains files created throughout lecture as practical exercises. As for the slides, follow [`this link`](http://slides.com/imeworkshop/oficina-html-css#/) (material created with https://slides.com/).

### custom tags:

* **class**: identify one or more elements. On HTML: `<tag class="classA"></tag>`. On CSS: `.classA`;
* **id**: unique. On HTML: `<tag id="idA"></tag>`. On CSS: `#idA`;

## On CSS

### Attributes for txt.

* `font-size (1.2em)`: `em` is relative;
* `text-align (justify)`: equally spaced
* On HTML, `This <span class="purple"> text to be purple </span>.` Here, only "text to be purple" will be changed.

### Complex selectors:

All `<p>` inside `<li>` will be customized:

        li p {
            color: purple;
        }

`sel1 sel2`: separated by space. All `sel2` inside `sel1`.

### Tables

* `<table>`
    * `<tr>`: title;
    * `<th>` ;
    * `<td>`;

### Boxes

`div` are our boxes. It attributes are **padding**, **border**, **margin**, **width/height**.

### Borders

On CSS3 has radius!

### Display

Display are blocks. Act as `inline`, having **width/height** though.

### Position

Another similar property of *Display* is *Position*.

**Absolute** looks for the first non-static father.

### Float

Approximates a magazine design.

`clear: both` solves overlapping design issues.


## Lecture2
# Second course: Javascript + jQuery
*lecture given by Gustavo Silva*
The folder on this repository named [`160811_js_jq`](https://github.com/blackjuice/sectionAlpha/tree/master/Lecture/160811_js_jq) contains files created throughout lecture as practical exercises. As for the slides, follow [`this link`](http://slides.com/imeworkshop/oficina-js-jquery#/) (material created with https://slides.com/).

## Javascript Syntax

Straightforward example of a single script:

        var c1 = {};
        var c2 = {};
        c1.marca = "BMW";
        c2.marca = "Ferrari";
        c1.preco = 500;
        c2.preco = 700;

        if (c1.marca == "Mercedes") {
            // c1 também pode pode assumir tipos que não são objetos
            c1 = "workshop";
        }

        for (var i = 0; i < 5; i++) {
            c2.preco += 300;
        }

        var somador = function(x) {
            var k = 350;
            return k + x;
        }

        c3 = somador(c2.preco);

## jQuery Syntax

* `.contato .tel`: all child;
* `ul.lista2 > a`: direct child;