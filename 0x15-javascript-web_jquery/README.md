# 0x15. JavaScript - Web jQuery

### Tasks

**0. No JQuery**
Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

    - You must use document.querySelector to select the HTML tag
    - You can’t use the JQuery API

Please test with this HTML file in your browser: 

```
guillaume@ubuntu:~/0x15$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

**1. With JQuery**
Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

    - You can’t use document.querySelector to select the HTML tag
    - You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```
