# replit_keep_alive (RKA)
![Tests](https://github.com/Reathe/RKA/actions/workflows/tests.yml/badge.svg)

Easy way to keep your replit alive by calling keep_alive, and then pinging it. For example you can have https://uptimerobot.com monitor the page it created

Install with
```
pip install RKA
```

In your code:

```python
from RKA import keep_alive

keep_alive()
```

Don't forget to add a monitor to the created page, so it gets visited every few minutes. As long it has visitors, it won't die ! 
