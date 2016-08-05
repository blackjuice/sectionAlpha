# Introdução à Web
*workshop by: IME Workshop*

This lecture consists on 4 parts:

| date   | topic |
|:-------|:------|
| 160804 | HTML + CSS |
| 1608XX | JavaScript + jQuery |
| 1608XX | Forms + AJAX + JSON |
| 1608XX | Bootstrap |

Description:
> Na primeira oficina do ciclo de Introdução a Web, vamos ver os conceitos de HTML5 e CSS3 que nos permitem estruturar o layout da nossa aplicação Web e estilizá-la como quisermos.

## Quick notes

* MariaDB, PostgreSQL are MySQL open-source alternatives;
* *tool: https://jsfiddle.net/*;
* It was recommended to learn AngularJS;
* LAMP is a stack type.

# First course: HTML + CSS
*lecture given by Gustavo Silva*

The folder on this repository named [`160804_html_css`](https://github.com/blackjuice/sectionAlpha/tree/master/Lecture/160804_html_css) contains files created through lecture as practical exercises.

custom tags:

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